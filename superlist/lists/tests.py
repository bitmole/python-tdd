from django.test import TestCase

class SmokeTest(TestCase):
    def test_altfacts(self):
        self.assertEqual(1 + 1, 3)
