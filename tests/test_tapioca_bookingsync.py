# -*- coding: utf-8 -*-

import os
import unittest

from tapioca_bookingsync import BookingSync


class TestBookingSyncTapioca(unittest.TestCase):
    def setUp(self):
        self.api_client = BookingSync(
            client_id=os.getenv('BOOKINGSYNC_CLIENT_ID', default=''),
            access_token=os.getenv('BOOKINGSYNC_ACCESS_TOKEN', default=''),
        )

    def test_resource_access(self):
        resource = self.api_client.rentals()
        import ipdb; ipdb.set_trace()
        assert resource.data == 'https://www.bookingsync.com/api/v3/rentals'


if __name__ == '__main__':
    unittest.main()
