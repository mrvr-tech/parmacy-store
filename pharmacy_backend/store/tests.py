from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import StoreItem


class StoreInventoryTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='storekeeper',
            password='testpass123',
            role='store',
        )
        self.client.force_login(self.user)

    def create_item(self, *, category, item_name, sr_no):
        return StoreItem.objects.create(
            category=category,
            sr_no=sr_no,
            item_name=item_name,
            packages='1 unit',
            quantity=10,
            price=250.0,
            tax=5.0,
            bill_no=f'B{sr_no}',
            date=date.today(),
            expiry_date=date.today() + timedelta(days=180),
            vendor_name='Test Vendor',
            vendor_address='Test Address',
            vendor_pan='ABCDE1234F',
        )

    def test_add_item_form_saves_category_and_redirects(self):
        response = self.client.post(
            reverse('add_item_form'),
            {
                'category': 'chemicals',
                'item_name': 'Acetone',
                'packages': '500ml',
                'quantity': '20',
                'price': '250',
                'tax': '18',
                'bill_no': 'B101',
                'date': '2026-03-14',
                'expiry_date': '2027-03-14',
                'vendor_name': 'ABC Chemicals',
                'vendor_address': 'Pune',
                'vendor_pan': 'AAAPA1234A',
            },
        )

        self.assertRedirects(response, reverse('manage_inventory'))
        item = StoreItem.objects.get(item_name='Acetone')
        self.assertEqual(item.category, 'chemicals')
        self.assertEqual(item.sr_no, 1)

    def test_manage_inventory_filters_by_category_and_search(self):
        matching_item = self.create_item(category='chemicals', item_name='Acetone', sr_no=1)
        self.create_item(category='glassware', item_name='Beaker', sr_no=2)
        self.create_item(category='chemicals', item_name='Sodium Chloride', sr_no=3)

        response = self.client.get(
            reverse('manage_inventory'),
            {'category': 'chemicals', 'q': 'Ace'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['items']), [matching_item])
        self.assertEqual(response.context['selected_category'], 'chemicals')
        self.assertContains(response, 'Chemicals')
        self.assertContains(response, 'Acetone')
        self.assertNotContains(response, 'Beaker')
