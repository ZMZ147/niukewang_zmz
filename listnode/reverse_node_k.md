给定一个链表，每K个节点翻转一次

将给出的链表中的节点每\ k *k* 个一组翻转，返回翻转后的链表
如果链表中的节点数不是\ k *k* 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。
要求空间复杂度 \ O(1) *O*(1)

例如：

给定的链表是1\to2\to3\to4\to51→2→3→4→5

对于 \ k = 2 *k*=2, 你应该返回 2\to 1\to 4\to 3\to 5  2→1→4→3→5

对于 \ k = 3 *k*=3, 你应该返回 3\to2 \to1 \to 4\to 5   3→2→1→4→5





```
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head , k ):
        # write code here
        #对于当前位置进行记录
        #给一个sstart节点 和 一个end节点t 来保存信息
        start ,end= head, None
        pointer ,pre = head, None
        counter = 0
        while pointer:
            counter += 1
            #翻转的临界节点 end
            end = pointer
            #临界节点的下一个节点，下一次翻转的起始节点
            pointer = pointer.next
            if counter == k:
            	#本次翻转过程的起始节点和前置节点
                current_tmp,current_pre = start,pre
                #K个节点的翻转
                while counter > 0:
                    tmp = start.next
                    start.next = pre
                    pre = start
                    start = tmp
                    counter -= 1
                #第一次翻转的时候 应该重新确定头结点
                if not current_pre:
                    head = pre
                else:
                    #处于链表中间的K节点  应该对于start,end节点的next域 都要做修改
                    current_pre.next = end
                #每一次翻转后，头结点都会变为尾结点，并且 需要对下一次的pre节点做更新
				current_tmp.next,pre = pointer, current_tmp
        return head

```

题意破解：每K个节点就进行翻转，所以 代码过程必然会有一次 K个节点的内部翻转

而每一次的翻转 都会设计    pre-->start------>end -->end.next

每一次翻转会设计到四个变量   

所以 引申出来了 记录这四个变量的 current_tmp,current_pre

题意做了一个什么动作过程，需要哪些变量
