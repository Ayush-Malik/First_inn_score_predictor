from django.db import models




# Create your models here.



class input_form_class(models.Model):
    added_date = models.DateTimeField()
    name       = models.CharField(max_length = 200 , null = True)
    venue      = models.CharField(max_length = 200)
    Batting_Team = models.CharField(max_length = 200 , null = True)
    Bowling_Team = models.CharField(max_length = 200 , null = True)
    overs        = models.CharField(max_length = 3 , null = True)
    runs         = models.CharField(max_length = 3 , null = True)
    wickets      = models.CharField(max_length = 2 , null = True)
    runs_last_5  = models.CharField(max_length = 3 , null = True)
    wickets_last_5 = models.CharField(max_length = 2 , null = True)

    def __str__(self): # Set the name of objects of class in database as name variable given by user
        return self.name