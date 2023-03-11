#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide util functions."""
from urllib.parse import quote

def sanitize_topic(topic: str) -> str:
    """Sanitize a topic for wikipedia input."""
    return quote(topic.replace(' ', '_').encode('utf-8'))
