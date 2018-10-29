RESOURCE_MAPPING = {
    'accounts': {
        'resource': 'accounts/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/accounts/#list-accounts',
        'methods': [
            'GET',
        ]
    },
    'account': {
        'resource': 'accounts/{account_id}',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/accounts/#get-a-single-account',
        'methods': [
            'GET',
        ]
    },
    'availabilities': {
        'resource': 'availabilities/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/availabilities/#list-availabilities',
        'methods': [
            'GET',
        ]
    },
    'availability': {
        'resource': 'availabilities/{availability_id}/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/availabilities/#get-a-single-availability',
        'methods': [
            'GET',
        ]
    },
    'clients': {
        'resource': 'clients/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/clients/#list-clients',
        'methods': [
            'GET',
        ]
    },
    'client': {
        'resource': 'clients/{client_id}',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/clients/#get-a-single-client',
        'methods': [
            'GET',
        ]
    },
    'rentals': {
        'resource': 'rentals/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/rentals/#list-rentals',
        'methods': [
            'GET',
            'POST'
         ]
    },
    'search_rentals': {
        'resource': 'rentals/search/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/rentals/#search-rentals',
        'methods': [
            'GET',
         ]
    },
    'rental': {
        'resource': 'rentals/{rental_id}',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/rentals/#get-a-single-rental',
        'methods': [
            'GET',
            'PUT',
            'DELETE'
         ]
    },
    'rental_photos': {
        'resource': 'rentals/{rental_id}/photos/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/photos/#create-a-new-photo',
        'methods': [
            'GET',
            'POST',
         ]
    },
    'bookings': {
        'resource': 'bookings/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/bookings/#list-bookings',
        'methods': [
            'GET',
         ]
    },
    'booking': {
        'resource': 'bookings/{booking_id}',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/bookings/#list-bookings',
        'methods': [
            'GET',
            'PUT',
            'DELETE'
        ]
    },
    'inquiry': {
        'resource': 'inquiries/{id}',
        'methods': [
            'GET',
            'PUT',
            'DELETE'
         ],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#get-a-single-inquiry'
    },
    'inquiries': {
        'resource': 'inquiries/',
        'methods': ['GET'],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#list-inquiries'
    },
    'create_inquiry': {
        'resource': 'rentals/{rental_id}/inquiries',
        'methods': ['POST'],
        'docs': 'http://developers.bookingsync.com/reference/endpoints/inquiries/#create-a-new-inquiry'
    },
    'bookings_tags': {
        'resource': 'bookings_tags/',
        'methods': ['GET'],
        'docs': None
    },
    'bookings_tag': {
        'resource': 'bookings_tags/{bookings_tag_id}',
        'methods': ['GET'],
        'docs': None
    },
    'amenities': {
        'resource': 'amenities/',
        'docs': 'http://developers.bookingsync.com/reference/endpoints/amenities/',
        'methods': [
            'GET',
            'POST'
         ]
    },
    'rates': {
        'resource': 'rates/',
        'methods': ['GET'],
        'docs': None
    },
    'rate': {
        'resource': 'rates/{rate_id}',
        'methods': ['GET'],
        'docs': None
    },
    'rates_tables': {
        'resource': 'rates_tables/',
        'methods': ['GET', 'POST'],
        'docs': None
    },
    'rate_table': {
        'resource': 'rates_tables/{rate_table_id}',
        'methods': ['GET', 'PUT', 'DELETE'],
        'docs': None
    },
}
