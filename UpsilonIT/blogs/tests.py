from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token


class Tests(APITestCase):
    fixtures = ['db.json']

    def setUp(self):
        self.client = APIClient()
        token = Token.objects.get(user__email='123@mail.ru')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_blog(self):
        data = {'user': '1', 'title': '3', 'description': '3'}
        self.client.post('/api/blog/', data, format='json')

    def test_get_blogs(self):
        self.client.get('/api/blog/', format='json')

    def test_get_blog(self):
        self.client.get('/api/blog/1/', format='json')

    def test_update_blog(self):
        data = {'user': '1', 'title': '3', 'description': '3'}
        self.client.put('/api/blog/1/', data, format='json')

    def test_delete_blog(self):
        self.client.delete('/api/blog/1/', format='json')

    def test_custom_params(self):
        self.client.get('/api/blog/?max=True', format='json')
        self.client.get('/api/blog/?start=2015-08-20', format='json')
        self.client.get('/api/post/?name=123&', format='json')
        self.client.get('/api/post/?name=123&is_deleted=True', format='json')
        self.client.get('/api/post/?start=2015-08-20&end=2015-08-31&name=123&is_deleted=True', format='json')

    def test_create_post(self):
        data = {'user': '1', 'title': '123', 'description': '123', 'blog': '1'}
        self.client.post('/api/post/', data, format='json')

    def test_update_post(self):
        data = {'user': '1', 'title': '123', 'description': '123', 'blog': '1'}
        self.client.put('/api/post/1/', data, format='json')

    def test_delete_post(self):
        self.client.delete('/api/post/1/', format='json')



