from django.db import models

# Generally, each class corresponds to a database table,
# and each attribute corresponds to a table column.


class QAReport(models.Model):
    qa_class = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    def __str__(self):
        return '%s' % self.qa_class


class Package(models.Model):
    package = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    repository = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    qa_report = models.ForeignKey(QAReport)
    def __str__(self):
        return '%s-%s' % (self.package, self.version)


class Maintainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    irc_nick = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    packages = models.ManyToManyField(Package)
    def __str__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name,
                                self.irc_nick, self.email)


# Info about all herds can be found in an xml doc:
# /gentoo/xml/htdocs/proj/en/metastructure/herds/herds.xml
class Herd(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    packages = models.ManyToManyField(Package)
    maintainers = models.ManyToManyField(Maintainer)
    def __str__(self):
        return '%s %s' % (self.name, self.email)
