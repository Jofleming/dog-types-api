from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Dog_type


class DogTypeTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_dog_type = Dog_type.objects.create(
            breed="husky",
            owner=testuser1,
            description="Fluffy good dog.",
        )
        test_dog_type.save()

    def test_dog_type_model(self):
        dog_type = Dog_type.objects.get(id=1)
        actual_owner = str(dog_type.owner)
        actual_breed = str(dog_type.breed)
        actual_description = str(dog_type.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_breed, "husky")
        self.assertEqual(
            actual_description, "Fluffy good dog."
        )

    def test_get_dog_type_list(self):
        url = reverse("dog_type_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dog_types = response.data
        self.assertEqual(len(dog_types), 1)
        self.assertEqual(dog_types[0]["breed"], "husky")

    def test_get_dog_type_by_id(self):
        url = reverse("dog_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dog_type = response.data
        self.assertEqual(dog_type["breed"], "husky")

    def test_create_dog_type(self):
        url = reverse("dog_type_list")
        data = {"owner": 1, "breed": "boxer", "description": "short haired, funny face."}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        dog_types = Dog_type.objects.all()
        self.assertEqual(len(dog_types), 2)
        self.assertEqual(Dog_type.objects.get(id=2).breed, "boxer")

    def test_update_dog_type(self):
        url = reverse("dog_detail", args=(1,))
        data = {
            "owner": 1,
            "breed": "husky",
            "description": "Black and white fluffy good dog.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dog_type = Dog_type.objects.get(id=1)
        self.assertEqual(dog_type.breed, data["breed"])
        self.assertEqual(dog_type.owner.id, data["owner"])
        self.assertEqual(dog_type.description, data["description"])

    def test_delete_dog_type(self):
        url = reverse("dog_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        dog_types = Dog_type.objects.all()
        self.assertEqual(len(dog_types), 0)
