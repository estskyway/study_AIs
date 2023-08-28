# 예제 [[16.34, 87.21]]
# input() return str() -> float()
texture_mean = float(input('texture_mean : '))
perimeter_mean = float(input('perimeter_mean : '))

import pickle

with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식맞게 적용
    result_predict = loaded_model.predict(input_labels)
    print('predict radius_mean result : {}'.format(result_predict))
    pass

# array([13.45096511])