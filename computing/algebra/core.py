class averages():
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
    def median(self, num_list):
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
    Author: carole luo
    Mean/Average:
    Mean = average of all terms = sum of all terms/number of terms
    """
    def mean(self, num_list):
        num_of_numbers = len(num_list)
        sum = 0
        for num in num_list:
            sum += num
        mean = sum / num_of_numbers
        return mean

    """
    Mode:
    Most common term(s)
    """
    def mode(self, num_list):
        pass

    """
    Author: carole luo
    Hamonic Mean:
    In mathematics, the harmonic mean is one of several kinds of average, and in particular, is one of the three Pythagorean means. 
    Typically, it is appropriate for situations when the average rate is desired. 
    Example: If we travel 10 km at 60 km/h, then another 10 km at 20 km/h, what is our average speed? 
    The formula would be harmonic mean = 2/(1/60 + 1/20) = 30 km/h.
    Code example:
    x = averages()
    lst = [1,2,4]
    result = x.harmonic_mean(lst)
    print (result)
    Output: 1.7142857142857142
    """
    def harmonic_mean(self, num_list):
        sum = 0
        for i in num_list:
            if not i == 0:
                sum += 1/i
        if not sum == 0:
            return len(num_list)/sum
        else:
            return sum

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

    """
    Author:Andrew
    nth_term: The nth term is start term + (n-1)step
    Example: 
    x=arithemtic(4, 14, 2)
    print(x.nth_term(2))

    output:8
    This is because 8 is the second term in this sequence.
    """


    def nth_term(self, n):
        if n < len(self.array) * (-1) or n >= len(self.array):
            return None
        return(self.array[n])

    """
    Author:Andrew
    Sum: The sum is when you add all the numbers in the arithimetic sequence.
    Example: 
    x=arithemtic(4, 14, 2)
    print(x.sum())

    output:40
    This is because all the digits add up to 40.
    """



    def sum(self):
        sum=0
        for x in self.array:
            sum += x
        return sum


        
