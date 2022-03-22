from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Tag(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200, default=None)
    
    def __str__(self) -> str:
        return self.slug

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now, null = True, blank = True)
    # date_created = models.DateTimeField
    date_closed = models.DateTimeField(null = True, blank = True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'owner_projects'
    )
    # owner = models.CharField(max_length=200)
    category = models.ForeignKey(
        Tag, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='category'
    )
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',on_delete=models.CASCADE,
        related_name='pledges'
        )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )


# class QA(models.Model):





