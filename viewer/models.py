from django.db.models import (
    Model, CharField, ForeignKey, DO_NOTHING,
    IntegerField, DateField, TextField, DateTimeField
)
from django.contrib import admin


# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(Model):
    firstName = CharField(max_length=128)
    lastName = CharField(max_length=128)
    email = CharField(max_length=128)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Author)
