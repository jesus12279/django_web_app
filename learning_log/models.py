from django.db import models

# Create your models here.

"""Creating a topic model"""

class Topic(models.Model):
    """Topic a user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	"""Return a string representation of my topic model"""
    	return self.text