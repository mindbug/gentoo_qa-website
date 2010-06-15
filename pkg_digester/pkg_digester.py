#! /usr/bin/env python
# Maintainer: John-Patrik Nilsson, IRC: mindbug, themindbug@gmail.com
# TODO
# Copyright 

""" pkg_digester: a module for translating a pickle stream of pkgcore_checks objects into a human-readable collection of strings.
"""
from snakeoil.pickling import iter_stream

def load_pickles(file):
    """load_pickles(file='qa-results.pcheck'): returns a tuple of pcheck result objects from the given pickle file."""
    return tuple(iter_stream(open(file)))

# TODO
#   Get it to work..
# Notes:
#   The pickled objects can be represented as tuples of
#   len(_keywords) elements.
def formatter(tuple):
    """formatter(tuple): formats and organizes the objects in the tuple, returns a tuple."""
    # Formatting keywords; the stuff I want to save.
    _keywords = (".package", ".version", "category",
                ".short_desc", ".keywords", ".long_desc")
    # Create and return a list containing objects converted into tuples.
    _formatted_list = []
    return _formatted_list

def text_outputter(tuple):
    for item in tuple[1:]:
        classname = str(item.__class_).strip("<class '>").split(".")[-1].lower()
        print (item.category, item.package, item.version, 
        classname, item.short_desc)

def main():
    checks = load_pickles(qa-results.pcheck)
    checks = formatter(checks)

# If called as a script call main(), otherwise be a module.
if __name__ == '__main__':
    main()
else:
    print("I'm a module! :O")
