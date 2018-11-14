import numpy as np
#np开辟数组np(i,j)下标从0开始，长度为i,j
#构造一个weight,value矩阵，w表示背包重量，v表示当前最大价值
#w从0到weight遍历，求解当w=weight时的v即可
class Solution(object):#N*W空间复杂度
    def dp_backage(self,v,w,totalw):
        result = np.zeros((len(v),totalw+1),dtype=np.int32)
        for i in range(1,len(w)):
            for j in range(0,totalw+1,w[1]):
                if w[i]>j:
                    result[i,j]=result[i-1,j]
                else:
                    result[i,j]=max(result[i-1,j-w[i]]+v[i],result[i-1,j])
        return result[-1,-1]

class Solution2(object):#W空间复杂度
    def dp_backage(self,v,w,totalw):
        result = np.zeros((totalw+1),dtype=np.int32)
        for i in range(1,len(w)):
            for j in range(totalw,0,-w[1]):
                if w[i]<=j:
                    result[j]=max(result[j-w[i]]+v[i],result[j])
        return result[-1]

if __name__ == '__main__':
    v = [0,60,100,120]#价格
    w = [0,1,2,3]#重量
    weight = 5
    print(Solution2().dp_backage(v,w,weight))

