import random

from datatypes.bits.Bit import *
from Utility import *



class Int8:
    def __init__(self,value=0,bits=None,randomize=False):
        """Signed integer made from an array of 8 Bits. (from -128 to 127)
        the representation is in two's complement
        We chose a convention for our arrays of bits :
        when we initiate a byte, the first bit of the array is the Most Significant Bit.
        The last one is the Least Significant Bit.
        Thus, bits[0] = MSB, bits[bits.length()] = LSB

        :raises InstantiationError: if the array is too long/short
        """
        self.testOverflow = PlainBit(False)
        self.carryOut = PlainBit(False)
        self.borrowOut = PlainBit()
        if bits != None:
            if(len(bits) < 8):
                raise InstantiationError('Cannot instanciate a 8-Bit integer, not enough bits given : ' + str(len(bits)) + ' given')
            elif(len(bits) > 8):
                raise InstantiationError('Cannot instanciate a 8-Bit integer, too many bits given : ' + str(len(bits)) + ' given')
            else:
                self.bits = bits
        elif isinstance(value,int) and not(randomize):
            binary_repres = [int(x) for x in bin(abs(value))[2:]]
            self.bits = []
            self.bits += [0] * (8 - len(binary_repres))
            self.bits = self.bits + binary_repres
            for i in range(0, len(self.bits)):
                if i > len(self.bits)-1 or self.bits[i] == 0:
                    self.bits[i] = PlainBit(False)
                else:
                    self.bits[i] = PlainBit(True)
            if (value < 0):
                self.bits = (-self).bits
        elif isinstance(value,int) and randomize:
            binary_repres = [int(x) for x in bin(abs(value))[2:]]
            self.bits = []
            self.bits += [0] * (8 - len(binary_repres))
            self.bits = self.bits + binary_repres
            for i in range(0, len(self.bits)):
                if i > len(self.bits) - 1 or self.bits[i] == 0:
                    if(random.random() >= 0.5):
                        self.bits[i] = PlainBit(False)
                    else:
                        self.bits[i] = CryptoBit(False)
                else:
                    if (random.random() >= 0.5):
                        self.bits[i] = PlainBit(True)
                    else:
                        self.bits[i] = CryptoBit(True)
            if(value < 0):
                self.bits = (-self).bits

    def __abs__(self):
        """Returns the absolute value. Since our integers are coded in two's complement, absolute value of -128 cannot be represented. However if self equals -128 the result will have its testOverflow bit set to
        indicate that an overflowError has occurred.

        :returns: the absolute value, except for -128 for which it returns 0.
        :rtype: Int8
        """
        boolTest = self.bits[0]
        tmpInt = Int8(bits=([boolTest] * len(self)))
        firstInt = tmpInt & -self
        secondInt = ~tmpInt & self
        overflowBit = (self == -Int8(128))
        firstInt.testOverflow = overflowBit
        secondInt.testOverflow = overflowBit
        return firstInt | secondInt

    def __add__(self, other):
        """This method will add 2 Int8.
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: Int8
        :returns: the sum of the two Int8
        :rtype: Int8
        """
        if(isinstance(other,Int8)):
            answerInt = Int8(bits=[PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False),PlainBit(False), PlainBit(False), PlainBit(False)])
            carry = PlainBit(False)
            carries = []
            for i in xrange(7, -1, -1):
                answerInt.bits[i],carry=completeAddOnOneBit(self.bits[i], other.bits[i], carry)
                carries += [carry]
            testOverflow = carries[len(carries)-1].XOR(carries[len(carries)-2])
            answerInt.carryOut = carries[len(carries)-1] + self.carryOut + other.carryOut
            answerInt.testOverflow = testOverflow + self.testOverflow + other.testOverflow
            return answerInt

    def __and__(self, other):
        """bitwise AND operation, returns an Int8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: Int8
        :returns: bitwise AND operation, returns an Int8
        :rtype: Int8
        """
        bits = []
        for i in range (0,len(self)):
            bits += [self.bits[i] * other.bits[i]]
        return Int8(bits=bits)

    def __or__(self, other):
        """bitwise OR operation, returns an Int8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: Int8
        :returns: bitwise OR operation, returns an Int8
        :rtype: Int8
        """
        bits = []
        for i in range(0, len(self)):
            bits += [self.bits[i] + other.bits[i]]
        return Int8(bits=bits)

    def __xor__(self, other):
        """bitwise XOR operation, returns an Int8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: Int8
        :returns: bitwise XOR operation, returns an Int8
        :rtype: Int8
        """
        bits = []
        for i in range(0, len(self)):
            bits += [self.bits[i] ^ other.bits[i]]
        return Int8(bits=bits)

    def __neg__(self):
        """returns the opposite Int8
        We override this operator to be able to write operations more easily

        :returns: opposite Int8, except for -128
        :rtype: Int8
        """
        newInt = self - Int8(1)
        bits = []
        for i in xrange(0, len(newInt.bits)):
            bits.append(-newInt.bits[i])
        return Int8(bits=bits)

    def __invert__(self):
        """returns the one's complement Int8
        We override this operator to be able to write operations more easily

        :returns: the one's complement Int8
        :rtype: Int8
        """
        newInt = self
        bits = []
        for i in xrange(0, len(newInt.bits)):
            bits.append(~newInt.bits[i])
        return Int8(bits=bits)

    def __lshift__(self, other):
        """returns an Int8 that its bits were shifted to the left
        We override this operator to be able to write operations more easily
        Note that this operation performs an arithmetic shift and not a binary shift
        This means that the sign bit is ignored by the operation, and it will not be shifted as a consequence

        :param other: integer to know how much we shift
        :type other: integer
        :returns: an Int8, its bits were shifted to the left
        :rtype: Int8
        """
        newBits = []
        testOverflow = PlainBit(False)
        newBits += [self.bits[0]]
        for i in xrange(1,len(self)-other):
            newBits += [self.bits[i+other]]
        for i in xrange(i+1,len(self)):
            testOverflow += self.bits[len(self)-i]
            newBits += [PlainBit(False)]
        newInt = Int8(bits=newBits)
        newInt.testOverflow = testOverflow
        return newInt

    def __rshift__(self, other):
        """returns an Int8 that its bits were shifted to the right
        We override this operator to be able to write operations more easily
        Note that this operation performs an arithmetic shift and not a binary shift
        This means that the sign bit is ignored by the operation, and it will not be shifted as a consequence

        :param other: integer to know how much we shift
        :type other: integer
        :returns: an Int8, its bits were shifted to the right
        :rtype: Int8
        """
        newBits = []
        newBits += [self.bits[0]]
        for i in xrange(1, other+1):
            newBits += [self.bits[0]]
        for i in xrange(i + 1, len(self)):
            newBits += [self.bits[i-other]]
        newInt = Int8(bits=newBits)
        return newInt

    def __le__(self, other):
        """test if an Int8 is lesser or equal than/to another one

        :param other: Int8 to compare
        :type other: Int8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        tests_eq = []
        tests_inf = []
        tests = []
        for i in xrange(1, len(self)):
            tests_eq += [-(-self.bits[i] * other.bits[i] + self.bits[i] * -(other.bits[i]))]
            tests_inf += [-self.bits[i] * other.bits[i]]
            for j in xrange(0, i):
                tests_inf[i-1] += tests_inf[j]
            tests += [tests_eq[i-1] + tests_inf[i-1]]
        test = reduce(lambda x, y: x * y, tests)

        return -other.bits[0]*self.bits[0] + test*(self.bits[0]*other.bits[0] + -self.bits[0]*-other.bits[0])

    def __lt__(self, other):
        """test if an Int8 is lesser than another one

        :param other: Int8 to compare
        :type other: Int8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        tests_eq = []
        tests_inf = []
        tests = []
        for i in xrange(1, len(self)):
            tests_eq += [-(-self.bits[i] * other.bits[i] + self.bits[i] * -(other.bits[i]))]
            tests_inf += [-self.bits[i] * other.bits[i]]
            for j in xrange(0, i):
                tests_inf[i - 1] += tests_inf[j]
            tests += [tests_eq[i - 1] + tests_inf[i - 1]]
        test = reduce(lambda x, y: x * y, tests)
        test_eq = reduce(lambda x, y: x * y, tests_eq)

        return -other.bits[0] * self.bits[0] + test * -test_eq * (self.bits[0] * other.bits[0] + -self.bits[0] * -other.bits[0])

    def __ge__(self, other):
        """test if an Int8 is greater or equal than/to another one

        :param other: Int8 to compare
        :type other: Int8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        return -(self < other)

    def __gt__(self, other):
        """test if an Int8 is greater than another one

        :param other: Int8 to compare
        :type other: Int8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        return -(self <= other)

    def __eq__(self, other):
        """test if two Int8 are equal

        :param other: Int8 to compare
        :type other: Int8
        :returns: True or False, in form of a CryptoBit or a PlainBit
        :rtype: CryptoBit or PlainBit
        """
        tests = []
        for i in xrange(0,len(self)): #We check for every pair of bits, whether they're different or not
            tests += [-(self.bits[i] ^ other.bits[i])] #If true then equals, If false then different
        #We must now check that not a single one of thoses bits is set to false
        #For that we will use and operator, if even a single bit is set to false, then it will return false.
        return reduce(lambda x, y: x*y,tests)

    def __ne__(self, other):
        """test if two Int8 are not equal

        :param other: Int8 to compare
        :type other: Int8
        :returns: True or False, in form of a CryptoBit or a PlainBit
        :rtype: CryptoBit or PlainBit
        """
        tests = []
        for i in range(0, len(self)):  # We check for every pair of bits, whether they're different or not
            tests += [-(self.bits[i] ^ other.bits[i])]  # If true then equals, If false then different
        # We must now check that not a single one of thoses bits is set to false
        # For that we will use and operator, if even a single bit is set to false, then it will return false.
        return -reduce(lambda x, y: x*y,tests)

    def __len__(self):
        """returns the length of the array of bits of an Int8 (which is always 8)
        We override this operator to be able to write operations more easily

        :returns: an integer, the size of the array of bits of Int8 (which is 8)
        :rtype: integer
        """
        return len(self.bits)

    def __sub__(self,other):
        """This method will substract 2 Int8.
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: Int8
        :returns: the difference of the two Int8
        :rtype: Int8
        """
        if (isinstance(other, Int8)):
            answerInt = Int8(bits=[PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False),PlainBit(False), PlainBit(False)])
            borrow = PlainBit(False)
            borrows = []
            for i in xrange(7, -1, -1):
                answerInt.bits[i], borrow = completeSubOnOneBit(self.bits[i], other.bits[i], borrow)
                borrows += [borrow]
            testOverflow = borrows[len(borrows) - 1].XOR(borrows[len(borrows) - 2])
            answerInt.borrowOut = borrows[len(borrows) - 1] + self.borrowOut + other.borrowOut
            answerInt.testOverflow = testOverflow
            return answerInt

    def __div__(self, other):
        """This method will divide 2 Int8.
        We override this operator to be able to write operations more easily
        DIVISION IS ROUNDED TOWARDS 0 since it uses the division from the absolutes value of the arguments given.
        This means that there might be an isssue when using -128 as an operand, cf __abs__ function

        :param other: Right Operand
        :type other: Int8
        :returns: the result of division of the two Int8
        :rtype: Int8
        """
        #We will first take absolute values from operands and divide them, once this is done we will correct the sign of the result if needed
        dividend = self.toUInt8()
        divisor = other.toUInt8()
        sign = (self.bits[0] ^ other.bits[0])
        mask = Int8(bits=([sign]*len(self)))
        result = (dividend / divisor).toInt8()
        return (mask & (-result)) + (~mask & result)

    def __mod__(self, other):
        """This method will return the remainder of the division between 2 Int8.
        We override this operator to be able to write operations more easily
        As a convention the result will be positive and will be the rest from the euclidian division of the absolute values of the two arguments

        :param other: Right Operand
        :type other: Int8
        :returns: the remainder of the division between two Int8
        :rtype: Int8
        """
        # We will first take absolute values from operands and divide them, once this is done we will correct the sign of the result if needed
        dividend = self.toUInt8()
        divisor = other.toUInt8()
        result = (dividend % divisor).toInt8()
        return result

    def toUInt8(self):  # This will return abs value of integer as Unsigned Integer
        """returns the abs value of integer as Unisgned Integer (UInt8)

        :returns: abs value of integer as UInt8
        :rtype: UInt8
        """
        from UInt8 import UInt8
        return UInt8(bits=abs(self).bits)

    def debug_showValue(self):
        """This method is for debug purposes only, it will reveal the integer value of the Int8

        :returns: an integer, the value of the Int8
        :rtype: integer
        """
        byte = ''
        for i in self.bits:
            if (isinstance(i, CryptoBit)):
                byte += str(i.decrypt())
            else:
                byte += str(i)

        value = int(byte, 2)
        if (value & (1 << (len(byte) - 1))) != 0:
            value = value - (1 << len(byte))
        return value

    def encrypt(self):
        """This method makes every PlainBit into CryptoBit

        """
        if (isinstance(self.testOverflow, PlainBit)):
            self.testOverflow = self.testOverflow.encrypt()
        if (isinstance(self.carryOut, PlainBit)):
            self.carryOut = self.carryOut.encrypt()
        if (isinstance(self.borrowOut, PlainBit)):
            self.borrowOut = self.borrowOut.encrypt()
        for i in xrange(0, len(self.bits)):
            if isinstance(self.bits[i], PlainBit):
                self.bits[i] = self.bits[i].encrypt()

    def decrypt(self):
        """This method makes every CryptoBit into PlainBit

        """
        if (isinstance(self.testOverflow, CryptoBit)):
            self.testOverflow = self.testOverflow.decrypt()
        if (isinstance(self.carryOut, CryptoBit)):
            self.carryOut = self.carryOut.decrypt()
        if (isinstance(self.borrowOut, CryptoBit)):
            self.borrowOut = self.borrowOut.decrypt()
        for i in xrange(0, len(self.bits)):
            if isinstance(self.bits[i], CryptoBit):
                self.bits[i] = self.bits[i].decrypt()

    def __repr__(self):
        """Return representation of Int8

        :returns: integer, the value of the Int8
        :rtype: integer
        """
        byte = ''
        for i in self.bits:
            byte += str(i)
        value = int(byte, 2)
        return value
