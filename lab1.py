import matplotlib.pyplot as plot
x=[10,20,30,40,50,60,70]
y=[90,110,130,150,180,210,250]
x_mean=sum(x)/len(x);
y_mean=sum(y)/len(y);

n=0;
d=0;
k=-1;
for i in x:
    k=k+1;
    n=n+((i-x_mean)*(y[k]-y_mean));
    d=d+(i-x_mean)**2;    
m=n/d;
c=y_mean-m*x_mean;
print(m,c);
y_temp=[];
for i in x:
    y_temp.append(m*i+c);
    
plot.scatter(x,y_temp,color='red')
plot.plot(x,y_temp,color='blue')
plot.xlabel('x data')
plot.ylabel('y data')
plot.show()










