'''
Problem 1: 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''

def is_divisible(a: int, b: int) -> bool:
    '''
    This function takes two integers and checks if they are divisbile
    '''
    if a%b == 0:
        return True
    else:
        return False
    
def return_multiples(array: list, a: int) -> list:
    '''
    This function checks an array/list of numbers for mutiples of a given
    number integer a
    '''
    multiples = []
    for val in array:
        if is_divisible(val, a):
            multiples.append(val)
        else:
            pass
    return multiples


if __name__ == "__main__":
    num_max = 1000
    search_range = range(1, num_max)
    #calculate all multiples of 3 that are less than num_max 
    multiples_3 = return_multiples(search_range, 3);
    #calculate all multiples of 5 that are less than num_max
    multiples_5 = return_multiples(search_range, 5);
    #use sets to calcualte the set union (or function)
    multiples_3_or_5 = list(set(multiples_3) | set(multiples_5))
    #print answer
    answer = f"\nThe sum of all multiples of 3 or 5 that are less than "
    answer += f"{num_max} is {sum(multiples_3_or_5)}.\n"
    print(answer)

    #note that the above problem can also be solved as a one liner
    #in python as follows
    another_solution = sum([x for x in range(1, 1000) if (x%3 == 0) or (x%5 == 0)])
    #print(another_solution)
    #print another answer
    answer_2 = f"\nThe solution using list comprehension is also " 
    answer_2 += f"{another_solution}.\n"
    print(answer_2)
