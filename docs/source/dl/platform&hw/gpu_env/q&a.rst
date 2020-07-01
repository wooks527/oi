========================
Q&A and Troubleshooting
========================

Q&A
====

* CUDA와 CUDA toolkit의 차이점

    * 내용

        * CUDA is a library used by many other programs like TensorFlow or OpenCV.
        * CUDA toolkit is an extra set software on top of CUDA which makes GPU programming with CUDA easy. For instance Nsight as the debugger (in Visual Studio).
    
    * 참조
    
        * `Quora, What's the difference between Nvidia CUDA toolkit and CUDA? <https://www.quora.com/Whats-the-difference-between-Nvidia-CUDA-toolkit-and-CUDA>`_


Troubleshooting
================

* docker: Error response from daemon: Unknown runtime specified nvidia.

    * 내용

        * docker의 옵션으로 ``--runtime nvidia`` 또는 ``--runtime==nvidia`` 를 사용했을 때 발생하는 에러
        * ``--runtime nvidia`` 는 nvidia-docker2에서 사용하던 옵션임
        * nvidia-docker에서는 ``--gpus all`` 이라는 옵션을 사용하면 됨

    * 참조

        * `GitHub, NVIDIA/nvidia-docker <https://github.com/NVIDIA/nvidia-docker/issues/838#issuecomment-558962338>`_
