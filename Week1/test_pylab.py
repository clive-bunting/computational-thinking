import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4], linewidth=30)

pylab.show()

pylab.figure(2)
pylab.plot([1,4,2,3], [5,6,7,8], 'ro')
pylab.title('My title')
pylab.xlabel('x lab', fontsize=6)
pylab.ylabel('y lab')

pylab.show()

pylab.figure(1)
pylab.plot([5,6,10,3])

pylab.savefig('test-fig')

pylab.show()
