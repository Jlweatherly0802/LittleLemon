from django.test import TestCase
from .models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        value = "Icecream : 80"
        item = MenuItem.objects.create(title="Icecream", price=80, inventory=100)
        self.assertEqual(item, value)