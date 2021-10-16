from binaryTree import BinaryTree

tr = BinaryTree([5,9,7,4,6,1,2, 8])
print(tr)
print('find 2', tr.search(2))
print('find 22', tr.search(22))
#tr.delete(2)
tr.delete(1)
print(tr)
print