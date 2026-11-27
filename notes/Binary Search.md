- Finds position of target value in a sorted array
- Binary search compares the target value to the middle element of the array, if they are not equal it removes the half corresponding to whether the target value is > or < the middle element of the array
- This is repeated until the target value is found
## Worked example

Array A = [1, 5, 6, 9, 15, 22], target = 6.

I tracked the part of the array still in play with two indices instead of slicing. Slicing broke the link between indices in the small list and the original list.
- low = 0
- high = len(A) - 1 = 5

I computed the middle as mid = (low + high) // 2. This works for odd and even lengths, so I did not need an odd/even special case.

Step 1
- low = 0, high = 5, mid = 2
- I checked A[mid] against the target.
- A[mid] = 6 == target therefore we can just return mid
## Rules I derived

- If target == A[mid], I returned mid. Done.
- If target < A[mid], the target could only be to the left, so I set high = mid - 1.

- I repeated while low <= high.- If target > A[mid], the target could only be to the right, so I set low = mid + 1.
- If low > high, nothing was left in play, so the target was not in the array. I returned -1.

## Mistakes I made on the first attempt

- I used A(M) instead of A[M]. Round brackets call a function, square brackets index.
- I compared the target to the index M instead of the value A[M].
- I forgot Python is 0-indexed, so my +1 in the midpoint formula was wrong.
- I sliced the list, which lost the original positions.

## Still to answer

- Why does halving each step give O(log n)?
The most common attributes of logarithmic running-time function is that the choice of an element to perform some action is one of several possibilities and only one will need to be chosen.

i.e. looking up people in a phonebook is O(log n) as we use divide and conquer by looking where their name is alphabetically. In every section you will need 

- What should I return when there are duplicates?