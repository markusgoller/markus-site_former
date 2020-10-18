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
    'static',
    ]

MENUITEMS = [('Home', '/'), ('Archives', '/archives.html')]

# pelican-themes
THEME = './pelican-themes/attila'
#THEME = './pelican-themes/pelican-clean-blog'

# COVERS for pelican-themes (pictures have to be at the pelican-themes path)
#
# On each blog is the same HEADER_COVER  
#HEADER_COVER = 'static/IMG_20200819_130938_resize.jpg'
#
# Can set individual COVERS
HOME_COVER = 'static/IMG_20200819_130938_resize.jpg'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
