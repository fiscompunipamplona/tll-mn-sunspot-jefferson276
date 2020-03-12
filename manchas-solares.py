from pylab import plot, show, xlim, ylim, xlabel, ylabel
from numpy import linspace, loadtxt

a=loadtxt("sunspots.txt",float)
xlabel("mes")
ylabel("numero de manchas")
plot(a[:,0],a[:,1])
show()

plot(a[:,0],a[:,1])
xlim(0,1000)
show()

r=5

for in i range(0,100):


