from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    
    def test_main_page_context(self):
        client = Client()
        response = client.get('/main/')
        
        self.assertEqual(response.context['name'], ['Sword', 'Shield', 'Potion'])
        self.assertEqual(response.context['description'], ['A sword made of steel', 'A shield made of steel', 'A potion of healing'])
        
        
