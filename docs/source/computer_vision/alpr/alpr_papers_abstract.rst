==================
Other ALPR papers
==================

2020
=====

A Robust Attentional Framework for License Plate Recognition in the Wild
*************************************************************************

---------
Abstract
---------

Recognizing car license plates in natural scene images is an important yet still challenging task in realistic applications. Many existing approaches perform well for license plates collected under constrained conditions, e.g., shooting in frontal and horizontal view-angles and under good lighting conditions. However, their performance drops significantly in an unconstrained environment that features rotation, distortion, occlusion, blurring, shading or extreme dark or bright conditions. In this work, we propose a robust framework for license plate recognition in the wild. It is composed of a tailored CycleGAN model for license plate image generation and an elaborate designed image-to-sequence network for plate recognition. On one hand, the CycleGAN based plate generation engine alleviates the exhausting human annotation work. Massive amount of training data can be obtained with a more balanced character distribution and various shooting conditions, which helps to boost the recognition accuracy to a large extent. On the other hand, the 2D attentional based license plate recognizer with an Xception based CNN encoder is capable of recognizing license plates with different patterns under various scenarios accurately and robustly. Without using any heuristics rule or post-processing, our method achieves the state-of-the-art performance on four public datasets, which demonstrates the generality and robustness of our framework. Moreover, we released a new license plate dataset, named “CLPD”, with 1200 images from all 31 provinces in mainland China. The dataset can be available from: https://github.com/wangpengnorman/CLPD_dataset.

* Writers: Linjiang Zhang, Peng Wang, Hui Li, Zhen Li, Chunhua Shen, Yanning Zhang
* Journal: arXiv
* Submitted date: 6 Jun 2020
* Paper link (`here <https://arxiv.org/pdf/2006.03919.pdf>`_)


DELP-DAR system for license plate detection and recognition
************************************************************

---------
Abstract
---------

Automatic License Plate detection and Recognition (ALPR) is a quite popular and active research topic in the field of computer vision, image processing and intelligent transport systems. ALPR is used to make detection and recognition processes more robust and efficient in highly complicated environments and backgrounds. Several research investigations are still necessary due to some constraints such as: completeness of numbering systems of countries, different colors, various languages, multiple sizes and varied fonts. For this, we present in this paper an automatic framework for License Plate (LP) detection and recognition from complex scenes. Our framework is based on mask region convolutional neural networks used for LP detection, segmentation and recognition. Although some studies have focused on LP detection, LP recognition, LP segmentation or just two of them, our study uses the maskr-cnn in the three stages.

The evaluation of our framework is enhanced by four datasets for different countries and consequently with various languages. In fact, it tested on four datasets including images captured from multiple scenes under numerous conditions such as varied orientation, poor quality images, blurred images and complex environmental backgrounds. Extensive experiments show the robustness and efficiency of our suggested Extensive experiments show the robustness and efficiency of our suggested system that achieves in accuracy rate 99.3% on AOLP and 98.9% on Caltech dataset.

* Paper link (`here <https://www.sciencedirect.com/science/article/pii/S0167865519303216>`_)


SEE-LPR: A Semantic Segmentation Based End-to-End System for Unconstrained License Plate Detection and Recognition
*******************************************************************************************************************

---------
Abstract
---------

Most previous works regard License Plate detection and Recognition (LPR) as two or more separate tasks, which often leads to error accumulation and low efficiency. Recently, several new studies use end-to-end training to overcome these problems and achieve better results. However, challenges like misalignment and variable-length or multi-language LPs still exist. In this paper, we propose a novel Semantic segmentation based End-to-End multilingual LPR system SEE-LPR to solve these challenges. Our system has four components which are convolution backbone, LP capture, LP alignment, and LP recognition. Specifically, LP alignment is used to connect LP capture and LP recognition, allowing the gradient back-propagate through the whole network and can handle oblique LPs. Connectionist Temporal Classification (CTC) module used in LP recognition makes our system able to handle LPs with variable-length or multi-language. Comparative studies on several challenging benchmark datasets show that the proposed SEE-LPR system significantly outperforms the state-of-the-art systems in both accuracy and efficiency.

