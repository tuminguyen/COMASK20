# **COMASK20 DATASET**
The COMASK20 was collected for research purpose of our work on recognition with masked face. 

For the reference paper: **Masked Face Recognition with Convolutional Neural Networks and Local Binary Patterns**, please check [here]().

This repository contains a README file for some instructions on using the data. 

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

## **Contact**
For further expand the data, you are welcome to send me (huongnm.ptit@gmail.com) an email attached with your personal pictures in 2 contexts: with and without mask. We will process the received pictures and add it to the repo afterwards.
