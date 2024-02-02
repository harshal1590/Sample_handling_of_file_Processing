import os
import string
import random
import shutil

def generate_random(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

folder_1 = '/home/harshal/Documents/main/'
os.makedirs(folder_1, exist_ok=True)

multiple_files = os.listdir(folder_1)

if not multiple_files:
    for i in range(100):
        filename = generate_random(length=8)
        file_path = os.path.join(folder_1, filename)
        with open(file_path, 'w') as file:
            for _ in range(random.randint(5, 10)):
                random_line = generate_random(length=44)
                file.write(f"{random_line}\n")
    print('Successfully created files.')
else:
    print('Files already exist.')

folder_2 = '/home/harshal/Documents/harshal1/'

if len(multiple_files) >= 40:
    man_file_2 = random.sample(multiple_files, 40)
else:
    print("Not enough1")
    man_file_2 = multiple_files

os.makedirs(folder_2, exist_ok=True)

for harshal in man_file_2:
    path = os.path.join(folder_1, harshal)
    j_path = os.path.join(folder_2, harshal)
    shutil.move(path, j_path)

multiple_files = os.listdir(folder_1)

folder_3 = '/home/harshal/Documents/harshal2/'

if len(multiple_files) >= 20:
    man_file_3 = random.sample(multiple_files, 20)
else:
    print("Not enough2")
    man_file_3 = multiple_files

os.makedirs(folder_3, exist_ok=True)

for harshal in man_file_3:
    path = os.path.join(folder_1, harshal)
    j_path = os.path.join(folder_3, harshal)
    shutil.move(path, j_path)

multiple_files = os.listdir(folder_1)

folder_4 = '/home/harshal/Documents/harshal3/'

if len(multiple_files) >= 20:
    man_file_4 = random.sample(multiple_files, 20)
else:
    print('Not enough3')
    man_file_4 = multiple_files

os.makedirs(folder_4, exist_ok=True)

for harshal in man_file_4:
    path = os.path.join(folder_1, harshal)
    j_path = os.path.join(folder_4, harshal)
    shutil.move(path, j_path)
