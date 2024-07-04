from __future__ import annotations

from django.test import TestCase

from api.user.models import User


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="testuser", email="test@example.com")

    def test_user_creation(self) -> None:
        assert self.user.username == "testuser"
        assert self.user.email == "test@example.com"
