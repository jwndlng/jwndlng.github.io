#!/usr/bin/env python3
"""
This program is small website generator for creating static webpages
based on markdown and jinja2 template engine.
"""

import argparse
from jweb import WebApplication

# MAIN
def main():
    parser = argparse.ArgumentParser(description='Generating static webpage')
    parser.add_argument('-c', '--config', default='config.yml')
    parser.add_argument('-r', '--reset', action='store_true')
    args = parser.parse_args()
    
    # Clean application
    if args.reset:
        pass

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
