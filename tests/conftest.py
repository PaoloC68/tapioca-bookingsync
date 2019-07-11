import pytest

from tapioca_bookingsync import BookingSync


@pytest.fixture
def api_client():
    return BookingSync()


@pytest.fixture
def search_bookings(api_client):
    return api_client.search_bookings()


@pytest.fixture
def rentals(api_client):
    return api_client.rentals()
