from django.db import models

# Create your models here.


class Post(models.Model):
    """Model representing a post from news board."""

    title = models.CharField(max_length=200, help_text="What's new?")
    link = models.URLField(max_length=250, help_text="Don't forget to provide a link")
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title


class Comment(models.Model):
    """Model representing a comment on post."""

    author_name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, help_text="Share your opinion...")
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "Commented by {}".format(self.author_name)
