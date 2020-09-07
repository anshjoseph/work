from django.db import models
# Create your models here.
class Contact(models.Model):
    ques = models.TextField()
    # models.CharField(max_length=122)
    # models.TextField()
    #models.DateField()
    data = models.DateField()
    def __str__(self):
        return self.ques
