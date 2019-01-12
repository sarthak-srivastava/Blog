from django.test import TestCase
from blogapp.models import Post
from django.utils import timezone
from blogapp.forms import PostForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.contrib.auth import authenticate, login
from django.http.request import HttpRequest
# models test


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

