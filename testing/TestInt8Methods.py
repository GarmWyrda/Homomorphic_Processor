import unittest
from datatypes.integers.Int8 import *

class TestInt8Methods(unittest.TestCase):
    def setUp(self):
        self.int1 = Int8(127)  # '01111111' = 127
        self.int2 = Int8(0)  # '00000000' = 0
        self.int3 = -Int8(1)  # '11111111' = -1
        self.int4 = -Int8(128) # '10000000' = -128
        self.int5 = Int8(7)  # '00000111' = 7
        self.int6 = -Int8(11)  # '11110101' = -11
        self.randomInts = []
        for i in range(0,50):
            self.randomInts += [random.randint(-128,127)]

    def test_int8_debugshowValue(self):
        self.assertEquals(self.int1.debug_showValue(),127)
        self.assertEquals(self.int2.debug_showValue(), 0)
        self.assertEquals(self.int3.debug_showValue(), -1)
        self.assertEquals(self.int4.debug_showValue(), -128)
        self.assertEquals(self.int5.debug_showValue(), 7)
        self.assertEquals(self.int6.debug_showValue(), -11)
        for i in range(0,len(self.randomInts)):
            self.assertEquals(Int8(self.randomInts[i]).debug_showValue(),self.randomInts[i])

    def test_int8_addition(self):
        addInt1 = self.int1 + self.int2  # 127 + 0 = 127
        addInt2 = self.int1 + self.int3  # 127 + -1 = 126
        addInt3 = self.int1 + self.int4  # 127 + -128 = -1
        addInt4 = self.int2 + self.int3  # 0 + -1 = -1
        addInt5 = self.int2 + self.int4  # 0 + -128 = -128
        addInt6 = self.int3 + self.int3  # -1 + -1 = -2
        addInt7 = self.int5 + self.int6  # 7 + -11 = -4
        addInt8 = self.int1 + self.int5  # 127 + 7 = -120 OVERFLOW BUT CANNOT BE DETECTED DUE TO CRYPTOBIT
        addInt9 = self.int4 + self.int6  # -128 + -11 = 117 OVERFLOW BUT CANNOT BE DETECTED DUE TO CRYPTOBIT
        self.assertTrue((addInt1 == Int8(127)).debug__printAsBoolean())
        self.assertTrue((addInt2 == Int8(126)).debug__printAsBoolean())
        self.assertTrue((addInt3 == -Int8(1)).debug__printAsBoolean())
        self.assertTrue((addInt4 == -Int8(1)).debug__printAsBoolean())
        self.assertTrue((addInt5 == -Int8(128)).debug__printAsBoolean())
        self.assertTrue((addInt6 == -Int8(2)).debug__printAsBoolean())
        self.assertTrue((addInt7 == -Int8(4)).debug__printAsBoolean())
        self.assertTrue(addInt8.debug_showValue() == -122 and addInt8.testOverflow.debug__printAsBoolean() == True)
        self.assertTrue(addInt9.debug_showValue() == 117 and addInt9.testOverflow.debug__printAsBoolean() == True)
        for i in range(0, len(self.randomInts)):
            for j in range(0,len(self.randomInts)):
                result = (Int8(self.randomInts[i]) + Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i]+self.randomInts[j]
                if expectedresult > 127 or expectedresult < -128:
                    self.assertTrue(result.testOverflow.debug__printAsBoolean())
                else:
                    self.assertEquals(result.debug_showValue(),expectedresult)

    def test_int8_subtraction(self):
        subInt1 = self.int1 - self.int2  # 127 - 0 = 127
        subInt2 = self.int1 - self.int3  # 127 - (-1) = -128 OVERFLOW
        subInt4 = self.int2 - self.int3  # 0 - 1 = 1
        subInt5 = self.int2 - self.int4  # 0 - 128 = -128
        subInt6 = self.int3 - self.int3  # -1 - (-1) = 0
        subInt7 = self.int5 - self.int6  # 7 - (-11) = 18
        subInt8 = self.int1 - self.int5  # 127 - 7 = 120
        subInt9 = self.int4 - self.int6  # -128 - (-11) = -117

        self.assertTrue((subInt1 == Int8(127)).debug__printAsBoolean())
        self.assertTrue((subInt2 == -Int8(128)).debug__printAsBoolean() and subInt2.testOverflow.debug__printAsBoolean() == True)
        self.assertTrue((subInt4 == Int8(1)).debug__printAsBoolean())
        self.assertTrue((subInt5 == -Int8(128)).debug__printAsBoolean())
        self.assertTrue((subInt6 == Int8(0)).debug__printAsBoolean())
        self.assertTrue((subInt7 == Int8(18)).debug__printAsBoolean())
        self.assertTrue((subInt8 == Int8(120)).debug__printAsBoolean())
        self.assertTrue((subInt9 == -Int8(117)).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) - Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] - self.randomInts[j]
                if expectedresult > 127 or expectedresult < -128:
                    self.assertTrue(result.testOverflow.debug__printAsBoolean())
                else:
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_int8_division(self):
        divInt1 = Int8(29) / Int8(3)  # 29 / 3 = 9
        divInt2 = Int8(85) / Int8(7)  # 85 / 7 = 12
        divInt3 = Int8(0) / Int8(12)  # 0 / 12 = 0

        self.assertTrue((divInt1 == Int8(9)).debug__printAsBoolean())
        self.assertTrue((divInt2 == Int8(12)).debug__printAsBoolean())
        self.assertTrue((divInt3 == Int8(0)).debug__printAsBoolean())

        divInt1 = -Int8(29) / Int8(3)  # 29 / 3 = 9
        divInt2 = Int8(85) / -Int8(7)  # 85 / 7 = 12
        divInt3 = -Int8(24) / -Int8(12)  # 24 / 12 = 2


        self.assertTrue((divInt1 == -Int8(9)).debug__printAsBoolean())
        self.assertTrue((divInt2 == -Int8(12)).debug__printAsBoolean())
        self.assertTrue((divInt3 == Int8(2)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) / Int8(self.randomInts[j]))
                if self.randomInts[j] != 0 and self.randomInts[i] != -128:
                    expectedresult = int(float(self.randomInts[i]) / self.randomInts[j])
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_int8_mod(self):
        divInt1 = Int8(29) % Int8(3)  # 29 % 3 = 2
        divInt2 = Int8(85) % Int8(7)  # 85 % 7 = 1
        divInt3 = Int8(0) % Int8(12)  # 0 % 12 = 0

        self.assertTrue((divInt1 == Int8(2)).debug__printAsBoolean())
        self.assertTrue((divInt2 == Int8(1)).debug__printAsBoolean())
        self.assertTrue((divInt3 == Int8(0)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) % Int8(self.randomInts[j]))
                if self.randomInts[j] != 0:
                    expectedresult = abs(self.randomInts[i]) % abs(self.randomInts[j])
                    self.assertEquals(result.debug_showValue(), expectedresult)

    def test_int8_abs(self):
        for i in range(0, len(self.randomInts)):
            result = abs(Int8(self.randomInts[i]))
            expectedresult = abs(self.randomInts[i])
            if (expectedresult != 128):
                self.assertEquals(result.debug_showValue(),expectedresult)
            else:
                self.assertTrue(result.testOverflow.debug__printAsBoolean())


    def test_int8_eq_ne(self):
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
                result = (Int8(self.randomInts[i]) == Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] == self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_int8_le(self):
        int1 = Int8(value=125);
        inf_int1 = Int8(value=122);
        sup_int1 = Int8(value=127);
        int2 = -Int8(value=125);
        sup_int2 = -Int8(122);
        inf_int2 = -Int8(127);

        self.assertTrue((inf_int1 <= int1).debug__printAsBoolean())
        self.assertTrue((-(sup_int1 <= int1)).debug__printAsBoolean())
        self.assertTrue((int1 <= int1).debug__printAsBoolean())
        self.assertTrue((inf_int2 <= int2).debug__printAsBoolean())
        self.assertTrue((-(sup_int2 <= int2)).debug__printAsBoolean())
        self.assertTrue((int2 <= int2).debug__printAsBoolean())
        self.assertTrue((-(int1 <= int2)).debug__printAsBoolean())
        self.assertTrue((int2 <= int1).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) <= Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] <= self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_int8_lt(self):
        int1 = Int8(125)
        inf_int1 = Int8(122)
        sup_int1 = Int8(127)
        int2 = -Int8(125)
        sup_int2 = -Int8(122)
        inf_int2 = -Int8(127)

        self.assertTrue((inf_int1 < int1).debug__printAsBoolean())
        self.assertTrue((-(sup_int1 < int1)).debug__printAsBoolean())
        self.assertTrue((-(int1 < int1)).debug__printAsBoolean())
        self.assertTrue((inf_int2 < int2).debug__printAsBoolean())
        self.assertTrue((-(sup_int2 < int2)).debug__printAsBoolean())
        self.assertTrue((-(int2 < int2)).debug__printAsBoolean())
        self.assertTrue((-(int1 < int2)).debug__printAsBoolean())
        self.assertTrue((int2 < int1).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) < Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] < self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_int8_ge(self):
        int1 = Int8(125)
        inf_int1 = Int8(122)
        sup_int1 = Int8(127)
        int2 = -Int8(125)
        sup_int2 = -Int8(122)
        inf_int2 = -Int8(127)


        self.assertTrue((-(inf_int1 >= int1)).debug__printAsBoolean())
        self.assertTrue((sup_int1 >= int1).debug__printAsBoolean())
        self.assertTrue((int1 >= int1).debug__printAsBoolean())
        self.assertTrue((-(inf_int2 >= int2)).debug__printAsBoolean())
        self.assertTrue((sup_int2 >= int2).debug__printAsBoolean())
        self.assertTrue((int2 >= int2).debug__printAsBoolean())
        self.assertTrue((int1 >= int2).debug__printAsBoolean())
        self.assertTrue(-(int2 <= int1).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) >= Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] >= self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_int8_gt(self):
        int1 = Int8(125)
        inf_int1 = Int8(122)
        sup_int1 = Int8(127)
        int2 = -Int8(125)
        sup_int2 = -Int8(122)
        inf_int2 = -Int8(127)

        self.assertTrue((-(inf_int1 > int1)).debug__printAsBoolean())
        self.assertTrue((sup_int1 > int1).debug__printAsBoolean())
        self.assertTrue((-(int1 > int1)).debug__printAsBoolean())
        self.assertTrue((-(inf_int2 > int2)).debug__printAsBoolean())
        self.assertTrue((sup_int2 > int2).debug__printAsBoolean())
        self.assertTrue((-(int2 > int2)).debug__printAsBoolean())
        self.assertTrue((int1 > int2).debug__printAsBoolean())
        self.assertTrue(-(int2 < int1).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (Int8(self.randomInts[i]) > Int8(self.randomInts[j]))
                expectedresult = self.randomInts[i] > self.randomInts[j]
                self.assertEquals(result.debug__printAsBoolean(), expectedresult)

    def test_int8_lshift(self):
        int1 = Int8(42)
        int2 = -Int8(42)
        shift_int1 = int1 << 1
        shift2_int1 = int1 << 2
        shift_int2 = int2 << 1
        shift2_int2 = int2 << 2
        self.assertTrue((shift_int1.debug_showValue() == 84))
        self.assertTrue((shift2_int1.debug_showValue() == 40 and shift2_int1.testOverflow.debug__printAsBoolean()))
        self.assertTrue((shift_int2.debug_showValue() == -84))
        self.assertTrue((shift2_int2.debug_showValue() == -40 and shift2_int2.testOverflow.debug__printAsBoolean()))

    def test_int8_rshift(self):
        int1 = Int8(42)
        int2 = -Int8(42)
        shift_int1 = int1 >> 1
        shift2_int1 = int1 >> 2
        shift_int2 = int2 >> 1
        shift2_int2 = int2 >> 2
        self.assertTrue((shift_int1.debug_showValue() == 21))
        self.assertTrue((shift2_int1.debug_showValue() == 10))
        self.assertTrue((shift_int2.debug_showValue() == -21))
        self.assertTrue((shift2_int2.debug_showValue() == -11))