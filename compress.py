from PIL import Image
import numpy

#open the image and return 3 matrices, each corresponding to one channel (R, G, B)
def openImage(imagePath):
    imOriginal = Image.open(imagePath)
    im = numpy.array(imOriginal)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue, imOriginal]


#compress the matrix of a single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = numpy.linalg.svd(channelDataMatrix)
    k = min(singularValuesLimit, len(sChannel))  # Adjust k based on the actual number of singular values

    leftSide = numpy.matmul(uChannel[:, 0:k], numpy.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = numpy.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    
    return aChannelCompressed

#main program
print('*** Image Compression Using SVD ***')
aRed, aGreen, aBlue, originalImage = openImage('/Users/apricuz/Downloads/grayscale-v1.jpg')


imageWidth = 512
imageHeight = 512

singularValuesLimit = 100

aRedCompressed = compressSingleChannel(aRed, singularValuesLimit)
aGreenCompressed = compressSingleChannel(aGreen, singularValuesLimit)
aBlueCompressed = compressSingleChannel(aBlue, singularValuesLimit)

imr = Image.fromarray(aRedCompressed, mode=None)
img = Image.fromarray(aGreenCompressed, mode=None)
imb = Image.fromarray(aBlueCompressed, mode=None)

newImage = Image.merge("RGB", (imr,img,imb))

# originalImage.show()
newImage.show()