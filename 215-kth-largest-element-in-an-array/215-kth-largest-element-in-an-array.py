import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxheap = [-n for n in nums]
        # heapq.heapify(maxheap)
        # # print(maxheap)
        # for i in range(k-1):
        #     heapq.heappop(maxheap)
        # return -maxheap[0]
    
        minHeap = []
        for x in nums:
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]
        
        # maxHeap = [-x for x in nums]
        # heapify(maxHeap)
        # for i in range(k-1):
        #     heappop(maxHeap)
        # return -maxHeap[0]        