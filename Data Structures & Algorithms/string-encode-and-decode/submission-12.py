class Solution:

    def encode(self, strs: List[str]) -> str:
        c = ''
        for s in strs:
            c += "#" + str(len(s)) + "#" + s
            
        return c

    def decode(self, s: str) -> List[str]:
        
        answer = []
        print(s)
        i = 0

        count_int = 0
        sub = ''
        while i < len(s):
            b = s[i]
            if b == "#" and count_int == 0: #길이를 가져온다 #가 나올때까지 
                count, sub = '', ''
                for j in range(i+1, len(s)):
                    if s[j] == "#":
                        break
                    count += s[j]
                count_int = int(count)
                #print(count_int, j)
                i = j+1
            
            #print(count_int)
            if count_int == 0:
                answer.append("")
                continue
            sub += s[i]
            count_int -= 1
            i += 1
            if sub and count_int == 0:
                answer.append(sub)
        
        
        #print(answer)
        return answer
