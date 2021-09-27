from rest_framework.test import APITestCase
from authenticate.models import User

class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user('prabhash','pks@gmail.com','pass!@123')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'pks@gmail.com')

    def test_with_no_username(self):
        self.assertRaises(ValueError,User.objects.create_user,username='',email='pks@gmail.com',password='pass!@123')

    def test_with_no_email(self):
        self.assertRaises(ValueError,User.objects.create_user,username='pks',email='',password='pass!@123')

    def test_with_superuser_isstaff(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username='pks',email='',password='pass!@123',is_staff=False)

    def test_with_superuser_issuperuser(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username='pks',email='',password='pass!@123',is_superuser=False)

    def test_create_super_user(self):
        user = User.objects.create_superuser('prabhash','pks@gmail.com','pass!@123')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'pks@gmail.com')

    