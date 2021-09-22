#!/usr/bin/env python3
"""
This program is small website generator for creating static webpages
based on markdown and jinja2 template engine.
"""

import argparse
import markdown
import pathlib
import yaml
from jinja2 import Environment, FileSystemLoader


# CONSTANTS
BASE_DIR = pathlib.Path(__file__).parent
TPL_DIR = BASE_DIR.joinpath('templates')
CONTENT_SEPARATOR = '-----'

# TODO change to config
NAV_TPL = 'nav.j2'
DEF_TPL = 'default.j2'
SOCIAL_MEDIA_TPL = 'social_media.j2'
SOCIAL_MEDIA_HEADER_TPL = 'social_media_header.j2'


# APPLICATION
class WebApplication:
    
    def __init__(self, config_file):
        # Load configuration
        self.load_config(config_file)
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

        def __init__(self, page, config, page_type=PTYPE_MAIN, params={}):
            self.tpl_env = Environment(loader=FileSystemLoader(TPL_DIR))
            self.page = page
            self.pages = config.get('pages', [])
            self.social_media = config.get('social_media', {})
            self.type = page_type
            self.params = {
                'meta': {
                    'author': config['base']['author'],
                    'description': ''
                }
            }
            self.content = []

        def add_content(self, title, meta, content):
            self.content.append({
                'title': title,
                'meta': meta,
                'content': content
            })

        def get_params(self):
            params = self.params
            params['print_content'] = self.render_content()
            params['print_main_navigation'] = self.render_nav(
                "main",
                [p for p in self.pages if self.NAV_MAIN in p['nav']]
            )
            params['print_foot_navigation'] = self.render_nav(
                "foot",
                [p for p in self.pages if self.NAV_FOOTER in p['nav']]
            )
            params['print_social_media'] = self.render_social_media()
            params['print_social_media_header'] = self.render_social_media(
                tpl_file=SOCIAL_MEDIA_HEADER_TPL
            )
            params['title'] = self.page['title']
            return params

        def render(self):
            params = self.get_params()
            tpl = self.tpl_env.get_template(DEF_TPL)
            return tpl.render(**params)

        def render_content(self):
            if self.page['type'] == self.CONTENT_TYPE_DEFAULT:
                return self.render_overview()
            elif self.page['type'] == self.CONTENT_TYPE_ARTICLE:
                if self.type == self.PTYPE_MAIN:
                    return self.render_article_overview()
                else:
                    return self.render_article()

        def render_overview(self):
            tpl = self.tpl_env.get_template('page_default.j2')
            return tpl.render(content=self.content)

        def render_article_overview(self):
            tpl = self.tpl_env.get_template('page_article_overview.j2')
            return tpl.render(content=self.content)

        def render_article(self):
            tpl = self.tpl_env.get_template('page_article_detail.j2')
            return tpl.render(content=self.content)

        def render_nav(self, name, pages, tpl_file=NAV_TPL):
            # prepare data
            nodes = []
            for page in pages:
                node = {
                    'href': f"{page['file']}.html",
                    'name': page['name'],
                    'is_active': False
                }
                if page['name'] == self.page['name']:
                    node['is_active'] = True
                nodes.append(node)
            # read template
            tpl = self.tpl_env.get_template(tpl_file)
            # render
            return tpl.render(name=name, nodes=nodes)

        def render_social_media(self, tpl_file=SOCIAL_MEDIA_TPL):
            # read template
            tpl = self.tpl_env.get_template(tpl_file)
            # render
            return tpl.render(social_media=self.social_media)


    # Render
    def render(self):
        for page in self.pages:

            page_obj = self.Page(page, self._config)
            
            # Create folder for subpages
            if page.get('type', '') == self.Page.CONTENT_TYPE_ARTICLE:
                self.create_folder(page['file'])

            for filepath in self.get_content_pages(page['file']):

                # TODO
                # Two things are important here
                # - Get content to be added on main page
                # - Create subpage if its type article
                title, meta, preview, content = self.parse_markdown_file(filepath)

                if page.get('type', '') == self.Page.CONTENT_TYPE_ARTICLE:
                    #self.render_subpage(page, filepath)
                    page_obj.add_content( title, meta, preview)
                else:
                    page_obj.add_content( title, meta, content)
            
            self.create_page(
                page['file'],
                page_obj.render()
            )
                    
        return 0



    def parse_markdown_file(self, filepath):
        state = 0
        title = ''
        preview = ''
        meta = {}
        content = ''
        with open(filepath, 'r', encoding='utf-8') as m_file:
            for line in m_file.readlines():
                if line.strip() == CONTENT_SEPARATOR:
                    # States title -> meta data -> content
                    state+=1
                    continue             
                if state == 0:
                    title = line
                elif state == 1:
                    splits = line.split(':')
                    meta[splits[0].strip()] = splits[1].strip()
                elif state == 2:
                    preview += line
                elif state == 3:
                    content += line
                else:
                    raise Exception(f"Reached unknown state {state}")
        return title, meta, preview, markdown.markdown(content)

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
