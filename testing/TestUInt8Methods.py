from datatypes.integers.UInt8 import *
import unittest

class TestUInt8Methods(unittest.TestCase):
    def setUp(self):
        self.int1 = UInt8(127)
        self.int2 = UInt8(0)
        self.int3 = UInt8(255)
        self.int4 = UInt8(128)
        self.int5 = UInt8(7)
        self.int6 = UInt8(12)
        self.randomInts = []
        for i in range(0, 50):
            self.randomInts += [random.randint(0, 255)]

    def test_uint8_debugshowValue(self):
        self.assertEquals(self.int1.debug_showValue(),127)
        self.assertEquals(self.int2.debug_showValue(), 0)
        self.assertEquals(self.int3.debug_showValue(), 255)
        self.assertEquals(self.int4.debug_showValue(), 128)
        self.assertEquals(self.int5.debug_showValue(), 7)
        self.assertEquals(self.int6.debug_showValue(), 12)
        for i in range(0, len(self.randomInts)):
            self.assertEquals(UInt8(self.randomInts[i]).debug_showValue(), self.randomInts[i])

    def test_uint8_addition(self):
        addInt1 = self.int1 + self.int2  # 127 + 0 = 127
        addInt2 = self.int1 + self.int3  # 127 + 255 = 126 OVERFLOW
        addInt3 = self.int1 + self.int4  # 127 + 128 = 255
        addInt4 = self.int2 + self.int3  # 0 + 255 = 255
        addInt5 = self.int2 + self.int4  # 0 + 128 = 128
        addInt7 = self.int5 + self.int6  # 7 + 12 = 19
        addInt8 = self.int1 + self.int5  # 127 + 7 = 134
        addInt9 = self.int4 + self.int6  # 128 + 12 = 140

        self.assertTrue((addInt1 == UInt8(127)).debug__printAsBoolean())
        self.assertTrue((addInt2 == UInt8(126)).debug__printAsBoolean() and addInt2.testOverflow.debug__printAsBoolean())
        self.assertTrue((addInt3 == UInt8(255)).debug__printAsBoolean())
        self.assertTrue((addInt4 == UInt8(255)).debug__printAsBoolean())
        self.assertTrue((addInt5 == UInt8(128)).debug__printAsBoolean())
        self.assertTrue((addInt7 == UInt8(19)).debug__printAsBoolean())
        self.assertTrue((addInt8 == UInt8(134)).debug__printAsBoolean())
        self.assertTrue((addInt9 == UInt8(140)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) + UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] + self.randomInts[j]
                if expectedresult > 255 or expectedresult < 0:
                    self.assertTrue(result.testOverflow.debug__printAsBoolean())
                else:
                    self.assertEquals(result.debug_showValue(), expectedresult)


    def test_uint8_subtraction(self):
        subInt1 = self.int1 - self.int2  # 127 - 0 = 127
        subInt2 = self.int1 - self.int3  # 127 - 255 = 128 OVERFLOW
        subInt4 = self.int2 - self.int3  # 0 - 1 = 1 OVERFLOW
        subInt7 = self.int6 - self.int5  # 12 - 7 = 5
        subInt8 = self.int1 - self.int5  # 127 - 7 = 120
        subInt9 = self.int4 - self.int6  # 128 - 12 = 116

        self.assertTrue((subInt1 == UInt8(127)).debug__printAsBoolean())
        self.assertTrue((subInt2 == UInt8(128)).debug__printAsBoolean() and subInt2.testOverflow.debug__printAsBoolean() == True)
        self.assertTrue((subInt4 == UInt8(1)).debug__printAsBoolean() and subInt4.testOverflow.debug__printAsBoolean() == True)
        self.assertTrue((subInt7 == UInt8(5)).debug__printAsBoolean())
        self.assertTrue((subInt8 == UInt8(120)).debug__printAsBoolean())
        self.assertTrue((subInt9 == UInt8(116)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) - UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] - self.randomInts[j]
                if expectedresult > 255 or expectedresult < 0:
                    self.assertTrue(result.testOverflow.debug__printAsBoolean())
                else:
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_uint8_division(self):
        divInt1 = UInt8(29) / UInt8(3)  # 29 / 3 = 9
        divInt2 = UInt8(85) / UInt8(7)  # 85 / 7 = 12
        divInt3 = UInt8(0) / UInt8(12)  # 85 / 7 = 12

        self.assertTrue((divInt1 == UInt8(9)).debug__printAsBoolean())
        self.assertTrue((divInt2 == UInt8(12)).debug__printAsBoolean())
        self.assertTrue((divInt3 == UInt8(0)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) / UInt8(self.randomInts[j]))
                if self.randomInts[j] != 0:
                    expectedresult = self.randomInts[i] / self.randomInts[j]
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_uint8_mod(self):
        divInt1 = UInt8(29) % UInt8(3)  # 29 % 3 = 2
        divInt2 = UInt8(85) % UInt8(7)  # 85 % 7 = 1
        divInt3 = UInt8(0) % UInt8(12)  # 0 % 12 = 0

        self.assertTrue((divInt1 == UInt8(2)).debug__printAsBoolean())
        self.assertTrue((divInt2 == UInt8(1)).debug__printAsBoolean())
        self.assertTrue((divInt3 == UInt8(0)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) % UInt8(self.randomInts[j]))
                if self.randomInts[j] != 0:
                    expectedresult = self.randomInts[i] % self.randomInts[j]
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_uint8_eq_ne(self):
        eq_int1 = self.int1
        eq_int2 = self.int2
        eq_int3 = self.int3
        self.assertTrue((self.int1 != self.int2).debug__printAsBoolean())
        self.assertTrue((self.int1 != self.int3).debug__printAsBoolean())
        self.assertTrue((self.int1 == eq_int1).debug__printAsBoolean())
        self.assertTrue((self.int2 != self.int1).debug__printAsBoolean())
        self.assertTrue((self.int2 != self.int3).debug__printAsBoolean())
        self.assertTrue((self.int2 == eq_int2).debug__printAsBoolean())
        self.assertTrue((self.int3 != self.int2).debug__printAsBoolean())
        self.assertTrue((self.int3 != self.int1).debug__printAsBoolean())
        self.assertTrue((self.int3 == eq_int3).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) == UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] == self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_uint8_le(self):
        int1 = UInt8(125)
        inf_int1 = UInt8(122)
        sup_int1 = UInt8(127)

        self.assertTrue((inf_int1 <= int1).debug__printAsBoolean())
        self.assertTrue((-(sup_int1 <= int1)).debug__printAsBoolean())
        self.assertTrue((int1 <= int1).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) <= UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] <= self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_uint8_lt(self):
        int1 = UInt8(125)
        inf_int1 = UInt8(122)
        sup_int1 = UInt8(127)

        self.assertTrue((inf_int1 < int1).debug__printAsBoolean())
        self.assertTrue((-(sup_int1 < int1)).debug__printAsBoolean())
        self.assertTrue((-(int1 < int1)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) < UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] < self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_uint8_ge(self):
        int1 = UInt8(125)
        inf_int1 = UInt8(122)
        sup_int1 = UInt8(127)

        self.assertTrue((-(inf_int1 >= int1)).debug__printAsBoolean())
        self.assertTrue((sup_int1 >= int1).debug__printAsBoolean())
        self.assertTrue((int1 >= int1).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) >= UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] >= self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_uint8_gt(self):
        int1 = UInt8(125)
        inf_int1 = UInt8(122)
        sup_int1 = UInt8(127)

        self.assertTrue((-(inf_int1 > int1)).debug__printAsBoolean())
        self.assertTrue((sup_int1 > int1).debug__printAsBoolean())
        self.assertTrue((-(int1 > int1)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt8(self.randomInts[i]) > UInt8(self.randomInts[j]))
                expectedresult = self.randomInts[i] > self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_uint8_lshift(self):
        int1 = UInt8(42)
        shift_int1 = int1 << 1
        shift2_int1 = int1 << 2
        shift3_int1 = int1 << 3
        self.assertTrue((shift_int1.debug_showValue() == 84) )
        self.assertTrue((shift2_int1.debug_showValue() == 168))
        self.assertFalse((shift_int1.testOverflow.debug__printAsBoolean()))
        self.assertFalse((shift2_int1.testOverflow.debug__printAsBoolean()))
        self.assertTrue((shift3_int1.testOverflow.debug__printAsBoolean()))

    def test_uint8_rshift(self):
        int1 = UInt8(42)
        shift_int1 = int1 >> 1
        shift2_int1 = int1 >> 2
        self.assertTrue((shift_int1.debug_showValue() == 21))
        self.assertTrue((shift2_int1.debug_showValue() == 10))
