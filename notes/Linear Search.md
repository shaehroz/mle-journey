
Given an array find a target number x from said array and return the position. If number x isn't in array return -1.

for i in range(len(arr)):
	if arr[i] == target:
		return i
return -1


