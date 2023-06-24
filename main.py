# To list directory
# import os
# path = "linn.valentine2"
# dir_list = os.listdir(path)

# print(f"files and directories in {path} :")
# print(dir_list)

# To list only files in a directory
# print("To only get files")

# path = input("Enter path")

# files = os.listdir(path)
# files = [f for f in files if os.path.isfile(path+'/'+f)]
# print(*files, sep="\n")
# jeg    .   jpg 

#  To move each file by extension in a folder
import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path,file)):
        file_extension = os.path.splitext(file)[1][1:].lower()

        destination_folder = os.path.join(path, file_extension)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        current_file_path = os.path.join(path,file)
        new_file_path = os.path.join(destination_folder, file)
        shutil.move(current_file_path, new_file_path)

print("files moved successfully")