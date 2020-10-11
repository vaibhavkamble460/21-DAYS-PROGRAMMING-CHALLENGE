import matplotlib.pyplot as plt

depts=['Civil','Mech','Comp','It']

s=[5,4,10,8]

c=['y','r','g','b']

plt.pie(s,labels=depts,colors=c,startangle=90,shadow=True, explode=(0.05,0.05,0.05,0.05),radius=1.2,autopct='%1.1f%%')

plt.legend(loc='lower right')
plt.show()