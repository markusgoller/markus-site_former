#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus'
SITENAME = 'Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# path-specific metadata
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'}, 
    'static/CNAME': {'path': 'CNAME'},
    'static/.nojekyll': {'path': '.nojekyll'},
    }

# Static files
STATIC_PATHS = [
    'images',
    'static',
    ]

MENUITEMS = [('Home', '/'), ('Archives', '/archives.html')]

# pelican-themes
THEME = "themes/attila"

# Can set individual COVERS
#HOME_COVER = '../images/bike_tour_berlin_notebook/IMG_20200819_130938_resize.jpg'
HOME_COLOR = 'green'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
