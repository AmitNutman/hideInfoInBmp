#עמית נוטמן וטל שיינברג


import os
from PIL import Image
import stepic
from stegano import lsb



while True:
    img_name = input("enter exit or image path: ")
    if img_name.lower() == "exit":
        break
    if os.path.exists(img_name):
        if img_name[-3:] == "bmp":
            hide_or_extract = input("enter if you want to hide information or extract information: ")
            if hide_or_extract.lower() == "hide":
                data_to_add = input("enter data to add to img: ")
                if len(data_to_add) <= 5:
                    what_way = input("enter 1 if with change size or 0 without: ")
                    #with change size
                    if what_way == "1":
                        # encryption
                        img = Image.open(img_name)
                        img1 = stepic.encode(img, data_to_add.encode())
                        img1.save(img_name)
                        #r+b so the content of the file won't be deleted when writing to the file
                        with open(img_name, "r+b") as f:
                            #there is an unused byte in offset 57 - seek moves the pointer 57 places
                            f.seek(57)
                            f.write(b'1')
                    #without changing size in bmp
                    elif what_way == "0":
                        secret_image = lsb.hide(img_name, data_to_add)
                        secret_image.save(img_name)
                        # r+b so the content of the file won't be deleted when writing to the file
                        with open(img_name, "r+b") as f:
                            # there is an unused byte in offset 57 - seek moves the pointer 57 places
                            f.seek(57)
                            f.write(b'2')
                    else:
                        print("not legal way - must enter 1 / 0")
                else:
                    print("data length has to be 5 or less")
            elif hide_or_extract.lower() == "extract":
                with open(img_name, "rb") as f:
                    #get to the unused byte - seek moves the pointer 57 places
                    f.seek(57)
                    #reads one byte
                    unused_bytes = f.read(1)
                if unused_bytes == b"1":
                    # decryption
                    img = Image.open(img_name)
                    s = stepic.decode(img)
                    data = s.encode()
                    print(data.decode())
                elif unused_bytes == b"2":
                        revealed_message = lsb.reveal(img_name)
                        print(revealed_message)
                else:
                    print("not legal img")
            else:
                print("not legal command")
        else:
            print("img needs to be bmp")
    else:
        print("couldn't find img")