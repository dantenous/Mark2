from django.db import models

# Create your models here.


class Domacnost(models.Model):
    cas = models.CharField(max_length=150)
    teplota = models.CharField(max_length=150)
    tlak = models.CharField(max_length=150)
    vlhkost = models.CharField(max_length=150)
    teplotav = models.CharField(max_length=150)
    teplotazdanliva = models.CharField(max_length=150)
    rosnybod = models.CharField(max_length=150)
    vlhostv = models.CharField(max_length=150)
    densrazky = models.CharField(max_length=150)
    tlakv = models.CharField(max_length=150)
    smervetru = models.CharField(max_length=150)
    rychlostvetru = models.CharField(max_length=150)
    narazovyvitr = models.CharField(max_length=150)
    co2 = models.CharField(max_length=150)

    def __str__(self):
        return self.cas
