from django.db import models


#class Package(models.Model):
    #name = models.CharField(max_length=255)
    #category = models.CharField(max_length=255)
    #version = models.CharField(max_length=255)
    #def __unicode__(self):
        #return '%s/%s-%s' % (self.category, self.name, self.version)


class QAReport(models.Model):
    category = models.CharField(max_length=255)
    package = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    qa_class = models.CharField(max_length=255)
    short_desc = models.TextField()
    arch = models.CharField(max_length=255)
    threshold = models.CharField(max_length=255)
    #description = models.TextField()
    #package = models.ForeignKey(Package)
    def __unicode__(self):
        return '%s/%s-%s: %s' % (self.category, self.package, self.version, self.qa_class)
