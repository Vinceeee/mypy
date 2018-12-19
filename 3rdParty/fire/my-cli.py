#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fire

class Sub_run(object):

    def hi(self):
        return "Hi" 

class Cli(object):
    
    def __init__(self):
        self.run = Sub_run()

    def hello(self, msg="world"):
        return "hello {}".format(msg)

if __name__ == '__main__':
    fire.Fire(Cli)
