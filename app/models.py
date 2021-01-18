# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Films(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie = models.CharField(max_length=55)
    director = models.CharField(max_length=55, blank=True, null=True)
    stars = models.CharField(max_length=67, blank=True, null=True)
    country = models.CharField(max_length=27, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    release_year = models.CharField(max_length=4)
    released = models.CharField(max_length=10, blank=True, null=True)
    plot = models.CharField(max_length=729, blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'films'
