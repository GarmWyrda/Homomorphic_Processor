import unittest
from datatypes.integers.UInt import UInt
import random

class TestUIntMethods(unittest.TestCase):
    def setUp(self):
        self.int1 = UInt(127)
        self.int2 = UInt(0)
        self.int3 = UInt(255)
        self.int4 = UInt(65536)
        self.int5 = UInt(7)
        self.int6 = UInt(12)
        self.randomInts = []
        for i in range(0, 50):
            self.randomInts += [random.randint(0,4294967295)]

    def test_uint_debugshowValue(self):
        self.assertEquals(self.int1.debug_showValue(), 127)
        self.assertEquals(self.int2.debug_showValue(), 0)
        self.assertEquals(self.int3.debug_showValue(), 255)
        self.assertEquals(self.int4.debug_showValue(), 65536)
        self.assertEquals(self.int5.debug_showValue(), 7)
        self.assertEquals(self.int6.debug_showValue(), 12)
        for i in range(0, len(self.randomInts)):
            self.assertEquals(UInt(self.randomInts[i],fixedSize=4).debug_showValue(), self.randomInts[i])

    def test_uint_addition(self):
        addInt1 = self.int1 + self.int2  # 127 + 0 = 127
        addInt2 = self.int1 + self.int3  # 127 + 255 = 382
        addInt3 = self.int1 + self.int4  # 127 + 65536 = 65663
        addInt4 = self.int2 + self.int3  # 0 + 255 = 255
        addInt5 = self.int2 + self.int4  # 0 + 65536 = 65536
        addInt7 = self.int5 + self.int6  # 7 + 12 = 19
        addInt8 = self.int1 + self.int5  # 127 + 7 = 134
        addInt9 = self.int4 + self.int6  # 65536 + 12 = 65548

        self.assertTrue((addInt1 == UInt(127)).debug__printAsBoolean())
        self.assertTrue(addInt2.testOverflow.debug__printAsBoolean())
        self.assertTrue((addInt3 == UInt(65663)).debug__printAsBoolean())
        self.assertTrue((addInt4 == UInt(255)).debug__printAsBoolean())
        self.assertTrue((addInt5 == UInt(65536)).debug__printAsBoolean())
        self.assertTrue((addInt7 == UInt(19)).debug__printAsBoolean())
        self.assertTrue((addInt8 == UInt(134)).debug__printAsBoolean())
        self.assertTrue((addInt9 == UInt(65548)).debug__printAsBoolean())
        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt(self.randomInts[i],fixedSize=4) + UInt(self.randomInts[j],fixedSize=4))
                expectedresult = self.randomInts[i] + self.randomInts[j]
                if expectedresult <= 4294967295:
                        self.assertTrue(result.debug_showValue() == expectedresult)
                else:
                        self.assertTrue(result.testOverflow.debug__printAsBoolean())

    def test_uint_subtraction(self):
        subInt1 = UInt(255) - UInt(127)
        subInt2 = UInt(65000) - UInt(15000)
        subInt3 = UInt(15000) - UInt(15000)
        subInt4 = UInt(65) - UInt(127)
        subInt5 = UInt(65000) - UInt(100)

        self.assertTrue((subInt1 == UInt(128)).debug__printAsBoolean())
        self.assertTrue((subInt2 == UInt(50000)).debug__printAsBoolean())
        self.assertTrue((subInt3 == UInt(0)).debug__printAsBoolean())
        self.assertTrue(subInt4.testOverflow.debug__printAsBoolean())
        self.assertTrue((subInt5 == UInt(64900)).debug__printAsBoolean())

        for i in range(0, len(self.randomInts)):
            for j in range(0, len(self.randomInts)):
                result = (UInt(self.randomInts[i], fixedSize=4) - UInt(self.randomInts[j], fixedSize=4))
                expectedresult = self.randomInts[i] - self.randomInts[j]
                if expectedresult >= 0:
                    self.assertEquals(result.debug_showValue(), expectedresult)
                else:
                    self.assertTrue(result.testOverflow.debug__printAsBoolean())