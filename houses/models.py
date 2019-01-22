from django.db import models
from django.urls import reverse

# Create your models here.


class HomeQuerySet(models.query.QuerySet):

    def featured(self):
        return self.filter(featured=True)


class HomeListingManager(models.Manager):

    def get_queryset(self):
        return HomeQuerySet(self.model, using=self.db)

    def get_state(self, query):
        return self.get_queryset().filter(state__icontatins=query)

    def featured(self):
        return self.filter(featured=True)


class HomeListing(models.Model):

    address = models.CharField(max_length=120, blank=False, null=False)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120,)
    zip_code = models.CharField(max_length=9)
    number_of_bed = models.IntegerField(blank=False, default=1)
    number_of_bath = models.DecimalField(decimal_places=1, max_digits=10,)
    year_built = models.IntegerField(blank=False)
    sq_ft = models.IntegerField()
    img = models.ImageField(upload_to='house_photos', blank=True, null=True,
                            default='beach.jpg')
    list_date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    cost = models.IntegerField(default=1)

    objects = HomeListingManager()

    class Meta:

        verbose_name_plural = 'Homes'

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('houses:detail', kwargs={'pk': self.pk})

    def full_address(self):
        return self.address + ', ' + self.city



















