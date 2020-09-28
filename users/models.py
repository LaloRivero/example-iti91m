""" Users Models  """

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """ Profile model 
        Proxi model that extends data with other information
    """

    user = models.OnetoOneField(User, on_delete=models.CASCADE)
