#User function Template for python3
#9:22
"""
cur = A

"""
class Solution:
    def find_permutation(self, S):
        # Code here
        out = []
        path = []
        
        # def permute(S, index, path, out):
        #     for i in range(index):
        #         permute(S,S[:i],)
                
        
        # permute(S, 0, path, out )
        # return out
        
        if len(S) == 1:
            # print("ret", S)
            return S
        
        for i in range(len(S)):
            curS = S[:i] + S[i+1:]
            perms = self.find_permutation(curS)
            # print("find perms:", perms, " for ", curS )
            temp = []
            for perm in perms:
                newperm = str(perm) + str(S[i])
                temp.append(str(newperm))
            # print("after append of ", S[i], " perms is", temp)
            out.extend(temp)
            # S += ch
        out.sort()
        return out

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends