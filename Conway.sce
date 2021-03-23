clc
function y=update()
     for m=2:p-1
            for n=2:p-1
                sum_neighbours=sum(new_disturbence(m-1:m+1,n-1:n+1))-new_disturbence(m,n); // sum of neighbours 
                // conditions
                // active=1 
                //inactive=0
                // if number of active elements are more than zero and less than 4 then it will become active
                // else it will become inactive 
                if [sum_neighbours<4 sum_neighbours>0 new_disturbence(m,n)<0.5] then
                     b(m,n)=1;
                 elseif [sum_neighbours<4 sum_neighbours>0 new_disturbence(m,n)>0.5] then
                     b(m,n)=1;
                elseif new_disturbence(m,n)>0.5 then
                     b(m,n)=0;
                 else
                     b(m,n)=0;
                end
               // disp(sum_neighbours)
            end
        end
        b(p,:)=0;
        b(:,p)=0;
       // disp(b)
        new_disturbence=b;
       // disp(new_disturbence)
        y=new_disturbence;
endfunction

//disturbence=input("enter the initial conditions")
//new_disturbence=q;
//g=size(disturbence);
//size_disturbence=input("size of matrix")
//size_disturbence=20;
p=50+2;
new_disturbence=zeros(p,p)
new_disturbence(25:27,25:27)=[0 0 1;0 0 1;0 1 0];
//mgetl(life)
//new_disturbence=csvRead(life)
    q=[1:p]';
w=[1:p]';

scf()
//plot3d1(q,w,new_disturbence)
//step=input("number of steps");
step=1000;
//cycle=input("enter the number of cycles")
cycle=1;
for i=1:cycle
    for j=1:step
     new_disturbence=update()
        q=[1:p]';
        w=[1:p]';
        
 plot3d1(q,q,new_disturbence);
 // mark_size_unit="point"
sleep(200)
end
end



