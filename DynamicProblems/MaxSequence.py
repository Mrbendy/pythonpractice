import numpy as np
#求解最长公共子序列，构造Max(i,j),i,j表示s1,s2左边i,j个字符组成的子串
#求解Max(len(s1),len(s2))即可

def MaxSeq(s1,s2):#这就是动态规划,构造矩阵从m(0,0)求解到m(n,m)
    result = np.zeros((len(s1),len(s2)),dtype=np.int32)
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i]==s2[j]:
                result[i,j]=result[i-1,j-1]+1
            else:
                result[i,j]=max(result[i-1,j],result[i,j-1])
    return result[-1,-1]

def MaxSeq2(s1,s2,l1,l2):#递归求解，但是重复子问题太多，可以加备忘录
    if l1==0 and l2==0:
        return 0
    elif l1==0:
        return 0
    elif l2==0:
        return 0

    if s1[l1-1]==s2[l2-1]:
        return MaxSeq2(s1[:l1 - 1], s2[:l2 - 1], l1 - 1, l2 - 1) + 1
    else:
        return max(MaxSeq2(s1[:l1-1],s2,l1-1,l2),MaxSeq2(s1,s2[:l2-1],l1,l2-1))

if __name__=='__main__':
    #为了防止越界需要#
    s1='#programming'
    s2='#contest'
    print(MaxSeq(s1,s2))
    #print(MaxSeq2(s1,s2,len(s1),len(s2)))
