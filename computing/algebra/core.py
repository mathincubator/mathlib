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
x=arithemtic_sequence(4, 11, 2)
a=x.sequence()
print(a)
for c in a:
    print(c)
output:4, 6, 8, 10
"""

class arithemtic_sequence:
    def __init__(self, start, stop, step):
        self.start = start
        self.step = step
        self.stop = stop
        self.array = range(self.start,self.stop, self.step )

    def sequence(self):
        return self.array

    """
    Author:Bryan
    This will return the number of numbers in the sequence
    Example:
    x=arithemtic(4, 11, 2)
    print(x.num_terms())

    output: 4

    """

    def num_terms(self):
        return(len(self.array))

    """
    Author:Bryan
    This will return the mean of the numbers in the sequence.
    Example:
    x=arithemtic(4, 11, 2)
    print(x.average())
    output: 7.0
    """
    def average(self):
        if len(self.array) == 0:
            raise Exception("Your list is empty")
 
        else:
            numofnums = len(self.array)
            sum = 0
            for num in self.array:
                sum += num
            average = sum / numofnums
            return average

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
            raise Exception("Number is not in the index range")
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


class quadratic:
    """
    Author:Gavin
    Quadratic: A quadratic function a*x^2 + b*x + c discriminant is b^2 - 4*a*c
    It can be positive, zero, or negative, and this determines how many solutions there are to the given quadratic equation.
    .A positive discriminant indicates that the quadratic has two distinct real number solutions.
    .A discriminant of zero indicates that the quadratic has a repeated real number solution.(a.k.a one solution)
    .A negative discriminant indicates that neither of the solutions are real numbers.(a.k.a no real solutions)

    Parameters:
    a: The coefficient of the second degree
    b: The coefficient of the first degree
    c: The constant
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    """
    Return the discriminant of a quadratic function.
    """
    def discriminant(self):
        discriminant = pow(self.b,2) - 4*self.a*self.c
        return discriminant

    """
    Author: carole luo
    Quadratic equation:
    In algebra, the quadratic equation is an equation where x represents an unknown term, and a, b, and c represent known numbers,
    and where a≠0.
    If a=0, then the equation is linear, not quadratic, as there would be no ax^2 term. 
    The numbers a, b, and c are coefficients of the equation and may be differentiated by calling them the quadratic coefficient,
    the linear coefficient and the constant/free term.
    Example:
    x = quadratic()
    y = x.roots(-2, 2, 3)
    print(y)
    Output:
    (-0.8228756555322954, 1.8228756555322954)
    """
    def roots(self, a, b, c):
        D = (b*b - 4*a*c)**0.5
        self.root1 = (-b + D)/(2*a)
        self.root2 = (-b - D)/(2*a) 
        roots = (self.root1, self.root2)
        return roots

    
"""
Created on Sun Oct  3 20:13:10 2021
Calculate the sum of n even numbers from 2 to 2n.
2 + 4 + 6 + · · · + 2n = n(n + 1)
@author: gavin
"""
class EvenNumberSeries:
    """
    n is the number of even elements.
    
    """
    def __init__(self, n):
        
        self.n = n
        
    """
    Calculate the sum of even numbers
    Return the sum of even numbers from 2 to 2n.
    """
    def sumSeries(self):
        acc = 0
        item = 0
        while ( item <= 2 * self.n ) :
            acc = acc + item
            item = item + 2
        return acc 
    
    """
    Use the formula to calculate the sum of the even number series.
    """
    def sumUsingFormula(self):
        return self.n * ( self.n + 1 ) 

"""
@author: Shaoming
Calculates the number of subsets of size n and the formula to find it is 2^n

Example:
if n = [1, 2, 3, 4, 5]
then we the number of elements in the set, which in this case, is 5.
Result:
s = Subsets([1,2,3,4,5])
a = s.findSubsets()
print(a)
Output: 32
2^n = 2^5 = 32
Therefore the amount of subsets of size n is 32.
"""
class Subsets:
    """
    n represents the number of elements in the set.
    """
    def __init__(self, n):
        self.n = n
    
    def findSubsets(self):
        amt = 1
        for x in range(len(self.n)):
            amt *= 2
        return amt 
    """
    To find the amount of proper subsets, subtract 1 a = findSubsets([1, 2, 3])-1
    """
"""
@auther: Fred Xu
Calculates the sum of the first n odd numbers.
1+3+5... (2n+1)=n²

Example:
if n = 5
then we are calculating the sum of the first 5 odd numbers [1, 3, 5, 7, 9]

Result:
n² = 5² = 25
Therefore the sum of the first 5 odd numbers is 25.
"""
class OddNumberSequence:
    """ 
    n is the number of numbers in the odd number sequence.
    """ 
    def __init__(self, n):

        self.n = n
    
    """
    Checks if the number given is valid.
      - the number must be greater or equal to 0
    """
    def validat(self):
        if self.n < 0:
            raise Exception('The length of the sequence cannot be a negative number.')
            
    """
    Calculates the sum without the formula.
    """
    def sumWithoutFormula(self):
        OddNumberSequence.validat(self)
        total = 0
        for i in range(1, self.n+1):
            total += i*2-1
        return total
    
    """
    Calculates the sum using the formula n²
    """
    def sumWithFormula(self):

        OddNumberSequence.validat(self)
        
        return self.n ** 2

