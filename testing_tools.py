import inspect
import time
class TestCases:
    def __init__(self,function, cases):
        self.function = function
        self.times = []
        self.cases = cases

    def get_results(self):
    
        function = self.function
        times = self.times 

        for element in self.cases:
            start_time = time.time()
            result = function(*element)
            end_time = time.time()
            self.times.append(end_time-start_time)

            print(f"{element}\n")
            print(f"{result}\n")
        
    def get_times(self):
        print(self.times)


            