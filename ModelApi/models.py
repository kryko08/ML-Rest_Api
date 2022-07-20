from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

import os

from datetime import datetime
now = datetime.now()



class AlgorithmRequest(models.Model):
    requested_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_input = models.CharField(max_length=200)
    response = models.CharField(max_length=150)