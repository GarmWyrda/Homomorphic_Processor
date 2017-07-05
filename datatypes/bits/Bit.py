from errors.InstantiationError import *
from errors.BitwiseOperationError import *
from errors.OpNotAllowedError import *
import random

class Bit:
    """General purpose bit, might be encrypted or not.
    This is an abstract class and therefore might not be instantiated
    """
    def __init__(self):
        """

        :raises InstantiationError: if called.
        """
        raise InstantiationError('Cannot instanciate a Bit, instanciate either a PlainBit or CryptoBit instead')
    def AND(self,other):
        """This method should be overridden in subclasses to perform a logical AND operation between two bits.

        :raises OpNotAllowedError: if called
        """
        raise OpNotAllowedError("Cannot do operation on Bit instance")
    def OR(self,other):
        """This method should be overridden in subclasses to perform a logical OR operation between two bits.

        :raises OpNotAllowedError: if called
        """
        raise OpNotAllowedError("Cannot do operation on Bit instance")
    def NOT(self):
        """ This method should be overridden in subclasses to perform a logical NOT operation on self.

        :raises OpNotAllowedError: if called
        """
        raise OpNotAllowedError("Cannot do operation on Bit instance")
    def XOR(self,other):
        """This method should be overridden in subclasses to perform a logical XOR operation between two bits.

        :raises OpNotAllowedError: if called
        """
        raise OpNotAllowedError("Cannot do operation on Bit instance")
    def debug__printAsBoolean(self):
        """This method is for debug purposes only, it will reveal the Boolean value in the bit

        :raises OpNotAllowedError: if called
        """
        raise OpNotAllowedError("Cannot do operation on Bit instance")

    def __add__(self, other):
        """This method just calls the OR operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.OR(other)

    def __mul__(self, other):
        """This method just calls the AND operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.AND(other)

    def __and__(self, other):
        """This method just calls the AND operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.AND(other)

    def __neg__(self):
        """This method just calls the NOT operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.NOT()

    def __or__(self, other):
        """This method just calls the OR operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.OR(other)

    def __xor__(self, other):
        """This method just calls the XOR operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.XOR(other)

    def __invert__(self):
        """This method just calls the NOT operation
        We overrode this operator to be able to write logic equations more easily
        """
        return self.NOT()

