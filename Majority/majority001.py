#Moore voting摩尔投票法
#适用于一定存在众数的情况
#这里众数的定义为出现次数大于n/2的数
def MooreVoting(array):
    major = array[0]
    count=1
    for i in range(1,len(array)):
        if array[i]==major:
            count+=1
        else:
            count-=1
            if count<=0:
                major = array[i]
                count=1

    return major

if __name__=='__main__':
    a=[1,23,5,5,5,6]
    print(MooreVoting(a))
