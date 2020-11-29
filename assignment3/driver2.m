[V,t,neval]=adaptiveRK(@FBrusselator,0,20,[1.5;3],0.1,1e-2);

plot(t,V,'-*')
