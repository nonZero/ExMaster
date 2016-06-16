import markdown
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    content_html = models.TextField(editable=False)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content_html = markdown.markdown(self.content)
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse("blog:detail", args=(self.pk,))


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title

        # def get_absolute_url(self):
        #     return reverse("blog:detail", args=(self.pk,))


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('post', 'user'),
        )
