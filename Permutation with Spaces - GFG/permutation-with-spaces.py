#User function Template for python3
"""
ABC


"""
class Solution:
    def permutation(self, S):
        # code here
        permstrs = []
        
        def helper(curstr, start, permstrs, length):
            # print(curstr, start, permstrs,length)
            if start == length - 1:
                permstrs.append(curstr)
                return
            
            helper(curstr,start+1,permstrs,length)
            helper(curstr[:start+1] + " " + curstr[start+1:],start+2,permstrs,length+1)

        helper(S,0, permstrs, len(S))
        
        permstrs.sort()
        return permstrs
        

        
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends