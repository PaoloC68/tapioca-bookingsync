def test_resource_access_rentals(api_client, rentals):
    assert rentals.data == 'https://www.bookingsync.com/api/v3/rentals/'


def test_resource_search_bookings(api_client, search_bookings):
    assert search_bookings.data == 'https://www.bookingsync.com/api/v3/bookings/'
