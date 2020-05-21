#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rainasmoon'
SITENAME = 'COSPLAY'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('全了的', 'https://www.rainasmoon.com/'),
         ('商品进化论', 'https://www.pay1all.top/'),
        )
# Social widget
SOCIAL = (('Weibo', 'https://www.weibo.com/rainasmoon'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['/home/hht/git/pelican-plugins']
PLUGINS = ['i18n_subsites',]

THEME = 'themes/notmyidea' 

DISCLAIMER = '<p>备案号：冀ICP备15002959号-1  <a href="http://he.beian.miit.gov.cn/state/outPortal/loginPortal.action">河北备案网站</a></p>'

COPYRIGHT = 'I will try it 1stly and think it 2ndly.'

EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        }

STATIC_PATHS = [
        'pictures',
        'extra/robots.txt',
        ]


