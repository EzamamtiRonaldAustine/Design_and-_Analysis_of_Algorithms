#Question 2

# 2. Consider the following grading policy, specifically the rounding policy. 
# A. Every student receives a grade or mark in the range of 0 to 100. No 
# negatives are allowed. 
# B. Any grade below 50 is a failure.  
# C. If the difference between the grade or mark and the next multiple of 5 is 
# less than 3 , round grade or mark  up to the next multiple of 5. (Guess you 
# would love this rule) e.g.  if mark = 69 round to 70 (70 - 69 is less than 3) 
# D. If the value of is less than 50, no rounding occurs as the result will still be 
# a failing grade e.g.  if mark = 43 is less than 50, no rounding. 
# Write down your pseudo code to implement an algorithm that takes in a mark 
# and implements the rules suggested above. 

#Pseudo code
# 1. Define a function called rounding_grade that takes a list of marks.
# 2. Create an empty list called rounded_marks to store the final results.
# 3. For each mark in the list, do the following:
#    a. If the mark is less than 0 or more than 100: Print "Invalid mark" along with the mark and 
#       skip to the next mark.   
#    b. If the mark is below 50:
#       - Add the mark to the rounded_marks list without changing it.
# 4. For marks 50 or above:
#    a. Find the next multiple of 5 (eg for 69 is 70).
#    b. Check the difference between the mark and this next multiple of 5:
#       - If the difference is less than 3, round up to this next multiple of 5.
#       - Otherwise, keep the original mark unchanged and add it to the list.
# 5.return the rounded_marks list.



#The  following is a Python code that implements the pseudo code:
def rounding_grade(marks):
    # Create a new list to store the rounded marks
    rounded_marks = []

    for mark in marks:
        # Check for invalid marks
        if mark < 0 or mark > 100:
            print(f"Invalid mark: {mark}.")
            continue  # Skip to the next mark
        
        elif mark < 50:
            rounded_marks.append(mark)  # Add the mark unchanged
        
        else:
            # Calculate the next multiple of 5
            next_multiple_of_five = (mark // 5 + 1) * 5
            
            # Check if the difference is less than 3
            if next_multiple_of_five - mark < 3:
                # Round up to the next multiple of 5
                rounded_marks.append(next_multiple_of_five)
            else:
                rounded_marks.append(mark)  # Add the original mark if no rounding occurs
    
    # Return the updated list of marks
    return rounded_marks

marks_list = [-1, 167, 45, 82, 39, 88, 92, 87, 74, 81, 73]
print(f"Original mark list: {marks_list}")
rounded_marks = rounding_grade(marks_list)
print(rounded_marks)
print(sorted(rounded_marks)) 