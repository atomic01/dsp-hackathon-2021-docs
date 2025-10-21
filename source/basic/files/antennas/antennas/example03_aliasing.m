% *********************************************
% Aliasing in spectral domain - grating lobes
% *********************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% We observe the effect of aliasing, which occurs when the line source
% distance is larger than \lambda/2. In that case the spectral images from
% discretization come into visible region and grating lobes would occur at
% some angles. The "safest" direction from aliasing is the broadside one 
% and it tolerates the distances of up to \lambda.

% In this example we fix the array total length to 6*\lambda.We reduce the
% number of elements from 12 (Nyquist distance \lambda/2) to 8 and 4 and
% observe how the grating lobe arrives into visible region.

clear all;

beta_n =[(-3:0.005:3)]'; %normalized wavenumber space (beta_z/beta = cos(theta))

%Setting the array parameters...

L=6; %total array length (normalized to wavelength)
N=[12 8 4]; %numbers of antenna elements
d=L./N; % distance between antennas

% The normalized array factor is taken in closed form...
% Additional factor 2*pi is due to normalization!

AF = sin((beta_n*2*pi*N.*d)/2) ./ ...
    (N.*sin((beta_n*2*pi*d)/2)); %normalized array factor of array 
AF(abs(AF)>1)=1; % removing numerical glitches
AF(abs(AF)<1e-8)=0; % removing numerical glitches
AF=AF/(max(AF,[],'all')); %normalization

AF_dB = 20*log10(abs(AF));

% We plot the array factors for observed cases separately to ensure
% visibility

%plotting case without aliasing
figure(1);
plot(beta_n, AF_dB (:,1));
axis([min(beta_n) max(beta_n) -30 5]);
x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized array factor in spectral domain');
legend ('d=0.5 \lambda - no aliasing');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

% plotting case with aliasing but not "strong" enough to bring grating lobe
figure(2);
plot(beta_n, AF_dB(:,2));
axis([min(beta_n) max(beta_n) -30 5]);
x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized array factor in spectral domain');
legend ('d=0.75 \lambda - aliasing but no grating lobe in visible region');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

% plotting case with aliasing and grating lobe in visible region
figure(3);
plot(beta_n, AF_dB (:,3));
axis([min(beta_n) max(beta_n) -30 5]);
x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized array factor in spectral domain');
legend ('d=1.5 \lambda - aliasing; grating lobes in visible region');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

% Polar plot of visible region in \theta plane (i.e. in angular domain)

%Extracting the visible region for generation of polar plot
beta_v=beta_n (find(beta_n==-1)):0.005:beta_n(find(beta_n==1)); 
nn=size(beta_v,2);
for k=1:nn
    AF_v(k,:)=AF_dB(find(beta_n==-1)+k-1,:);
           
end;
theta=acos(beta_v); %Transformation from spectral to angular domain

% Now we plot array factor in polar graph - again separately for each case

%plotting case without aliasing
figure (4);
pa=polaraxes ('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Top','ThetaLim',[0 180]);
hold on;
p4=polarplot (theta,AF_v(:,1));
title('Normalized array factor in \theta- plane');
legend ('d=0.5 \lambda - no aliasing');
rticks([-30 -20 -10 0])
rticklabels({'-30 dB', '-20 dB','-10 dB','0 dB'});

% plotting case with aliasing but not "strong" enough to bring grating lobe
figure (5);
pa=polaraxes ('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Top','ThetaLim',[0 180]);
hold on;
p4=polarplot (theta,AF_v(:,2));
title('Normalized array factor in \theta- plane');
legend ('d=0.75 \lambda - aliasing but no grating lobe in visible region');
rticks([-30 -20 -10 0])
rticklabels({'-30 dB', '-20 dB','-10 dB','0 dB'});

% plotting case with aliasing and grating lobe in visible region
figure (6);
pa=polaraxes ('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Top','ThetaLim',[0 180]);
hold on;
p4=polarplot (theta,AF_v(:,3));
title('Normalized array factor in \theta- plane');
legend ('d=1.5 \lambda - aliasing; grating lobes in visible region');
rticks([-30 -20 -10 0])
rticklabels({'-30 dB', '-20 dB','-10 dB','0 dB'});
