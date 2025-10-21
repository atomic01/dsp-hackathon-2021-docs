% ***************************************
%  Linear phase shift - beam steering
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Here we observe the effect of adding the progressive phase shift \alpha*d
% along the array. Within visible region we will see how the spectrum 
% (i.e. the array factor) moves along normalized beta_z axis. The array is
% discretized with distance of \lambda/2 (Nyquist criterion)
%


clear all;

beta_n =[(-3:0.005:3)]'; %normalized wavenumber space (beta_z/beta = cos(theta))

%Setting the discretized line source (d=lambda/2, uniform magnitude)

d=0.5; %normalized distance in wavelength
N=20; %Number of antenna elements
L=N*d; %total array length
theta_0=[120 90 45]; %desired angle of maximum radiation
alpha_n=-cos(deg2rad(theta_0)); %required linear phase shift rate(normalized to beta)
psi_n=beta_n*d+alpha_n*d; %auxiliary angle for array factor calculations

%The normalized array factor is taken in closed form by inserting auxiliary 
%angle \psi instead of beta_n*d (this angle takes phase shift into account)

AF = sin((psi_n*2*pi*N)/2) ./ ...
    (N.*sin((psi_n*2*pi)/2)); %normalized array factor of array (factor 2*pi is due to normalization!)
AF_dB = 20*log10(abs(AF));

figure(1);
p1=plot(beta_n, AF_dB);
axis([min(beta_n) max(beta_n) -30 5]);

x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized array factor in spectral domain');
legend ('\theta_0=120deg.','\theta_0=90deg.','\theta_0=45deg.');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

%Plotting array factor in angular (\theta) domain ...

%Extracting the visible region
beta_v=beta_n (find(beta_n==-1)):0.005:beta_n(find(beta_n==1)); 
nn=size(beta_v,2);
for k=1:nn
    AF_v(k,:)=AF_dB(find(beta_n==-1)+k-1,:);
           
end;
theta=acos(beta_v);

%Now we plot the array factor
figure (2);


pa=polaraxes ('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Top','ThetaLim',[0 180]);
hold on;
p2=polarplot (theta,AF_v);
title('Normalized array factor in \theta- plane');
legend ('\theta_0=120deg.','\theta_0=90deg.','\theta_0=45deg.');
rticks([-30 -20 -10 0])
rticklabels({'-30 dB', '-20 dB','-10 dB','0 dB'});
hold off;

