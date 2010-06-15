#! /usr/bin/env python
# Maintainer: John-Patrik Nilsson, IRC: mindbug, themindbug@gmail.com
# TODO Copyright 

# This script does not define any objects, nor does it use
# an Object Oriented approach to the database interaction.
# Suggestions: Define each of the pickled objects as a new
# kind of object, just for this script. Could make it cleaner.
# Also, perhaps using SQLAlchemy to interface with the db?
# But, for now, I consider that premature optimization.

""" pkg_digester: a module for translating a pickle stream of pkgcore_checks objects into a human-readable collection of strings.
"""
from snakeoil.pickling import iter_stream

def load_pickles(file):
    """ load_pickles(file='qa-results.pcheck'): returns a tuple of pcheck result objects from the given pickle file.
    """
    return tuple(iter_stream(open(file)))

# TODO
# Notes:
#   The pickled objects can be represented as tuples.
#   We want there to be only one row in the list with
#   the combined values of category, package, and version.
#   So, for all versions of the package:
#       create a new row with identical other_stuff.
def formatter(tuple):
    """ formatter(tuple): formats and organizes the objects in a list of tuples, returns a list.
    """
    formatted_list = []
    for item in tuple[1:]:
        version = " ".join(item.version)
        formatted_list.append((item.category, item.package, item.version, classname, item.short_desc))
    return _formatted_list

def gen_tuple(result_obj):
    """ gen_tuple(result_obj): outputs a tuple with pcheck info.
    """
    # Category
    category = result_obj.category
    # Package
    package = result_obj.package
    # Version
    # TODO I want the versions not as a concatenated str, but as a
    # new object.
    try:
        version = " ".join(result_obj.version)
    # Class
    classname = str(result_obj.__class_).strip("<class '>").split(".")[-1].lower()
    # Short description
    short_desc = result_obj.short_desc
    # Keywords
    try:
        keywords = " ".join(result_obj.keywords).strip()
    except AttributeError as error:
        keywords = "None"
    return (category, package, version, keywords, classname)

def main():
    checks = load_pickles("qa-results.pcheck")
    checks = formatter(checks)

# If called as a script call main(), otherwise be a module.
if __name__ == '__main__':
    main()
else:
    print("I'm a module! :O")
