function uW_AMCAD_CST_deembedding(filename,filename2,Sin,Sout)

	// Dev
	// filename="C:\PUBLIC\2007WW41_David_Eudyna\courbes_2G_prj.cst";
    format ("v",15);
	// Tableau de valeurs connues
	liste_frequence=[];
	correct_in=list();
	correct_out=list();
	

	// Lecture du fichier
	data=mgetl(filename);
	
	// Correspondace des colones
	// 1ere colone : frequence
	// derniere colone Im[b2]
	// ordre des ondes : a1 b1 a2 b2
	
	
	// === Stockage des mesures dans l'ordre du fichier
	pos_begin=grep(data,"#BEGIN")+1;
	pos_end=grep(data,"#END")-1;
	
	
	
	nb_courbe=min(size(pos_begin,"c"),size(pos_end,"c"));
	for i=1:nb_courbe,
		measure=[];
		for j=pos_begin(i):pos_end(i),
				measure=evstr(tokens(data(j)," ")).';
				
				frequence=measure(1);
				a1=measure($-7)+%i*measure($-6);
				b1=measure($-5)+%i*measure($-4);
				a2=measure($-3)+%i*measure($-2);
				b2=measure($-1)+%i*measure($);
				
				recherche_frequence=find(liste_frequence==frequence);
				
				if recherche_frequence==[] then,
					// Stocke la nouvelle frequence
					liste_frequence=[liste_frequence;frequence];
					
					// Interpolation du Sin
					
					f_Sij=Sin.frequency;
					
					Sin_f=[];
					for k=1:4,
						Sij=Sin(2+k);
						M_Sij=abs(Sij);
						P_Sij=uW_unwarp(Sij);
				
						M2_Sij=interp(frequence, f_Sij,M_Sij, splin(f_Sij,M_Sij,"monotone")); 
						P2_Sij=interp(frequence, f_Sij,P_Sij, splin(f_Sij,P_Sij,"monotone")); 
			
						Sin_f=[Sin_f;M2_Sij.*exp(%i*%pi*P2_Sij/180)];
					end;
					Sin_f=matrix(Sin_f,2,2).';
					
					Sout_f=[];
					for k=1:4,
						Sij=Sout(2+k);
						M_Sij=abs(Sij);
						P_Sij=uW_unwarp(Sij);
				
						M2_Sij=interp(frequence, f_Sij,M_Sij, splin(f_Sij,M_Sij,"monotone")); 
						P2_Sij=interp(frequence, f_Sij,P_Sij, splin(f_Sij,P_Sij,"monotone")); 
			
						Sout_f=[Sout_f;M2_Sij.*exp(%i*%pi*P2_Sij/180)];
					end;
					Sout_f=matrix(Sout_f,2,2).';
					
					Tin=(1/Sin_f(2,1))*[1,-Sin_f(2,2);Sin_f(1,1),-Sin_f(1,1)*Sin_f(2,2)+Sin_f(1,2)*Sin_f(2,1)];
					Tout=(1/Sout_f(2,1))*[1,-Sout_f(2,2);Sout_f(1,1),-Sout_f(1,1)*Sout_f(2,2)+Sout_f(1,2)*Sout_f(2,1)];
				

					// Sauvegarde des ondes de-embeddées
					correct_in($+1)=inv(Tin);
					correct_out($+1)=Tout;
					_input=correct_in($)*[a1;b1];
					_output=correct_out($)*[b2;a2];

					
				else,
					_input=correct_in(recherche_frequence)*[a1;b1];
					_output=correct_out(recherche_frequence)*[b2;a2];
								
				end;
				
				a1=_input(1);
				b1=_input(2);
				b2=_output(1);
				a2=_output(2);
				
				// Ecriture des données en mémoire
				measure($)=imag(b2);
				measure($-1)=real(b2);
				measure($-2)=imag(a2);
				measure($-3)=real(a2);
				measure($-4)=imag(b1);
				measure($-5)=real(b1);
				measure($-6)=imag(a1);
				measure($-7)=real(a1);
				data(j)=strcat(string(measure),ascii(9));
			
		end;
	end;

	// Ecriture du fichier
	
	mputl(data,filename2);
	
	


endfunction