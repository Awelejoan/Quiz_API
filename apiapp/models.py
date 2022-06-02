from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.question



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)

    def __str__(self):
        return self.a

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.answer