# -*- coding:utf-8 -*-
import unittest
from TestCase.gloVal import gloVal

class unittest_StartEnd(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL
        self.header = gloVal.BOSS_HEADER
