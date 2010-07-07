from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    def __unicode__(self):
        return '%s/%s-%s' % (self.category, self.name, self.version)


class QAReport(models.Model):
    qa_class = models.CharField(max_length=255)
    keywords = models.TextField()
    description = models.TextField()
    package = models.ForeignKey(Package)
    def __unicode__(self):
        return '%s: %s' % (self.package.name, self.qa_class)
