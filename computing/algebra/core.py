from fractions import Fraction

class polynomial():
    '''
    Author: Kyler Luo
    '''
    def __polynomial_calculation(self, co_list, x):
        # Degree is one less than the length of the co_list, because of the constant term.
        degree = len(co_list) - 1
        # A possible solution.
        result = 0

        # Assemble the polynomial.
        for co in co_list:
            result += co * x ** degree
            degree -= 1

        return result
    
    '''
    Author: Kyler Luo
    The rational root theorem uses the leading coefficient and the constant term
    of a polynomial to determine its rational roots (zeros).
    P is an integer factor of the constant term a0.
    Q is an integer factor of the leading coefficient aN.

    Example: 
    2x**2 - 5x - 3
    x = polynomial()
    roots = x.rational_roots([2,-5,-3])
    print(roots)

    Output: 
    [-0.5, 3]
    '''

    def rational_roots(self, co_list):
        # If the coeficient list is empty, raise an exception.
        if len(co_list) == 0:
            raise Exception("Coefficient can not be empty.")

        aN = co_list[0] # aN is the leading coefficient, hence the first element in co_list.
        a0 = co_list[-1] # a0 is the constant, hence the last element in co_list.
        aN_factors = [] # List for aN's factors.
        a0_factors = [] # List for a0's factors.
        possible_solutions = [] # Possible solutions.
        solutions = [] # Real solution(s)/root(s).

        # Check if the leading coefficient or the constant term is zero. If so, raise an exception.
        if a0 == 0 or aN == 0:
            raise Exception("Leading coefficient and/or the constant term can not be zero.")

        # Find the factors of the leading coefficient aN
        for i in range(1, abs(aN) + 1):
            if aN % i == 0:
                aN_factors.append(-i) 
                aN_factors.append(i)
        
        # Find the factors of the constant term a0
        for i in range(1, abs(a0) + 1):
            if a0 % i == 0:
                a0_factors.append(-i)
                a0_factors.append(i)

        # Add the p/q possible solutions to the possible_solutions list as fractions.
        for num1 in a0_factors:
            for num2 in aN_factors:
                possible_solutions.append(Fraction(num1, num2))

        # Create a possible solution set to avoide duplicates.
        possible_solution_set = set(possible_solutions)

        # Test the possible solution with the polynomial_calculation function.
        for i in possible_solution_set:
            s = self.__polynomial_calculation(co_list, i)
            # If the result is a zero (root), then add it to the solutions list.
            if s == 0:
                solutions.append(float(i))

        return solutions

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
    Author:Frankie
    Most common term(s)
    Mode: Most common elements in set.
    Example:
    Find the mode in the set below:
    [1,1,1,1,2,3,4]
    The mode is 1.
    Exmaple code:
    x = averages()
    y = x.mode([1,1,1,2,3,4,5,6])
    print(y)
    output：1

    """
    def mode(self, num_list):
            num_dict = {} # Empty dictionary for numbers in the num_list and their frequency
            num_set = set() # Empty set for numbers in num_list to avoide duplicates
            mode = [0] # List of modes (in case there is more than one mode)
            most_occurences = [0] # List of largest values (in case there is more than one mode)
            
            for num in num_list:
                num_set.add(num) # Add each number in num_list to the set
                occurences = 0 # Set the occurences to 0 inside the loop so it reset every to count for each number
                for x in num_list: # Loop over the num_list again to check occurences
                    if x == num: 
                        occurences += 1
                num_dict[num] = occurences # Add the number and its occurences to the dictionary
                
            for key in num_set:
                if num_dict[key] > most_occurences[0]: # Check if the number is greater than the current largest value
                    mode.clear() # Clear the mode list if a new largest number is found
                    mode.append(key) # Add the new largest number to the list
                    most_occurences.clear() # Clear the most_occurences list if there is a new largest value
                    most_occurences.append(num_dict[key]) # Add the new largest value
                
                elif num_dict[key] == most_occurences[0]: # Check if the number of occurences is equal than the current highest
                    most_occurences.append(num_dict[key]) # If they are the same then add the number of occurences to the list with the other value
                    mode.append(key) # Add the number to the list of modes, since it is tied with at least one other number
            
            if len(most_occurences) == 1: # If there is only one mode, convert it to an integer instead of a list
                mode = int(mode[0]) 
            
            return mode
    
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
    n is the number of even elements
    
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
Author:Andrew
Factorial: In mathematics, the factorial of a non-negative integer n is written as n! which is the product of all non-negative integers less or equal to n.
Example: 
print(factorial(4)) 
output:24
"""
def factorial(n):
    if n == 1:
        return 1 
    elif n > 1:
        return n * factorial(n-1)
    else:
        raise Exception("Your number has to be bigger or equal to 1")

"""
Author:Andrew
Combination: A combination is a possible arrangement in a collection of items where the order of the selection does not matter
Parameters:
n is the total amount of objects.
r is the amount of objects you want from n.
Example: 
print(combination(6,2)) 
output:15
"""
def combination(n,r):
    if n < r  or r < 0:
        raise Exception("r has to be bigger then 0 and smaller then n")
    else:
        return int(factorial(n) / (factorial(r)*factorial(n-r)))

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

"""
Author: Shaoming
Primes:
Prime numbers are numbers that has 2 factors and can only be divisible by 1 and itself.
For example, 7 is a prime number because its factors are only 1 and itself.
27 is not a prime number because it's factors are 1, 3, 9, 27.
1 is also not a prime number because its only factor is 1.

Prime Factorization:
Prime Factorization is the process of decomposing a non-prime (composite) number until it becomes a prime number.
Example: 27: 27/3 = 9, 9/3 = 3. Prime factors are 3, 3, 3. It can also be written as 3^3.

Example Code:
a = Primes(27)
print(a.primeFactorization()) 
prints the list: [3, 3, 3]
print(a.checkPrime())
prints False (because 27 isn't prime)

"""
class Primes:
    def __init__(self, n):
        self.n = n
    
    def primeFactorization(self): # Function for prime factorization
        list = []
        y = self.n
        x = 2
        for i in range(2, int(self.n)): # Loop for prime factorization
            while y%x == 0: # Adds factor to list if self.n%x = 0. Continues until it isn't then add 1 to x and repeat.
                list.append(x)
                y /= x
            x += 1
        if len(list) == 0:
            list.append(1)
            list.append(self.n)
        return list

    def checkPrime(self): # Function for checking primes
        if self.n == 1 or self.n == 0 or (self.n % 2 == 0 and self.n > 2): # Checks if a is greater than 1, not even, and not 2.
            return False
        else: 
            for i in range(3, int(self.n**(1/2))): # Dividing by 3 and then progressively adding one until equal to self.n. 
                if self.n % 2 == 0:
                    return False
            return True


"""
Author:Allan
Geometric: A geometric sequence is a sequence of numbers with the same ratio between consecutive terms.
1,2,4,8,16,32...,1024 is a geometric sequence because there is always a ratio of 2 between consecutive terms.

Example:
print(sequence(2,3,9))
first number is your first term, second number is your common ratio, third number is how many terms you want it to output
"""

class geometrics:

    def geometric_sequence(num, constant, length):
        sequence = []
        x = num
        for i in range(length):
            x *= constant
            sequence.append(x)
        return sequence 
    