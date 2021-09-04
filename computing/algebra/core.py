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