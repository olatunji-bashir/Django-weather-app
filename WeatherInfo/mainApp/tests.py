from django.test import Client
from django.test import TestCase


# Create your tests here.
class MyViewTest(TestCase):
    def setUp(self):
        self.client = Client()
