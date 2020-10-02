#!/usr/bin/env python3
# coding: utf8
"""
Docstring
"""


def flatten(containers):
    """
    provided that containers is a list (or more generally an iterable)
    of elements that are themselves iterables, this function
    returns a list of the items in these elements
    """
    return [element for container in containers for element in container]
