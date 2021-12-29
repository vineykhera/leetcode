class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        biright = 0
        bileft = 0
    
        def binsearch(nums, target, searchleft):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (end - start)//2 + start
                # print(mid, nums[mid], searchleft)
                if searchleft:
                    if nums[mid] == target and (mid == start or nums[mid-1] < target):
                        return mid
                    # elif nums[mid] == target and nums[mid-1] >= target:                        
                    elif nums[mid] >= target:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if nums[mid] == target and (mid == end or nums[mid+1] > target):
                        return mid
                    elif nums[mid] <= target:
                        start = mid + 1
                    else:
                        end = mid - 1
                    
            return -1
        
        if len(nums) > 1:
            bileft = binsearch(nums, target, True)
            biright = binsearch(nums, target, False)
        else:
            if target not in nums:
                return [-1,-1]
            else:
                return [0,0]
        return [bileft, biright]
