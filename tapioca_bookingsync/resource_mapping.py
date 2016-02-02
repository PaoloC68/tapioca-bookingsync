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
        'resource': '/rentals/search',
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
    'inquiry': {
        'resource': 'inquiries/{id}',
        "methods": [
            "GET",
            "PUT",
            "DELETE"
         ],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#get-a-single-inquiry'
    },
    'inquiries': {
        'resource': 'inquiries',
        'methods': ['GET'],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#list-inquiries'
    },
    'create_inquiry': {
        'resource': '/rentals/{rental_id}/inquiries',
        'methods': ['POST'],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#create-a-new-inquiry'
    },
}
