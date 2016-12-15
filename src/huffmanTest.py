'''
Created on Oct 31, 2012

@author: gsrinivasaraghavan
'''
import unittest
import filecmp
import os
from testgenDecorator import for_examples
from heap import Heap
from stack import Stack
from utils import areListsEqual
from huffman import Huffman

class TestHeap(unittest.TestCase):

    def priorityFloat2Int(self, a):
        return int(a)

    @for_examples(("text1", 370), ("text2", 5900))
    def testMaxElements(self, originalFile, compressedSize):
        '''
        Test max elements of the heap
        '''
        huff = Huffman()
        compressedfile = huff.compress(originalFile)
        self.assertLessEqual(os.path.getsize(compressedfile), compressedSize)
        recoveredFile = huff.uncompress(compressedfile)
        self.assertEqual(os.path.getsize(originalFile), os.path.getsize(recoveredFile))
        self.assertEqual(True, filecmp.cmp(originalFile, recoveredFile))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()