#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Shanquel Scott in study group w/ Gabby and Sondos"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('text', type=str, help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    echo_str = ""
    if not ns:
        parser.print_usage()
        sys.exit(1)
    str1 = args[0]
    if len(args) == 1:
        echo_str = str1
    if len(args) > 2:
        echo_str = str1
        for x in args:
            if x == "-u" or "--upper":
                continue
            if x == "-t" or "--title":
                echo_str = echo_str.title()
                continue
            if x == "-l" or "--lower":
                echo_str = echo_str.lower()
                continue
    else:
        if ns.lower:
            echo_str = str1.lower()
        if ns.upper:
            echo_str = str1.upper()
        if ns.title:
            echo_str = str1.title()
        if ns.title and ns.upper and ns.lower is False:
            echo_str = str1
    print(echo_str)


if __name__ == '__main__':
    main(sys.argv[1:])
