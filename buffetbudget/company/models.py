from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12)
    representant_name = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Company'
        verbose_name_plural = u'Companies'

