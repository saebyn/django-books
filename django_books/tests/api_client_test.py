"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class APIClientTest(TestCase):
    def create_dummy_client(self, fixtures):
        from django_books.utils.api.client import Client
        from django_books.utils.api.dummy import DummyAPI
        client = Client(manual_api_selection=True)
        client.add_api(DummyAPI(fixtures))
        return client

    def test_api_results_all_combinations(self):
        isbn = '123456789'
        client = self.create_dummy_client({isbn: [{'title': 'A title',
                                                   'desc': 'A desc.',
                                                   'author': 'me'},
                                                  {'title': 'A title',
                                                   'desc': 'A different desc.',
                                                   'tag': '',
                                                   'author': 'me'},
                                                  {'title': 'A different title',
                                                   'desc': 'A desc.',
                                                   'tag': 'yes',
                                                   'author': 'me'}]})
        result = client.search({'isbn': isbn})
        self.assertIn(isbn, result)
        self.assertItemsEqual(('A title', 'A different title'), result[isbn]['title'])
        self.assertItemsEqual(('A desc.', 'A different desc.'), result[isbn]['desc'])
        self.assertItemsEqual(('yes', ''), result[isbn]['tag'])
        self.assertItemsEqual(('me',), result[isbn]['author'])
