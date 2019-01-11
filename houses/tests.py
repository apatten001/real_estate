from django.test import TestCase
from .models import HomeListing
import datetime
from django.utils import timezone

# Create your tests here.


# address = models.CharField(max_length=120, blank=False, null=False)
#     city = models.CharField(max_length=120)
#     state = models.CharField(max_length=120,)
#     zip_code = models.CharField(max_length=9)
#     number_of_bed = models.IntegerField(blank=False, default=1)
#     number_of_bath = models.DecimalField(decimal_places=1, max_digits=10,)
#     year_built = models.IntegerField(blank=False)
#     sq_ft = models.IntegerField()
#     img = models.ImageField(upload_to='house_photos', blank=True,null=True,
#                              default='default_home_pic.jpg')
#     list_date = models.DateTimeField(auto_now_add=True)
#     featured = models.BooleanField(default=False)
#     cost = models.IntegerField(default=1)


class HomeListingTestCase(TestCase):

    def setUp(self):
        HomeListing.objects.create(address='32 Charles St.', city='Durham', state='NC', zip_code='23482',
                                   number_of_bed=3, number_of_bath=2, year_built=2015, sq_ft=3105)
        HomeListing.objects.create(address='48 Charles St.', city='Durham', state='NC', zip_code='23482',
                                   number_of_bed=4, number_of_bath=2.5, year_built=2014, sq_ft=3005)

    def test_string_representation(self):
        home1 = HomeListing.objects.get(address='32 Charles St.')

        self.assertEquals(str(home1), home1.address)

    def test_home_listing_full_address(self):

        home1 = HomeListing.objects.get(address='32 Charles St.')
        home2 = HomeListing.objects.get(address='48 Charles St.')

        self.assertEquals(home1.full_address(), '32 Charles St., Durham')
        self.assertEquals(home2.city, 'Durham')

    def test_verbose_plural_name(self):

        self.assertEquals(str(HomeListing._meta.verbose_name_plural), 'Homes')









