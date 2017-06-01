import numpy as np
import matplotlib.pylab as plt

import matplotlib

# Study 1
"""
matrix=[[ -10   ,  -10,  -10,  -10,  -10],
       [ 0.39 ,  -10.   ,  -10, -10,  -10],
       [ 0.555,  0.893,  -10.   ,  -10,  -10],
       [ 0.778,  0.098,  0.304,  -10.   ,  -10],
       [ 0.505,  0.632,  0.624,  0.182,  -10.   ]]

m_rev=[]
for i in range(len(matrix)):
	temp=[]
 	for j in reversed(matrix[i]):
 		temp.append(j)
 	m_rev.append(temp)

data=np.array(m_rev)

plt.pcolor(data.T, cmap=matplotlib.cm.Blues,vmin=-0.1,vmax=0.9)
plt.colorbar()
plt.xticks([])
plt.yticks([])

plt.savefig('study1_composite.png',dpi=500)
"""

# Study 2

matrix=[[ -10.   ,  -10 ,  -10,  -10,  -10],
       [ 0.168,  -10.   ,  -10,  -10,  -10],
       [ 0.424,  0.798,  -10.   ,  -10,  -10],
       [ 0.689, -0.069,  0.163,  -10.   ,  -10],
       [ 0.585,  0.422,  0.534,  0.279,  -10.   ]]

m_rev=[]
for i in range(len(matrix)):
	temp=[]
 	for j in reversed(matrix[i]):
 		temp.append(j)
 	m_rev.append(temp)

data=np.array(m_rev)

plt.pcolor(data.T, cmap=matplotlib.cm.Blues,vmin=-0.1,vmax=0.9)
plt.colorbar()
plt.xticks([])
plt.yticks([])

plt.savefig('study2_composite.png',dpi=500)

#matrix=[[ 0.   ,  0.168,  0.424,  0.689,  0.585],
#       [ 0.39 ,  0.   ,  0.798, -0.069,  0.422],
#       [ 0.555,  0.893,  0.   ,  0.163,  0.534],
#       [ 0.778,  0.098,  0.304,  0.   ,  0.279],
#       [ 0.505,  0.632,  0.624,  0.182,  0.   ]]

