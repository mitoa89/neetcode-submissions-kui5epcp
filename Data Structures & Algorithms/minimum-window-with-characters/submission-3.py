class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        counter = Counter(t)
        window = Counter()
        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(counter)
        for r in range(len(s)):
            word = s[r]
            window[word] += 1
            if s[r] in counter and window[word] == counter[word]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        
        #start, end. list중에서 가장 짧은것
        '''
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
        '''
        return output