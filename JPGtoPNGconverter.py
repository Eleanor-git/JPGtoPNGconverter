import sys, os, re
from PIL import Image
import pdb

path = os.getcwd()
png_file_name = "new"
pattern = '.*.jpg$'


def whether_dir_exist(check_file):
    while not os.path.exists(
            check_file):  # not false (i.e. while True) 才會進來，所以 os.path.exists(jpg_dir) = False -> 就會進入 while loop
        print(f"{check_file} doesn't exist!! Pls Provide an existing jpg directory name")
        filename = input("Pls Provide a correct filename: ")
        check_file = f"{path}/{filename}"
    return [os.path.exists(check_file), check_file]


def create_file(file_name):
    try:
        os.mkdir(f'{path}/{file_name}')
        print("png directory has just been created as \"new\"")
        png_dir = f'{path}/{file_name}'
    except FileExistsError:
        print(f"Destination (PNG File): {file_name} exists")
        png_dir = f'{path}/{file_name}'
        print(f"Destination (PNG File): {png_dir}")
    return png_dir


# ---------------------- Main ---------------------

if len(sys.argv) < 2:  # [只有檔名]
    jpg_filename = input("Pls Provide a jpg image file name: ")
    jpg_dir = f"{path}/{jpg_filename}"
    jpg_dir = whether_dir_exist(jpg_dir)[1]
    print(f"Source (JPG File):  {jpg_dir}")

    # dealing with PNG Dir
    png_dir = create_file(png_file_name)

elif len(sys.argv) < 3:  # [檔名, JPG Dir]
    jpg_dir = f"{path}/{sys.argv[1]}"
    jpg_dir = whether_dir_exist(jpg_dir)[1]
    png_dir = create_file(png_file_name)

elif len(sys.argv) == 3:  # [檔名, JPG Dir, PNG Dir]
    jpg_dir = f"{path}/{sys.argv[1]}"
    jpg_dir = whether_dir_exist(jpg_dir)[1]

    png_dir = f"{path}/{sys.argv[2]}"
    if not os.path.exists(png_dir):
        png_dir = create_file(png_file_name)

else:
    print("Too many arguments, try again!")
    exit(1)

# loop through Dir1
for _ in os.listdir(jpg_dir):  # os.listdir(jpg_dir) = ['bulbasaur.jpg', '.DS_Store', 'pikachu.jpg', 'squirtle.jpg', 'charmander.jpg']
    obj_match = re.search(pattern, _)
    if obj_match is not None:
        with Image.open(f"{jpg_dir}/{_}") as im:
            im.save(f"{png_dir}/{_[:-4]}.png", "PNG")
