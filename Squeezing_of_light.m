clc
z=1:5;
alpha=3;
global w
w=1;
global s 
s=100;

% Annihilation and creation operator
global a_n
global a_d
a_n= zeros(s);
a_d= zeros(s);
for i=1:s-1
    a_n(i,i+1)=sqrt(i);
    a_d(i+1,i)=sqrt(i);
end

% ----------------------------------------------------------------------
%squeezing operator
neta=complex(4);
S1=((neta*a_n^2-conj(neta)*a_d^2)/2);
%  works
%  displacement operator
beta=complex(5,0);
phi=0;
r=2;
t_n= a_n*cosh(r)+exp(complex(0,1)*phi)*a_d*sinh(r);
t_d=t_n';
D=beta*t_d-conj(beta)*t_n;

Do=D+eye(s);
S=S1+eye(s);
for m=2:100
    Do=Do+(D^m)/(factorial(double(m)));
    S=S+(S1^m)/(factorial(double(m)));
end

%------------------------------------------------------------------------
% Experiment...
state=zeros(s,1);
eta=r;
for i=0:49
    th=tanh(eta);
    state=state+ (sqrt(factorial(double(2*i)))*(th^i)/((2^i)*factorial(double(i))))*numbstate(2*i+1);
end

state=Do*state;
norm=state'*state;
state=state/(sqrt(norm));
tiledlayout(1,2);
nexttile;
Qplotter(state);
title('Q Distribution');
xlabel('Real(alpha)');
ylabel('imaginary(alpha)')

nexttile;
ElectricField(state);
title('Electric field vs Time')
xlabel('time');
ylabel('Electric Field');

% -----------------------------------------------------------------------
function y=Qplotter(state)
    alphar=-10:0.1:10;
    alphai=-10:0.1:10;
    i=0;
    ou=zeros(length(alphar),length(alphai));
    for ar=alphar
        i=i+1;
        j=0;
        for ai=alphai
            j=j+1;
            ou(j,i)=Qvalue(state,ar,ai);
        end
    end
    [aa,bb]=meshgrid(alphar,alphai);
   
    contourf(aa,bb,ou);
    grid on;
    ax=gca();
    ax.XAxisLocation= "origin";
    ax.YAxisLocation="origin";
    ax.XColor="r";
    ax.YColor="r";    
    title('Qplot')
    xlabel('alpha');
    colormap("turbo");
    y=ou;
end


function y=Qvalue(state,alphar,alphai)
    c=coherent(complex(alphar,alphai));
    y= abs((c'*state))^2;
end


function y= ElectricField(state)
    m=0;
    st=1000;
    E2=zeros(st,1);
    E2s=zeros(st,1);
    for t=0:((8)/st):8
        m=m+1;
        E2(m,1)=((state)')*Eo(t)*state;
        E2s(m,1)=((state)')*Eo(t)*Eo(t)*state;
        %handle1.XData=t;
        %handle1.YData=real(E2t);
    end
    E2ss=(E2s-(E2.^2)).^(0.5);
    Eobserved= E2+E2ss.*randn(length(E2),1);
    t=1:((8-4)/st):5;
    plot(t,real(E2),t,real(E2ss),t,real(Eobserved));
    legend('E','stdE','Eobserved');
    y= E2s;
end
function y= coherent(alpha)
    global s
    d=zeros(s,1);
    for n=1:s
     d=d+((alpha^(n-1))/sqrt(factorial(n-1)))*numbstate(n);
    end
    d=d*exp(-(abs(alpha)^2)/2);
    y=d;
end
    
function  y= numbstate(k)
    global s
    dummy=zeros(s,1);
    dummy(k,1)=1;
    y=dummy;
end
function y= Eo(t)
% electric field operator = c*( a e^(i(k.r-wt)) - a* e^(-i(k.r-wt)  )
% Vector potential = c*( a e^(i(k.r-wt)) + a* e^(-i(k.r-wt) )
    global w
    global a_n
    global a_d
    y = complex(0,1)*(a_n*exp(complex(0,1)*(-w*t)) - a_d * exp(complex(0,1)*(w*t)));
end
function y= Ao(t);
% electric field operator = c*( a e^(i(k.r-wt)) - a* e^(-i(k.r-wt)  )
% Vector potential = c*( a e^(i(k.r-wt)) + a* e^(-i(k.r-wt) )
    global w
    global a_n
    global a_d
    y = a_n*exp(complex(0,1)*(-w*t)) + a_d * exp(complex(0,1)*(w*t));
end

