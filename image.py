from PIL import Image
import numpy
import base64
from io import BytesIO
from pathlib import Path


# info: image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()

# info: formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)

# info: color_data prepares a series of images for data analysis
def image_data(path=Path("static/rgb/"), img_list=None):  # info: path of static images is defaulted
    if img_list is None:  # info: color_dict is defined with defaults and these are the images showing up
        img_list = [
            {'source': "Ceramics 2", 'label': "Nadira Haddach", 'file': "lassen-volcano-256.jpg"},
            {'source': "Drawing and Painting 1", 'label': "Bria Gilliam", 'file': "waterpolo.jpeg"}
        ]

    # info: gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # to fix static images
        file = path / img_dict['file']
        print(file)

        img_reference = Image.open(file)
        img_data = img_reference.getdata()  # https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size

        # info: Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])

        # info: Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # grayscale
        img_dict['gray_data'] = []


        # info: 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # info: create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                # grayscale
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                # grayscale
                img_dict['gray_data'].append((average, average, average))
        #  end for loop for pixel
        # grayscale
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        # create color scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/

        # for hex and binary values
        # grayscale
        img_dict['hex_array_GRAY'] = []
        img_dict['binary_array_GRAY'] = []
        # for grayscale binary/hex changes
        for pixel in img_dict['gray_data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array_GRAY'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array_GRAY'].append(bin_value)