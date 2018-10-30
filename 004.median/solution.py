class Solution(object):#合并的复杂度为O(m+n),限制为log(m+n)考虑二分查找
    def findMedian(self,n1,n2):
        n = len(n1)
        m = len(n2)
        r = []
        i = 0
        j=0
        while i < n and j < m:
            if n1[i] < n2[j]:
                r.append(n1[i])
                i=i+1
            else:
                r.append(n2[j])
                j=j+1

        if i==n:
            while j < m:
                r.append(n2[j])
                j=j+1
        else:
            while i < n:
                r.append(n1[i])
                i=i+1

        if (m+n)%2==0:
            pos = int((m+n)/2)
            return r[pos]
        else:
            pos = int((m + n) / 2)
            return (r[pos]+r[pos+1])/2

if __name__=='__main__':
    n1=[1,2]
    n2=[2,3]
    r = Solution().findMedian(n1,n2)
    print(r)