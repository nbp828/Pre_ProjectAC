from django.db import models

from django.db import models


class Query(models.Model):
    query_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Result(models.Model):
    result_text = models.CharField(max_length=200)
