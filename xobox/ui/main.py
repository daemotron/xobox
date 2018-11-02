# -*- coding: utf-8 -*-

"""
    xobox.ui.main
    ~~~~~~~~~~~~~
    :copyright: Copyright 2018 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import sys

from ..utils import sysexits


def main() -> int:
    """
    xobox main function

    Central entry point for xobox. This function evaluates command
    line arguments, prepares and executes the ui and ensures clean
    exit behaviour.
    """
    return sysexits.EX_OK
