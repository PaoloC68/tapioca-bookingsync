# -*- coding: utf-8 -*-
from tapioca_bookingsync import BookingSync


def test_resource_access_rentals():
    api_client = BookingSync()
    resource = api_client.rentals()
    assert resource.data == 'https://www.bookingsync.com/api/v3/rentals/'
