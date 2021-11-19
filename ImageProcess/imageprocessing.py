from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
from array import *

boxBlurKernel = [[0.1111,0.1111,0.1111],
                 [0.1111,0.1111,0.1111],
                 [0.1111,0.1111,0.1111]]

gaussianBlurKernel = [[0.0625,0.1250,0.0625],
                      [0.1250,0.2500,0.1250],
                      [0.0625,0.1250,0.0625]]

edgedetectionkernel = [[-1.0000,-1.0000,-1.0000],
                       [-1.0000,8.0000,-1.0000],
                       [-1.0000,-1.0000,-1.0000]]

sharpenkernel = [[0.0000,-1.0000,0.0000],
                 [-1.0000,5.0000,-1.0000],
                 [0.0000,-1.0000,0.0000]]

print("Enter the matrix elements")
lengthrow = int(input("Enter Number of rows: "))

matrix = []
print("Enter the complete row in order")
for i in range(0,lengthrow):
    i = i + 1
    iprow = input(f'row{i}:')
    matrix.append([int(j) for j in iprow.split(',')])
print(matrix)
ip = matrix

loop = 'true'
while (loop == 'true'):
    print("1. Box Blur")
    print("2. Gaussian Blur")
    print("3. Edge Detection")
    print("4. Sharpen")
    print("5. All")
    print("6. Change input matrix")
    print("7. Quit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            f = ndimage.convolve(ip, boxBlurKernel)
            print('Box Blur matrix: ')
            print(f)
            plt.subplot(121), plt.imshow(ip), plt.title('Original image')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(f), plt.title('Box Blur filter image')
            plt.xticks([]), plt.yticks([])
            plt.imshow(f, interpolation='nearest')
            plt.show()
            print('=' * 250)
            break
        if choice == '2':
            f = ndimage.convolve(ip, gaussianBlurKernel)
            print('Gaussian Blur matrix: ')
            print(f)
            plt.subplot(121), plt.imshow(ip), plt.title('Original image')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(f), plt.title('Gaussian Blur filter image')
            plt.xticks([]), plt.yticks([])
            plt.imshow(f, interpolation='nearest')
            plt.show()
            print('=' * 250)
            break
        if choice == '3':
            f = ndimage.convolve(ip, edgedetectionkernel)
            print('Edge Detection matrix: ')
            print(f)
            plt.subplot(121), plt.imshow(ip), plt.title('Original image')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(f), plt.title('Edge Detection filter image')
            plt.xticks([]), plt.yticks([])
            plt.imshow(f, interpolation='nearest')
            plt.show()
            print('=' * 250)
            break
        if choice == '4':
            f = ndimage.convolve(ip, sharpenkernel)
            print('Sharpen filter matrix: ')
            print(f)
            plt.subplot(121), plt.imshow(ip), plt.title('Original image')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(f), plt.title('Sharpen filter image')
            plt.xticks([]), plt.yticks([])
            plt.imshow(f, interpolation='nearest')
            plt.show()
            print('=' * 250)
            break
        if choice == '5':
            fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5)
            ax1.imshow(ip, interpolation='nearest')
            ax1.set_title('Original image')
            f = ndimage.convolve(ip, boxBlurKernel)
            print('Box Blur matrix: ')
            print(f)
            ax2.imshow(f, interpolation='nearest')
            ax2.set_title('Box Blur filter image')

            f = ndimage.convolve(ip, gaussianBlurKernel)
            print('Gaussian Blur matrix: ')
            print(f)
            ax3.imshow(f, interpolation='nearest')
            ax3.set_title('Gaussian Blur filter image')

            f = ndimage.convolve(ip, edgedetectionkernel)
            print('Edge Detection matrix: ')
            print(f)
            ax4.imshow(f, interpolation='nearest')
            ax4.set_title('Edge Detection filter image')

            f = ndimage.convolve(ip, sharpenkernel)
            print('Sharpen filter matrix: ')
            print(f)
            ax5.imshow(f, interpolation='nearest')
            ax5.set_title('Sharpen filter image')

            plt.show()
            print('=' * 250)
            break
        if choice == '6':
            print("Enter the matrix elements")
            lengthrow = int(input("Enter Number of rows: "))
            matrix = []
            print("Enter the complete row in order")
            for i in range(0, lengthrow):
                i = i + 1
                iprow = input(f'row{i}:')
                matrix.append([int(j) for j in iprow.split(',')])
            print(matrix)
            ip = matrix
            break
        if choice == '7':
            loop = 'false'
            break
