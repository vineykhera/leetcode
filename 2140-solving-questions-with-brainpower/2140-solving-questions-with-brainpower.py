"""
min > lambda : k: k[1]
max > lambda : k: k[0]
graph[0] = 3
1:
2:
3:

0:3
1:5
2:
3:
5:
                  4   4   2
                        

"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        rightmax = [0]* len(questions)
        maxatpos = [0]* len(questions)
        totques = len(questions)
        
        for i in range(totques-1, -1,-1):
            if i+1+questions[i][1] <= len(questions) -1 and rightmax[i+1+questions[i][1]]:
                maxatpos[i] = questions[i][0] + rightmax[i+1+questions[i][1]]
            else:
                maxatpos[i] = questions[i][0]

            if i+1 <= len(questions) -1 and rightmax[i+1]:
                rightmax[i] = max(maxatpos[i],rightmax[i+1])
            else:
                rightmax[i] = maxatpos[i]
                
        # print(maxatpos)
        # print(rightmax)
        return rightmax[0]    