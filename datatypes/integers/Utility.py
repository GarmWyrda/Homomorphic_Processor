from datatypes.bits.Bit import *

def completeSubOnOneBit(minuend, subtrahend, borrowIn):
    """This method will subtract 2 Bits.

    :param minuend: Left Operand
    :type minuend: Bit (CryptoBit or PlainBit)
    :param subtrahend: Right Operand
    :type subtrahend: Bit (CryptoBit or PlainBit)
    :param borrowIn: The borrowIn for the subtraction. A Bit (CryptoBit or PlainBit)
    :type borrowIn: Bit (CryptoBit or PlainBit)
    :returns: A bit : the result of XOR between the two Bits. And a Bit that is the BorrowIn
    :rtype: Bit, Bit
    """
    if (isinstance(minuend, Bit) & isinstance(subtrahend, Bit) & isinstance(borrowIn, Bit)):
        difference = (minuend ^ subtrahend) ^ borrowIn
        borrowOut = -minuend * subtrahend + -(minuend ^ subtrahend)*borrowIn
        return difference, borrowOut
        Bit.XOR()
    else:
        raise BitwiseOperationError('The given value was not a Bit')


def completeAddOnOneBit(firstBit, secondBit, carry) :
    """This method will add 2 Bits.

    :param firstBit: Left Operand
    :type firstBit: Bit (CryptoBit or PlainBit)
    :param secondBit: Right Operand
    :type secondBit: Bit (CryptoBit or PlainBit)
    :param carry: The carry for the addition. A Bit (CryptoBit or PlainBit)
    :type carry: Bit (CryptoBit or PlainBit)
    :returns: A bit : the result of XOR between the two Bits. And a Bit that is the carry
    :rtype: Bit, Bit
    """
    if (isinstance(firstBit,Bit) & isinstance(secondBit, Bit) & isinstance(carry, Bit)):
        resultBit = carry.XOR(firstBit.XOR(secondBit))
        tempValue = firstBit.XOR(secondBit)
        tempValue2 = firstBit.AND(secondBit)
        tempValue3 = carry.AND(tempValue)
        carryOut = tempValue3.OR(tempValue2)

        return resultBit,carryOut
    else:
        raise BitwiseOperationError('The given value was not a Bit')


'''
#This method is the recurrence method for multiplying two UInt8 or two Int8, with the Karatsuba algorithm
#However it is not yet properly functional

def multRecurrence(arrayX, arrayY):
    m = max(len(arrayX), len(arrayY))

    if m ==0 :
        m = 1

    if (len(arrayX) == 0 | len(arrayY) == 0):
        return [PlainBit(False)]

    if (len(arrayX) == 1 & len(arrayY) ==1):
        if (isinstance(arrayX[0], Bit) & isinstance(arrayY[0], Bit)):
            return [arrayX[0].AND(arrayY[0])]

    m2 = m/2

    # x = x1*(2**m) + x0
    # y = y1*(2**m) + y0

    if (len(arrayX) != len(arrayY)):
        if (len(arrayX) < len(arrayY)):
            for i in xrange(len(arrayX), m-1):
                arrayX.insert(0, PlainBit(False))
        else:
            for i in xrange(len(arrayY), m-1):
                arrayY.insert(0, PlainBit(False))

    x1, x0 = arrayX[:m2], arrayX[m2:]
    y1, y0 = arrayY[:m2], arrayY[m2:]

    # Upper half of the bits
    z2 = multRecurrence(x1, y1)
    # Lower half of the bits
    z0 = multRecurrence(x0, y0)

    # ( x1 + x0 )( y1 + y0 )

    sumX = []
    sumY = []
    carryX = PlainBit(False)
    carryY = PlainBit(False)

    for j in xrange(min(len(x1), len(x0))-1,-1, -1):
        tempValueX,carryX=completeAddOnOneBit(x1[j], x0[j], carryX)
        sumX.insert(0, tempValueX)

    if (len(x1) != len(x0)):
        if(len(x1) > len(x0)):
            sumX.insert(0, x1[len(x1)-1])
        else:
            sumX.insert(0, x0[len(x0)-1])

    if (carryX.bit == 1):
        sumX.insert(0, PlainBit(True))

    for j in xrange(min(len(y1), len(y0))-1,-1, -1):
        tempValueY,carryY=completeAddOnOneBit(y1[j], y0[j], carryY)
        sumY.insert(0, tempValueY)

    if (len(y1) != len(y0)):
        if(len(y1) > len(y0)):
            sumY.insert(0, y1[len(y1)-1])
        else:
            sumY.insert(0, y0[len(y0)-1])

    if (carryY.bit == 1):
        sumY.insert(0, PlainBit(True))

    z1 = multRecurrence(sumX, sumY)


    # z1 - z2 - z0
    sizeMaxZ = max (len(z1), len(z2), len(z0))
    while(len(z1) < sizeMaxZ ):
        z1.insert(0, PlainBit(False))
    while(len(z2) < sizeMaxZ ):
        z2.insert(0, PlainBit(False))
    while(len(z0) < sizeMaxZ ):
        z0.insert(0, PlainBit(False))

    result = []
    borrow = PlainBit(False)

    for i in xrange (sizeMaxZ -1, -1, -1):
        tempValueResult, borrow = completeSubOnOneBit(z1, z2, borrow)
        result.insert(0, tempValueResult)

    borrow = PlainBit(False)
    for i in xrange (sizeMaxZ -1, -1, -1):
        tempValueResult, borrow = completeSubOnOneBit(result, z0, borrow)
        result.insert(0, tempValueResult)

    # TODO : next, the result is z2 shifted 2*m2 + z1 shifted m2 + z0
    # faut-il mettre le resulat sous forme de tableau de 16 bits a partir de la ?
    # Cela poserai-t-il un probleme dans la recurrence ensuite ?
'''
