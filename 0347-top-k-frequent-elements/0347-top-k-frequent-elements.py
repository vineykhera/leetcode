"""
1,3
2,2
3,1

push to min heap of size k
if len(heap) becomes > k then pop 


"""

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heaparr = []
        cntnums = collections.Counter(nums)
        #heaparr = [(cnt,n) for n, cnt in cntnums.items()]
        
        #heapq.heapify(heaparr)

        for n,cnt in cntnums.items():
            heapq.heappush(heaparr, (cnt, n))
            if len(heaparr) > k:
                heapq.heappop(heaparr)
        
        return [y for x,y in heaparr]
        