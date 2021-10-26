from PQue import PriorityQue

print('test internal operations')
print('test position dict operations')

pq = PriorityQue([])

pq.insertPosition(3, 2)
pq.insertPosition(7,4)
pq.insertPosition(7,5)
print(pq.posDict)
print('get positions')
print('getting position 3:', pq.getPosition(3))
print('getting position 3:', pq.getPosition(7))
print('removing items')
print('remove 7:4', pq.removePosition(7,4))
print(pq.posDict)
print('remove 7:8', pq.removePosition(7,8))
print(pq.posDict)
print('remove 1:8', pq.removePosition(1,8))
print(pq.posDict)
print('remove 3:2', pq.removePosition(3,2))
print(pq.posDict)
print('++++++++++++++++++++++++++++++++++++++++')
print('test parents and node values')

pq = PriorityQue([1,3,6,8,9,11,12])

print(pq)
pos = pq.getPosition(3)
print('3: parent = ', pq.getParentValue(pos), 'children = ', \
pq.getLeftChildValue(pos), pq.getRightChildValue(pos))
pos = pq.getPosition(6)
print('6: parent = ', pq.getParentValue(pos), 'children = ', \
pq.getLeftChildValue(pos), pq.getRightChildValue(pos))
pos = pq.getPosition(1)
print('1: parent = ', pq.getParentValue(pos), 'children = ', \
pq.getLeftChildValue(pos), pq.getRightChildValue(pos))
pos = pq.getPosition(8)
print('8: parent = ', pq.getParentValue(pos), 'children = ', \
pq.getLeftChildValue(pos), pq.getRightChildValue(pos))

print('++++++++++++++++++++++++++++++++')
print('test x >= y')
print('None >= 1', pq.greaterThanEq(None,1))
print('1 >= None', pq.greaterThanEq(1,None))
print('None >= None', pq.greaterThanEq(None,None))
print('1 >= 2', pq.greaterThanEq(1,2))
print('2 >= 1', pq.greaterThanEq(1,2))