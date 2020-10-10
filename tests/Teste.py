import unittest

from src.func_valid_IP import func_valid_ip,func_Valid_True

class MyTestCase(unittest.TestCase):
    def test_CT0(self):
        print("test_CT0 ")
        res = func_valid_ip("125.125.125.125")
        func_Valid_True(res)

    def test_CT01(self):
        print("test_CT01 ")
        res = func_valid_ip("0.125.125.125")
        func_Valid_True(res)

    def test_CT02(self):
        print("test_CT02 ")
        res = func_valid_ip("-1.125.125.125")
        func_Valid_True(res)

    def test_CT03(self):
        print("test_CT03 ")
        res = func_valid_ip("1.125.125.125")
        func_Valid_True(res)

    def test_CT04(self):
        print("test_CT04 ")
        res = func_valid_ip("255.125.125.125")
        func_Valid_True(res)

    def test_CT05(self):
        print("test_CT05 ")
        res = func_valid_ip("256.125.125.125")
        func_Valid_True(res)

    def test_CT06(self):
        print("test_CT06 ")
        res = func_valid_ip("254.125.125.125")
        func_Valid_True(res)

    def test_CT07(self):
        print("test_CT07 ")
        res = func_valid_ip("k.125.125.125")
        func_Valid_True(res)

    def test_CT08(self):
        print("test_CT08 ")
        res = func_valid_ip("125.125.125")
        func_Valid_True(res)

    def test_CT09(self):
        print("test_CT09 ")
        res = func_valid_ip("125.125.125.125.125")
        func_Valid_True(res)

    def test_CT10(self):
        print("test_CT10")
        res = func_valid_ip("...125.125.125.")
        func_Valid_True(res)

    def test_CT11(self):
        print("test_CT11")
        res = func_valid_ip("")
        func_Valid_True(res)

    def test_CT12(self):
        print("test_CT12")
        res = func_valid_ip("154165481")
        func_Valid_True(res)

    def test_CT13(self):
        print("test_CT13")
        res = func_valid_ip("0000.125.125.125")
        func_Valid_True(res)

    def test_CT14(self):
        print("test_CT14")
        res = func_valid_ip("000.125.125.-000")
        func_Valid_True(res)
