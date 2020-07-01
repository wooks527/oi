=====================
English ALPR dataset
=====================

Cars Dataset
=============

The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

:h3:`Reference`

* `Cars Dataset <http://ai.stanford.edu/~jkrause/cars/car_dataset.html>`_

AOLP Database
==============

LPR applications can be split into three categories: Access Control (AC), Traffic Law Enforcement (LE), and Road Patrol (RP).

Access Control (AC)
********************

Access control refers to the cases that a vehicle passes a fixed passage at a reduced speed or with a full stop, such as at a toll station or the entrance/exit of a region. In access control scenarios, the camera is often placed less than 5 meters from the plate, within -30 to +30 degrees in pan and 0 to 60 degrees in tilt (as 0 degree tilt is parallel to the ground).

In the image, the width of a plate is between 0.2 to 0.25 the width of the image (shown as width ratio in Application Parameters), and its orientation is less than 10 degrees (Note that both are measured in the image by the plate projected onto the image plane). The parameters in Application Parameters are generalized from the 681 images collected at various access control scenes.

The illumination covers indoor, outdoor, daytime, night time, and different weather conditions. If measured by the average intensity over a plate, it varies from 60 to 130 degrees in an 8-bit gray scale. The above parameters of access control are summarized in Application Parameters, along with those for the other two applications.

Traffic Law Enforcement (LE)
*****************************

Traffic law enforcement refers to the cases that a vehicle travels at a regular or higher speed but violates traffic laws, such as a traffic signal or speed limit, and is captured by a roadside camera. 757 images were collected for this application category.

Road Patrol (RP)
*****************

Road patrol refers to the cases that the camera is installed or handheld on a patrolling vehicle which takes images of the vehicles with arbitrary viewpoints and distances. The purposes of road patrol include search for lost vehicles, scan for parking violation, security check in a restricted area, or others. 611 images were collected for this application scenario.

:h3:`Reference`

* `Application Oriented License Plate(AOLP) Database <http://aolpr.ntust.edu.tw/lab/index.html>`_


OPEN ALPR
==========

* `GitHub, openalpr/benchmarks <https://github.com/openalpr/benchmarks>`_


SSIG
=====

* `senselab, Sense License Plate Character Segmentation Database <http://smartsenselab.dcc.ufmg.br/en/dataset/sense-segplate/>`_
