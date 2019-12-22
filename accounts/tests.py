from django.conf import settings
from django.core import mail
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class LoginViewTest(TestCase):
    def _create_user(self, username, email, password=None):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

    def test_show_page(self):
        r = self.client.get(reverse('accounts:login'))
        self.assertEqual(r.status_code, 200)

    def test_redirect_to_index_after_login(self):
        username = 'taro'
        email = 'taro@example.com'
        password = 'testpassword'
        self._create_user(
            username=username,
            email=email,
            password=password,
        )
        data = {
            'username': username,
            'password': password,
        }
        r = self.client.post(reverse('accounts:login'), data)
        self.assertRedirects(
            r,
            settings.LOGIN_REDIRECT_URL,
            fetch_redirect_response=False,
        )


class ProfileViewTest(TestCase):
    def _create_user(self, username, email, password=None):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

    def test_show_page(self):
        user = self._create_user(
            username='taro',
            email='taro@example.com',
            password='testpassword',
        )
        self.client.force_login(user)
        r = self.client.get(reverse('accounts:profile'))
        self.assertEqual(r.status_code, 200)


class PasswordResetViewTest(TestCase):
    def _create_user(self, username, email, password=None):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

    def test_show_page(self):
        r = self.client.get(reverse('accounts:password_reset'))
        self.assertEqual(r.status_code, 200)

    def test_send_reset_mail(self):
        email = 'taro@example.com'
        self._create_user(
            username='taro',
            email=email,
            password='testpassword',
        )

        data = {'email': email}
        r = self.client.post(reverse('accounts:password_reset'), data)
        self.assertRedirects(r, reverse('accounts:password_reset_done'))

        self.assertEqual(len(mail.outbox), 1)
        self.assertListEqual(mail.outbox[0].to, [email])
