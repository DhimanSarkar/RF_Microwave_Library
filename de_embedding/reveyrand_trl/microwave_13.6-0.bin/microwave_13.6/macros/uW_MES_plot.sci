
// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_MES_plot",path);

// ###########################
// # Lecture de fichier MES
// ###########################

// ========================================
// Tracé du MES ===========================
// ========================================
// Ne marche que pour des coubres FET
// à Vgs=cste
	 
function uW_MES_plot(MES,n_network,my_x,my_y,style,leg,rect,vlegend)	
// ==== Reseau Id vs Vd	

	//
	[lhs,rhs]=argn(0)
	
	if rhs<2 then
		disp("Wrong number of argument");
		disp("uW_MES_plot(DATA,Network,X,Y)");
		return
	end
	
	
	// ================ Commandes provenant de polarplot.sci
	opts=[]
    isframeflag=%f,isrect=%f
	if exists('style','local')==1 then opts=[opts,'style=style'],end
	
	// if exists('strf','local')==1 then 
    // opts=[opts,'strf=strf'],
    // isstrf=%t
    // end
	
	if exists('leg','local')==1 then opts=[opts,'leg=leg'],end

	if exists('rect','local')==1 then
		opts=[opts,'rect=rect'],
		isrect=%t
    end
	
	if exists('frameflag','local')==1 then 
		opts=[opts,'frameflag=frameflag'],
		isframeflag=%t
	end

	// if size(opts,2)<rhs-5 then  error('invalid named arguments'),end
	// disp("toto");
	// ================ 
	
	// if ~isrect then
	//	rect=[-rm -rm rm rm]*1.1
	//	opts=[opts,'rect=rect']
	// end

	// if isstrf& isframeflag then
	// 	error('frameflag  cannot be used with strf')
	// end

	// if ~(isstrf) then
	// 	axesflag=0
	// 	opts=[opts,'axesflag=axesflag'],
	// end

	// if ~(isstrf|isframeflag) then
	// if ~(isframeflag) then
	//	frameflag=4
	//	opts=[opts,'frameflag=frameflag'],
	// end
	
	// execstr('plot2d(x,y,'+strcat(opts,',')+')')

	

   // Plot the network by yourself : Id=f(Vds)
   for network=n_network,
   for c=1:size(MES.network(network).curve),
      X=[];
	  Y=[];
      for p=1:size(MES.network(network).curve(c).plot),
		  xx=evstr("MES.network(network).curve(c).plot(p)."+my_x);
		  yy=evstr("MES.network(network).curve(c).plot(p)."+my_y);
	      X=[X;xx];
		  Y=[Y;yy];
      end;
	  // plot2d(X,Y,network);
	  // plot2d(X,Y,2);
	  
	  if exists('vlegend','local')==1,
	    xxx=find(X==max(X));
		yyy=Y(xxx);
		if (vlegend=="max"),
			xxx=find(Y==max(Y));
			xxx=xxx(1);
		end;
		
		xstring(X(xxx),Y(xxx),"V1 = "+string(round (MES.network(network).curve(c).plot(1).v1*10)/10));
	  end;
	  
	  
	  // plot2d(X,Y,-6);
	  execstr('plot2d(X,Y,'+strcat(opts,',')+')')
	  
	  
	  
   end;
   end;
endfunction;
  
 


