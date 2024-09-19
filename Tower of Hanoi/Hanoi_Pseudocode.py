# Start the program to move disks from one peg to another

# 1. Define a function "towers_of_hanoi" with the following inputs:
#     - n (number of disks)
#     - source (the starting peg)
#     - target (the destination peg)
#     - transit (the temporary peg)
#     - count_moves (a list to count the number of moves)
#     - count_recursion (a list to count the number of recursive calls)

# 2. Every time the function is called, increase the recursive call count by 1.

# 3. If there is only 1 disk:
#     - Move the disk from the source peg to the target peg.
#     - Print this move.
#     - Increase the move count by 1.
#     - Return from the function.

# 4. Otherwise, if there are more than 1 disk:
#     - Move the first n-1 disks from the source peg to the transit peg, using the target peg as temporary storage.
#     - Move the nth (largest) disk from the source peg to the target peg.
#     - Print this move.
#     - Increase the move count by 1.
#     - Move the n-1 disks from the transit peg to the target peg, using the source peg as temporary storage.

# 5. After solving the problem, print the total number of moves and the total number of recursive calls.

# 6. To calculate the expected (theoretical) values:
#     - The expected number of moves is 2^n - 1.
#     - The expected number of recursive calls is 2^(n+1) - 1.

# 7. Print both the actual and expected values for moves and recursive calls.

# End the program.
