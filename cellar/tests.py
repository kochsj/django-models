from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from .models import Bottle

# Create your tests here.
class CellarTests(TestCase):
    """Want to work with test db"""

    def setUp(self):
        """Sets up the user and store before each test"""
        self.user = get_user_model().objects.create_user(username='testuser', email='test@test.test', password='password')
        self.bottle = Bottle.objects.create(User=self.user,Winery='test_winery',Description='Very good')

    def test_string_repr(self):
        """Test string repr of a store instance"""
        bottle = Bottle.objects.get(id=1)
        self.assertEqual(str(bottle), 'test_winery')

    def test_store_content(self):
        """Tests that description is matching"""
        bottle = Bottle.objects.get(id=1)
        self.assertEqual(bottle.Description, 'Very good')

    def test_store_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_store_list_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_store_detail_view(self):
        url = reverse('wine_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)