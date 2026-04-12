class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #start, end. list중에서 가장 짧은것
        found = False
        output = ''
        charSet = Counter(t)

        for l in range(len(s)):

            window = Counter()

            if s[l] in charSet:
                for r in range(l, len(s)):
                    if s[r] in charSet:
                        window[s[r]] += 1
                    
                    if window >= charSet:
                        temp = s[l:r+1]

                        print(temp, window, charSet)
                        if found == False:
                            found = True
                            output = temp
                        if len(temp) < len(output):
                            output = temp
                        break
                    
            else:
                l += 1

        return output