======
NumPy
======

* Indexing

    * `SciPy.org, Indexing <https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html>`_

* where

    * `SciPy.org, numpy.where <https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html>`_
    * `PinkWink, numpy의 where 함수 사용법 <https://pinkwink.kr/1236>`_

* 2d list ￫ numpy array

    * numpy.array()

        * 코드

        ::

            a_list = [[1, 2], [3, 4]]
            an_array = np.array(a_list)

            print(an_array)

        * 출력

        ::
            
            [[1 2]
            [3 4]]

        * 참조

            * `kite, How to convert a 2D list into a NumPy array in Python <https://kite.com/python/answers/how-to-convert-a-2d-list-into-a-numpy-array-in-python>`_

* numpy array ￫ list

    * tolist()

        * 코드

            * 1D array

            ::

                >>> a = np.array([1, 2])
                >>> list(a)
                [1, 2]
                >>> a.tolist()
                [1, 2]

            * 2D array

            ::

                >>> a = np.array([[1, 2], [3, 4]])
                >>> list(a)
                [array([1, 2]), array([3, 4])]
                >>> a.tolist()
                [[1, 2], [3, 4]]

        * 참조

            * `SciPy.org, numpy.ndarray.tolist <https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html>`_

* Copy numpy array into higher dimensions

    * np.expand_dims and np.concatenate

        * 코드

        ::

            arr = np.expand_dims(arr, axis=2)
            arr = np.concatenate((arr,arr,arr), axis=2)

        * 참조

            * `StackOverflow, how to copy numpy array value into higher dimensions <https://stackoverflow.com/a/39463055>`_

    * np.repeat

        * 코드
            
        ::

            arr3D = np.repeat(arr[...,None], 3, axis=2)

        * 참조

            * `StackOverflow, how to copy numpy array value into higher dimensions <https://stackoverflow.com/a/39463055>`_
