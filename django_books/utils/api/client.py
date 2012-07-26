"""
A client for available API modules that passes the query dictionary to each
and returns a list of possible match dictionaries.
"""

from django_books.utils.api import dummy
from django.conf import settings


class Client(object):
    def __init__(self, manual_api_selection=False):
        self._apis = []
        if not manual_api_selection:
            self.load_apis()

    def add_api(self, api_instance):
        self._apis.append(api_instance)

    def load_apis(self):
        """
        Load a list of book APIs from django.conf.settings.

        Example:

        import django_books.utils.api.dummy.DummyAPI
        results = {...}
        BOOK_CLIENT_APIS = (
          (django_books.utils.api.dummy.DummyAPI, (results,), {}),
        )

        Where the first element of the tuple is the class to add as an API, the
        second element is the positional arguments to the __init__ method of 
        the API class, and the third element is the keyword arguments.
        """
        for api, args, kwargs in getattr(settings, 'BOOK_CLIENT_APIS', []):
            self.add_api(api(*args, **kwargs))

    def search(self, search_dict):
        results_dict = {}

        for api in self._apis:
            # Query each API for a list of possible matches, binned by ISBN
            for isbn, results_list in api.search(search_dict).iteritems():
                if isbn not in results_dict:
                    results_dict[isbn] = {}

                # Aggregate the book results for each ISBN, so that each result
                # has each field with a list of possible values for that field.
                for result in results_list:
                    for field, value in result.iteritems():
                        if field not in results_dict[isbn]:
                            results_dict[isbn][field] = set()

                        results_dict[isbn][field].add(value)

        return results_dict
