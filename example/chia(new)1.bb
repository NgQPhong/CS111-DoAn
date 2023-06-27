// Z = X // Y
// T = X % Y
// X = 10
// Y = 5

clear Z;
clear T;

clear X;
incr X;
incr X;
incr X;
incr X;
incr X;
incr X;
incr X;
incr X;
incr X;
incr X;


clear Y;
incr Y;
incr Y;
incr Y;
incr Y;
incr Y;

clear temp;
clear temp1;
clear temp2;
clear temp3;

while X not 0 do
	incr temp1;
	incr temp;
	decr X;
end;
while temp not 0 do
	incr X;
	decr temp;
end;

while Y not 0 do
	incr temp2;
	incr temp;
	decr Y;
end;
while temp not 0 do
	incr Y;
	decr temp;
end;

while temp1 not 0 do
	incr Z;
	clear T;
	clear temp3;
	while temp1 not 0 do
		incr T;
		incr temp;
		decr temp1;
		incr temp3;
	end;
	while temp not 0 do
		incr temp1;
		decr temp;
	end;
	while temp2 not 0 do
		decr temp1;
		incr temp;
		decr temp2;
	end;
	while temp not 0 do
		incr temp2;
		decr temp;
	end;
end;

while temp3 not 0 do
	decr temp2;
	decr temp3;
end;
incr temp3;
while temp2 not 0 do
	decr Z;
	clear temp2;
	clear temp3;
end;
while temp3 not 0 do
	clear temp3;
	clear T;
end;