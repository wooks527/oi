======
Numpy
======

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
        