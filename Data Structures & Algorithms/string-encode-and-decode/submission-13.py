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

        sub = ''
        while i < len(s):

            count_int = 0
            b = s[i]
            if b == "#": #길이를 가져온다 #가 나올때까지 
                count, sub = '', ''
                for j in range(i+1, len(s)):
                    if s[j] == "#":
                        break
                    count += s[j]
                count_int = int(count)
                #print(count_int, j)
                i = j+1
            
            #print(count_int)
            #if count_int == 0:
                #answer.append("")
                #continue
            sub = s[i:i+count_int]
            #count_int -= 1
            i += count_int
            #if sub and count_int == 0:
            answer.append(sub)
        
        
        #print(answer)
        return answer
