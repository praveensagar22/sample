from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    options = models.JSONField(default=list)  # Store options as a JSON list
    answer = models.CharField(max_length=255)
