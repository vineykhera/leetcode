class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        if placed == n:
            return True

        length = len(flowerbed)
        if length >=2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = "x"
            placed = 1
            
        for i in range(1, len(flowerbed)-2):
            if placed < n and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = "x"
                placed += 1
                
        # print(flowerbed)
        
        if placed != n and flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            flowerbed[len(flowerbed)-1] = "x"
            placed += 1

        print(flowerbed)
        
        return True if placed == n else False
    
        # def helper(start, placed):
        #     if n == placed:
        #         return True
        #     for i in range(start, len(flowerbed)-2):
        #         if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        #             placed += 1
        #             helper(i+1,placed)
        #             # placed -= 1
        
        # return helper(1,0)