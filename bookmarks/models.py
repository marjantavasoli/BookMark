from django.db import models
from django.conf import settings


class Tag(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tags"
    )
    name = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner","name"],
                name= "unique_tag_per_owner"
            )
        ]
        ordering = ["name"]

    def __str__(self):
        return self.name


class BookMark(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='bookmarks')
    url = models.URLField(max_length=2000)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag,related_name='bookmarks',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-created_at"]
        indexes = [models.Index(fields=["owner","-created_at"]),
       ]
    def __str__(self):
        return self.title

