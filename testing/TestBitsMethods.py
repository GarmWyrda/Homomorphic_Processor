import unittest

from datatypes.bits.Bit import *


class TestBitsMethods(unittest.TestCase):
    def test_or(self):
        bit1 = PlainBit(True)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(True)
        bit3 = bit1 + bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3,expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(False)
        bit3 = bit1 + bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(True)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(True)
        bit3 = bit1 + bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(True)
        bit3 = bit1 + bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

    def test_and(self):
        bit1 = PlainBit(True)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(False)
        bit3 = bit1 * bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(False)
        bit3 = bit1 * bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(True)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(True)
        bit3 = bit1 * bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(False)
        bit3 = bit1 * bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

    def test_xor(self):
        bit1 = PlainBit(True)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(True)
        bit3 = bit1 ^ bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(False)
        expectedResult = PlainBit(False)
        bit3 = bit1 ^ bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(True)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(False)
        bit3 = bit1 ^ bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)

        bit1 = PlainBit(False)
        bit2 = CryptoBit(True)
        expectedResult = PlainBit(True)
        bit3 = bit1 ^ bit2
        bit3 = bit3.decrypt()
        self.assertEqual(bit3, expectedResult)