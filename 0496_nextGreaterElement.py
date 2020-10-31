'''
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 
中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

'''

'''
思路：
想象每个元素都是一个人，元素的值就是人的高度，向数组的尾部看去，看到的第一个比自己高的人，就是答案。
单调栈，倒序遍历数组，元素依次入栈，首先要判断栈顶的元素是不是比当前元素大，小于或等于的
都可以出栈，反正前面的人也看不到。
'''

def nextGreaterElement(nums1, nums2):

    dic = dict()
    for i, v in enumerate(nums1):
        dic[v] = i
    
    stack = []
    for num in reversed(nums2):
        while stack and num >= stack[-1]:
            stack.pop()
        print(stack)
        if num in nums1:
            nums1[dic[num]] = stack[-1] if stack else -1
        stack.append(num)
    return nums1

print(nextGreaterElement([4,1,2], [1,3,4,2]))
