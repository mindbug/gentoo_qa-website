#! /usr/bin/env python
# Maintainer: John-Patrik Nilsson 
# mail:themindbug@gmail.com
# irc:<mindbug>

"""module depends on pkgcore_checks.report_stream"""

import sys

from snakeoil.pickling import iter_stream

class Digester:
    def __init__(self, pickle_file):
        # unpack the pkgcore_checks reports
        pchecks = unpack_pchecks(pickle_file)
        # format the pickles into QAReport objects
        qareports = format_pchecks(pchecks)
        # feed the objects to database
        # then,
        # write_to_mysql(user, host, password, database, table)
        # write_to_sqlite3(file, table)
        # write_to_stdout()

    def digest(self, pickle_file):
        """digest(pickle_file) loads pickles from the file, formats them, and
           returns them as a list
        """
        reports = []
        # unpack the pickled pkgcore_checks report objects into a tuple
        pickles = self.unpack_pickles(pickle_file)
        for item in pickles:
            reports.append(self.format_report(item))
        return reports

    def write_to_stdout(self):
        for item in self.reports:
            print(item)

    def printPackages(self):
        for item in self.reports:
            print(item["package"])
   
    def write_to_sqlite(self, db=":memory:", table="qareports"):
        """insert the reports in self.reports into a table in db"""
        # db table should exist!!
        # overwrite (or possibly replace) the qareports in table qareports
        import sqlite3
        connection = sqlite3.connect(db)
        c = connection.cursor()
        try:
            c.execute('''create table qareports
                (id int, category text, package text, version text, 
                 keywords text, classname text)''')
        except sqlite3.OperationalError:
            print 'The table already exists!'
        for count, report in enumerate(self.reports):
            t = tuple([
                        count, 
                        report["category"], 
                        report["package"], 
                        report["version"], 
                        report["keywords"], 
                        report["qa_class"]
                     ])
            c.execute('insert into qareports values (?, ?, ?, ?, ?, ?)', t)
        connection.commit()
        c.close()
       
    def unpack_pickles(self, filename):
        """returns a tuple containing pkgcore_checks report objects"""
        return tuple(iter_stream(open(filename)))
    
    def format_report(self, report):
        try:
            category = report.category
        except AttributeError:
            category = "n/a"
        try:
            package = report.package
        except AttributeError:
            package = "n/a"
        try:
            version = report.version
            if isinstance(version, tuple):
                version = " ".join(version)
        except AttributeError:
                version = "n/a"
        classname = (str(report.__class__).strip("<class '>").
                    split(".")[-1].lower())
        try:
            short_desc = report.short_desc
        except AttributeError:
            short_desc = "n/a"
        try:
            keywords = " ".join(report.keywords).strip()
        except AttributeError:
            keywords = "n/a"
        return {'category': category, 'package': package, 'version': version, 
                'keywords': keywords, 'qa_class': classname}


# keep?
class QAReport:
    def __init__(self, category, package, version, keywords, qa_class):
        self.category = category
        self.package = package
        self.version = version
        self.keywords = keywords
        self.qa_class = qa_class

    def __conform__(self, protocol):
        if protocol in sqlite3.PrepareProtocol:
            return "%s;%s;%s;%s;%s" % (self.category, self.package, 
                                  self.version, self.keywords, self.qa_class)

    def adapt_qareport(qareport):
        return "%s;%s;%s" % (self.category, self.package, self.version)

   
def main():
    #print sys.argv[1:]
    #pickle_file = sys.argv[1]
    #db = sys.argv[2]
    d = Digester("reports.pickle")
    d.printAll()
    
if __name__ == '__main__':
    main()
