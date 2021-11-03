

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
    Mode:Most common term(s) in a data set.
    Author:frankie
    Example:
        Evaluate the set and find the mode:[1,2,3,4,5,6,7,8,9,1,1,1]
        The mode is the element shown the most commonly in a set.
        The mode in the set is 1; and is unimodal because there is only one mode.
        
    TEST Code:
def mode(num_list):
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
            
        for key in num_dict:
            print(key, ":", num_dict[key])
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
        
        print("The mode is", mode)
        return mode
    
mode([1,2,1,1,3,4,1,4,7,7,7,7,7,7,7,7,1,1,1,1,1,7,8,8,8,8,8,8,8,8,8])
        
    """
def mode(self,num_list):
        num_dict = {} # Empty dictionary for numbers in the num_list and their frequency
        self.mode
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
            
        for key in num_dict:
            print(key, ":", num_dict[key])
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
