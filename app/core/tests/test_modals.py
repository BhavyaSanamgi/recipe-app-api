from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@email.com"
        password = "test@123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['TEst2@Example.com', 'TEst2@example.com'],
            ['test3@Example.COM', 'test3@example.com']
        ]

        for email, expected_mail in sample_emails:
            user = get_user_model().objects.create_user(email, 'Sample123')
            self.assertEquals(user.email, expected_mail)

    def test_new_user_withour_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)