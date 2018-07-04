# -*- coding: utf-8 -*-

from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from utils import clean_text

_scrap_url = 'https://www.index.hr'
_sections = ['vijesti', 'sport', 'magazin']
_html = urlopen(_scrap_url)
_content = _html.read()
_page = BeautifulSoup(_content, 'html.parser')


def _text(elem):
    return clean_text(elem.get_text()) if elem else ''


def _url(elem):
    return '%s%s' % (_scrap_url, elem.get('href')) if elem else None


def _section_right_data(section):
    for parent in _page.findAll('div', {'class': 'right-part'}):
        items = parent.findAll('a', {'class': '%s-text-hover' % section})
        if not items:
            continue
        return [{
            'type': 'article',
            'text': _text(n),
            'url': _url(n)
        } for n in items]


def _header_data(section):
    cubes = _page.findAll('div', {'class': 'cube-big-mainnews-holder'})
    for cube in cubes:
        if not re.search(r"%s-text-hover" % section, str(cube)):
            continue
        url_elem = cube.find('a', {'class': '%s-text-hover' % section})
        text_elem = cube.find('h2', {'class': 'title'})
        return {
            'type': 'article',
            'text': _text(text_elem),
            'url': _url(url_elem)
        }


def scrapped_data():
    data = []
    for s in _sections:
        data.append({
            'type': 'section',
            'text': s,
            'url': ''
        })
        data.append(_header_data(s))
        data.extend(_section_right_data(s))
    return data
