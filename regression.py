import time
print("SOLN:_________________________________________________________________________________________")
sum_error_xsq = tcal = sum_error_ysq = Sb = Se = expvar = totalvar = sumx = sumy = sumxsq = sumysq = sumxy = meany  = meanx = Rsq = 0.0
sumydiffmean = sumxdiffmean = 0.0
# input values
x = [100, 150, 200, 300, 400, 500, 600]
y = [20, 18, 15, 12, 9, 5, 2]
# predicted y
yp = []
# y-meany
sumymeany = 0.0
ydiffmean = []
ydiffmeansq = []
# yp-meany
sumypmeany = 0.0
ypdiffmean = []
ypdiffmeansq = []


for i in x:
    sumx = sumx + i
    sumxsq = sumxsq + i*i
meanx = sumx / len(x)

for i in y:
    sumy = sumy + i
    sumysq = sumysq + i*i
    
meany = sumy / len(y)

for i in range(len(x)):
    sumxy = sumxy + x[i]*y[i]
    


print("\nsumx= "+str(round(sumx, 3))+"   sumxsq= "+str(sumxsq)+"   sumy= "+str(sumy)+"   sumysq= "+str(sumysq)+"   sumxy= "+str(sumxy))
print(str(sumy)+" = "+str(len(x))+"a + "+str(sumx)+"b")#eqn1
print(str(sumxy)+" = "+str(sumx)+"a + "+str(sumxsq)+"b")#eqn2

a = (sumxsq*sumy - sumx*sumxy) / (len(x)*sumxsq -sumx*sumx)
b = (len(x)*sumxy - sumx*sumy) / (len(x)*sumxsq -sumx*sumx)

meany = round(meany, 2)
for i in range(len(x)):
    t = a + b*x[i]
    yp.append(t)
for i in range(len((x))):
    expvar = expvar + (yp[i] - meany)*(yp[i] - meany)
    totalvar = totalvar + (y[i] - meany)*(y[i] - meany)
Rsq = expvar/totalvar

for i in range(len(x)):
    u = y[i] - meany
    ydiffmean.append(u)
    ydiffmeansq.append(u*u)
    v = yp[i] - meany
    ypdiffmean.append(v)
    ypdiffmeansq.append(v*v)

# calculation of standard error of slope estimate
for i in range(len(x)):
    sum_error_ysq = sum_error_ysq + (ypdiffmean[i] - ydiffmean[i])*(ypdiffmean[i] - ydiffmean[i])
    sum_error_xsq = sum_error_xsq + (x[i] - meanx)*(x[i] - meanx)
    sumydiffmean = sumydiffmean + ydiffmeansq[i]
Sb = ( sum_error_ysq / ( (len(x)-2) * sum_error_xsq ) ) ** 0.5
tcal = b / Sb
for i in range(len(x)):
    sumxdiffmean = sumxdiffmean + (x[i] - meanx)*(ydiffmean[i])
Se = ( (sumydiffmean - b*sumxdiffmean)/(len(x)-2) ) ** 0.5
print("a = %.3f" % round(a, 3))
print("b = %.3f" % round(b, 3))
print("Rsq = %.3f" % round(Rsq, 3))
print("Mean of y = %.3f" % round(meany, 3))
print("Mean of x = %.3f" % round(meanx, 3))
print("Sb = %.3f" %(Sb))
print("Se = %.3f" %(Se))
print("T calculated = %.3f" %(tcal))
print("___________________________________________________________________________________________\n")
print("yp              y-mean(y)             (y-mean(y))sq         yp-mean(y)        (yp-mean(y))sq\n")
print("___________________________________________________________________________________________\n")
for i in range(len(x)):
    print("%.3f      |      %.3f      |      %.3f      |      %.3f      |      %.3f\n" %(yp[i], ydiffmean[i], ydiffmeansq[i], ypdiffmean[i], ypdiffmeansq[i]))
time.sleep(600)