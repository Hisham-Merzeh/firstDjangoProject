from django.db import models




class Index(models.Model):
    pname = models.CharField(blank=True, max_length=100)
    pdescription = models.TextField(blank=True)
    sold = models.BooleanField(default=False)


    def __str__(self):
        return self.pname
