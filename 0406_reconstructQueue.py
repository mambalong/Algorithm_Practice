'''
406. Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''

'''
先举一个简单的例子，(7, 0), (7, 1) 就是 h 都相同，但是 k 不同的，我们只需要对 k 进行排序就行了。
那么这个时候加一个 (6, 1) 呢，我们只需要把它加入到对应的位置 k 处就可以了，即插入到位置 1 处。
这样对 (6, 1) 来说是符合的，对 (7, 1) 来说情况也是没变的，应为 6 要矮一点，(7, 1) 压根看不到它，
就是说，向一个已经排好序的，高度一样的数组中插入一个高度小的，不会改变原本的相对排序，数组依然是成立的。

这样我们就是需要把相同高度的进行排序，在向高度高的排序中依次插入高度较低的就好了
注意，排序的时候，高度是降序，k 是升序

'''

class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        ans = []

        for h, k in people:
            ans.insert(k, (h, k))
        
        return ans

    
