# coding: utf-8

import unittest
from tapioca_bookingsync import BookingSync


class TestTapiocaBookingsync(unittest.TestCase):

    def setUp(self):
        self.wrapper = BookingSync()


if __name__ == '__main__':
    unittest.main()
