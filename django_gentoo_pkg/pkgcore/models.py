from django.db import models

# Generally, each class corresponds to a database table,
# and each attribute corresponds to a table column.


class Package(models.Model):
    package = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.TextField()
    version = models.CharField(max_length=100)
    qa_description = models.TextField()
    qa_keywords = models.CharField(max_length=100)
    qa_class = models.CharField(max_length=30)
    website = models.URLField()


class Maintainer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    irc_nick = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    packages = models.ManyToManyField(Package)


# Info about all herds can be found in an xml doc:
# /gentoo/xml/htdocs/proj/en/metastructure/herds/herds.xml
class Herd(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    packages = models.ManyToManyField(Package)
    maintainers = models.ManyToManyField(Maintainer)
