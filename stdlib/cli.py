#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 vince <vince@cl1010>
#
# Distributed under terms of the MIT license.
"""
sample for python cli
"""

import argparse


def add(*args):
    return sum(args)


def sub(*args):
    return 0 - sum(args)


# declear
parser = argparse.ArgumentParser(prog="cli",
                                 description='sample for command line parser',
                                 version="0.1")

sub_parser = parser.add_subparsers(help="help text for sub command")

sub_add = sub_parser.add_parser('add',
                                help=" sample for sum the input ",
                                add_help=False)

# 必须要输入的参数/
sub_add.add_argument(
    'integers',
    metavar='int',
    nargs='+',  # 代表至少一个
    type=int,
    help='an integer to be summed')

# 可选参数
sub_add.add_argument('-b',
                     '--base',
                     default=0,
                     type=int,
                     help='an base value for the sum (default is 0)')
sub_add.set_defaults(func=add)

sub_sub = sub_parser.add_parser('sub',
                                parents=[sub_add],
                                help=" sample for sub the input")

sub_sub.set_defaults(func=sub)

if __name__ == "__main__":
    # sample usage : python % add 1 2 3
    # sample usage : python % add 1 2 3 -b 100
    # sample usage : python % sub 1 2 3
    args = parser.parse_args()
    print('%s' % (args.func(*args.integers) + args.base))
