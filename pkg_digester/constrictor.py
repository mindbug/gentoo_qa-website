#! /usr/bin/env python
# Maintainer: John-Patrik Nilsson 
# mail:themindbug@gmail.com
# irc:<mindbug>
#
# TODO
#   * exception handling
#   * option parsing when executing from CL
#   * usage help printing

"""module depends on pkgcore_checks.report_stream"""

import sys

from snakeoil.pickling import iter_stream


def digest(pickle_file):
    con = Constrictor()
    con.digest(pickle_file)
    return con


class Constrictor:
    def __init__(self):
        self.qareports = ("",)

    def digest(self, pickle_file):
        """Loads pkgcore_checks reports from pickle_file, formats them as 
           QAReport objects, and stuffs them into a tuple.
        """
        qareports = []
        pchecks = tuple(iter_stream(open(pickle_file)))
        # The first pcheck is a pickle streamheader, and the last is an
        # unusedglobalflagresult, whatever that means, anyways, I don't
        # want them.
        for pcheck in pchecks[1:-1]:
            qareports.append(QAReport(pcheck))
        self.qareports = tuple(qareports)

    def write_to_stdout(self):
        for report in self.qareports:
            print str(report)

    def write_to_sqlite3(self, db_file=":memory:", table="simple_qa_qareport"):
        import sqlite3
        connection = sqlite3.connect(db_file)
        c = connection.cursor()
        try:
            query = "%s %s" % ("DROP TABLE IF EXISTS", table)
            c.execute(query)
        except sqlite3.OperationalError as e:
            print "%s, %s." % ("Could not drop table because: ", e)

        try:
            query = "%s %s %s" % ("CREATE TABLE IF NOT EXISTS", table,
            '''("id" integer NOT NULL PRIMARY KEY, 
            "category" varchar(255) NOT NULL, 
            "package" varchar(255) NOT NULL, 
            "version" varchar(255) NOT NULL, 
            "keywords" varchar(255) NOT NULL, 
            "qa_class" varchar(255) NOT NULL)''')
            c.execute(query)
        except sqlite3.OperationalError as e:
            print "%s, %s." % ("Could not create table because: ", e)

        try:
            for count, report in enumerate(self.qareports):
                t = (count, report.category, report.package, report.version,
                    report.keywords, report.qa_class)
                query = "%s %s %s" % ("INSERT INTO", table, 
                        "VALUES (?, ?, ?, ?, ?, ?)")
                c.execute(query, t)
        except sqlite3.OperationalError as e:
            print "%s, %s." % ("Could not insert values because: ", e)

        connection.commit()
        c.close()

    def write_to_mysql(self, user="", host="", passwd="", db="gentoo", 
                       table="simple_qa_qareport"):
        import MySQLdb
        connection = MySQLdb.connect(db=db, host=host, user=user, 
                                     passwd=passwd)
        c = connection.cursor()
        try:
            query = "%s %s" % ("DROP TABLE IF EXISTS", table)
            c.execute(query)
        except _mysql_exceptions.OperationalError as e:
            print e

        try:
            query = "%s %s %s" % ("CREATE TABLE IF NOT EXISTS", table,
            '''(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
            `category` varchar(255) NOT NULL,
            `package` varchar(255) NOT NULL,
            `version` varchar(255) NOT NULL,
            `keywords` varchar(255) NOT NULL,
            `qa_class` varchar(255) NOT NULL)''')
            c.execute(query)
        except _mysql_exceptions.OperationalError as e:
            print e

        try:
            for report in self.qareports:
                query = "%s %s %s %s" % ("INSERT INTO", table, 
                "(category, package, version, keywords, qa_class)",
                "VALUES (%s, %s, %s, %s, %s)")
                t = (report.category, report.package, report.version,
                     report.keywords, report.qa_class)
                c.execute(query, t)
            #
            # If we could represent QAReports as tuples instead we could do:
            # c.executemany('''INSERT INTO simple_qa_qareport values (
            # %s, %s, %s, %s, %s, %s)''', self.qareports)
        except _mysql_exceptions.OperationalError as e:
            print e

        connection.commit()
        c.close()


class QAReport:
    def __init__(self, pcheck):
        self.attributes = self.format(pcheck)
        self.category = self.attributes["category"]
        self.package = self.attributes["package"]
        self.version = self.attributes["version"]
        self.keywords = self.attributes["keywords"]
        self.qa_class = self.attributes["qa_class"]

    def format(self, pcheck):
        """formats the pcheck object into a dictionary of QA values"""
        try:
            category = pcheck.category
        except AttributeError:
            category = "n/a"
        try:
            package = pcheck.package
        except AttributeError:
            package = "n/a"
        try:
            version = pcheck.version
            if isinstance(version, tuple):
                version = " ".join(version)
        except AttributeError:
                version = "n/a"
        classname = (str(pcheck.__class__).strip("<class '>").
                    split(".")[-1].lower())
        try:
            short_desc = pcheck.short_desc
        except AttributeError:
            short_desc = "n/a"
        try:
            keywords = " ".join(pcheck.keywords).strip()
        except AttributeError:
            keywords = "n/a"
        return {'category': category, 'package': package, 'version': version, 
                'keywords': keywords, 'qa_class': classname}

    def __str__(self):
        return '%s/%s-%s:%s:%s' % (self.category, self.package, self.version,
                                   self.keywords, self.qa_class)

    def adapt_qareport(qareport):
        return "%s;%s;%s" % (self.category, self.package, self.version)
  

def main():
    #print sys.argv[1:]
    #pickle_file = sys.argv[1]
    #db = sys.argv[2]
    #d = Digester("reports.pickle")
    #d.printAll()
    print "usage!"
    
if __name__ == '__main__':
    main()
