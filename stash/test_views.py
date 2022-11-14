from django.test import TestCase
from .models import Yarn
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class TestViews(TestCase, LoginRequiredMixin):

    def setUp(self):
        test_user1 = User.objects.create_user(
            id='9',
            username='testuser1',
            email='',
            password='workaholic!?/', )
        test_user1.save()

        test_yarn = Yarn.objects.create(
            id='1',
            name='Yarn name',
            body='',
            user=test_user1,
            color_group='',
            color_name='',
            color_code='1',
            amount='1',
            weight='',
            material='',
            favorite='True',
            frogged='False', )
        test_yarn.save()

        pass

    def tearDown(self):
        pass

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stash/index.html')

    def test_user_page(self):
        response = self.client.get('/user_page')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stash/user_page.html')

