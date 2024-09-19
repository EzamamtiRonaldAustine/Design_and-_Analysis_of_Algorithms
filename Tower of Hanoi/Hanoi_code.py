import math

def towers_of_hanoi(n, source, target, transit, count_moves, count_recursion):
    count_recursion[0] += 1
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        count_moves[0] += 1
        return
    
    #Recursive call: move n - 1 disks from source to transit using target as transit peg
    towers_of_hanoi(n - 1, source, transit, target, count_moves, count_recursion)
    
    print(f"Move disk {n} from {source} to {target}")
    count_moves[0] += 1 
    
    #Recursive call: move n - 1 disks from transit to target using source as transit peg
    # count_recursion[0] += 1
    towers_of_hanoi(n - 1, transit, target, source, count_moves, count_recursion)
   
n = 5 #number of disks
count_moves = [0] 
count_recursion = [0]

towers_of_hanoi(n, 'A', 'B', 'C', count_moves, count_recursion)

print()
print(f"Total_number of moves/operations: {count_moves[0]}")
print(f"Total_number of recursive calls: {count_recursion[0]}")

expected_moves = 2**n - 1
excepted_recursion = 2**(n+1) - 1 # recursion counts both moves and calls
print()
print(f"Expected number of moves: {expected_moves}")
print(f"Expected number of recursive calls: {excepted_recursion}")