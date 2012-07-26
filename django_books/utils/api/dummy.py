"""
A dummy API for reference / testing.
"""

class DummyAPI(object):
    def __init__(self, results):
        """
        Prepare the API for use.

        API implementations that need keys or other information to begin use
        can collect that information here.
        """
        self.results = results

    def search(self, search_dict):
        """
        Perform a search using the API.

        Fields in the search_dict that are not available for the implemented
        API can be ignored, but the results returned should use the same field
        keys as the passed search_dict does.
        """
        return self.results
