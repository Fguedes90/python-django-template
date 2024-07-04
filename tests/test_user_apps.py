from __future__ import annotations

from django.apps import AppConfig
from django.test import TestCase

from api.user.apps import UserConfig


class UserConfigTest(TestCase):
    def test_apps(self) -> None:
        assert UserConfig.name == "api.user"
        assert isinstance(UserConfig(), AppConfig)
