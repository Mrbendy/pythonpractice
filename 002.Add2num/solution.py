class listnode(object):
    def __init__(self,x,p=None):
        self.val = x
        self.next = p

    def get_value(self):
        return self.val

class linklist(object):
    def __init__(self):
        self.head = None

    def get_len(self):
        len = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            len = len+1
        return len

    def is_empty(self):
        return self.get_len() == 0

    def plist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def init(self,data):
        self.head = listnode(data[0])
        cur = self.head
        for i in data[1:]:
            cur.next = listnode(i)
            cur = cur.next
        cur.next=None

class Solution(object):
    def convert(self,l):#将链表转化成数字
        cur = l
        p = 1
        result = 0
        while cur != None :
            result = p * cur.val + result
            p = p * 10
            cur = cur.next

        return result

    def add2num(self,l1,l2):
        a = Solution().convert(l1)
        b = Solution().convert(l2)
        c = a+b
        return c


if __name__ == "__main__":
    #输入两个链表
    l1=listnode(2)
    l1.next=listnode(4)
    l1.next.next=listnode(3)
    l2 = listnode(5)
    l2.next = listnode(6)
    l2.next.next = listnode(4)
    #计算得到结果并输出
    result = Solution().add2num(l1,l2)
    print(result)
