import os
import shutil
from socket import J1939_PGN_ADDRESS_CLAIMED 

from_dir="/Users/aneessh/downloads" 
to_dir = "/Users/aneessh/documents/file_manager"

list_files=os.listdir(from_dir) 
print(list_files) 
for file in list_files:
    root,extension=os.path.splitext(file) 
    # print(root)  
    # print(extension)

    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docs", ".pdf"]:
        path1 = from_dir + "/" + file

        path2 = to_dir + "/" + "pdf_files"
        path3 = to_dir + "/" + "pdf_files" + "/" + file

        if os.path.exists(path2):
            print("moving" + file + "....")
            shutil.move(path1, path3)

        else:
            os.mkdir(path2)
            print("moving" + file + "....")
            shutil.move(path1, path3)

