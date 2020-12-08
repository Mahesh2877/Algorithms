#https://www.linkedin.com/posts/coding-club_asked-codingmafia-india-activity-6741324523674615808-Wl9K

"""
Problem Statement:-
Given an array called "input_array" -> Check if it can become non-decreasing
by changing utmost one element.

When read from left -> right, the elements must always be non-decreasing.
If not, it should become one by modifying at most one element.
"""

"""
Solution:-
We use a Stack for this.
Iterate through the list, If the element is increasing -> Push it on the Stack.
If the element is decreasing -> Pop the top of stack and compare it with the new top.

The number of times we pop from the stack indicates the number of elements we
need to modify.
If we Pop twice -> we can return FALSE immediately.
If we successfully go through the entire list while popping at most once -> we
can return TRUE.
"""

def non_decreasing_array(input_array):
    count = 0
    stack = []
    top = 0
    stack.append(input_array[0])

    for i in range(1, len(input_array)):
        if(stack[top] <= input_array[i]):
            top += 1
            stack.append(input_array[i])
            continue
        while(stack[top] > input_array[i]):
            top -= 1
            stack.pop()
            count += 1
            if(count > 1):
                return False
            if(top < 0):
                break
        top += 1
        stack.append(input_array[i])

    return True


#Test Case 1, should return FALSE
input1 = [1, 4, 6, 8, 5, 7]
print(input1)
print(non_decreasing_array(input1))
print("\n")

#Test Case 1, should return TRUE
input2 = [4, 2, 3]
print(input2)
print(non_decreasing_array(input2))
print("\n")