class PlainBit(Bit):
    """This class represents a bit which is not encrypted
    Its goal is just to wrap a boolean and allow us to do operation with CryptoBits
    """
    def __init__(self,value = False):
        """

        :param value: Defines the value of the bit, defaults to False
        :type value: Boolean
        """
        if(value):
            self.bit = True
        else:
            self.bit = False

    def __repr__(self):
        """Return representation of Plain Bit

        :returns: 1 if bit is set to True, 0 otherwise
        """
        if self.bit:
            return '1'
        else:
            return '0'

    def __eq__(self, other):
        """Test if two bits are Equals

        :param other: Bit to compare
        :type other: PlainBit
        :returns: True if bits are equal, False otherwise
        :rtype: Boolean
        :raises OpNotAllowedError: if other is not of type PlainBit
        """
        if(isinstance(other,PlainBit)):
            if self.bit == other.bit:
                return True
            else:
                return False
        else:
            raise OpNotAllowedError("Cannot test directly if a PlainBit equals a thing that is not a CryptoBit")

    def encrypt(self):
        """Encrypts the PlainBit

        :returns: CryptoBit containing the value of the PlainBit
        :rtype: CryptoBit
        """
        return CryptoBit(self.bit)

    def AND(self,other):
        """Performs a logical AND operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the AND operation
        :rtype: PlainBit if right operand is PlainBit, CryptoBit if right operand is CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                if self.bit and other.bit:
                    return PlainBit(True)
                else:
                    return PlainBit(False)
            elif isinstance(other,CryptoBit):
                return other.AND(self)

    def OR(self,other):
        """Performs a logical OR operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the OR operation
        :rtype: PlainBit if right operand is PlainBit, CryptoBit if right operand is CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                if self.bit or other.bit:
                    return PlainBit(True)
                else:
                    return PlainBit(False)
            elif isinstance(other,CryptoBit):
                return other.OR(self)


    def XOR(self, other):
        """Performs a logical XOR operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the XOR operation
        :rtype: PlainBit if right operand is PlainBit, CryptoBit if right operand is CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                if (self.bit or other.bit) and not(self.bit and other.bit):
                    return PlainBit(True)
                else:
                    return PlainBit(False)
            elif isinstance(other,CryptoBit):
                return other.XOR(self)


    def NOT(self):
        """Performs a logical NOT operation on self

        :returns: A bit containing the result of the NOT operation
        :rtype: PlainBit
        """
        return PlainBit(not(self.bit))

    def debug__printAsBoolean(self):
        """This method is for debug purposes only, it will reveal the Boolean value in the bit

        :returns: Boolean value of bit
        :rtype: Boolean
        """
        return bool(self.bit)


class CryptoBit(Bit):
    """Emulated homomorphic bit, we forbid ourselves to read the bit value.
    Upon creation, the apparent value of the bit will be random.
    The plain value is stored in the __bit member.
    """
    def __init__(self,value=False,verbose=True):
        """

        :param value:(optional) Defines the value of the bit, defaults to False
        :param verbose:(optional) Defines whether or not the bit will print a message upon refresh, defaults to False
        """
        if(value):
            self.__bit = True
        else:
            self.__bit = False
        self.verbose = verbose #If set to true, it will display when refreshed
        self.noise = 0
        self.threshold = 10
        if random.random() >= 0.5:
            self.bit = True
        else:
            self.bit = False

    def __repr__(self):
        """Return representation of Crypto

        Note that this value is not the real value but a random value, so you should not rely on it
        :returns: 1 if bit is set to True, 0 otherwise
        """
        if self.bit:
            return '1'
        else:
            return '0'

    def __eq__(self, other):
        """Test if two bits are Equals, however since two Cryptobits cannot be compared directly, this function always returns an exception

        :raises OpNotAllowedError: if other is not of type PlainBit
        """
        raise OpNotAllowedError("A CryptoBit cannot be compared directly")

    def refresh(self):
        """Resets the bit's noise, if the bit's verbose attribute is set, then it will print a message

        """
        self.noise = 0
        if self.verbose:
            print  str(self.__class__) + "  was refreshed"

    def setNoise(self,value=0):
        """Sets the bit's noise, if the noise is above the threshold, then it will trigger a refresh

        :param value: The value that should be set, defaults to 0
        :type value: int
        """
        self.noise = value
        if self.noise >= self.threshold:
            self.refresh()


    def decrypt(self):
        """Decrypt the CryptoBit

        :returns: PlainBit containing the value of the CryptoBit
        :rtype: PlainBit
        """
        return PlainBit(self.__bit)

    def AND(self,other):
        """Performs a logical AND operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the AND operation
        :rtype: CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                rightoperand = other.encrypt()
            elif isinstance(other,CryptoBit):
                rightoperand = other;
            if self.__bit and rightoperand.__bit:
                newBit = CryptoBit(True)
                newBit.setNoise(self.noise + rightoperand.noise)
                return newBit
            else:
                newBit = CryptoBit(False)
                newBit.setNoise(self.noise + rightoperand.noise)
                return newBit

    def OR(self,other):
        """Performs a logical OR operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the OR operation
        :rtype: CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                rightoperand = other.encrypt()
            elif isinstance(other,CryptoBit):
                rightoperand = other;
            if self.__bit or rightoperand.__bit:
                newBit = CryptoBit(True)
                newBit.setNoise(self.noise + rightoperand.noise + 3)
                return newBit
            else:
                newBit = CryptoBit(False)
                newBit.setNoise(self.noise + rightoperand.noise + 3)
                return newBit

    def NOT(self):
        """Performs a logical NOT operation on self

        :returns: A bit containing the result of the NOT operation
        :rtype: CryptoBit
        """
        newBit = CryptoBit(not(self.__bit))
        newBit.setNoise(self.noise + 1)
        return newBit

    def XOR(self,other):
        """Performs a logical XOR operation between self and other

        :param other: RightOperand
        :type other: PlainBit or CryptoBit
        :returns: A bit containing the result of the XOR operation
        :rtype: CryptoBit
        :raises BitwiseOperationError: if the right operand is not a Bit
        """
        if not(isinstance(other,Bit)):
            raise BitwiseOperationError('The given value was not a Bit')
        else:
            if isinstance(other,PlainBit):
                rightoperand = other.encrypt()
            elif isinstance(other,CryptoBit):
                rightoperand = other
            if (self.__bit or rightoperand.__bit) and not(self.__bit and rightoperand.__bit):
                newBit = CryptoBit(True)
                newBit.setNoise(max(self.noise,rightoperand.noise) + 1)
                return newBit
            else:
                newBit = CryptoBit(False)
                newBit.setNoise(max(self.noise,rightoperand.noise) + 1)
                return newBit

    def debug__printAsBoolean(self):
        """This method is for debug purposes only, it will reveal the Boolean value in the bit

        :returns: Boolean value of bit
        :rtype: Boolean
        """
        return bool(self.decrypt().bit)