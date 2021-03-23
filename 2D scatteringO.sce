//2 Dimensional scattering of particles by various potential
//numerical method parameters
position_lower=-60
position_higher=60
step_size_position=0.5

hb=1973
me=0.511*(10**6)
c=(hb^2)/(2*me)
es=3.795
cs=3*(10**18)/hb
cs1=3*(10**18)
step_size_time=0.0002/cs
//calculating method parametrs value
number_of_bins=((position_higher-position_lower)/(step_size_position))+1
// psi(x,t)
Psi=zeros(number_of_bins,number_of_bins)
//initial conditions
x=[position_lower:step_size_position:position_higher]
[X,Y]=meshgrid(x,x)
function z=init(y,x)
    po=-1
    z=exp(-0.5*(0.2*((x+20).^2)+0.0001*(y).^2)).*exp(-%i*po*x)
    //z=exp(complex(0,-1)*po*(x))
endfunction
Psi_initial=init(X,Y)
figure(5)
contourf(x,x,abs(Psi_initial),10)
xlabel("x axis")
ylabel("y axis")
Norm=sum(Psi_initial.*conj(Psi_initial))*(step_size_position)^2
Psi=Psi_initial./(Norm)^0.5
Del=zeros(number_of_bins,number_of_bins)
for j=4:number_of_bins-4
    Del(j,j-2:j+2)=[-1,16,-30,16,-1]./12
end
Del=Del./(step_size_position)^2
function z=ele(x,y)
    Z=10
    es=3.795
    z=es*es*((x.^2+(y+20).^2).^(-0.5))+es*es*(((x-10).^2+(y+10).^2).^(-0.5))+es*es*(((x-20).^2+(y).^2).^(-0.5))+es*es*(((x+10).^2+(y+20).^2).^(-0.5))+es*es*(((x).^2+(y+10).^2).^(-0.5))+es*es*(((x-10).^2+(y).^2).^(-0.5))
endfunction
V=ele(X,Y)
V(int(number_of_bins/2)-39,int(number_of_bins/2)+1)=4*es*es/step_size_position
V(int(number_of_bins/2)-19,int(number_of_bins/2)+1)=4*es*es/step_size_position
V(int(number_of_bins/2)-19,int(number_of_bins/2)+1+20)=4*es*es/step_size_position
V(int(number_of_bins/2)+1,int(number_of_bins/2)+1+40)=4*es*es/step_size_position
V(int(number_of_bins/2)-39,int(number_of_bins/2)-19)=4*es*es/step_size_position
V(int(number_of_bins/2)+1,int(number_of_bins/2)+21)=4*es*es/step_size_position
V(1:2,:)=zeros(2,size(V)(2))
V($-1:$,:)=zeros(2,size(V)(2))
aaa=gca()
figure()
subplot(121)
contourf(x,x,V',20)
subplot(122)
for j=1:100
    for l=0:500
    
        delta_psi=((c*(1)*((Del*(Psi))+1*((Psi)*Del')))+1*V'.*Psi)*step_size_time*%i*cs1/hb
        Psi=Psi+delta_psi
        //Norm=sum(Psi.*conj(Psi))*(step_size_position)^2
        //Psi=Psi/(Norm)^0.5
        
    end
    clf()
    contourf(x,x,abs(Psi),20)
end
clear Psi Psi_initial V
disp(X,Y)
