from django.test import TestCase
from datetime import date
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Recursos, Reservas

# Create your tests here.
class ReservasAPITest(APITestCase):
    fixtures = ['user', 'recursos', 'reservas']
    
    def authenticate(self):
        my_user = User.objects.get(id=1)
        token = Token.objects.create(user = my_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ token.key)
    
    def test_get_booking(self):
        response = self.client.get('/api/reservas/')
        response_json = response.json()
        
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response_json), 2)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)
        self.assertIsInstance(response_json[1], dict)
       