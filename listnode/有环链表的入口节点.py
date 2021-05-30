"给一条有环链表 说明其入口节点"
"给一条有环链表 说明其入口节点"
"""
假如链表有环
且快慢指针则一定会在环上某点相遇  记相遇点到环口的距离为 b 
慢指针走过的环外长度a 换上长度b  环被分割为两部分 m+n
慢指针：a+b
快指针： 2*（a+b）
且快指针在环上已经走过K圈
2*（a+b） =a+（m+n）*k +b
a+b = (m+n)*K
b== n
a = (k-1)*(m+n)+m
那么说明 慢指针在相遇节点从头走起的时间  与 快节点 以同样的速度走到环扣的时间一致
"""

class Solution:
    def detectCycle(self , head ):
        # write code here
        if not head or not head.next:
            return None
        a,b = head,head
        meetNode = None
        try:
            while b.next and b.next.next:
                a = a.next
                b = b.next.next
                if a == b  :
                    meetNode = a
                    a = head
                    while meetNode != a:
                        a = a.next
                        meetNode = meetNode.next
                    return meetNode
        except:
            return None
          
          


