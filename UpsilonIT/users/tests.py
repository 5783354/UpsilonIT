from rest_framework.test import APITestCase, APIClient


class UserTests(APITestCase):

    def test_create_user(self):
        self.client = APIClient()
        data = {'first_name': '123', 'last_name': '123', 'email': '123@mail.ru',
                'password': '123', 'phone': '123'}
        self.client.post('/api/user/', data, format='json')