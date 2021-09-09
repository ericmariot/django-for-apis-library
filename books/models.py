from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=13
    )  # is a unique 13-character identifier to every published book

    def __str__(self):
        return self.title
