#  [[14.67, 23.19, 96.08]]
# 입원기간 신장 Large_Lymphocyte

radius_worst = float(input('radius_worst : '))
texture_worst = float(input('texture_worst : '))
perimeter_worst = float(input('perimeter_worst : '))

import pickle

with open('datasets/BreastCancerWisconsin.pkl', 'rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_labels = [[radius_worst, texture_worst, perimeter_worst]] 
    result_predict = loaded_model.predict(input_labels)
    print('predict age result : {}'.format(result_predict))
    pass
# array([1]
# [1]