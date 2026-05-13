class Solution:
    def isHappy(self, n: int) -> bool:
        
        num = set()

        temp_sum = n
        while temp_sum not in num:
            num.add(temp_sum)
            s = str(temp_sum)
            
            temp_sum = 0
            for tmp in s:
                temp_sum += int(tmp) * int(tmp)
            
            print(s, temp_sum, num)
            if temp_sum == 1:
                return True
        return False
