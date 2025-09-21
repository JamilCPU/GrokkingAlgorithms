#Binary Search
from typing import List
import random
randomNumbers = [random.randint(1, 65000) for _ in range(2000)]
sortedList = sorted(list(set(randomNumbers)))
target = 0;

def binarySearch(sortedList: List[int]):
    print(randomNumbers)
    target = input("Enter a number to perform binary search for!\n\n")
    target = int(target)

    print("Finding the index of " + str(target) + " using binary search")

    l, r= 0, len(sortedList)-1
    #Two pointers are created. 
    # One at the beginning of the list, the other at the end.
    while l <= r:
        #Find the mid-point between the left and right pointers
        m = (l + r) // 2

        #If we found the target simply return the target's index
        if sortedList[m] == target:
            break
        #If we found a number above target...
        #Update the right pointer, so we can look to find a smaller mid-point next iteration
        if sortedList[m] > target:
            r = m-1
        #If we found a number below target...
        #Update the left pointer, so we can look to find a larger mid-point next iteration
        else:
            l = m+1
    if sortedList[m] == target:
        print(str(target) + " was located at index: " + str(m))
    else:
        print(str(target) + " does not exist within the list")

binarySearch(sortedList)
