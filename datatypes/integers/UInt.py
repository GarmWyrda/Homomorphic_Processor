from datatypes.integers.UInt8 import *
from datatypes.bits.Bit import *
from error.BadRightOperand import BadRightOperand

class UInt:
    def __init__(self,value=0,ints=None,fixedSize=None,randomize=False):
        """Unsigned integer made from an array of UInt8s.
        We chose a convention for our arrays of bits :
        when we initiate a byte, the first bit of the array is the Most Significant Bit.
        The last one is the Least Significant Bit.

        :raises InstantiationError: if the array is too long/short
        """
        self.testOverflow = PlainBit(False)
        if ints != None:
            self.ints = ints
        elif isinstance(value, int) or isinstance(value,long):
            binary_repres = [int(x) for x in bin(value)[2:]]
            if(fixedSize != None):
                if(value <= 2**(fixedSize*8)):
                    lastintlength = len(binary_repres)%8
                    if(lastintlength != 0):
                        binary_repres = [0] * (8-lastintlength) + binary_repres
                    nbints = len(binary_repres) / 8
                    binary_repres = [0] * 8 * (fixedSize-nbints) + binary_repres
                    self.ints = []
                    for i in xrange(0,nbints):
                        bits = binary_repres[8 * i:(8 * i) + 8]
                        byte = ''
                        for j in bits:
                            byte += str(j)
                        int_value = int(byte, 2)
                        self.ints += [UInt8(int_value,randomize=randomize)]
                else:
                    raise InstantiationError("The given value cannot fit in the given dynamic")
            else:
                lastintlength = len(binary_repres) % 8
                if (lastintlength != 0):
                    binary_repres = [0] * (8 - lastintlength) + binary_repres
                nbints = len(binary_repres) / 8
                self.ints = []
                for i in xrange(0, nbints):
                    bits = binary_repres[8 * i:(8 * i) + 8]
                    byte = ''
                    for j in bits:
                        byte += str(j)
                    int_value = int(byte, 2)
                    self.ints += [UInt8(int_value, randomize=randomize)]

    def __abs__(self):
        """return the absolute value which is itself

        :returns: the absolute value (itself)
        :rtype: UInt
        """
        return self

    def __add__(self, other):
        """We wanted to append another 8-bit word if an overflow was detected, however we realized it could weaken the encryption.
        Therefore, we decided to return both the incorrect result and the carryOut bit to be properly handled by the user once decrypted.
        There may be some error in this function. When we add two UInt of different sizes, or when we add an UInt of value zero.

        /!\ Be aware of this potential error

        :param other: UInt
        :return: The sum of two UInts
        :rtype: UInt
        """
        if (isinstance(other, UInt)):
            len_self = len(self)
            len_other = len(other)
            effective_len = min(len_other,len_self)
            max_len = max(len_self,len_other)
            newUInts = [UInt8(0,randomize=False)] * max_len
            intCarry = UInt8(0,randomize=False)
            i = max_len-1
            for i in xrange(i, effective_len-1,-1):
                if (max_len == len_self and len_self != len_other):
                    newUInts[max_len - 1 - i] = self.ints[max_len - 1 - i] + intCarry
                    intCarry = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].carryOut])
                elif (max_len == len_other and len_self != len_other):
                    newUInts[max_len - 1 - i] = other.ints[max_len - 1 - i] + intCarry
                    intCarry = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].carryOut])
            if i==effective_len:
                i -= i
            for i in xrange(i,-1,-1):
                if (max_len == len_self and len_self != len_other):
                    newUInts[i+len_other-len_self+1] = self.ints[i+len_self-len_other] + other.ints[i] + intCarry
                    intCarry = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].carryOut])
                elif (max_len == len_other and len_self != len_other):
                    newUInts[i+len_self-len_other+1] = self.ints[i] + other.ints[i+len_other-len_self] + intCarry
                    intCarry = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].carryOut])
                else:
                    newUInts[i] = self.ints[i] + other.ints[i] + intCarry
                    intCarry = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].carryOut])
            newUInt = UInt(ints=newUInts)
            newUInt.testOverflow = newUInts[0].carryOut
            newUInt.ints = newUInt.ints
            return newUInt
        else:
            raise BadRightOperand('Right operand must be UInt')

    def __sub__(self, other):
        """This method will subtract 2 UInt.
        We override this operator to be able to write operations more easily

        :param other: Right Operand
        :type other: UInt
        :returns: the difference of the two UInt
        :rtype: UInt
        """
        if (isinstance(other, UInt)):
            len_self = len(self)
            len_other = len(other)
            effective_len = min(len_other, len_self)
            max_len = max(len_self, len_other)
            newUInts = [UInt8(0, randomize=False)] * max_len
            intBorrow = UInt8(0, randomize=False)
            for i in xrange(effective_len - 1, -1, -1):
                if (max_len == len_self and len_self != len_other):
                    newUInts[max_len - 1 -i] = self.ints[i + len_self - len_other] - other.ints[
                        i] - intBorrow
                    intBorrow = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].borrowOut])
                elif (max_len == len_other and len_self != len_other):
                    newUInts[max_len - 1 -i] = self.ints[i] - other.ints[
                        i + len_other - len_self] - intBorrow
                    intBorrow = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].borrowOut])
                else:
                    newUInts[i] = self.ints[i] - other.ints[i] - intBorrow
                    intBorrow = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].borrowOut])
            for i in xrange(max_len - 1, effective_len - 1, -1):
                if (max_len == len_self and len_self != len_other):
                    newUInts[max_len - 1 - i] = self.ints[max_len - 1 - i] - intBorrow
                    intBorrow = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].borrowOut])
                elif (max_len == len_other and len_self != len_other):
                    newUInts[max_len - 1 - i] = other.ints[max_len - 1 - i] - intBorrow
                    intBorrow = UInt8(bits=[PlainBit(False)] * 7 + [newUInts[i].borrowOut])

            newUInt = UInt(ints=newUInts)
            newUInt.testOverflow = newUInts[0].borrowOut
            newUInt.ints = newUInt.ints
            return newUInt
        else:
            raise BadRightOperand('Right operand must be UInt')

    def __len__(self):
        """returns the length of the array of UInt8s
        We override this operator to be able to write operations more easily

        :returns: an integer, the size of the array of UInt8s
        :rtype: integer
        """
        return len(self.ints)

    def __eq__(self, other):
        """test if two UInts are equal

        :param other: UInt to compare
        :type other: UInt
        :returns: True or False, in form of a CryptoBit or a PlainBit
        :rtype: CryptoBit or PlainBit
        :raises: BadRightOperand
        """
        if (isinstance(other,UInt)):
            tests = []
            effective_len = min(len(self),len(other))
            max_len = max(len(self),len(other))
            for i in xrange(0, effective_len):  # We check for every pair of bits, whether they're different or not
                tests += [self.ints[i] == other.ints[i]]  # If true then equals, If false then different
            if max_len != effective_len and len(self) == max_len:
                tests += [self.ints[i] == UInt8(0)]
            elif max_len != effective_len and len(other) == max_len:
                tests += [other.ints[i] == UInt8(0)]
            return reduce(lambda x, y: x * y, tests)
        else:
            raise BadRightOperand('Right operand must be UInt')

    def __ne__(self, other):
        """test if two UInts are not equal

        :param other: UInt to compare
        :type other: UInt
        :returns: True or False, in form of a CryptoBit or a PlainBit
        :rtype: CryptoBit or PlainBit
        :raises: BadRightOperand
        """
        return ~(self==other)

    def debug_showValue(self):
        """This method is for debug purposes only, it will reveal the integer value of the UInt

        :returns: an integer, the value of the UInt
        :rtype: integer
        """
        byte = ''
        for j in self.ints:
            for i in j.bits:
                if (isinstance(i, CryptoBit)):
                    byte += str(i.decrypt())
                else:
                    byte += str(i)
            if len(self.ints) >= 3:
                value = long(byte,2)
            else:
                value = int(byte, 2)
        return value