import datetime

from django.db import models
from django.utils import timezone       # import datetime and from django.utils import timezone, to reference Python’s standard datetime module and Django’s time-zone-related utilities in django.utils.timezone, respectively.
from django.contrib import admin
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):                                                                      # <--- 2.4.2 inicio
        return self.question_text                                                           #       
    # def was_published_recently(self):                                                     #       2.4.3 - Updated on 5.2.4
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)                # <---  2.4.3 fim - Updated on 5.2.4
    def was_published_recently(self):                                                       # 5.2.4 inicio
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now                     # 5.2.4 fim
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
