from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class UserProfileDB(models.Model):
    userid = models.ForeignKey(User,related_name = 'userProfile' ,on_delete=models.CASCADE)
    description = models.TextField()
    random_fun = models.TextField()

    def __str__(self):
        return f"{self.userid} - {self.description} - {self.random_fun}"


class UserPersonalityDB(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    cnp = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.userid} - {self.cnp}"


class QuestionsDB(models.Model):
    question = models.TextField()
    asnwer_a = models.TextField()
    asnwer_b = models.TextField()
    asnwer_c = models.TextField()

    def __str__(self):
        return f"{self.question} => a.){self.asnwer_a} b.){self.asnwer_b} c.){self.asnwer_c}"
