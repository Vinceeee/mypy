import pytest
from ..utils import sorted_by_key
from ..models import Role


@pytest.mark.parametrize(
    "arr, key, expected_first",
    [
        ([dict(a=1, b=2), dict(a=2, b=1), dict(a=-1, b=3)], "a", dict(a=-1, b=3)),
        ([dict(a=1, b=2), dict(a=2, b=1), dict(a=-1, b=3)], "b", dict(a=2, b=1)),
    ],
)
def test_sorted_by_key(arr, key, expected_first):
    sorted_by_key(arr, key)
    assert arr[0] == expected_first


@pytest.mark.django_db
def test_role():
    assert Role.objects.get(name="test-01")


def test_add(client):
    resp = client.get("/api/cal/add", data=dict(a=1, b=2))
    assert resp.status_code == 200
    # assert resp.json()["result"] == 3
