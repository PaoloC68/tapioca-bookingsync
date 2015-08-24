# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

RESOURCE_MAPPING = {
    'rentals': {
        'resource': 'rentals',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/rentals/#list-rentals',
        "methods": [
            "GET",
            "POST"
         ]
    },
    'search_rentals': {
        'resource': '/rentals/search{params}',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/rentals/#search-rentals',
        "methods": [
            "GET",
         ]
    },
    "rental": {
        "resource": "rentals/{rental_id}",
        'docs': "http://developers.bookingsync.com/reference/endpoints/rentals/#get-a-single-rental",
        "methods": [
            "GET",
            "PUT",
            "DELETE"
         ]
    },
    'bookings': {
        'resource': 'bookings.json',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/bookings/#list-bookings',
        "methods": [
            "GET",
         ]
    },
    'search_bookings': {
        'resource':
            'bookings.json',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/bookings/#search-bookings',
        "methods": [
            "GET",
         ]
    },
}
