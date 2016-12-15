'''
Created on Nov 4, 2012

@author: ramesh
'''

class Heap(object):
    '''
    classdocs
    '''

    def __init__(self,l=[]):
        '''
        Constructor
        '''
        self.l=l
        
    def indices(self,n):
        return 2*n+1,2*n+2
    
    def restoreheap(self,parent,n):
        left, right=self.indices(parent)
        if (right<n):
            if (self.l[parent][1]> min(self.l[left][1],self.l[right][1])):
                if (self.l[left][1]<self.l[right][1]):
                    self.l[parent],self.l[left]=self.l[left],self.l[parent]
                    self.restoreheap(left,n)
                else:
                    self.l[parent],self.l[right]=self.l[right],self.l[parent]
                    self.restoreheap(right,n)
        elif (left<n):
            if(self.l[parent][1]>self.l[left][1]):
                self.l[parent],self.l[left]=self.l[left],self.l[parent]
        return self.l
            
            
    def makeHeap(self):
        n=len(self.l)
        for i in range (0,n):
            left ,right=self.indices(n-1-i)
            if (right<n):
                if (self.l[n-i-1][1]> min(self.l[left][1],self.l[right][1])):
                    if (self.l[left][1]<self.l[right][1]):
                        self.l[n-1-i],self.l[left]=self.l[left],self.l[n-1-i]
                        self.restoreheap(left,n)
                    else:
                        self.l[n-1-i],self.l[right]=self.l[right],self.l[n-1-i]
                        self.restoreheap(right,n)
            elif (left<n):
                if(self.l[n-1-i][1]>self.l[left][1]):
                    self.l[n-1-i],self.l[left]=self.l[left],self.l[n-1-i]
        
        return self.l
    
    def add(self,t):
        self.l.insert(0,t)
    
    def rm(self):
        self.l.pop(0)
        
if __name__=='__main__':
    
    l=[('a',2),('b',3),('c',4),('d',5),('e',6),('f',7),('z',8),('x',9),('k',100),('g',20)]
    h=Heap(l)
    print h.makeHeap()
    h.add(('w',3))
    print h.l
    h.rm()
    print h.l
    