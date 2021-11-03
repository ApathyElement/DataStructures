from UnionFind import UnionFind

X = ['x','y','a','b','4','7','d']
uf = UnionFind(X)
print(uf)
print('find root: b ', uf.find('b'))
print('find root: d ', uf.find('d'))
print('find root: zz', uf.find('zz'))

print('Unify x and b', uf.unify('x','b'))
print('Unify b and d', uf.unify('b','d'))
print('Unify a and y', uf.unify('a','y'))

print(uf)
print('find root: b ', uf.find('b'))
print('find root: d ', uf.find('d'))
print('find root: x ', uf.find('x'))
print('find root: a ', uf.find('a'))
print('find root: y ', uf.find('y'))
print('find root: zz', uf.find('zz'))

print('components:', uf.components)
