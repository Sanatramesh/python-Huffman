'''
Created on Nov 4, 2012

@author: ramesh
'''
from heap import Heap
from stack import Stack


class Huffman(object):
  
    def compress(self,File,CompFile=''):
        cHash={}
        heap=[]
        s=[]
        fp=open(File,"r")
        data=fp.read()
        fp.close()
        #print data
        words=data
        for word in words:
            for ch in word:
                if ch in cHash:
                    cHash[ch]+=1
                else:
                    cHash[ch]=1
        for key in cHash:
            heap.append((key,cHash[key]))
        H=Heap(heap)
        H.makeHeap()
        S=Stack()
        while len(H.l)>2:
            t=S.add(H().l[0], H.l[1])
            H.rm()
            H.rm()
            H.l.append(t)
            H.makeHeap()
            
        t=S.add(H.l[1],H.l[0])
        S.s.append((t[0],'',''))
        S.s=S.s[::-1]
        
        while(S.s!=[]):
            if S.s[0][1]!='':
                cHash[S.s[0][0]]=cHash[S.s[0][1]]+S.s[0][2]
            else:
                cHash[S.s[0][0]]=S.s[0][2]
            
            S.s.pop(0)

        k=[]
        for key in cHash:
            if len(key)>1 and key != '\n':
                k.append(key)
        
        for key in k:
            del cHash[key]
    
        st=""
        
        for ch in data:
            st+=cHash[ch]
        
        out=""

        pad=len(st)%8
        temp=''
        while(len(st)>7):
            temp=st[:8]
            ch=int(temp,2)
            st=st[8:]
            out+=chr(ch)
        if (pad!=0):
            st+='0'*(8-pad)
            out+=chr(int(st,2))
            
        if (CompFile==''):
            CompFile=File+'.huff'
        fp=open(CompFile,"w")
        for key in cHash:
            fp.write(key+' ')
            fp.write(cHash[key]+' ')
        fp.write('###')
        
        fp.write(str(8-pad)+'###')
        #print out
        fp.write(out)
        fp.close()
        #print cHash
        return CompFile
        
        
        
    def uncompress(self,compFile,recFile=''):
        if(recFile==''):
            recFile=compFile[:-5:]+'.txt'
        fp=open(compFile,"r")
        data=fp.read()
        data=data.split('###')
        l=data[0].split(' ')
        i=0
        while(1):
            i=l.index('')
            l.pop(i)
            if '' not in l:
                break
            
        cHash={}
        while l!=[]:
            if len(l[0])>1:
                cHash[l[0]]=' '                
                l.pop(0)
            else:
                cHash[l[1]]=l[0]
                l.pop(0)
                l.pop(0)
        st=""
        pad=int(data[1])
        
        for ch in data[2]:
            ch=bin(ord(ch))[2:]
            st+='0'*(8-len(ch))+ch
        
        st=st[:-pad]
        
        ch=''
        out=''
        fp=open(recFile,"w")
        for i in range(0,len(st)):
            ch+=st[i]
            if ch in cHash.keys():
                fp.write(cHash[ch])
                ch=''
                        
        fp.close()
        return recFile
    
if __name__=='__main__':
    Comp=Huffman()
    print Comp.compress("text2")
    print Comp.uncompress("text2.huff")