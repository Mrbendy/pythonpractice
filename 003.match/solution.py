class Solution(object):
    def longestSubstring(self,s):
        i = 1
        temp = 1
        longest = 0
        sub = s[0]
        while i < len(s) :
            #如果出现重复改变起始点
            if s[i] in sub :
                if len(s)-i <= longest:
                    break
                else:
                  longest = temp
                  longest_sub = sub
                  temp = 1
                  sub = s[i]
            else:#否则长度+1,此时计算并保留最长的字串
                temp = temp+1
                sub = sub+s[i]
                if temp > longest:
                    longest = temp
                    longest_sub = sub
            i=i+1
        return longest, longest_sub

if __name__ == '__main__':
    s = 'abcbbac'
    length,substring = Solution().longestSubstring(s)
    print(length,substring)
