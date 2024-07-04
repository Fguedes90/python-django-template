from __future__ import annotations

from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from api.user.admin import UserAdmin
from api.user.models import User


class MockRequest:
    pass


class UserAdminTest(TestCase):
    def setUp(self) -> None:
        self.site = AdminSite()
        self.user_admin = UserAdmin(User, self.site)
        self.user = User(username="testuser", email="test@example.com")

    def test_save_model(self) -> None:
        request = MockRequest()
        self.user_admin.save_model(request, self.user, None, False)
        assert self.user.username == "testuser"
        assert self.user.email == "test@example.com"
