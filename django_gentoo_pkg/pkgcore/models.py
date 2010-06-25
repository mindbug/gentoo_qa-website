from django.db import models

# Generally, each class corresponds to a database table,
# and each attribute corresponds to a table column.


class Repository(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return '%s' % self.name


class Package(models.Model):
    package = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    herd = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    # A Package belongs to a Repository.
    repository = models.ForeignKey(Repository)
    def __unicode__(self):
        return '%s/%s-%s:%s' % (self.category, self.package, 
                             self.version, self.repository)


class QAReport(models.Model):
    qa_class = models.CharField(max_length=255)
    keywords = models.TextField()
    description = models.TextField()
    # A QAReport belongs to a package.
    package = models.ForeignKey(Package)
    def __unicode__(self):
        return '%s' % self.qa_class


class Maintainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    irc_nick = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    packages = models.ManyToManyField(Package)
    def __unicode__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name,
                                self.irc_nick, self.email)


##  Info about all herds can be found in an xml doc:
## /gentoo/xml/htdocs/proj/en/metastructure/herds/herds.xml
# class Herd(models.Model):
#    name = models.CharField(max_length=20)
#    description = models.TextField()
#    email = models.EmailField()
#    packages = models.ManyToManyField(Package)
#    maintainers = models.ManyToManyField(Maintainer)
#    def __unicode__(self):
#        return '%s %s' % (self.name, self.email)
