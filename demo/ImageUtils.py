from datatypes.integers.UInt8 import UInt8
from PIL import Image
import numpy as np
import pickle

def dump(data,path):
    """This will write a python object to a file, in our case we will use it to transfer the data between bob and alice

    :param data: The python object to save
    :type data: Python Object
    :param path: Path to save the object
    :type path: String
    """
    f = open(path, 'w')
    pickle.dump(data,f)
    f.close()

def load(path):
    """ This function will read a python object written with pickel from a file

    :param path: Path to file to read
    :type path: String
    :return: Python object retrieved from the file
    :rtype: Python Object
    """
    f = open(path, 'r')
    data = pickle.load(f)
    f.close()
    return data

def encode(path):
    """This function will take an RGB image of bit depth 24 and encode all of its data into our datatypes

    :param path: This is the path to the image, image must be of type RGB and and a 24 bit depth
    :type path: String
    :returns: Pixels Matrix encoded with our datatypes
    :rtype: 2D Matrix of UInt8 tuple of size 3
    """
    img = Image.open(path)
    width = img.width
    height = img.height
    pixels = []
    for x in xrange(0, height):
        pixels += [[]]
        for y in xrange(0, width):
            r, g, b = img.getpixel((x, y))
            r = UInt8(r)
            g = UInt8(g)
            b = UInt8(b)
            pixels[x] += [(r, g, b)]
    img.close()
    return pixels

def decode(pixels,path):
    """This function will take a 2D Matrix of 3-sized tuple UInt8 and return the corresponding image

    :param pixels: This is the pixels data
    :type pixels: 2D Matrix of UInt8 tuple of size 3
    :param path: This is the path that the image will be saved on
    :type path: String
    :returns: Pixels Matrix encoded with our datatypes
    :rtype: 2D Matrix of UInt8 tuple of size 3
    """
    width = len(pixels)
    height = len(pixels[0])
    decoded_pixels = []
    for x in xrange(0, height):
        decoded_pixels += [[]]
        for y in xrange(0, width):
            r = pixels[y][x][0]
            g = pixels[y][x][1]
            b = pixels[y][x][2]
            new_r = r.showValue()
            new_g = g.showValue()
            new_b = b.showValue()
            decoded_pixels[x] += [(new_r,new_g,new_b)]
    decoded_pixels = np.asarray(decoded_pixels)
    decoded_pixels = decoded_pixels.astype('uint8')
    newImage = Image.fromarray(decoded_pixels,'RGB')
    newImage.save(path)
    newImage.close()

def encrypt(pixels):
    """This function will take a 2D Matrix of 3-sized tuple UInt8 and encrypt it

    :param pixels: This is the pixels data
    :type pixels: 2D Matrix of UInt8 tuple of size 3
    :returns: Encrypted Pixels Matrix encoded with our datatypes
    :rtype: 2D Matrix of UInt8 tuple of size 3
    """
    width = len(pixels)
    height = len(pixels[0])
    encrypted_pixels = []
    for x in xrange(0, height):
        encrypted_pixels += [[]]
        for y in xrange(0, width):
            r = pixels[x][y][0]
            g = pixels[x][y][1]
            b = pixels[x][y][2]
            r.encrypt()
            g.encrypt()
            b.encrypt()
            encrypted_pixels[x] += [(r,g,b)]
    return encrypted_pixels

def decrypt(pixels):
    """This function will take an encrypted 2D Matrix of 3-sized tuple UInt8 and decrypt it

    :param pixels: This is the pixels data
    :type pixels: 2D Matrix of UInt8 tuple of size 3
    :returns: Decrypted Pixels Matrix encoded with our datatypes
    :rtype: 2D Matrix of UInt8 tuple of size 3
    """
    width = len(pixels)
    height = len(pixels[0])
    decrypted_pixels = []
    for x in xrange(0, height):
        decrypted_pixels += [[]]
        for y in xrange(0, width):
            r = pixels[x][y][0]
            g = pixels[x][y][1]
            b = pixels[x][y][2]
            r.decrypt()
            g.decrypt()
            b.decrypt()
            decrypted_pixels[x] += [(r,g,b)]
    return decrypted_pixels

def negate(pixels):
    """This function will take a 2D Matrix of 3-sized tuple UInt8 and invert its values

    :param pixels: This is the pixels data
    :type pixels: 2D Matrix of UInt8 tuple of size 3
    :returns: Negated Pixels Matrix
    :rtype: 2D Matrix of UInt8 tuple of size 3
    """
    width = len(pixels)
    height = len(pixels[0])
    negated_pixels = []
    for x in xrange(0, height):
        negated_pixels += [[]]
        for y in xrange(0, width):
            r = pixels[x][y][0]
            g = pixels[x][y][1]
            b = pixels[x][y][2]
            new_r = ~r
            new_g = ~g
            new_b = ~b
            negated_pixels[x] += [(new_r,new_g,new_b)]
    return negated_pixels