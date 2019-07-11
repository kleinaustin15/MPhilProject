#import necessary packages
from sklearn.linear_model import LinearRegression
import numpy as np
import statistics as stat
import csv
import matplotlib.pyplot as plt

#read in file containing only repeated cell lines
repeat_file = open('cosmic_repeats.csv','r')
data = csv.reader(repeat_file,skipinitialspace=True)
x=[]
y=[]
i=0
for line in data:
	if i==0:
		cosmic_id = line[0]
		i+=1
	else:	
		x.append(line[0])
		y.append(line[1])

for l in range(len(x)):
	x[l] = float(x[l])

for n in range(len(y)):
	y[n] = float(y[n])

#create x an y lists
x=np.array(x)
y=np.array(y)


xp = np.linspace(-3,4,50)
yp= xp

X =x[:,np.newaxis]

#calculate linear regression model
model=LinearRegression(fit_intercept=False)
model.fit(X,y)

#plot linear regression
fig,ax=plt.subplots(figsize=(10,10))
ax.scatter(x,y)
plt.xlim(-3,4)
plt.ylim(-3,4)
ax.plot(x,model.coef_*x+model.intercept_,':r')
ax.plot(xp,yp,'.k')
plt.grid(True)
coef = str(model.coef_)
plt.title(cosmic_id+coef)
plt.savefig(cosmic_id+'.png')
plt.show()