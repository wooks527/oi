========================================================================================
Multinational Licnese Plate Recognition Using Generalized Character Sequence Detection
========================================================================================

Introduction
=============

* Multinational ALPR is a challenging issue

    * The differences in license plate (LP) layouts among different countries
    * The non-availability of public multinational LP datasets


Materials and methods
======================

Dataset
********

----
LPD
----

=======  ==============  =========  =========  =========  ============  ====================  =============  =============
Purpose  KarPlate (LPD)  AOLP (AC)  AOLP (LE)  AOLP (RP)  Medialab LPR  University of Zagreb  OpenALPR (EU)  OpenALPR (US)
=======  ==============  =========  =========  =========  ============  ====================  =============  =============
Train    3,417 → 30,000  681        757        －         279 → 259     401                   108            244          
Test     850             681        757        611        437 → 431     100                   －             －
Total    4,267 → ?       681        757        611        716 → 690     510 → 501             108            244
=======  ==============  =========  =========  =========  ============  ====================  =============  =============

---
LPR
---

=======  ==============  =========  =========  =========  ============  ========================  ====================  =============  =============
Purpose  KarPlate (LPR)  AOLP (AC)  AOLP (LE)  AOLP (RP)  Medialab LPR  Caltech Cars (Rear) 1999  University of Zagreb  OpenALPR (EU)  OpenALPR (US)
=======  ==============  =========  =========  =========  ============  ========================  ====================  =============  =============
Train    3,417 → 60,000  681        757        －         279 → 259     80                        401                   108            244          
Test     850             681        757        611        437 → 431     46                        100                   －             －
Total    4,267 → ?       681        757        611        716 → 690     126                       510 → 501             108            244
=======  ==============  =========  =========  =========  ============  ========================  ====================  =============  =============


:h2:`Reference`

* Multinational Licnese Plate Recognition Using Generalized Character Sequence Detection, CVPR, 2019
