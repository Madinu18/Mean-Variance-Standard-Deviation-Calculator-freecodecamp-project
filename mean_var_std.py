import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(input_list).reshape(3, 3)

    mean_axis1 = np.mean(arr, axis=0).tolist()
    mean_axis2 = np.mean(arr, axis=1).tolist()
    mean = float(np.mean(arr))

    var_axis1 = np.var(arr, axis=0).tolist()
    var_axis2 = np.var(arr, axis=1).tolist()
    var = float(np.var(arr))

    std_axis1 = np.std(arr, axis=0).tolist()
    std_axis2 = np.std(arr, axis=1).tolist()
    std = float(np.std(arr))

    max_axis1 = np.max(arr, axis=0).tolist()
    max_axis2 = np.max(arr, axis=1).tolist()
    max_value = float(np.max(arr))

    min_axis1 = np.min(arr, axis=0).tolist()
    min_axis2 = np.min(arr, axis=1).tolist()
    min_value = float(np.min(arr))

    sum_axis1 = np.sum(arr, axis=0).tolist()
    sum_axis2 = np.sum(arr, axis=1).tolist()
    sum_value = float(np.sum(arr))

    calculations = {
        'mean': [mean_axis1, mean_axis2, mean],
        'variance': [var_axis1, var_axis2, var],
        'standard deviation': [std_axis1, std_axis2, std],
        'max': [max_axis1, max_axis2, max_value],
        'min': [min_axis1, min_axis2, min_value],
        'sum': [sum_axis1, sum_axis2, sum_value]
    }

    return calculations
