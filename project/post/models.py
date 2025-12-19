from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True, null=True)
    is_publish = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post} --- {self.text[:7]}..."