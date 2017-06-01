import numpy as np
import matplotlib.pylab as plt

import matplotlib

matrix=[[ 0.   ,  0.168,  0.424,  0.689,  0.585],
       [ 0.39 ,  0.   ,  0.798, -0.069,  0.422],
       [ 0.555,  0.893,  0.   ,  0.163,  0.534],
       [ 0.778,  0.098,  0.304,  0.   ,  0.279],
       [ 0.505,  0.632,  0.624,  0.182,  0.   ]]

m_rev=[]
for i in range(len(matrix)):
	temp=[]
 	for j in reversed(matrix[i]):
 		temp.append(j)
 	m_rev.append(temp)

data=np.array(m_rev)

plt.pcolor(data.T, cmap=matplotlib.cm.Blues_r)
plt.colorbar()
plt.xticks([])
plt.yticks([])




matrix=[[ 0.   ,  0.39 ,  0.555,  0.778,  0.505],
       [ 0.168,  0.   ,  0.893,  0.098,  0.632],
       [ 0.424,  0.798,  0.   ,  0.304,  0.624],
       [ 0.689, -0.069,  0.163,  0.   ,  0.182],
       [ 0.585,  0.422,  0.534,  0.279,  0.   ]]
