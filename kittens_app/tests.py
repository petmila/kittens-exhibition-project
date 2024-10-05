from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from kittens_app.models import Kitten, Breed


class ModelDataTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.breed = Breed.objects.create(name="Siberian").id
        cls.user_id = User.objects.create(username='user', password='user1234', email='user@mail.ru').id
        cls.kitten = Kitten.objects.create(breed_id=cls.breed, age="101", color="orange",
                                           description="Does funny tricks", name="Manny", user_id=cls.user_id)

    def test_that_gets_kittens_by_breed(self):
        self.assertEqual(self.kitten.id, Kitten.objects.all().filter(breed=self.breed).get().id)

class KittenViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.breed = Breed.objects.create(name="British").name
        cls.user_id = User.objects.create(username='user', password='user1234', email='user@mail.ru').id

    def test_view_url_exists_at_desired_location__authorized_user(self):
        token, created = Token.objects.get_or_create(user_id=self.user_id)
        response = self.client.get('/kittens/kitten/', headers={'Authorization': 'Token ' + token.key})
        self.assertEqual(response.status_code, 200)

    def test_view_create__authorized_user(self):
        token, created = Token.objects.get_or_create(user_id=self.user_id)
        self.breed = Breed.objects.get(name=self.breed).id
        data = {
            "name": "Miay",
            "age": 150,
            "color": "white",
            "breed": self.breed,
            "description": "Has already won multiple times"
        }
        response = self.client.post('/kittens/kitten/', data=data, headers={'Authorization': 'Token ' + token.key})
        self.assertEqual(response.status_code, 201)

    def test_view_update__authorized_user_is_not_owner(self):
        token, created = Token.objects.get_or_create(user_id=self.user_id)
        self.breed = Breed.objects.get(name=self.breed).id
        data = {
            "name": "Miay",
            "age": 150,
            "color": "white",
            "breed": self.breed,
            "description": "Has already won multiple times"
        }
        self.client.post('/kittens/kitten/', data=data, headers={'Authorization': 'Token ' + token.key})
        data = {
            'id': str(Kitten.objects.get(name="Miay").id),
            "name": "Miay",
            "age": 151,
            "color": "grey",
            "breed": self.breed,
            "description": "Became dirty"
        }
        response = self.client.put('/kittens/kitten/', data=data, headers={'Authorization': 'Token ' + token.key})
        self.assertEqual(response.status_code, 405)

