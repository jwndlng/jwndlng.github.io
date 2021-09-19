#!/usr/bin/env python3
"""
This program is small website generator for creating static webpages
based on markdown and jinja2 template engine.
"""

import argparse
import pathlib
import yaml
from jinja2 import Template


# CONSTANTS
BASE_DIR = pathlib.Path(__file__).parent

# APPLICATION
class WebApplication:
    
    def __init__(self, config_file):
        # Load configuration
        self.load_config(config_file)
        # Set paths

        self._raw_content = BASE_DIR.joinpath(
            self._config.get('base', {}).get('content', '')
        )

    def load_config(self, config_file):
        if not BASE_DIR.joinpath(config_file).exists():
            raise FileNotFoundError(f"Please select a config file that exists. The file {config_file} does not exists!")
        with open(BASE_DIR.joinpath(config_file)) as yfile:
            self._config = yaml.safe_load(yfile)

    # Render
    def render(self):
        pages = self._config.get('pages', {})
        for page in pages:
            self.render_page(page, pages[page])

    def render_page(self, name, page):
        # Render the entry page
        print(page['title'])
        # Render subpages - detaillink!
        self.get_subpages(name)

    # Helper
    def get_subpages(self, name):
        print(name)
        subfolder = self._raw_content.joinpath(name)
        print(subfolder)


# MAIN
def main():
    parser = argparse.ArgumentParser(description='Generating static webpage')
    parser.add_argument('-c', '--config', default='config.yml')
    args = parser.parse_args()
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
