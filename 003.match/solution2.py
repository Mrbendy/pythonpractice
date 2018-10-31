class Solution(object):
    def longestSubstring(self,s):
        rlen = 0
        start = 0
        sub={}#遍历时需要一个dict来记录字符和位置，以便于更新start
        for pos,val in enumerate(s):#发现重复字符需要改变遍历位置
            # 由于sub中记录了字符出现的位置，
            # 当某字符在sub里但是其出现位置在start之前，说明该字符并不在当前遍历串中重复
            if val in sub and sub[val]>=start:
                rlen = max(rlen,pos-start)
                start=sub[val]+1#改变为上次这个字符出现的位置+1

            sub[val]=pos #在遍历中不断更新字符上一次出现的位置

        return max(rlen,len(s)-start)

if __name__=='__main__':
    s='aijiaf'
    longest = Solution().longestSubstring(s)
    print(longest)