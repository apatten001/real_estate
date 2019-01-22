from django.db import models

# Create your models here.


class Contact(models.Model):

    """
    Store contact information
    """

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


