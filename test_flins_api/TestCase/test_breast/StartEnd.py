# -*- coding:utf-8 -*-
import unittest
from TestCase.gloVal import gloVal

class unittest_StartEnd(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.BASE_URL
        self.header = gloVal.C_HEADER
