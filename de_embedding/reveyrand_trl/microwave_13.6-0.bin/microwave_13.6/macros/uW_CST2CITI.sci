
function uW_CST2CITI(filename)

	// ===========================
	data=mgetl(filename);

	// #FUNDAMENTAL FREQUENCY: 3.2 GHz
	// #HARMONICS: 2


	// Récupère la fréquence
	tmp=grep(data,"#FUNDAMENTAL FREQUENCY:");
	tmp=tmp(1);
	tmp=tokens(data(tmp)," ");
	fund_freq=evstr(tmp($-1))*uW_freq_unit(tmp($));

	// Récupère le nombre d'harmoniques

	tmp=grep(data,"#HARMONICS:");
	tmp=tmp(1);
	tmp=tokens(data(tmp)," ");
	nb_harm=1+evstr(tmp($));


	// Récupère le nombre de mesures
	i_start=grep(data,"#BEGIN")+1;
	i_end=grep(data,"#END")-1;

	i_file=[1:length(i_start)];
	source=data;

	data_v1=[];
	data_i1=[];
	data_v2=[];
	data_i2=[];

	nb_pts=[];
	for meas=i_file,
		// Récupère les DATA
		// data=fscanfMat(filename);

		data=source([i_start(meas):i_end(meas)]);
		cmd=["data=["+data(1)+";"];
		cmd=[cmd;data(2:$-1)+";"];
		cmd=[cmd;data($)+"];"];
		execstr(cmd);
		
		nb_pts=[nb_pts;size(data,1)/nb_harm];
	end;



	for meas=i_file,
		// Récupère les DATA
		// data=fscanfMat(filename);

		data=source([i_start(meas):i_end(meas)]);
		cmd=["data=["+data(1)+";"];
		cmd=[cmd;data(2:$-1)+";"];
		cmd=[cmd;data($)+"];"];
		execstr(cmd);

		// nb_pts=size(data,1)/nb_harm;

		// disp(nb_pts);



		a1=matrix(data(:,6)+%i*data(:,7),nb_harm,nb_pts(meas));
		b1=matrix(data(:,8)+%i*data(:,9),nb_harm,nb_pts(meas));
		a2=matrix(data(:,10)+%i*data(:,11),nb_harm,nb_pts(meas));
		b2=matrix(data(:,12)+%i*data(:,13),nb_harm,nb_pts(meas));
		// 
		v1=sqrt(50)*(a1+b1);
		i1=(1/sqrt(50))*(a1-b1);
		v2=sqrt(50)*(a2+b2);
		i2=(1/sqrt(50))*(a2-b2);
		//
		vin=matrix(data(:,2),nb_harm,nb_pts(meas));
		V1=[vin(1,:);v1];
		iin=matrix(data(:,3),nb_harm,nb_pts(meas));
		I1=[iin(1,:);i1];
		vout=matrix(data(:,4),nb_harm,nb_pts(meas));
		V2=[vout(1,:);v2];
		iout=matrix(data(:,5),nb_harm,nb_pts(meas));
		I2=[iout(1,:);i2];
		//
		V1=matrix(V1,-1,1);
		I1=matrix(I1,-1,1);
		V2=matrix(V2,-1,1);
		I2=matrix(I2,-1,1);
		//


		if(nb_pts(meas)<max(nb_pts)),
			for i=1:max(nb_pts)-nb_pts(meas),
				V1=[V1(1:nb_harm+1);V1];
				V2=[V2(1:nb_harm+1);V2];
				I1=[I1(1:nb_harm+1);I1];
				I2=[I2(1:nb_harm+1);I2];
			end;

		end;


		data_v1=[data_v1;string(real(V1))+","+string(imag(V1))];
		data_i1=[data_i1;string(real(I1))+","+string(imag(I1))];
		data_v2=[data_v2;string(real(V2))+","+string(imag(V2))];
		data_i2=[data_i2;string(real(I2))+","+string(imag(I2))];
	

	end;

	// Ecriture du CITIfile
	filename=tokens(filename,".");
	filename=filename+".citi";


	data=[	"CITIFILE A.01.01";
		"NAME LSNADataSet";
		"VAR FILE MAG "+string(size(i_file,2));
		"VAR INDEX MAG "+string(max(nb_pts));
		"VAR FREQ MAG "+string(nb_harm+1);
		"DATA V1 RI";
		"DATA I1 RI";
		"DATA V2 RI";
		"DATA I2 RI";
		"VAR_LIST_BEGIN";
		string(i_file.');
		"VAR_LIST_END";
		"SEG_LIST_BEGIN";
		"SEG 1 "+string(max(nb_pts))+" "+string(max(nb_pts));
		"SEG_LIST_END";
		"SEG_LIST_BEGIN";
		"SEG 0 "+string(fund_freq*nb_harm/10^9)+"e9 "+string(nb_harm+1);
		"SEG_LIST_END";
		"BEGIN";
		data_v1;
		"END";
		"BEGIN";
		data_i1;
		"END";
		"BEGIN";
		data_v2;
		"END";
		"BEGIN";
		data_i2;
		"END"];
	mputl(data,filename);
endfunction




