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

class PostTest(TestCase):
    

    def create_post(self, title="only a test", body="yes, this is only a test"):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        newrequest = HttpRequest()
        my_view(newrequest)


        return Post.objects.create(title=title, text=body, created_date=timezone.now())

    def test_post_creation(self):
        w = self.create_post()
        self.assertTrue(isinstance(w, Post))
        self.assertEqual(w.__unicode__(), w.title)
def my_view(request):
    username = request.POST['test']
    password = request.POST['secret']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
