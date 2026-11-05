import os
from PIL import Image
import stepic


changed_img = {}

while True:
    img_name = input("enter exit or image name: ")
    if img_name.lower() == "exit":
        break
    if os.path.exists(img_name):
        if img_name[-3:] == "bmp":
            hide_or_extract = input("enter if you want to hide information or extract information: ")
            if hide_or_extract.lower() == "hide":
                data_to_add = input("enter data to add to img: ")
                what_way = input("enter 1 if with change size or 0 without: ")
                #with change size
                if what_way == "1":
                    # encryption
                    img = Image.open(img_name)
                    img1 = stepic.encode(img, data_to_add.encode())
                    img1.save(img_name)
                    changed_img[img_name] = 1
                #without changing size
                elif what_way == "0":
                    changed_img[img_name] = 0
                else:
                    print("not legal way - must enter 1 / 0")
            elif hide_or_extract.lower() == "extract":
                if img_name in changed_img.keys():
                    if changed_img[img_name] == 1:
                        # decryption
                        img = Image.open(img_name)
                        s = stepic.decode(img)
                        data = s.encode()
                        print(data.decode())
                    else:
                        pass
                else:
                    print("not legal img")
            else:
                print("not legal command")
        else:
            print("img needs to be bmp")
    else:
        print("couldn't find img")