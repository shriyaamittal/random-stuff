import numpy as np
import matplotlib.pylab as plt

import matplotlib

# Study 1

matrix=[[-10,-10,-10,-10,-10,-10],
	[0.86,-10,-10,-10,-10,-10],
	[0.385,0.310,-10,-10,-10,-10],
	[.404,.376,0.914,-10,-10,-10],
	[0.543,0.515,0.799,0.850,-10,-10],
	[0.522,0.511,0.85,0.904,0.903,-10]]

m_rev=[]
for i in range(len(matrix)):
	temp=[]
 	for j in reversed(matrix[i]):
 		temp.append(j)
 	m_rev.append(temp)

data=np.array(m_rev)

plt.pcolor(data.T, cmap=matplotlib.cm.Blues,vmin=0,vmax=1)
plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.savefig('study1_individual.png',dpi=500)

# Study 2
"""
matrix=[[-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10],
	[0.678,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10],
	[0.715,.737,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10],
	[.727,0.675,.733,-10,-10,-10,-10,-10,-10,-10,-10,-10],
	[.295,.123,.210,.231,-10,-10,-10,-10,-10,-10,-10,-10],
	[.207,.054,.099,.144,.819,-10,-10,-10,-10,-10,-10,-10],
	[.155,.069,.097,.093,.806,.890,-10,-10,-10,-10,-10,-10],
	[.244,.073,.132,.132,.825,0.867,.912,-10,-10,-10,-10,-10],
	[0.454,.278,.39,.361,.742,.597,.64,.677,-10,-10,-10,-10],
	[.405,.319,.404,.4,.727,.612,.692,.673,.786,-10,-10,-10],
	[.459,.315,.387,.364,.729,.576,.624,.645,.808,.803,-10,-10],
	[.338,.135,.192,.241,.799,.737,.744,.753,.709,.702,.704,-10]]

m_rev=[]
for i in range(len(matrix)):
	temp=[]
 	for j in reversed(matrix[i]):
 		temp.append(j)
 	m_rev.append(temp)

data=np.array(m_rev)

plt.pcolor(data.T, cmap=matplotlib.cm.Blues,vmin=0,vmax=1)
plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.savefig('study2_individual.png',dpi=500)
"""
