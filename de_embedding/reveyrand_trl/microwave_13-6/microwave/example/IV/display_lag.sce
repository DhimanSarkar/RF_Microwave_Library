 // Script to display Lag effect
 // Select the following network
 //	1. Cold (0/0) ==> Black Network
 // 2. Gate Lag (-8/0) ==> Blue Network
 // 3. Drain Lag (-8/20) ==> Red Network





 
filename=tk_getfile("*.mes");


filename="C:\USERS\tibo\modele\QQ_R2_LNA\Q3_2x75\2x75_lag.mes"
data=uW_MES_read(filename);

transistor="Endeavour 2x75";
abscisse="Vds (V)";
ordonee="Id (A)";

color=[1,2,5];
network=[];
for i=1:3,
	network = [network,uW_MES_select_network(data)];
end;
uW_MES_plot(data,network(1),'v2','i2',style=1,vlegend=%T);
uW_MES_plot(data,network(2),'v2','i2',style=2);
uW_MES_plot(data,network(3),'v2','i2',style=5);


// Légende pour les réseaux
plot2d([0,0,0;0,0,0],[0,0,0;0,0,0],style=[1;2;5],leg="Cold Network (0/0)@Gate Lab (-8/0)@Drain Lag (-8/14)")*



// Propriétés du graph

f=get("current_figure"); //get the current figure 
f.children.title.text=transistor;  
f.children(1).x_label.text=abscisse;
f.children(1).x_label.font_size=4; 
f.children(1).y_label.text=ordonee;
f.children(1).y_label.font_size=4 
f.children(1).font_size = 4;
f.children(1).title.font_size=4;

// Grille
f.children(1).grid=[1,1];    

// Met le coin bas à 0/0
f.children(1).data_bounds([1,3])=[0,0];

// Epaisseur de toutes les courbes
// for i=1:size(f.children(1).children,"r"),
// if (f.children.children(i).children~=[]) then,
// f.children(1).children(i).children(1).thickness=2;
// end;
// end;



	if network~=0,
		uW_MES_plot(data,network,'v2','i2',style=color(i),vlegend=%T);
	end;
end;