from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Table(models.Model):
    title = models.CharField('Title', max_length=127)
    text = models.TextField('Description')
    date_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'

    def get_absolute_url(self):
        return reverse('table-detail', kwargs={'pk': self.pk})
