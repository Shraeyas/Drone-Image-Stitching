from operator import itemgetter
from PIL import Image
import ExifData, XMPData
import glob
import os


#input = open("datasets/imageData.txt","w+")

'''
:param fileName: Name of the pose data file in string form e.g. "datasets/imageData.txt"
:param imageDirectory: Name of the directory where images arer stored in string form e.g. "datasets/images/"
:return: dataMatrix: A NumPy ndArray contaning all of the pose data. Each row stores 6 floats containing pose information in XYZYPR form
allImages: A Python List of NumPy ndArrays containing images.
'''


def write():

    input = open("datasets/imageData.txt","w+")
    input.close()

    input = open("datasets/imageData.txt","a+")

    for image in sorted(glob.glob('datasets/images/*')):
        exif_data = ExifData.get_exif_data(Image.open(image))
        lat, lon = ExifData.get_lat_lon(exif_data)

        alt, roll, yaw, pitch = XMPData.xmp(image)
        #print lon, lat, alt, yaw, pitch, roll
        st = (os.path.basename(image)) + "," + str(float(lon)) + "," + str(float(lat)) + "," + str(float(alt)) + "," + str(float(yaw)) + "," + str(float(pitch)) + "," + str(float(roll)) + "\n"
        input.write(st)

    input.close()

    path = "datasets/imageData.txt"
    with open(path) as f:
        lines = [line.split(',') for line in f]

    output = open(path, 'w')

    for line in sorted(lines, key=itemgetter(4)):
        output.write(','.join(line))

    output.close()

#write()

if __name__ == '__main__':
    write()
