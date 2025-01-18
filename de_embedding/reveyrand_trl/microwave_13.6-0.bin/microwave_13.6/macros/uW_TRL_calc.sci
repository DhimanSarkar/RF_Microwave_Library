
function varargout=uW_TRL_calc(S_thru,S_line,S_reflect,REFLECT_STD)

T_THRU=uW_S2T(S_thru);
T_LINE=uW_S2T(S_line);

M11=[];M12=[];M21=[];M22=[];
N11=[];N12=[];N21=[];N22=[];

T_IN=list();
T_OUT=list();

K=[];

for i=1:size(T_THRU.frequency,1),
    T1=[T_THRU.T11(i),T_THRU.T12(i);T_THRU.T21(i),T_THRU.T22(i)];
    T2=[T_LINE.T11(i),T_LINE.T12(i);T_LINE.T21(i),T_LINE.T22(i)];
    M=inv(T1)*T2;
    N=T2*inv(T1);

    // Eqution TRL M    
    delta=(M(1,1)-M(2,2))^2-4*M(2,1)*(-M(1,2));
    X1=((M(2,2)-M(1,1))-sqrt(delta))/(2*M(2,1));
    X2=((M(2,2)-M(1,1))+sqrt(delta))/(2*M(2,1));
    Sol=[X1,X2];
    C1=Sol(find(abs(Sol)==max(abs(Sol))));  // OUTPUT - T22/T21
    C2=Sol(find(abs(Sol)==min(abs(Sol))));  // OUTPUT - T12/T11    
    
    // Equation TRL N
    delta=(N(1,1)-N(2,2))^2-4*N(2,1)*(-N(1,2));
    X1=((N(2,2)-N(1,1))-sqrt(delta))/(2*N(2,1));
    X2=((N(2,2)-N(1,1))+sqrt(delta))/(2*N(2,1));
    Sol=[X1,X2];
    C3=Sol(find(abs(Sol)==max(abs(Sol))));  // INPUT - D/C
    C4=Sol(find(abs(Sol)==min(abs(Sol))));  // INPUT - B/A 
 
    // Equation THRU FORWARD
    C5=(1+C4*S_thru.S11(i))/(S_thru.S21(i));    // T11/A

    // Equation THRU REVERSE    
    C6=(S_thru.S12(i))/(S_thru.S22(i)+C1);      // T21/D
    
    // Equation Reflect
    _X=(S_reflect.S22(i)+C2)/(S_reflect.S22(i)+C1);
    _Y=(1+C3*S_reflect.S11(i))/(1+C4*S_reflect.S11(i));
    sol=sqrt((C5*_X)/(_Y*C6*C3));       // C
    
    A=1;B=C4;C=sol;D=C3*C;
    GAMMA_STD=(C+D*S_reflect.S11(i))/(A+B*S_reflect.S11(i));
    if ((real(GAMMA_STD)>0)&REFLECT_STD=="SHORT")|((real(GAMMA_STD)<0)&REFLECT_STD=="OPEN") then,      // If OPEN, chose the other solution
         sol=sol*(-1); 
    end;
    
    //plot2d(real(GAMMA_STD),imag(GAMMA_STD),-8);
    
    
    A=1;B=C4;C=sol;D=C3*C;
    
    K=[K;(sqrt(1/(A*D-B*C)))];
    
    T_IN($+1)=inv([A,B;C,D]);
    T_OUT($+1)=[C5,C2*C5;C6*D,C1*C6*D];
 
end;

// === Reciprocity : K unwaping
        x=phasemag(K(2:$))-phasemag(K(1:($-1)));
		a=(x<-90)*180+(x>90)*(-180);	
		a=cumsum(a,'r');
		a=[0;a];
		uwp=real(phasemag(K(1:$))+a);
    
    
     
       
        
        
        
        
        cc=pinv([S_thru.frequency/10^9,uwp*0+1])*uwp;
        // if  (cc(2)>180) then, uwp=uwp-360;cc(2)=cc(2)-360;end;
        // if  (cc(2)<-180) then, uwp=uwp+360;cc(2)=cc(2)+360;end;
        
        uwp=uwp-cc(2)+modulo(cc(2),180);
        
        
           K=abs(K).*exp(%i*%pi*uwp/180);
          
            
     
// === BUILD T MATRIX
T11=[];T12=[];T21=[];T22=[];
for i=1:size(T_THRU.frequency,1),
    T11=[T11;T_IN(i)(1,1)];T12=[T12;T_IN(i)(1,2)];T21=[T21;T_IN(i)(2,1)];T22=[T22;T_IN(i)(2,2)];
end;
Port_IN=tlist(['T parameters';'frequency';'T11';'T12';'T21';'T22'],T_THRU.frequency,(1 ./K).*T11,(1 ./K).*T12,(1 ./K).*T21,(1 ./K).*T22);

T11=[];T12=[];T21=[];T22=[];
for i=1:size(T_THRU.frequency,1),
    T11=[T11;T_OUT(i)(1,1)];T12=[T12;T_OUT(i)(1,2)];T21=[T21;T_OUT(i)(2,1)];T22=[T22;T_OUT(i)(2,2)];
end;
Port_OUT=tlist(['T parameters';'frequency';'T11';'T12';'T21';'T22'],T_THRU.frequency,K.*T11,K.*T12,K.*T21,K.*T22);
    
// === Convert to S-param

S_IN=uW_T2S(Port_IN);
S_OUT=uW_T2S(Port_OUT);

S_R=uW_S2P_deembedding(S_reflect,S_IN,S_OUT);

       varargout=list(S_IN,S_OUT,S_R);
  

        
endfunction
