from PIL import Image
import os, sys

def resize(sourc, destination, w , h, char_replace, normalize):
    dirs = os.listdir(os.path.join(sourc,''))
    source = os.path.join(sourc,'')
    print(type(source))
    print(type(dirs))
    destination = os.path.join(destination,'')
    h = int(h)
    w = int(w)
    Image.MAX_IMAGE_PIXELS = None

    for item in dirs:
        try:
            if os.path.isfile(source+item):
                print(source+item)
                im = Image.open(source+item)
                imResize = im.resize((w,h), Image.ANTIALIAS)
                item_name = item
                item_name= item_name.replace("{}".format(char_replace), "")
                if normalize == "l" or normalize == "L":
                    item_name = item_name.lower()
                elif normalize == "U" or normalize == "u":
                    item_name = item_name.upper()
                else:
                    None
                imResize.save(destination + item_name, 'JPEG', quality=90)
                print(item_name + " - Transformmed")
        except:
            print("could not convert: {}".format(item))
    print("Done transforming and moving pictures to new Folder with follwing requirements:")
    print("Height: {}".format(h))
    print("Width: {}".format(w))

        #resize(sourceFolder, Destination Folder, Widith, Height, charToRemove)
resize("C:\\Users\\NN_Su\\Pictures\\Camera Roll","C:\\Users\\NN_Su\\Pictures\\Camera Roll", 250, 250,' ','l')