* Paper link (`here <https://link.springer.com/chapter/10.1007/978-3-030-37731-1_44>`_)


2019
=====

Robust license plate recognition using neural networks trained on synthetic images
***********************************************************************************

---------
Abstract
---------

In this work, we describe a License Plate Recognition (LPR) system designed around convolutional neural networks (CNNs) trained on synthetic images to avoid collecting and annotating the thousands of images required to train a CNN. First, we propose a framework for generating synthetic license plate images, accounting for the key variables required to model the wide range of conditions affecting the aspect of real plates. Then, we describe a modular LPR system designed around two CNNs for plate and character detection enjoying common training procedures and train the CNNs and experiment on three different datasets of real plate images collected from different countries. Our synthetically trained system outperforms multiple competing systems trained on real images, showing that synthetic images are effective at training a CNNs for LPR if the training images have sufficient variance of the key variables controlling the plate aspect.

* Writers: Tomas Björklund, Attilio Fiandrotti, Mauro Annarumma, Gianluca Francini, Enrico Magli 
* Journal: Pattern Recognition
* Accepted date: 9 April 2019
* Paper link (`here <https://www.sciencedirect.com/science/article/pii/S0031320319301475#bib0020>`_)


Automatic License Plate Recognition via sliding-window darknet-YOLO deep learning
**********************************************************************************

---------
Abstract
---------

Automatic License Plate Recognition (ALPR) is an important research topic in the intelligent transportation system and image recognition fields. In this work, we address the problem of car license plate detection using a You Only Look Once (YOLO)-darknet deep learning framework. In this paper, we use YOLO's 7 convolutional layers to detect a single class. The detection method is a sliding-window process. The object is to recognize Taiwan's car license plates. We use an AOLP dataset which contained 6 digit car license plates. The sliding window detects each digit of the license plate, and each window is then detected by a single YOLO framework. The system achieves approximately 98.22% accuracy on license plate detection and 78% accuracy on license plate recognition. The system executes a single detection recognition phase, which needs around 800 ms to 1 s for each input image. The system is also tested with different condition complexities, such as rainy background, darkness and dimness, and different hues and saturation of images.

* Paper link (`here <https://www.sciencedirect.com/science/article/pii/S0262885619300575>`_)


License Plate Localization in Unconstrained Scenes Using a Two-Stage CNN-RNN
*****************************************************************************

---------
Abstract
---------

Recent deep object detection methods neglect the intrinsic properties of the license plate, which limits the detection performance in unconstrained scenes. In this paper, we propose a two-stage deep learning-based method to locate license plates in unconstrained scenes, especially for special license plates such as fouling, occlusion, and so on. A deep network consisting of convolutional neural network (CNN) and recurrent neural network is designed. In the first stage, fine-scale proposals are detected according to the characteristics of the license plate characters, and CNN is used to extract the local features of characters. A vertical anchor mechanism is designed to jointly predict the position and confidence of each fix-width character. Furthermore, the sequential contexts of characters are modeled with the bi-directional long short-term memory, which greatly improves the locating rate of license plates in complex scenes. In the second stage, the whole license plate is obtained by connecting the fine-scale proposals. The experimental results show that the proposed method not only locates license plates of different countries accurately but also be robust to scenes of illumination variation, noise distortion, and blurry effects. The average precision reaches 97.11% on multi-country license plates, and the precision and recall reaches 99.10% and 98.68%, respectively, on Chinese license plate images.

* Paper link (`here <https://ieeexplore.ieee.org/abstract/document/8643978>`_)


Multi-Oriented and Scale-Invariant License Plate Detection Based on Convolutional Neural Networks
**************************************************************************************************

---------
Abstract
---------

