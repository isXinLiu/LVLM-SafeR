import os
from PIL import Image

def is_image_file(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except (IOError, SyntaxError) as e:
        return False

with open('download_img.sh', 'r') as f:
    lines = f.readlines()

with open('check.sh', 'w') as f:
    for line in lines:
        local_file = line.split(' ')[3]
        local_file = local_file[3:][:-1]
        if os.path.isfile(local_file) and is_image_file(local_file):
            continue
        f.write(line)
