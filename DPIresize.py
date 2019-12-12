from PIL import Image
import os
import glob

if not os.path.exists('./changed_dpi/'):
    os.makedirs('./changed_dpi/')

change_dpi = glob.glob('./*.jpg')

for im in change_dpi:
    new_im = Image.open(im)
    new_im.save('./changed_dpi/' + im, dpi=(500,500))

