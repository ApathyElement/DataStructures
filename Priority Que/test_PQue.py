from PQue import PriorityQue

pq = PriorityQue([11,7,3,2,13,2,2,7])
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('+++++++++++++++++++++++++++++++++++')
pq = PriorityQue([9,6,8,7,2,4,5])
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('poll', pq.poll())
print(pq)
print('insert 11:', pq.insert(11))
print('insert 7:', pq.insert(7))
print(pq)
print('+++++++++++++++++++++++++++++++++')
print('testing removal')
pq = PriorityQue([11,7,3,2,13,2,2,7])
print('removing 3:', pq.remove(3))
print(pq)
print('peeking:', pq.peek())
print('removing 2:', pq.remove(2))
print(pq)
print('peeking:', pq.peek())
print('removing 2:', pq.remove(2))
print(pq)
print('peeking:', pq.peek())
print('removing 2:', pq.remove(2))
print(pq)
print('peeking:', pq.peek())
print('removing 34:', pq.remove(2))
print(pq)
print('peeking:', pq.peek())