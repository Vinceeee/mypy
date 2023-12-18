#!/usr/bin/env python

import logging

def add_log_handle():
    """todo """
    pass

def add_nothing():
    """add some comment."""
    pass

def main():
    log_level = logging.INFO
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('./test.log')
    fh.setLevel(log_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info("test test")
    logger.debug("no debug test test")
    logger.error("test test")
    logger.warn("test test 2")
    logger.info("asdfd{}{}{}asdf".format("aaa","bbb","%aa"))

if __name__ == "__main__":
    main()
