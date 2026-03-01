import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def trigger_overflow(x):

    Max_Value = (2**31)-1
    Min_Value = -(2**31)-1
    if x > Max_Value:
        return Min_Value + x - Max_Value
    elif x < Min_Value:
        return Max_Value - x + Min_Value
    else:
        return x 


def number_to_digits(n):
    '''
    takes a number, and converts it to a list of digits
    '''
    digits = []
    
    while n > 0:
        n, digit = divmod(n,10)
        digits.append(digit)
    
    return digits 
    


def compare_digits(value1,value2,value3):
    """
    Conditions: 
        1 < a < b < m and 
        10 < b − a < 20
    Takes digitized numbers, gets a random value b that is between index 22
    and index max index - 1, and value a, which is between 
    b-18, and b+11. Then it compares each digit between indexes a and b
    """
    rng = np.random.default_rng()
    max_index = len(value1)
# 11 to 19
# 2 to len-1
    b = rng.integers(low=20, high = max_index-1)
    a = rng.integers(low=b-18, high = b+11)-1
    
    slice_1 = value1[a:b]
    slice_2 = value2[a:b]
    slice_3 = value3[a:b]
    print(f"indices a-b: {a}-{b}\n")
    for i in range(len(slice_1)+1):
        if slice_1[i]==slice_2[i]==slice_3[i]:
            print(f"index{i}: {slice_1[i]} {slice_2[i]} {slice_3[i]}\n")
        else:
            print("*****mismatch found********\n")
            print(f"index{i}: {slice_1[i]} {slice_2[i]} {slice_3[i]}\n")


def create_test_cases(n,min,max):
    test_cases = []
    rng = np.random.default_rng()
    for i in range(0,n+1):
        test_case = rng.integers(min,max,size=2)
        test_cases.append(test_case.tolist())
    return test_cases

  
def record_results(function,cases):
    calculations = []
    times = []
    for case in cases:
        st = time.time()
        result = function(*case)
        et = time.time()
        run_time = et - st 
        rt_milliseconds = run_time * 1000
        calculations.append(result)
        times.append(rt_milliseconds)

    dict = {
            "(x,n)": cases, 
            "polynomial": calculations,
            "run_time_ms": times
        },
    record = pd.DataFrame(data=dict)
 #   record.set_index("(x,n)",inplace=True)
    return record

def plot_results(results,names):
    colors = ["red","green","blue"]
    for result,name,color in results,names,colors:
        x = result["calculations"]
        y = result["times"]
        plt.plot(x,y,color = color,label=name)
    plt.xlabel("Polynomial Value")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.show()

#  def compare_digits(self):






