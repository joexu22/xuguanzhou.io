#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.curdir)
from datetime import date
from config.my_config import *
from _data.resume import *

AUTHOR = 'Xu GuanZhou'
NICKNAME = 'Joe'
SITE_NAME = 'Joe\'s Website'
SITE_URL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'
CURRENT_YEAR = date.today().year
CURRENT_DATE = date.today().strftime("%d %b %Y")

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('Joe\'s Website', 'http://xuguanzhou.io'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True