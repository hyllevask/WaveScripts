%%%%%%%%%%%%%%
% PARAMETERS %
%%%%%%%%%%%%%%
I0 = 1          %Incident Intensity W/m^2
l = 0.630e-6;   % Wavelength [m]
d = 600e-6;     % Slit Distance [m]
a = 200e-6;     % Slit Width [m]
N = 2;          % Number of slits
x_max = 0.05    % Maximum latteral distance 
L = 4;          % Distance from slit to screen

%%%%%%%%%%%%%%%%%%%%%%
% DERIVED PARAMETERS %
%%%%%%%%%%%%%%%%%%%%%%

k = 2*pi/l      %Wavenumber
x = linspace(-x_max,x_max,35000);   %Generete x-coordinates

theta = atan(x/L);    %Relate to angle

phi = k*d*sin(theta)
beta =  k*a*sin(theta)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GENERATE INTENSITY ON SCREEN AND PLOT %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


Ip = I0 * sin(beta/2).^2./(beta/2).^2 .* sin(N*phi/2).^2 ./ sin(phi/2).^2;

figure(1)
plot(x*1000,Ip)
xlabel("x [$mm$]")
ylabel("I [$W/m^2$]")