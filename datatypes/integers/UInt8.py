import random

from datatypes.bits.Bit import *
from Utility import *



class UInt8:

    def __init__(self,value=0,bits=None,randomize=False):
        """Unsigned integer made from an array of 8 Bits. (from 0 to 255)
        We chose a convention for our arrays of bits :
        when we initiate a byte, the first bit of the array is the Most Significant Bit.
        The last one is the Least Significant Bit.
        Thus, bits[0] = MSB, bits[bits.length()] = LSB
        Please note that this class can also be used to represent characters for example.
        Since we cannot access the data, its meaning is irrelevant to us, therefore UInt8 might as well be considered as Char

        :raises InstantiationError: if the array is too long/short
        """
        self.testOverflow = PlainBit(False)
        self.carryOut = PlainBit(False)
        self.borrowOut = PlainBit(False)
        if bits != None:
            if(len(bits) < 8):
                raise InstantiationError('Cannot instanciate a 8-Bit integer, not enough bits given : ' + str(len(bits)) + ' given')
            elif(len(bits) > 8):
                raise InstantiationError('Cannot instanciate a 8-Bit integer, too many bits given : ' + str(len(bits)) + ' given')
            else:
                self.bits = bits
        elif isinstance(value,int) and not(randomize):
            binary_repres = [int(x) for x in bin(value)[2:]]
            self.bits = []
            self.bits += [0] * (8 - len(binary_repres))
            self.bits = self.bits + binary_repres
            for i in range(0, len(self.bits)):
                if i > len(self.bits)-1 or self.bits[i] == 0:
                    self.bits[i] = PlainBit(False)
                else:
                    self.bits[i] = PlainBit(True)
        elif isinstance(value,int) and randomize:
            binary_repres = [int(x) for x in bin(value)[2:]]
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

    def __abs__(self):
        """return the absolute value which is itself

        :returns: the absolute value (itself)
        :rtype: UInt8
        """
        return self

    def __add__(self, other):
        """This method will add 2 UInt8.
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt8
        :returns: the sum of the two UInt8
        :rtype: UInt8
        """
        if(isinstance(other,UInt8)):
            answerInt = UInt8(bits=[PlainBit(False),PlainBit(False),PlainBit(False),PlainBit(False),PlainBit(False),PlainBit(False),PlainBit(False),PlainBit(False)])
            carry = PlainBit(False)
            carries = []
            for i in xrange(7, -1, -1):
                answerInt.bits[i],carry=completeAddOnOneBit(self.bits[i], other.bits[i], carry)
                carries += [carry]
            answerInt.carryOut = carries[len(carries)-1] + self.carryOut + other.carryOut
            answerInt.testOverflow = answerInt.carryOut
            return answerInt

    def __mul__(self, other):
        """This method will multiply 2 UInt8.
        We override this operator to be able to write operations more easily
        The multiplication seems to work fine, however there may be a problem in the addition of two UInt
        Since the addition od two UInt is used in this method there may be some error
        see addition of UInts of different sizes.

        :param other: Right Operand
        :type other: UInt8
        :returns: the product of the two UInt8 which is an UInt
        :rtype: UInt
        """
        from datatypes.integers.UInt import UInt
    #    if (isinstance(other, UInt8)):
    #        arrayX = self.bits
    #        arrayY = other.bits
    #        return UInt8(bits = multRecurrence(arrayX, arrayY))
        if (isinstance(other, UInt8)):
            result = []
            for i in xrange(7, -1, -1):
                arrayTemp = []
                result += [arrayTemp]
                for k in xrange (0, 7-i):
                        result[7-i].insert(0, PlainBit(False))
                for j in xrange(7, -1, -1):
                    result[7-i].insert(0, self.bits[i] * other.bits[j])

            for l in xrange(0, 8):
                while (len(result[l]) < 16):
                    result[l].insert(0, PlainBit(False))


            # We split results in two array of size 8. The form is (resultXb append resultXa) . Where X is the line number
            result1a = UInt8(bits=result[0][8:])
            result1b = UInt8(bits=result[0][:8])
            result1UInt = UInt(ints = [result1b, result1a])

            result2a = UInt8(bits=result[1][8:])
            result2b = UInt8(bits=result[1][:8])
            result2UInt = UInt(ints = [result2b, result2a])

            result3a = UInt8(bits=result[2][8:])
            result3b = UInt8(bits=result[2][:8])
            result3UInt = UInt(ints = [result3b, result3a])

            result4a = UInt8(bits=result[3][8:])
            result4b = UInt8(bits=result[3][:8])
            result4UInt = UInt(ints = [result4b, result4a])

            result5a = UInt8(bits=result[4][8:])
            result5b = UInt8(bits=result[4][:8])
            result5UInt = UInt(ints = [result5b, result5a])

            result6a = UInt8(bits=result[5][8:])
            result6b = UInt8(bits=result[5][:8])
            result6UInt = UInt(ints = [result6b, result6a])

            result7a = UInt8(bits=result[6][8:])
            result7b = UInt8(bits=result[6][:8])
            result7UInt = UInt(ints = [result7b, result7a])

            result8a = UInt8(bits=result[7][8:])
            result8b = UInt8(bits=result[7][:8])
            result8UInt = UInt(ints = [result8b, result8a])

            resultFinal = result1UInt + result2UInt + result3UInt + result4UInt + result5UInt + result6UInt + result7UInt + result8UInt

            return resultFinal

    def __and__(self, other):
        """bitwise AND operation, returns an UInt8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt8
        :returns: bitwise AND operation, returns an UInt8
        :rtype: UInt8
        """
        bits = []
        for i in range (0,len(self)):
            bits += [self.bits[i] * other.bits[i]]
        return UInt8(bits=bits)

    def __or__(self, other):
        """bitwise OR operation, returns an UInt8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt8
        :returns: bitwise OR operation, returns an UInt8
        :rtype: UInt8
        """
        bits = []
        for i in range(0, len(self)):
            bits += [self.bits[i] + other.bits[i]]
        return UInt8(bits=bits)

    def __xor__(self, other):
        """bitwise XOR operation, returns an UInt8
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt8
        :returns: bitwise XOR operation, returns an UInt8
        :rtype: UInt8
        """
        bits = []
        for i in range(0, len(self)):
            bits += [self.bits[i] ^ other.bits[i]]
        return UInt8(bits=bits)

    def __invert__(self):
        """returns the one's complement UInt8
        We override this operator to be able to write operations more easily

        :returns: the one's complement UInt8
        :rtype: UInt8
        """
        newInt = self
        bits = []
        for i in xrange(0, len(newInt.bits)):
            bits.append(~newInt.bits[i])
        return UInt8(bits=bits)

    def __neg__(self):
        """raise RuntimeError

        :raises: RuntimeErro
        """
        raise RuntimeError()

    def __lshift__(self, other):
        """returns an UInt8 that its bits were shifted to the left
        We override this operator to be able to write operations more easily
        Note that this operation performs an arithmetic shift and not a binary shift

        :param other: integer to know how much we shift
        :type other: integer
        :returns: an UInt8, its bits were shifted to the left
        :rtype: UInt8
        """
        newBits = []
        testOverflow = PlainBit(False)
        for i in xrange(0,len(self)-other):
            newBits += [self.bits[i+other]]
        for i in xrange(i+1,len(self)):
            testOverflow += self.bits[len(self)-1-i]
            newBits += [PlainBit(False)]
        newInt = UInt8(bits=newBits)
        newInt.testOverflow = testOverflow
        return newInt

    def __rshift__(self, other):
        """returns an UInt8 that its bits were shifted to the right
        We override this operator to be able to write operations more easily
        Note that this operation performs an arithmetic shift and not a binary shift, this means
        that the new bit inserted will be equal to the MSB

        :param other: integer to know how much we shift
        :type other: integer
        :returns: an UInt8, its bits were shifted to the right
        :rtype: UInt8
        """
        newBits = []
        for i in xrange(0, other+1):
            newBits += [self.bits[0]]
        for i in xrange(i + 1, len(self)):
            newBits += [self.bits[i-other]]
        newInt = UInt8(bits=newBits)
        return newInt

    def __le__(self, other):
        """test if an UInt8 is lesser or equal than/to another one

        :param other: UInt8 to compare
        :type other: UInt8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        tests_eq = []
        tests_inf = []
        tests = []
        for i in xrange(0, len(self)):
            tests_eq += [-(-self.bits[i] * other.bits[i] + self.bits[i] * -(other.bits[i]))]
            tests_inf += [-self.bits[i] * other.bits[i]]
            for j in xrange(0, i):
                tests_inf[i] += tests_inf[j]
            tests += [tests_eq[i] + tests_inf[i]]
        test = reduce(lambda x, y: x * y, tests)
        return test

    def __lt__(self, other):
        """test if an UInt8 is lesser than another one

        :param other: UInt8 to compare
        :type other: UInt8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        tests_eq = []
        tests_inf = []
        tests = []
        for i in xrange(0, len(self)):
            tests_eq += [-(-self.bits[i] * other.bits[i] + self.bits[i] * -(other.bits[i]))]
            tests_inf += [-self.bits[i] * other.bits[i]]
            for j in xrange(0, i):
                tests_inf[i] += tests_inf[j]
            tests += [tests_eq[i] + tests_inf[i]]
        test = reduce(lambda x, y: x * y, tests)
        test_eq = reduce(lambda x, y: x * y, tests_eq)
        return test * -test_eq

    def __ge__(self, other):
        """test if an UInt8 is greater or equal than/to another one

        :param other: UInt8 to compare
        :type other: UInt8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        return -(self < other)

    def __gt__(self, other):
        """test if an UInt8 is greater than another one

        :param other: UInt8 to compare
        :type other: UInt8
        :returns: CryptoBit or PlainBit (true or false)
        :rtype: CryptoBit or PlainBit
        """
        return -(self <= other)

    def __eq__(self, other):
        """test if two UInt8 are equal

        :param other: UInt8 to compare
        :type other: UInt8
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
        """test if two UInt8 are not equal

        :param other: UInt8 to compare
        :type other: UInt8
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
        """returns the length of the array of bits of an UInt8 (which is always 8)
        We override this operator to be able to write operations more easily

        :returns: an integer, the size of the array of bits of UInt8 (which is 8)
        :rtype: integer
        """
        return len(self.bits)

    def __sub__(self,other):
        """This method will subtract 2 UInt8.
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt8
        :returns: the difference of the two UInt8
        :rtype: UInt8
        """
        if (isinstance(other, UInt8)):
            answerInt = UInt8(bits=
                [PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False), PlainBit(False),
                 PlainBit(False), PlainBit(False)])
            borrow = PlainBit(False)
            borrows = []
            for i in xrange(7, -1, -1):
                answerInt.bits[i], borrow = completeSubOnOneBit(self.bits[i], other.bits[i], borrow)
                borrows += [borrow]
            answerInt.borrowOut = borrows[len(borrows) - 1] + self.borrowOut + other.borrowOut
            answerInt.testOverflow = answerInt.borrowOut
            return answerInt

    def __div__(self, other):
        """This method will divide 2 UInt8.
        We override this operator to be able to write operations more easily
        Note that by convention, the result will always be rounded towards 0

        :param other: Right Operand
        :type other: UInt8
        :returns: the result of division of the two UInt8
        :rtype: UInt8
        """
        if(isinstance(other,UInt8)):
            remainder = UInt8(0)
            quotient = UInt8(0)
            dividend = self
            divisor = other

            for i in xrange(0, len(self)):
                remainder = remainder << 1
                remainder.bits[len(remainder)-1] = dividend.bits[0]
                boolTest = remainder >= divisor
                quotient = (quotient << 1)
                quotient.bits[len(quotient)-1] = boolTest
                tmpInt = UInt8(bits=[boolTest]*len(self))#This integer's bits will all be equal to boolTest, therefore in any case we can and it with the variable divisor, and it will emulate the code above
                remainder = remainder - (tmpInt & divisor)
                dividend = dividend << 1
            return quotient
        else:
            raise OpNotAllowedError("Cannot divide with something else than integer")

    def __mod__(self, other):
        """This method will return the remainder of the division between 2 UInt8.
        We override this operator to be able to write operations more easily
        Note that by convention : The result will always be positive

        :param other: Right Operand
        :type other: UInt8
        :returns: the remainder of the division between two UInt8
        :rtype: UInt8
        """
        if (isinstance(other, UInt8)):
            remainder = UInt8(0)
            quotient = UInt8(0)
            dividend = self
            divisor = other

            for i in xrange(0, len(self)):
                remainder = remainder << 1
                remainder.bits[len(remainder) - 1] = dividend.bits[0]
                boolTest = remainder >= divisor
                quotient = (quotient << 1)
                quotient.bits[len(quotient) - 1] = boolTest
                tmpInt = UInt8(bits=[boolTest] * len(
                    self))
                remainder = remainder - (tmpInt & divisor)
                dividend = dividend << 1
            return remainder
        else:
            raise OpNotAllowedError("Cannot divide with something else than integer")

    def toInt8(
            self):  # This will return the value as a signed integer, however overflow might occur, if it happens, the variable testOverflow of the returned Integer will be set to true
        """returns the value of integer as Signed Integer (Int8)
        overflow might occur, if this is the case, the variable testOverflow of the returned Integer will be set to true

        :returns: value of integer as Int8
        :rtype: Int8
        """
        from Int8 import Int8
        newInt = Int8(bits=self.bits)
        newInt.testOverflow = self.bits[0]
        newInt.bits[0] = PlainBit()
        return newInt

    def debug_showValue(self):
        """This method is for debug purposes only, it will reveal the integer value of the UInt8

        :returns: an integer, the value of the UInt8
        :rtype: integer
        """
        byte = ''
        for i in self.bits:
            if (isinstance(i, CryptoBit)):
                byte += str(i.decrypt())
            else:
                byte += str(i)
        value = int(byte, 2)
        return value

    def encrypt(self):
        """This method makes every PlainBit into CryptoBit

        """
        if(isinstance(self.testOverflow,PlainBit)):
            self.testOverflow = self.testOverflow.encrypt()
        if (isinstance(self.carryOut, PlainBit)):
            self.carryOut = self.carryOut.encrypt()
        if (isinstance(self.borrowOut, PlainBit)):
            self.borrowOut = self.borrowOut.encrypt()
        for i in xrange(0,len(self.bits)):
            if isinstance(self.bits[i],PlainBit):
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
        """Return representation of UInt8

        :returns: integer, the value of the UInt8
        :rtype: integer
        """
        byte = ''
        for i in self.bits:
            byte += str(i)
        value = int(byte, 2)
        return str(value)

    def showValue(self):
        """This method will show the 'fake' value. It will read the value of the CryptoBit

        :returns: an integer, the 'fake' value of the UInt8
        :rtype: integer
        """
        byte = ''
        for i in self.bits:
            byte += str(i)
        value = int(byte, 2)
        return value