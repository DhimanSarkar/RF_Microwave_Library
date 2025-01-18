function d=%l_s_l(a,b)
	d=a;
	for i=3:size(a),
		d(i)=a(i)-b(i);
	end;
endfunction