License plate detection (LPD) is the first and key step in license plate recognition. State-of-the-art object-detection algorithms based on deep learning provide a promising form of LPD. However, there still exist two main challenges. First, existing methods often enclose objects with horizontal rectangles. However, horizontal rectangles are not always suitable since license plates in images are multi-oriented, reflected by rotation and perspective distortion. Second, the scale of license plates often varies, leading to the difficulty of multi-scale detection. To address the aforementioned problems, we propose a novel method of multi-oriented and scale-invariant license plate detection (MOSI-LPD) based on convolutional neural networks. Our MOSI-LPD tightly encloses the multi-oriented license plates with bounding parallelograms, regardless of the license plate scales. To obtain bounding parallelograms, we first parameterize the edge points of license plates by relative positions. Next, we design mapping functions between oriented regions and horizontal proposals. Then, we enforce the symmetry constraints in the loss function and train the model with a multi-task loss. Finally, we map region proposals to three edge points of a nearby license plate, and infer the fourth point to form bounding parallelograms. To achieve scale invariance, we first design anchor boxes based on inherent shapes of license plates. Next, we search different layers to generate region proposals with multiple scales. Finally, we up-sample the last layer and combine proposal features extracted from different layers to recognize true license plates. Experimental results have demonstrated that the proposed method outperforms existing approaches in terms of detecting license plates with different orientations and multiple scales.

* Paper link (`here <https://www.mdpi.com/1424-8220/19/5/1175/htm>`_)


An Efficient and Layout-Independent Automatic License Plate Recognition System Based on the YOLO detector
***********************************************************************************************************

---------
Abstract
---------

In this paper, we present an efficient and layout-independent Automatic License Plate Recognition (ALPR) system based on the stateof-the-art YOLO object detector that contains a unified approach for license plate (LP) detection and layout classification to improve the recognition results using post-processing rules. The system is conceived by evaluating and optimizing different models with various modifications, aiming at achieving the best speed/accuracy trade-off at each stage. The networks are trained using images from several datasets, with the addition of various data augmentation techniques, so that they are robust under different conditions. The proposed system achieved an average end-to-end recognition rate of 96.8% across eight public datasets (from five different regions) used in the experiments, outperforming both previous works and commercial systems in the ChineseLP, OpenALPR-EU, SSIG-SegPlate and UFPR-ALPR datasets. In the other datasets, the proposed approach achieved competitive results to those attained by the baselines. Our system also achieved impressive frames per second (FPS) rates on a high-end GPU, being able to perform in real time even when there are four vehicles in the scene. An additional contribution is that we manually labeled 38,351 bounding boxes on 6,239 images from public datasets and made the annotations publicly available to the research community.


* Writers: Tomas Björklund, Attilio Fiandrotti, Mauro Annarumma, Gianluca Francini, Enrico Magli 
* Journal: arXiv
* Submitted date: 4 Sep 2019
* Paper link (`here <https://arxiv.org/abs/1909.01754>`_)


2018
=====

Toward End-to-End Car License Plate Detection and Recognition With Deep Neural Networks
*****************************************************************************************

---------
Abstract
---------

In this paper, we tackle the problem of car license plate detection and recognition in natural scene images. We propose a unified deep neural network, which can localize license plates and recognize the letters simultaneously in a single forward pass. The whole network can be trained end-to-end. In contrast to existing approaches which take license plate detection and recognition as two separate tasks and settle them step by step, our method jointly solves these two tasks by a single network. It not only avoids intermediate error accumulation but also accelerates the processing speed. For performance evaluation, four data sets including images captured from various scenes under different conditions are tested. Extensive experiments show the effectiveness and the efficiency of our proposed approach.

* Writers: Hui Li, Peng Wang, Chunhua Shen
* Journal: IEEE Transactions on Intelligent Transportation Systems
* Publication date: 92 August 2018
* Paper link (`here <https://www.sciencedirect.com/science/article/pii/S0031320319301475#bib0020>`_)
