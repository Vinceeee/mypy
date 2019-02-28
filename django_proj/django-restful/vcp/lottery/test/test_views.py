from django.test import TestCase
from lottery.models import Candidate, Price


class TestCandidate(TestCase):
    def setUp(self):
        Candidate.objects.create(c_name='user1')

    def test_1_get(self):
        res = self.client.get("/lottery/candidate")
        self.assertTrue(res.status_code == 200)

    def test_2_post(self):
        data = {"c_id": "2", "c_name": "aaabbb"}
        res = self.client.post(r"/lottery/candidate", data=data)
        self.assertTrue(res.status_code == 201)

    def test_3_delete(self):
        res = self.client.delete(r"/lottery/candidate/1")
        self.assertTrue(res.status_code == 204)


class TestPrice(TestCase):
    def setUp(self):
        Price.objects.create(p_name="苹果手机")

    def test_get(self):
        res = self.client.get("/lottery/prices")
        self.assertTrue(res.status_code == 200)

    def test_post(self):
        data = {"p_id": "2", "p_name": "小米8"}
        res = self.client.post("/lottery/prices/2", data=data)
        self.assertTrue(res.status_code == 201)
