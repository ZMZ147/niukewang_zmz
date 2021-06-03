## https://leetcode-cn.com/problems/sliding-window-maximum/


给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。



超时解法

```
class Solution:

    def maxSlidingWindow(self, nums , k) :

        left,right = 0,0
        if len(nums) < k:
            return
        reduce_list,res = sorted(nums[:k],reverse=True) ,[]
        reduce_dict = {value:key for key,value in enumerate(reduce_list)}
        for ele in range(k,len(nums)):
            print(ele,nums[ele],'ele')
            res.append(reduce_list[0])
            current = nums[ele]
            #z找到左边即将移除的元素
            #因为存在重复元素  所以不进行删除
            index = reduce_dict[nums[left]]
            try:
                if reduce_list[index] == reduce_list[index-1]:
                    is_reperate = True
                else:
                    is_reperate = False
            except:
                is_reperate = False
            print(reduce_dict,reduce_list,nums[left],index,is_reperate)
            if not is_reperate:
                del reduce_dict[nums[left]]
            reduce_list.pop(index)
            count = 0
            while count < k-1:
                if current > reduce_list[count]:
                    break
                count += 1
            reduce_list.insert(count,current)
            #这里并没有维护索引的更新
            reduce_dict[current] = count
            #reduce_dict = {value:key for key,value in enumerate(reducce_list)}   这种写法会导致超时
            left += 1
        print(reduce_list,'reduce_list')
        res.append(reduce_list[0])
        return res
```

思路  维护一个长度为K个数组的降序列表和字典

每一次循环找到 新元素插入的位置，更新列表 维护一个新的字典（如果不维护新的字典，那么应该弹出元素的索引没有更新，所以不会被弹出）





leetcoed上的题解

# 只维护一个索引队列--------->这与超时的解法思维的出发点不一样  超时解法重点是维护数组的实际元素，保证每次直接弹出的是最大元素，利用字典来维护栈

当遍历元素大于栈内元素时，更新栈，保证当前栈内存放的是最新最大的元素

！ 当栈内元素是数组中的最大元素时，且最大元素对应的索引不在滑动窗口内---要条件判断及时更新

！当 滑动窗口长度满足时，取出栈顶元素，并更新左右边界

```
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left,right = 0,0
        if len(nums) < k:
            return
        #需要判断队首的索引是否在边界内，队内的索引
        reduce_list,res = [],[]
        for ele in range(len(nums)):
                while reduce_list:
                    if nums[ele] > nums[reduce_list[-1]]:
                        reduce_list.pop()
                        continue
                    break
                reduce_list.append(ele)
                if reduce_list[0]<left:
                    reduce_list.pop(0)
                if right - left +1 == k:
                    res.append(nums[reduce_list[0]])
                    left += 1
                right += 1
        return res
```

但是这样的时间复杂度还是比较高

执行用时：1068 ms, 在所有 Python3 提交中击败了7.66%的用户

内存消耗：27.1 MB, 在所有 Python3 提交中击败了45.07%的用户



# 如何能在线性时间满足要求？

！始终要和索引队列对应的元素进行比较