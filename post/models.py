from django.db import models
from django_quill.fields import QuillField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500, blank=False)
    body = QuillField()
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=100, blank=False,)
    likes = models.IntegerField(default=0, null=True)
    views = models.IntegerField(default=0, null=True)
    poster = models.ImageField(upload_to='media/poster/posts/')
    available = models.BooleanField(default=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


class Comment_Post(models.Model):
    body = models.CharField(max_length=500, blank=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        # value = self.ip + ' --viewed-- ' + \
        #     self.for_post.title + ' on ' + \
        #     str(self.viewed_on.day) + '/' + str(self.viewed_on.month) + \
        #     '/' + str(self.viewed_on.year) + ' at ' + str(self.viewed_on.hour) + \
        #     ':' + str(self.viewed_on.minute) + ':' + str(self.viewed_on.second)
        return self.name

    class Meta:
        ordering = ['commented_on']


class Views_Post(models.Model):
    ip = models.GenericIPAddressField(blank=False)
    viewed_on = models.DateTimeField(auto_now_add=True)
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        # value = self.ip + ' --viewed-- ' + \
        #     self.for_post.title + ' on ' + \
        #     str(self.viewed_on.day) + '/' + str(self.viewed_on.month) + \
        #     '/' + str(self.viewed_on.year) + ' at ' + str(self.viewed_on.hour) + \
        #     ':' + str(self.viewed_on.minute) + ':' + str(self.viewed_on.second)
        return self.ip

    class Meta:
        ordering = ['viewed_on']
