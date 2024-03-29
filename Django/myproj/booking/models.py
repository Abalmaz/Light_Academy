from django.db import models

# Create your models here.
class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author__isnull=False)

    def with_tag(self, tag):
        return self.get_queryset().filter(tags__name=tag)

class Author(models.Model):
    name = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag)
    tags_mtm = models.ManyToManyField(Tag, through='BookTags', related_name='book_mtm')

    with_author=BookManager()

    def __str__(self):
        return self.title+self.author.name


class BookTags(models.Model):
    book = models.ForeignKey(Book, models.CASCADE, related_name='book_mtm')
    tag = models.ForeignKey(Tag, models.CASCADE, related_name='book_tags')



