"""
Author: carole luo
Median:
After arranging the numbers in increasing or decreasing order:
- If number of terms is odd,
Median = middle number
- If number of terms is even,
Median = average of middle two numbers
Example: numbers = [3,2,5,4,1,0]
m = median(numbers)
print(m)
Output: 2.5
"""
class averages():
    def median(num_list):
        # Sort the list in ascending order.
        num_list.sort()
        # Check if the number of terms is odd or even.
        num_of_numbers = len(num_list)
        if num_of_numbers % 2 == 0:
            idx1 = num_of_numbers//2
            idx2 = num_of_numbers//2 -1
            sum_of_middle_two_numbers = num_list[idx1] + num_list[idx2]
            median = sum_of_middle_two_numbers/2
            return median
        else:
            idx = num_of_numbers//2
            median = num_list[idx]
            return median
 
    """
    Mean/Average
    """
    def mean(num_list):
        num_of_numbers = len(num_list)
        sum = 0
        for num in num_list:
            sum += num
        mean = sum / num_of_numbers
        return mean

    """Mode"""
    def mode(num_list):
        pass

"""
Author:Andrew
Arithemetic: An arithmetic sequence is a sequence of numbers
with the same difference between consecutive terms.
Parameters:
    Start: Where the interval starts (default is 0)
    Stop: Where the interval ends
    Step: how much it increaces every step
Example: 
x=arithemtic(4, 11, 2)
a=x.sequence()
print(a)
for c in a:
    print(c)

output:4, 6, 8, 10

"""
class arithemtic:
    def __init__(self, start, stop, step):
        self.start = start
        self.step = step
        self.stop = stop
        self.array = range(self.start,self.stop, self.step )

    def sequence(self):
        return self.array
        
        
    '''Author:Bryan
    This will return the number of numbers in the sequence
    Example:
    x=arithemtic(4, 11, 2)
    print(x.num_terms())
    '''

    def num_terms(self):
        return(len(self.array))
    '''Author:Bryan
    This will return the mean of the numbers in the sequence.
    Example:
    x=arithemtic(4, 11, 2)
    print(x.average())
    '''
    def average(self):
        if len(self.array) == 0:
            raise Exception("Your numbers do not have a list")
 
        else:
            numofnums = len(self.array)
            sum = 0
            for num in self.array:
                sum += num
            average = sum / numofnums
            return average
x=arithemtic(12, 11, 2)
print(x.average())