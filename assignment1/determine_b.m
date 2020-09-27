function b = determine_b

% determine_b =  Determine the base of the floating point number system on
% this computer
format long

% first phase
a = 1;
while ((a+1) -a) == 1,
   a = a*2
end

a+1
a
(a+1)-a

% second phase
i = 1;
while (a == (a+i)),
   i = i + 1
end

% result
a+i
a
b = (a + i) - a;