class Solution(object):
    def reverse(self, x):
        arr = list(str(x))
        n = len(arr)
        new_arr = [0] * n
        k = 0
        if arr[0] == '-':
            new_arr = [0] * (n-1)
            for i in range(n-1,0,-1):
                new_arr[k] = arr[i]
                k+=1
                ans = [str(integer) for integer in new_arr]
                a_string = "".join(ans)

                res = int(a_string) - 2*int(a_string)
        
        else:
            for i in range(n-1,-1,-1):
                new_arr[k] = arr[i]
                k+=1
                
                ans = [str(integer) for integer in new_arr]
                a_string = "".join(ans)

                res = int(a_string)
        
        return res