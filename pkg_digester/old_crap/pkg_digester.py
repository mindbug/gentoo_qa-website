#! /usr/bin/env python
# Maintainer: John-Patrik Nilsson 
#             IRC: <mindbug> @ #gentoo-soc, #gentoo-dev, #pkgcore
#             themindbug@gmail.com

""" pkg_digester: a module for translating a pickle stream of 
    pkgcore_checks objects into a human-readable collection of strings.
"""

import sys
import sqlite3

from snakeoil.pickling import iter_stream


""" This script does not define any objects, nor does it use an Object 
    Oriented approach to the database interaction.  
    Suggestions: Define each of the pickled objects as a new kind of 
    object, just for this script. Could make it cleaner.  Also, perhaps 
    using SQLAlchemy to interface with the db?  But, for now, I consider 
    that premature optimization.
"""

# TODO
# Copyright crap?
#
# Make all attribute names Pythonic.
#
# Change and copy the result items so that the rows which are put out does
# not have more than one version. This means that not two rows should have 
# an identical combination of category, package, and version.

def digest_to_stdout(picklefile):
    """ digest_to_stdout(filename): Formats and organizes the pcheck result 
        objects from the given file into tuples, which then are output to
        stdout.
    """
    unformatted_list = _load_pickles(picklefile)
    # formatted_list = []
    for item in unformatted_list[1:-1]:
        # formatted_item = _format_result(item)
        # formatted_list.append(formatted_item)
        # print formatted_item
        print _format_result(item)
    # return formatted_list


def digest_to_sqlite(picklefile):
    """ digest_to_sqlite(picklefile): Formats and organizes the pcheck result 
        objects from the given file into a list of tuples, and consumes 
        them into a database.
    """
    unformatted_list = _load_pickles(picklefile)

    # conn = sqlite3.connect('db.sqlite3')
    conn_ = sqlite3.connect(":memory:")
    cursor_ = conn_.cursor()
    cursor_.execute('''create table qa_data
        (category text, package text, version text, keywords text, 
        classname text)''')
    tmp = unformatted_list[2]
    tmp = _format_result(tmp)
    print tmp


def digest_to_mysql(picklefile):
    """digest_to_mysql(picklefile): Formats and organizes the qa results
       from picklefile into a MySQL database.
    """
    import mysqldb
    pass


class Table:
    def __init__(self, db, name):
        pass



# Experimental code, handle the generators with care. ;)
def _dict_generator():
    pass

def _tuple_generator():
    pass


def _load_pickles(file):
    """ _load_pickles(file): Unpickles the given file and returns a tuple 
        containing the objects within.
    """
    return tuple(iter_stream(open(file)))


def _format_result(result_obj):
    """ _format_result(result_obj): returns a dictionary with 
        pcheck info as strings.
    """
    try:
        category = result_obj.category
    except AttributeError:
        category = "n/a"
    try:
        package = result_obj.package
    except AttributeError:
        package = "n/a"
    try:
        version = result_obj.version
        if isinstance(version, tuple):
            version = " ".join(version)
    except AttributeError:
            version = "n/a"
    classname = (str(result_obj.__class__).strip("<class '>").
                 split(".")[-1].lower())
    short_desc = result_obj.short_desc
    try:
        keywords = " ".join(result_obj.keywords).strip()
    except AttributeError:
        keywords = "n/a"
    return {'category': category, 'package': package, 'version': version, 
            'keywords': keywords, 'class': classname}


def main():
    # pickle_file = "qa-results.pcheck"
    # digest_to_stdout(pickle_file)
    # digest_to_sqlite(pickle_file)
    pickle_file = sys.argv[1]
    db = sys.argv[2]
    print(pickle_file, db)

# If called as a script call main(), otherwise be a module (be passive).
if __name__ == '__main__':
    main()
