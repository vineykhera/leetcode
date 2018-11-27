#Given an array containing only digits 0-9, add one to the number and return the array.
#E.g. Given [1, 4, 2, 1] which represents 1421, return [1, 4, 2, 2] which represents 1422

class solution:
    def arraylast(self, num):
        result = [x for x in num]
        last = len(result) - 1
        result[last] += 1
        return result

sol = solution()
#print(sol.arraylast([1,2,3]))
res = sol.arraylast([1,2,3])
print(res)
print(''.join(str(res)))
