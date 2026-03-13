from re import M
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def trigger_overflow(x):
    '''
    tests a value x, if larger than the max value for a signed integer, takes the remainder of 
    x, and adds the minimum value to it, then repeats until x wraps around and becomes negative.
    '''
    Max_Value = (2**31)-1
    Min_Value = -(2**31)-1
    
    if x > Max_Value:
        value = (x % Max_Value)+Min_Value
        x = trigger_overflow(value)

    
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
    b = rng.integers(20, max_index)

    # choose valid distance
    diff = rng.integers(11, 20)  
    a = b - diff
    
    slice_1 = value1[a:b]
    slice_2 = value2[a:b]
    slice_3 = value3[a:b]
    print(f"indices a-b: {a}-{b}\n")

    for i in range(len(slice_1)):
        if slice_1[i]==slice_2[i]==slice_3[i]:
            print(f"index{i}: {slice_1[i]} {slice_2[i]} {slice_3[i]}\n")
        else:
            print("*****mismatch found********\n")
            print(f"index{i}: {slice_1[i]} {slice_2[i]} {slice_3[i]}\n")


def create_test_cases(n,min,max):
    '''
    creates n cases between min and max value
    '''
    test_cases = []
    rng = np.random.default_rng()
    for i in range(0,n+1):
        test_case = rng.integers(min,max,size=2)
        test_cases.append(test_case.tolist())
    return test_cases

  
def generate_results(function,cases):
    '''
    given a function, and a list of test cases, generates values and times for each case
    '''
    records = [] # keep track of data dictionaries
    for case in cases:
        record = {} # store experiment data in dictionary
    # run experiment, and record time in milliseconds
        st = time.time()
        result = function(*case)
        et = time.time()
        run_time = et - st 
        run_time_ms = run_time * 1000
    # store results of experiment
        record["x"]=case[0]
        record["n"]=case[1]
        record["value"]=result
        record["time_ms"]=run_time_ms
        records.append(record)

        result = pd.DataFrame(data=records,dtype='object')
        result.set_index('value',inplace=True)
        result.sort_index(inplace=True)

    return result

def plot_results(results,names):
    '''
    was not used
    '''
    colors = ["red","green","blue"]
    for result,name,color in results,names,colors:
        x = result.index
        y = result["time_ms"]
        plt.plot(x,y,color = color,label=name)
    plt.xlabel("Polynomial Value")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.show()








