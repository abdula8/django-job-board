from django.db import models

# Create your models here.
class Info(models.Model):
    # name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    # , blank=True, null=True

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email

