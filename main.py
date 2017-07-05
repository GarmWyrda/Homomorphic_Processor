from testing.TestBitsMethods import *
from testing.TestInt8Methods import *
from testing.TestUInt8Methods import *
from testing.TestUIntMethods import *


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBitsMethods))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestInt8Methods))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUInt8Methods))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUIntMethods))
result = unittest.TextTestRunner(verbosity=2).run(suite)

'''
int1 = UInt8(value=54)
int2 = UInt8(value=19)

int3 = int1 * int2

int3.debug_showValue()
'''
