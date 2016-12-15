'''
Created on Nov 23, 2012

@author: sumith
'''

class Stack(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.stack=[]
    
    def push(self,character,frequency,x):
        self.stack.append((self.character,self.frequency,self.x))
        self.heapify()

    def delete(self):
        if(len(self.stack)>1):
            t = self.stack[0]
            self.stack.remove(self.stack[0])
            self.heapify(self.stack)
            return t
        else:
            self.heapify(self.stack)
            return self.stack[0]

    
if __name__ == '__main__':
    pass