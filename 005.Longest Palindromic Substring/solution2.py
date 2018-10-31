class Solution(object):
    def isPalinSub(self,s,left,right):#由外向里的判断方法复杂度高，由里向外判别复杂度较低
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1#这里返回长度要减1是因为跳出循环左右各外扩了1，由R-L+1-2得到

    def longestPalinSub(self,s):
        start=0
        end=0
        for i in range(len(s)):
            len1=Solution().isPalinSub(s,i,i)#奇数回文判断
            len2=Solution().isPalinSub(s,i,i+1)#偶数回文判断
            length=max(len1,len2)
            if(length>end-start):#已知回文的长度，求出该回文的首尾位置,i为当前元素位置
                start=int(i-(length-1)/2)
                end=int(i+length/2)

        return s[start:end+1]

if __name__=='__main__':
    s = 'abbabbua'
    sub = Solution().longestPalinSub(s)
    print(sub)