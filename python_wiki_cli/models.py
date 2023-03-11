#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide pydantic models to the CLI from the webparser."""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class WikiContent(BaseModel, ABC):



class Page(BaseModel, ABC):
    """Provide a generic Page class."""
    title: str
    url: str
    lang: str
    content: WikiContent
    accessed: Optional[datetime] = datetime.utcnow()

    @abstractmethod
    def format(self) -> str:
        """Format the page to print it on the terminal."""

    @abstractmethod
    def



