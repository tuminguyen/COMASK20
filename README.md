# **COMASK20 DATASET**
The COMASK20 was collected for research purpose of our work on recognition with masked face. 

For the reference paper: **Masked Face Recognition with Convolutional Neural Networks and Local Binary Patterns**, please check [here](https://link.springer.com/article/10.1007/s10489-021-02728-1).

The repository is now attached with instructions on using the data. 

---
## **Hierarchical dataset structure**

```
.
├─ dataset/
│   ├── person_1/
│   ├── person_2/
│   ├── ...
│   ├── person_N/
├─ README.md
```

---
## **Usage**
Each folder of individual contains:

- **Masked face images:** images containing face **wearing** mask
- **Non-masked face images:** images containing face **without wearing** mask 

Depend on your purpose, you can split the data into non-masked vs masked images by checking for the term **_"nomask"_** on the name of the file. All the files contains this term will be non-masked images and the rest should be masked ones.

``` python
# Python

from imutils import paths

all_image_paths = list(paths.list_images(folder))
nomasked_imgs = [x for x in all_image_paths if x.lower().__contains__("nomask")]

```
```matlab
% Matlab


all_image_paths = [dir('*.jpg'); dir('*.png'); dir('*.jpeg')];

f=@(x) (append(x.folder, "/", x.name));
full_paths = arrayfun(f, all_image_paths);

nomasked_imgs = full_paths(contains(full_paths, "nomask") == 1);

```

## **Citation**
Please cite the paper, when you using this dataset
```
@article{article,
author = {Vu, Hoai and Nguyen, Mai and Pham, Cuong},
year = {2021},
month = {08},
pages = {},
title = {Masked face recognition with convolutional neural networks and local binary patterns},
journal = {Applied Intelligence},
doi = {10.1007/s10489-021-02728-1}
}

```


## **Contact**
For further expand the data, you are welcome to send me (huongnm.ptit@gmail.com) an email attached with your personal pictures in 2 contexts: with and without mask. We will process the received pictures and add it to the repo afterwards.
