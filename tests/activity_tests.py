import unittest
from models.activity_type import ActivityType
from models.activity import Activity
from models.member import Member
from models.booking import Booking


class TestActivity(unittest.TestCase):
    
    def setUp(self):
        self.activity = Activity("Aquafit")