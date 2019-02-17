from django.test import TestCase
from lottery.models import Candidate

class TestUser(TestCase):
    def setUp(self):
        Candidate.objects.create(c_name='user1')

    def test_1_get_normal(self):
        self.assertTrue(Candidate.objects.all().count() == 1)
