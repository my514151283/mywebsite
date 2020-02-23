from django.db import models


class Example(models.Model):
    post = models.CharField(max_length=600)
    response = models.CharField(max_length=600)
    result = models.CharField(max_length=600)


class Evaluation(models.Model):
    user = models.ForeignKey('login.MyUser', on_delete=models.CASCADE)
    example = models.ForeignKey(Example, on_delete=models.CASCADE)
    content = models.IntegerField()
    grammar = models.IntegerField()
    affect = models.IntegerField()
