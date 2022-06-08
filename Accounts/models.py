from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null= True, blank = True, 
    help_text= "We need to know your age for very not creepy purposes")
#null allows storing in a db as null. Blank is for the forms and allows an empty form 
#A common gotcha to be aware of is that the field type dictates how to use these values. Whenever you 
# have a string-based field like CharField or TextField, setting both null and blank as we’ve done will 
# result in two possible values for “no data” in the database. Which is a bad idea. The Django convention 
# is instead to use the empty string '', not NULL. Look up field options GFG has a chart for this one 
#god I hate the docs
