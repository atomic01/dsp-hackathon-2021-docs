% ***************************************
% Multibeam generation and analysis
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Want to radiate multiple beams? No problem. Due to linearity one can at
% the same time apply multiple current distributions with different linear
% phases giving rise to different beams at the same time (it is good to have
% a large enough array to have enough spatial resolution and to remain 
% within Nyquist criterion). 

% Note that this multibeam does not arise from aliasing but from the design
% of proper current distributions...

% This example shows how to generate beams at 60 and 120 degrees.The array
% factor and required current magnitudes are calculated and plotted.


clear all;

beta_n =[(-3:0.005:3)]'; % normalized wavenumber space (beta_z/beta = cos(theta))

%Setting the array parameters (we choose 10 \lambda array)

d=0.5; %normalized distance in wavelength
N=20; %Number of antenna elements
L=N*d; %total array length

% Setting desired angles of multiple beams
theta_0=[120 60]; 
%Calculating required linear phase shifts(normalized to beta)
alpha_n=-cos(deg2rad(theta_0)); 
psi_n=beta_n*d+alpha_n*d; %auxiliary angles for array factor calculations

% The calculated array factor is the sum of the array factors arising from
% each current distribution ...
AF=zeros(size(psi_n)); %initialization of array factor

% Summing contributions from each (uniform) current distribution
for m=1:size((psi_n),2)
AF = AF+sin((psi_n(:,m)*2*pi*N)/2) ./ ...
    (N.*sin((psi_n(:,m)*2*pi)/2)); %normalized array factor of array (factor 2*pi is due to normalization!)
end;
% AF=AF/max(AF); % normalization
AF_dB = 20*log10(abs(AF));

% Plotting array factor in spectral (beta_z) domain

figure(1);
p1=plot(beta_n, AF_dB);
axis([min(beta_n) max(beta_n) -30 5]);

x1=xline (1,'r--','Visible region boundary');
x2=xline (-1,'r--','Visible region boundary');
set(x1,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x2,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Multibeam array - spectral domain');
legend ('Beams at cos \theta=+-1/2');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');

% Plotting array factor for visible region in angular domain ...

% Extracting the visible region
beta_v=beta_n (find(beta_n==-1)):0.005:beta_n(find(beta_n==1)); 
nn=size(beta_v,2);
for k=1:nn
    AF_v(k,:)=AF_dB(find(beta_n==-1)+k-1,:);
           
end;
theta=acos(beta_v);

% Now we plot the array factor in \theta plane
figure (2);
pa=polaraxes ('RLim',[-30 0],'thetadir','Clockwise','thetazerolocation','Top','ThetaLim',[0 180]);
hold on;
p2=polarplot (theta,AF_v);
title('Multibeam array - angular (\theta) domain');
legend ('Beams at angles \theta of 60 and 120 deg.');
rticks([-30 -20 -10 0])
rticklabels({'-30 dB', '-20 dB','-10 dB','0 dB'});

% Calculation of current distribution at each antenna
% We need to sum contributions from each beam (total current is not uniform
% anymore)

I=zeros(N,1); %initialization of currents
M=size((alpha_n),2); %number of current distributions

% Summation...
for k=1:N
    for m=1:M
 I(k)= I(k)+exp(i*(k-1)*d*alpha_n(m));
    end;
end;

% Plotting current distributions (magnitude and phase) at each antenna...
figure(3);
subplot(2,1,1);
p3=stem ((abs(I/max(I))));
title('Beam indices - magnitudes');
xlabel('Antenna element number');
ylabel('Normalized current magnitude');
set(p3,'Linewidth',1);
grid on;

subplot(2,1,2);
p3=stem (rad2deg(angle(I)));
title('Beam indices - phases');
xlabel('Antenna element number');
ylabel('Current phase [degrees]');
grid on;
set(p3,'Linewidth',1);

