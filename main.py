"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    # Base Case if x is less than or equal to 1
    if x <= 1:
        return x
    else:
        ra = (foo(x-1)) # defines ra to be one number less than x, also a recursive call
        rb = (foo(x-2)) # defines rb to be two numbers less than x, also a recursive call
        return ra + rb # adds ra and rb together

def longest_run(mylist, key):
    ### TODO
    longest = 0 # Will store the longest run of "key"
    current = 0 # Will track the current run of consecutive key values

    # For loop to interate through the whole list
    for integer in mylist:
        # checks if the list value is equal to the key
        if integer == key:
            # if list value is equal to key, add one to current
            current += 1
        else:
            # If there is a different number than the key, update the longest value
            longest = max(longest, current)
            # Reset the count
            current = 0
    # Making sure longest equals the longest run of the key
    longest = max(longest, current)
    
    return longest 



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    # Base case if there's only one element in the key
    if len(mylist) == 1:
        if mylist[0] == key:
            # if the one element matches the key, return the corresponsing Result class object
            return Result(1, 1, 1, True)
        else: 
            # if the one element does not match the key, return the corresponsing Result class object
            return Result(0, 0, 0, False)
    
    # Divide and conquer part!
    middle = len(mylist) // 2 # Split list into two
    left_result = longest_run_recursive(mylist[:middle], key) # Recursively call the function on the left split of the list
    right_result = longest_run_recursive(mylist[middle:], key) # Recursively call the function on the right split of the list

    # Handles the left and right run size by checking if it's the entire range of values and if not, it merges them together
    left_size = left_result.left_size if not left_result.is_entire_range else left_result.left_size + right_result.left_size
    right_size = right_result.right_size if not right_result.is_entire_range else right_result.right_size + left_result.right_size

    # Computes the longest run size by taking the max of the right recursive result, left recursive result, and the combined ones over the middle
    longest_size = max(to_value(left_result), to_value(right_result), left_result.right_size + right_result.left_size)

    is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    # Returns result object
    return Result(left_size, right_size, longest_size, is_entire_range)



