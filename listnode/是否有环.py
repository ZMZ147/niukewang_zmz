"空间复杂度为O（1）的要求下 判断链表是否有环，"
"解法 ：使用双指针"
"不加入容错机制 总是会出现NoneType has no attribute next  但是我在这里已经对快指针的每一步都进行了核验 不应该产生这种问题"
"如果出错 说明没有环”



class Solution:
    def hasCycle(self , head):
        # write code here
        if head == None or head.next == None:
            return False
        slow,quick = head,head
        try:
            while quick.next != None and quick != None:
                slow = slow.next
                quick = quick.next.next
                if slow is quick:
                    return True
            return False            
        except:
            return False
