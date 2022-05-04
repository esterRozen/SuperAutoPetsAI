from unittest import TestCase


class TestBase(TestCase):
    def __init__(self):
        super(TestBase, self).__init__()
        self.fail()
