from __future__ import annotations

import unittest


class TestApiInit(unittest.TestCase):
    def test_imports(self) -> None:
        try:
            import api
        except ImportError:
            self.fail("Failed to import 'api' module")
