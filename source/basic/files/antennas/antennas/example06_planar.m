% ***************************************
% Planar array - array factor
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% We have seen that with linear arrays we can steer the beam in one plane
% only. With planar arrays we can achieve full 3D scan. We show the example
% of planar array with rectangular grid which acts as a product of two
% linear arrays in x- and y-direction. We calculate the two 1D (linear)
% array factors in spectral domain and take their product to obtain 2D
% array factor (we choose distances of lambda/2 to remain within Nyquist 
% criterion).

clear all;

betax_n =[(-3:0.005:3)]'; % normalized wavenumber space in x- direction(beta_x/beta = sin(theta)cos(phi))
betay_n = [(-3:0.005:3)]'; % normalized wavenumber space in y- direction(beta_y/beta = sin(theta)sin(phi))

%creating 2D wavenumber space (for plotting the surf plot)
[XX,YY]=ndgrid(betax_n,betay_n);

%Setting the array parameters in x- and y- direction

dx=0.5; %normalized distance in wavelength (in x-direction)
dy=0.5; %normalized distance in wavelength (in y-direction)
M=10; %Number of antenna elements in X
N=5; %Number of antenna elements in Y

% Setting desired angles of maximum for beam steering(we choose broadside direction)
% This gives us beamforming capability...

theta_0=[0]; % In this coordinates broadside appears at \theta=0!
phi_0=90; %This becomes interesting when we move from broadside

% Calculating required linear phase shift rates both in x- and y-direction(normalized to beta)
alphax_n=-sin(deg2rad(theta_0))*cos(deg2rad(phi_0)); 
alphay_n=-sin(deg2rad(theta_0))*sin(deg2rad(phi_0)); 
psix_n=XX*dx+alphax_n*dx; %auxiliary angles for array factor calculations (in X)
psiy_n=YY*dy+alphay_n*dy; %auxiliary angles for array factor calculations (in Y)

% Calculation of array factors in x- and y- direction via array
% parameters...

%Array factor in X...

AFx = sin((psix_n*2*pi*M)/2) ./ ...
    (M.*sin((psix_n*2*pi)/2)); % normalized array factor of array (factor 2*pi is due to normalization!)

AFx(abs(AFx)>1)=1; % removing numerical glitches
AFx(abs(AFx)<1e-8)=0; % removing numerical glitches
AFx=AFx/(max(AFx,[],'all')); %normalization
AFx_dB = 20*log10(abs(AFx)); %conversion to decibels

%Array factor in Y..
AFy = sin((psiy_n*2*pi*N)/2) ./ ...
    (N.*sin((psiy_n*2*pi)/2)); %normalized array factor of array (factor 2*pi is due to normalization!)

AFy(abs(AFy)>1)=1; % removing numerical glitches
AFy(abs(AFy)<1e-8)=0; % removing numerical glitches
AFy=AFy/(max(AFy,[],'all')); %normalization
AFy_dB = 20*log10(abs(AFy)); %conversion to decibels

% Plotting array factors in spectral domains (beta_x and beta_y) separately

figure(1);
p1=plot(betax_n, AFx_dB(:,1));
axis([min(betax_n) max(betax_n) -30 5]);

x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('X-direction - spectral domain');
% legend ('Beams at cos \theta=+-1/2');
xlabel('\beta_x/\beta=sin(\theta)\cdot cos(\phi)');
ylabel('Relative level [dB]');

% 
figure(2);
p2=plot(betay_n, AFy_dB(1,:));
axis([min(betay_n) max(betay_n) -30 5]);

x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Y-direction - spectral domain');
xlabel('\beta_y/\beta=sin(\theta)\cdot sin(\phi)');
ylabel('Relative level [dB]');

% Calculation of spectral domain array factor as a product of two array factors...
AF_tot=AFx.*AFy;
min_dB=-40;
AFtot_dB = max(20*log10(abs(AF_tot)), min_dB); % making the plot "nicer" by removing unnecesarry data
AFtot_dB(end,end) = -100;  % hack to avoid graphic glitch when saving plot

%Parameters of unit circle which defines visible region
th=linspace (0,2*pi,1001);
x=cos(th);
y=sin(th);

figure (3);
% plotting the array factor in 2D spectral domain (beta_x beta_y)..
p3=surf(XX, YY, AFtot_dB);
set(p3,'LineStyle','none');hold on;
%Adding unit circle as a visible region boundary
p3a=plot(x,y,'r--');
set (p3a, 'LineWidth',2);
text (-1,1.2,'Visible region ','Color','r','FontSize',16);
%Setting the plot parameters
caxis([-40 0]);
colormap(jet(-min_dB/2.5));
view(2); % 2D view
box on;
hb = colorbar;
axis image;
set(gca, 'TickDir', 'out');
grid off;
colorTitleHandle = get(hb,'Title');
titleString = 'dB';
set(colorTitleHandle ,'String',titleString);
title('Planar array - 2D spectral domain');
xlabel('\beta_x/\beta = sin(\theta)\cdot cos(\phi)','FontSize',14);
ylabel('\beta_y/\beta = sin(\theta)\cdot sin(\phi)','FontSize',14);



