from PIL import Image
import os

def imgcrop(input, save_path, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            fname = filename + "_" + str(i) + "_" + str(j) + file_extension
            savename = save_path + fname
            try:
                a.save(savename)
            except:
                pass

imgcrop("images/black_dog.jpg", 'images/cropImg/blackdog/' , 3, 3)
