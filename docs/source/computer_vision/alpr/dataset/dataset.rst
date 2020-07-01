========
Dataset
========

Automatic License Plate Recognition (ALPR)을 위한 여러 가지 모델을 학습시키거나 테스트 할 때 다양한 Dataset이 활용된다. 여기서는 ALPR에서 활용되는 Dataset을 정리하려고 한다.

국가별 License plates
=====================

여기에서는 국가별 License plates dataset과 각 Dataset이 어떤 논문에서 사용되었는지를 정리하려고 한다.

* Taiwanese

    * AOLP dataset

        * Features

            * 2,049 images with Taiwan license plates
            * Subsets: Access Control (AC), Traffic Law Enforcement (LE), and Road Patrol (RP)
            * Any two of these subsets for training and the remaining one for test (same for all)

        * Papers

            * A Robust Attentional Framework for License Plate Recognition in the Wild (arXiv, 2020)
            * Multinational License Plate Recognition Using Generalized Character Sequence Detection (IEEE Access, 2020)
            * Robust license plate recognition using neural networks trained on synthetic images (Pattern Recognition, 2019)
            * Toward End-to-End Car License Plate Detection and Recognition With Deep Neural Networks (IEEE Transactions on Intelligent Transportation Systems, 2018)

* Chinese

    * PKU dataset

        * Features

            * 2,253 images (?), About 4,000 images (?)
            * 5 subsets captured in increasingly difficult conditions (G1 ~ G5)

                * daylight, daylight with sunshine glare, nighttime, day- and nighttime with reflective glare, and in the final set, images with multiple plates at intersections with crosswalks

        * Papers
        
            * A Robust Attentional Framework for License Plate Recognition in the Wild (arXiv, 2020)

                * Training: 1352 images (randomly selected)
                * Test: 901 images (rest)

            * Robust license plate recognition using neural networks trained on synthetic images (Pattern Recognition, 2019)

                * Training: X
                * Test: 4 subsets

            * Toward End-to-End Car License Plate Detection and Recognition With Deep Neural Networks (IEEE Transactions on Intelligent Transportation Systems, 2018)

                * Training: X
                * Test: all

    * CCPD dataset

        * Features

            * 290k unique Chinese LP images with detailed annotations
            * CCPD-base: 200k images
            * Other sub-datasets: CCPD-DB, CCPD-FN, CCPD-Rotate, CCPD-Weather, CCPD-Challenge (90k images)

        * Papers

            * A Robust Attentional Framework for License Plate Recognition in the Wild (arXiv, 2020)

                * Training: CCPD-base 100k images
                * Test: CCPD-base 100k images, Other subdatasets 90k images

    * CLPD dataset

        * Features

            * 1,200 images across all provinces in mainland China, with different vehicle types included

        * Papers

            * A Robust Attentional Framework for License Plate Recognition in the Wild (arXiv, 2020)
            
                * Training: X
                * Test: all

    * CarFlag-Large

        * Features

            * 460,000 images
            * 1600 × 2048
            * Captured from frontal viewpoint by fixed surveillance cameras under different weather and illumination condition

        * Papers

            * Toward End-to-End Car License Plate Detection and Recognition With Deep Neural Networks (IEEE Transactions on Intelligent Transportation Systems, 2018)

                * Training: 322,000 images
                * Test: 138,000 images

* Italian 

    * platesmania.com

        * Total 71.469 photos
        * There are various license plates from various contries

            * Armenia Austria Azerbaijan Belarus Belgium Bosnia and Herzegovina Bulgaria Canada China Croatia Cyprus Czech Republic Denmark Estonia Finland France Georgia Germany Great Britain Greece Hong Kong Hungary Ireland Israel Italy Japan Kazakhstan Kyrgyzstan Latvia Lithuania Luxembourg Moldova Monaco Mongolia Montenegro Netherlands North Macedonia Norway Poland Portugal Romania Russia Serbia Slovakia Slovenia South Korea Spain Sweden Switzerland Thailand Turkey UAE USA USSR Ukraine Uzbekistan Vietnam Others

    * Papers

        * A Robust Attentional Framework for License Plate Recognition in the Wild (arXiv, 2020)

            * Training: 1,152 images
            * Test: X
                

.. toctree::
    :maxdepth: 1
    :caption: 종류

    kr_dataset
    en_dataset
