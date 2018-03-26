#!usr/bin/env python
# -*- coding:utf-8 -*-

LOGIN_URL = 'https://github.com/login'
SESSION_URL = 'https://github.com/session'
SEARCH_URL = 'https://github.com/%ssearch?o=%s&utf8=✓&q=%s&s=%s&type=%s'
PROECT__SEARCH_URL = 'https://github.com/%s/search?o=%s&utf8=✓&q=%s&s=%s&type=%s'

RESULT_NUM_RE_PROJ = '#js-repo-pjax-container > div > div.repository-content > div > div.columns > div.column.one-fourth > nav > a.menu-item.selected > span'
RESULT_NUM_RE = '#js-pjax-container > div > div.columns > div.column.one-fourth > nav > a.menu-item.selected > span'
PROECT_INFO_XPATH = 'div.d-inline-block.col-10 > a.text-bold'
ITEM_XPATH = 'div.d-inline-block.col-10 > a:nth-of-type(2)'

INTERVAL_TIME = 0.0001
NUM_PAGE = 10.0
MAX_PAGE = 50
