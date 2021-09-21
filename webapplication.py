#!/usr/bin/env python3
"""
This program is small website generator for creating static webpages
based on markdown and jinja2 template engine.
"""

import argparse
import pathlib
import yaml
from jinja2 import Environment, FileSystemLoader


# CONSTANTS
BASE_DIR = pathlib.Path(__file__).parent
TPL_DIR = BASE_DIR.joinpath('templates')
# TODO change to config
NAV_TPL = 'nav.j2'
DEF_TPL = 'default.j2'


# APPLICATION
class WebApplication:
    
    def __init__(self, config_file):
        # Load configuration
        self.load_config(config_file)
        # base params
        self.params = {
            'meta': {
                'author': self._config['base']['author'],
                'description': ''
            }
        }
        # variables
        self.pages = self._config.get('pages', [])
        # Set paths
        self._raw_content = BASE_DIR.joinpath(
            self._config.get('base', {}).get('content', '')
        )

    def load_config(self, config_file):
        if not BASE_DIR.joinpath(config_file).exists():
            raise FileNotFoundError(f"Please select a config file that exists. The file {config_file} does not exists!")
        with open(BASE_DIR.joinpath(config_file)) as yfile:
            self._config = yaml.safe_load(yfile)

    # Subclasses
    class Page:

        CONTENT_TYPE_DEFAULT = 'default'
        CONTENT_TYPE_ARTICLE = 'article'
        PTYPE_MAIN = 1
        PTYPE_CONTENT = 2
        NAV_MAIN = 'main'
        NAV_FOOTER = 'footer'

        def __init__(self, page, pages, page_type=PTYPE_MAIN, params={}):
            self.tpl_env = Environment(loader=FileSystemLoader(TPL_DIR))
            self.page = page
            self.pages = pages
            self.type = page_type
            self.params = params
            self.content = []

        def add_content(self, content):
            self.content.append(content)

        def render(self):
            params = self.params
            params['print_main_navigation'] = self.render_nav(
                "main",
                [p for p in self.pages if self.NAV_MAIN in p['nav']]
            )
            params['print_foot_navigation'] = self.render_nav(
                "foot",
                [p for p in self.pages if self.NAV_FOOTER in p['nav']]
            )
            params['title'] = self.page['title']
            tpl = self.tpl_env.get_template(DEF_TPL)
            return tpl.render(**params)

        def render_overview(self):
            pass

        def render_detail(self):
            pass

        def render_nav(self, name, pages, tpl_file=NAV_TPL):
            # prepare data
            nodes = []
            for page in pages:
                node = {
                    'href': f"{page['file']}.html",
                    'name': page['name'],
                    'is_active': False
                }
                if page == self.page['name']:
                    node['is_active'] = True
                nodes.append(node)
            # read template
            tpl = self.tpl_env.get_template(tpl_file)
            # render
            return tpl.render(name=name, nodes=nodes)

    # Render
    def render(self):
        for page in self.pages:
            self.create_page(
                page['file'],
                self.render_page(page, self.pages)
            )

            # Create folder for subpages
            if page.get('type', '') == self.Page.CONTENT_TYPE_ARTICLE:
                self.create_folder(page['file'])

            for filepath in self.get_content_pages(page['name']):

                # TODO
                # Two things are important here
                # - Get content to be added on main page
                # - Create subpage if its type article

                if page.get('type', '') == self.Page.CONTENT_TYPE_ARTICLE:
                    self.render_subpage(page, filepath)
        return 0

    def render_page(self, name, pages):
        # Render the entry page
        page = self.Page(name, pages, params=self.params)
        return page.render()

    def render_subpage(self, parent, filepath):
        """
        Renders a page defined in markdown
        """
        pass

    # Helper
    def create_folder(self, name):
        BASE_DIR.joinpath(name).mkdir(exist_ok=True)

    def create_page(self, filepath, content):
        with open(f'{filepath}.html', 'w', encoding='utf-8') as html_file:
            html_file.write(content)

    def get_content_pages(self, name):
        subfolder = self._raw_content.joinpath(name)
        files = subfolder.glob('*.md')
        return files


# CLEANUP    
def reset(config):
    # TODO implement cleanup function
    print("Remove pages and their folders!")


# MAIN
def main():
    parser = argparse.ArgumentParser(description='Generating static webpage')
    parser.add_argument('-c', '--config', default='config.yml')
    parser.add_argument('-r', '--reset', action='store_true')
    args = parser.parse_args()
    
    # Clean application
    if args.reset:
        reset(args.config)

    # run application    
    app = WebApplication(args.config)
    status = app.render()

    if status == 0:
        print("Rendered webapplication")
    elif status == 1:
        print("Rendered webapplication with warning")
    elif status == 2:
        print("Rendering was not successful!")
    else:
        print("Rendering exited with unknown code!")


if __name__ == '__main__':
    main()
