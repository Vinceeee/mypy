from django.test import TestCase
from oauth.models import User


# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        User.objects.create(user_name="用户1", user_passwd="abc")
        User.objects.create(user_name="用户2", user_passwd="abc")

    def test_1_get_normal(self):
        u1 = User.objects.get(user_name="用户1")
        passwd = u1.user_passwd
        passwd_hashing = User.hashing("用户1", "abc")
        self.assertTrue(passwd == passwd_hashing)

    def test_2_get_exception(self):
        try:
            User.DoesNotExist, User.objects.get(user_name="用户3")
        except Exception:
            self.assertTrue(1 == 1)
