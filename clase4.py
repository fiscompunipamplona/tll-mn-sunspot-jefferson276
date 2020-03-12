from pylab import plot,show
x=[]
y=[]
for i in range(10):
    y.append(i*i)
    x.append(2*i)
plot(x,y)
show()

from numpy import linspace,xlabel, sin
x=linspace(0,10,100)
y=sin
plot(x,y)
xlabel("Radians")
show()
xlabel("Radians")a=open("test.data","w")
for i in range(len(x)):
    a.write("%.2f %.2f\n"%(x[i],y[i]))
a.close()

from numpy import loadtxt
a=loadtxt("test.dat",float)
print(a[:,0])
print(a[:,1])   
plot((a[:,0]),(a[:,1]))


