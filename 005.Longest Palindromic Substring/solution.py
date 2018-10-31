class Solution(object): #本解法时间复杂度为O(N^3)
    def isPalinSubstr(self, s):
        i=0
        j=len(s)-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return -1

        return len(s)

    def LongestPalinSubstr(self,s):
        i=0
        j=len(s)-1
        longestLength=0
        longestSubstr=''
        while i < len(s):
            while j > i:#寻找s[i]的回文子串
                if s[j] == s[i]:
                    temp = s[i:j+1]
                    if len(temp) < longestLength:
                        break
                    else:
                        l = Solution().isPalinSubstr(temp)
                        if l>longestLength:
                            longestSubstr=temp
                            longestLength=l
                    break
                else:
                    j-=1
            i+=1
            j=len(s)-1

        return longestLength,longestSubstr



if __name__=='__main__':
    s = 'abbabbua'
    #l = Solution().isPalinSubstr(s)
    #print(l)
    res_l,res_s = Solution().LongestPalinSubstr(s)
    print(res_l,res_s)