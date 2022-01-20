import os
import cv2
import shutil

dest = 'Test'

for folder in os.listdir('dataset'):
    # print(folder)
    if folder != '.DS_Store':
        for file in os.listdir(f'dataset/{folder}'):
            if file != '.DS_Store':
            # cv2.imread(f'Test/{folder}/{file}')
            # os.remove(f'Test/{folder}/{file}')
                if 'nomask' not in file.lower():
                    print(file)
                    shutil.move(f'dataset/{folder}/{file}',f'{dest}/{folder}/{file}')

