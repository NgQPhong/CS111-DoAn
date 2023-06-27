// Z: 0 false 1 true
// X!=Y

clear Z1;
clear temp;
clear temp1;
clear temp2;

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
	decr temp1;
	decr temp2;
end;

while temp2 not 0 do
	incr Z1;
	clear temp2;
end;

clear Z2;
clear temp;
clear temp3;
clear temp4;

while X not 0 do
	incr temp3;
	incr temp;
	decr X;
end;
while temp not 0 do
	incr X;
	decr temp;
end;

while Y not 0 do
	incr temp4;
	incr temp;
	decr Y;
end;
while temp not 0 do
	incr Y;
	decr temp;
end;

while temp4 not 0 do
	decr temp3;
	decr temp4;
end;

while temp3 not 0 do
	incr Z2;
	clear temp3;
end;

clear Z;
while Z1 not 0 do
	incr Z;
	decr Z1;
end;
while Z2 not 0 do
	incr Z;
	decr Z2;
end;

clear tmp;
incr tmp;
while Z not 0 do
	decr Z;
	decr tmp;
end;

while tmp not 0 do
	decr tmp;
	incr Z;
end;