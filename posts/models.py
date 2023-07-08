from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_review')
    data_review = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text



