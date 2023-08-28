# [[2, 161, 26.7]]
# 입원기간 신장 Large_Lymphocyte

hospitality_day = float(input('입원기간 : '))
hight = float(input('신장 : '))
Large_Lymphocyte = float(input('Large Lymphocyte : '))

import pickle

with open('datasets/RecurrenceOfSurgery_Regression.pkl', 'rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_labels = [[hospitality_day, hight, Large_Lymphocyte]] 
    result_predict = loaded_model.predict(input_labels)
    print('predict age result : {}'.format(result_predict))
    pass

# array([43.432433]
# [43.432433]