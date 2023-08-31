py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
# type(py_list)
# > <class 'list'>

import numpy as np
np_array = np.array([[7,8]
                    ,[9,10]
                    ,[11,12]])   # 행렬 = array
# type(np_array)
# > <class 'numpy.ndarray'>
# np.mean(np_array)
# > 9.5
# np.mean(np_array, axis=0)
# > array([ 9., 10.])
# np.mean(np_array, axis=1)
# > array([ 7.5,  9.5, 11.5])

# 병합
np_array02 = np.array(py_list)
# np.concatenate((np_array, np_array02), axis=0)
# > array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
# np.concatenate((np_array, np_array02), axis=1)
# > array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])
pass   