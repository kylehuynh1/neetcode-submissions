import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #looks like we use heap/prio q for this question
        #hashmap, send into a heap ? 
        
        freqMap = {} #hashmap init

        #increment every number appearance by one
        #key = number, value = frequency
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        #creation of heap
        heap = []

        #send number and corresponding freq. to maxheap
        for num, freq in freqMap.items():
            heapq.heappush(heap, (-freq, num)) #neg. freq bc heaps are min by default
            
        result = [] #store top k freq, will be returned later
        for i in range(k): 
            freq, num = heapq.heappop(heap) #remove top k frequent elements
            result.append(num) #send to result array

        return result    
