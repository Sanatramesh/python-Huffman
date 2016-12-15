'''
Created on Oct 26, 2012

@author: ramesh
'''

def Stack(hash):
    #wh
        
    pass

def Count(filename):
    h={}
    fp=open(filename,'r')
    words=fp.read().lower().split()
    fp.close()
    for word in words:
        for ch in word:
            if ch in h:
                h[ch]+=1
            else:
                h[ch]=1
    return h 

def Compression(filename):
    h=Count(filename)
    stack=Stack(h)
    
def Decompression(filename):
    pass



if __name__ == '__main__':
    ComFile=Compression(file.txt)
    DecomFile=Decompression(ComFile)