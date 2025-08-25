a = np.array([[1,2,3],[4,5,6]])
a.shape   # (2, 3)

np.ndim(a)  # 2
np.size(a)
np.size(a)  # 6
np.reshape(a, newshape)
a = np.arange(6)
np.reshape(a, (2, 3))  
# [[0 1 2]
#  [3 4 5]]
np.transpose(a)
np.concatenate((a1, a2), axis=0)




a = np.array([1,2,3])
b = np.array([4,5,6])

np.add(a,b)       # [5 7 9]
np.subtract(a,b)  # [-3 -3 -3]
np.multiply(a,b)  # [4 10 18]
np.divide(a,b)    # [0.25 0.4  0.5 ]



np.power(a, 2)  # [1 4 9]


np.exp([1,2])   # [ 2.71828183  7.3890561 ]
np.log([1, np.e]) # [0. 1.]
np.sqrt([1,4,9]) # [1. 2. 3.]



a = np.array([1,2,3,4,5])
np.mean(a)   # 3.0
np.median(a) # 3.0
np.std(a)    # 1.414213562


np.sum(a)   # 15
np.min(a)   # 1
np.max(a)   # 5


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.dot(a,b)  
# [[19 22]
#  [43 50]]


np.linalg.inv(a)


np.linalg.det(a)


np.random.rand(2,3)
# Random 2x3 array in [0,1)


np.random.randint(1, 10, size=(2,2))
# Random integers between 1 and 9


np.random.choice([10,20,30], size=2)
# Random sample from given array

