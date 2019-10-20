#! /usr/bin/python

import sys

class PQueue:

  def OrdinaryComparison(a,b):
    if a < b: return -1
    if a == b: return 0
    return 1

  def __init__(self, comparator = OrdinaryComparison):
    self.cmpfunc = comparator
    self.queue = []

  def push(self, data):
    for x in range(len(self.queue)):
      if self.cmpfunc(self.queue[x],data) == -1:
        self.queue.insert(x,data)
        return
    self.queue.append(data)

  def pop(self):
    if len(self.queue) == 0: return None
    return self.queue.pop()

  def toList(self):
    l = []
    while (len(self.queue) > 0):
      l.append(self.queue.pop())
    return l

def newcmp(a,b):
    if len(a) < len(b): return -1
    if len(a) > len(b): return 1
    newA = a.lower()
    newB = b.lower()
    for i in range(len(a)):
        if newA[i] < newB[i]: return -1
        if newA[i] > newB[i]: return 1
    return 0

def read(file):
      fp = open(file,'r')
      s = fp.read()
      fp.close()
      if '\r\n' in s: lines = s.split('\r\n')
      else: lines = s.split('\n')
      return lines


def getCommands():
    pqueue = PQueue(newcmp)
    alist = sys.argv
    commands = read(alist[1])
    for x in commands:
        if x[:2] == "pu": pqueue.push(x.split(' ')[1])
        elif x[:1] == "p": pqueue.pop()
        else: return pqueue.toList()

def write(file):
    f = open(file, 'w')
    x = ','.join(getCommands())
    f.write(x)
    f.close

write(sys.argv[2])
