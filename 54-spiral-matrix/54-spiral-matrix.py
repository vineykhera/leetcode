class Solution:
    def spiralOrder(self, inputMatrix: List[List[int]]) -> List[int]:
        row = len(inputMatrix)
        col = len(inputMatrix[0])
        cnt = 0
        left, right, top, down = 0,col-1,0,row-1
        out = []

        while True:
            cnt = len(out)
            # print(cnt, row*col)
            if cnt == row*col:
                return out

            # print(left, right, top, down)

            for i in range(left,right+1): 
                out.append(inputMatrix[top][i])
            top += 1
            cnt = len(out)            
            if cnt == row*col:
                return out

            for j in range(top, down+1):
                out.append(inputMatrix[j][right])
            right -= 1
            cnt = len(out)
            if cnt == row*col:
                return out

            for k in range(right, left-1, -1): 
                out.append(inputMatrix[down][k])
            down -= 1
            cnt = len(out)
            if cnt == row*col:
                return out

            for l in range(down,top-1,-1): 
                out.append(inputMatrix[l][left])
            left += 1        
            cnt = len(out)
            if cnt == row*col:
                return out
        #cnt = len(out)
            # print(out)
        #return         