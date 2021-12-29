# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         # start = 0
#         # end = 1
#         # mid = (end-start)//2 + start
#         # print(mid)
#         start = 0
#         end = len(letters) -1
#         while start < end:
#             mid = (end-start)//2 + start
#             if letters[mid] > target:
#                 end = mid 
#                 # break
#             else:
#                 start = mid + 1
      
#         return letters[((start) % len(letters))]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_length = len(letters)
        low = 0
        high = letters_length - 1
        
		# target is outside the bounds of letters
		# because the array is circular, this means that the next greatest value 
		# must be the first value in the array. If the value is within the bounds
		# of the array we can perform our regular modified binary search
        if target < letters[low] or target >= letters[high]:
            return letters[low]

        while low <= high:
            middle =  (low + high) // 2
            candidate = letters[middle]
            
            if target < candidate: 
                high = middle - 1
            
			# becuase we're looking for the smallest value thats greater then the target
			# we can condense the typical case where target == letters[middle] into the 
			# the target > letters[middle] case
            if target >= candidate :
                low = middle + 1
        
        return letters[low]