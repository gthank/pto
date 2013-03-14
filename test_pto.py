#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for PTO."""
import unittest2 as unittest


import pto
import time


_TIMEOUT = 5
_FUZZ_FACTOR = 1


class SlowClass(object):
    @pto.timeout(_TIMEOUT)
    def slow_instance_method(self):
        cut_off = time.time() + _TIMEOUT
        while time.time() < cut_off + _FUZZ_FACTOR:
            pass
        return True

    @classmethod
    @pto.timeout(_TIMEOUT)
    def slow_class_method(cls):
        cut_off = time.time() + _TIMEOUT
        while time.time() < cut_off + _FUZZ_FACTOR:
            pass
        return True

    @staticmethod
    @pto.timeout(_TIMEOUT)
    def slow_static_method():
        cut_off = time.time() + _TIMEOUT
        while time.time() < cut_off + _FUZZ_FACTOR:
            pass
        return True


class PtoTestCase(unittest.TestCase):
    def setUp(self):
        self.slowInstance = SlowClass()

    def tearDown(self):
        pass

    def test_function(self):
        @pto.timeout(_TIMEOUT)
        def slow_func():
            cut_off = time.time() + _TIMEOUT
            while time.time() < cut_off + _FUZZ_FACTOR:
                pass
            return True
        self.assertRaises(pto.TimedOutException, slow_func)

    def test_instance_method(self):
        self.assertRaises(pto.TimedOutException, self.slowInstance.slow_instance_method)

    def test_class_method(self):
        self.assertRaises(pto.TimedOutException, self.slowInstance.slow_class_method)

    def test_static_method(self):
        self.assertRaises(pto.TimedOutException, SlowClass.slow_static_method)


if __name__ == '__main__':
    unittest.main()
