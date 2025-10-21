% ***************************************
%  Spatial factor of a line source
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 

% Here we observe how the length of line source of length L affects the
% beamwidth (and hence spatial resolution).
%
% Broadside sources (uniform magnitude) are assumed here. We observe lengths of 2, 5 and 10
% lambdas but one can play with them further...

clear all;
close all;

%% Define a line source and find its radiation pattern ("space factor")

% Normalized wavenumber space
% We take range -3:3 so that both visible and invisible ranges are seen
% beta_z/beta = cos(theta)
beta_n =[(-3:0.005:3)]';

% Normalized source length in units of lambda
L = [2 5 10];

% Spatial factor of line source normalized to its maximum (factor 2*pi is due to normalization!)
SF= sin((beta_n*2*pi*L)/2)./((beta_n*2*pi*L)/2); % normalized space factor of line source
SF_dB = 20*log10(abs(SF));

%% Plot the spatial factor

figure(1);
p1=plot(beta_n, SF_dB);
axis([min(beta_n) max(beta_n) -30 5]);

% Format the figure

x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized pattern in spectral domain - line source');
legend ('L=2\lambda','L=5\lambda','L=10\lambda');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

%% Extract only the visible range

beta_v=beta_n (find(beta_n==-1)):0.005:beta_n(find(beta_n==1)); 
nn=size(beta_v,2);
for k=1:nn
    SF_v(k,:)=SF_dB(find(beta_n==-1)+k-1,:);
           
end;
theta=acos(beta_v);

%% Plot the visible range

figure (2);

% Format the figure

polaraxes('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Left','ThetaLim',[0 180]);
hold on;
p2=polarplot(theta,SF_v);
title('Normalized pattern - line source');
legend ('L=2\lambda','L=5\lambda','L=10\lambda');
