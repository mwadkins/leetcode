# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class BinHeap:
    def __init__(self):
        self._heap=[]

    def percUp(self):
        pos=len(self._heap)-1
        while (pos):
            if (self._heap[pos]>self._heap[pos/2]):
                tmp=self._heap[pos/2]
                self._heap[pos/2]=self._heap[pos]
                self._heap[pos]=tmp
            pos = pos / 2
        
    def insert (self,val):
        self._heap.append(val)
        self.percUp()

    def printh(self):
        count=1
        done=False
        pos=0
        while (done==False):
            indent = len(self._heap)-(count-pos)/2
            for i in range (indent):
                print " ",
            for i in range (pos,count):
                if (i<len(self._heap)):
                    print self._heap[i]," ",
                else:
                    done=True
            print ""
            pos=count
            count=count*2
            
                
        
        
class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap=BinHeap()
        size=0
        for i in range (len(lists)):
                for j in range (len(lists[i])):
                    heap.insert(lists[i][j])
                    size+=1

        print heap._heap
        heap.printh()
        
sol=Solution()
l=[[0,9,5,6,2,3],[0,9,2,6,5,3],[0,2,3,5,6,9]]
sol.mergeKLists(l)
    
        
