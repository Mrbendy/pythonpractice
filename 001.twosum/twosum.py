class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for index, num in enumerate(nums):#enumerate函数返回序号和值
            if num in dic: #key和value都可以作为是否在字典的依据
                return [dic[num], index]
            dic[target - num] = index



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    #assert (Solution().twoSum(nums, target) == [0, 1])
    x=Solution().twoSum(nums,target)
    print(x)
    nums = [3, 2, 4]
    target = 6
    #assert (Solution().twoSum(nums, target) == [1, 2])
