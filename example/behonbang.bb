// Z: 0 false 1 true
// X<=Y

clear Z;
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

while temp2 not 0 do
	decr temp1;
	decr temp2;
end;

while temp1 not 0 do
	incr Z;
	clear temp1;
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