# -*- coding:utf-8
import numpy as np
import struct
import matplotlib.pyplot as plt

train_images_filename = '/home/steve/Desktop/mnist_programs/data/train-images.idx3-ubyte'
train_label_filename = '/home/steve/Desktop/mnist_programs/data/train-labels.idx1-ubyte'
test_images_filename = '/home/steve/Desktop/mnist_programs/data/t10k-images.idx3-ubyte'
test_label_filename = '/home/steve/Desktop/mnist_programs/data/t10k-labels.idx1-ubyte'

big_endian = '>'
four_bytes = 'IIII'
two_bytes = 'II'
picture_bytes = '784B'
label_bytes = '1B'

def get_images(filename):
	bin_file = open(filename,'rb')
	buf = bin_file.read()#all the file are put into memory
	bin_file.close()# release the measure of operating system
	index = 0
	magic, num_images, num_rows, num_colums = struct.unpack_from(big_endian+four_bytes, buf,index)

	index += struct.calcsize(big_endian + four_bytes)   # TODO why not multy 4?
	print num_images

	images = [] #temp images as tuple
	for x in range(num_images):
	    im = struct.unpack_from(big_endian + picture_bytes, buf, index)
	    index += struct.calcsize(big_endian + picture_bytes)
	    im = list(im)
	    for i in range(len(im)) :
	        if im[i] > 1:
	            im[i] = 1
	            
	    images.append(im)
	#a = np.array(images)
	return images
	
	
def get_label(filename):
	    bin_file = open(filename,'rb')
	    buf = bin_file.read()
	    bin_file.close()
	    index = 0
	    magic, num_items= struct.unpack_from(big_endian + two_bytes,buf,index)
	    
	    index += struct.calcsize(big_endian + two_bytes)
	    print num_items
	    labels = [];
	    for x in range(num_items):
		        im = struct.unpack_from(big_endian + label_bytes, buf,index)
		        index += struct.calcsize(big_endian + label_bytes)
		        labels.append(im[0])#whether the same as im ?
	    return labels

def get_train_images():
	    return get_images(train_images_filename)

def get_train_labels():
	    return get_label(train_label_filename)

def get_test_images():
	    return get_images(test_images_filename)

def get_test_labels():
	    return get_label(test_label_filename)