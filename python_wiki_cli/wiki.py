#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wrap the wiki settings."""
from typing import Optional

from bs4 import BeautifulSoup as Soup
from requests import get

from .utils import sanitize_topic

LANGUAGE = 'en'

WIKIPEDIA_TAGS = {
    'title':
        ['span', {'class': 'mw-page-title-main'}],
}


class WikiArticle:
    """Provide a representation of a wikipedia article."""
    WIKI_URL = "https://{language}.wikipedia.org/wiki"

    def __init__(self, topic: str, language: Optional[str] = LANGUAGE):
        """Initialize the wiki article."""
        self.topic = sanitize_topic(topic)
        self.url = self.WIKI_URL.format(language=language) + '/' + self.topic
        self.article = self.populate_article()
        self.title = self.retrieve_title()
        self.sections = self.retrieve_sections()

    def populate_article(self) -> Soup:
        """Soup the page of an article."""
        response = get(self.url, timeout=30)
        return Soup(response.text)

    def retrieve_title(self) -> str:
        """Retrieve the title from the article."""
        return self.article.find(WIKIPEDIA_TAGS.get('title')[0],
                                 WIKIPEDIA_TAGS.get('title')[1]).text

    def retrieve_sections(self) -> list:
        """Retrieve the sections."""


