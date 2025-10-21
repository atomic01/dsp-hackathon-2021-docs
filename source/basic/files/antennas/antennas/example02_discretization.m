% ***************************************
%  Discretization of line source
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 

% The total length of line source
% when discretized would correspond to total array length (L=N*d). If
% discretized by Nyquist criterium, we would also see that in visible region
% the array factor corresponds to the space factor of the line source.

clear all;
close all;

% Run Example 01 first
example01_line_sources;

%% Discretizing the line source

% Number of antenna elements ("samples")
N=[4 10 20]

% d= \lambda/2 (Nyquist criterion obeyed)
d=L./N;

% The array factor is obtained as convolution of sinc function
% centred at 2*pi*n/d for some integer 'n'.

AF = sin((beta_n*2*pi*N.*d)/2) ./ ...
    (N.*sin((beta_n*2*pi*d)/2));
AF_dB = 20*log10(abs(AF));

%% Plot the array factor

figure(3);
p3=plot(beta_n, AF_dB);
axis([min(beta_n) max(beta_n) -30 5]);

% Format the figure

x3=xline(1,'r--','Visible region boundary');
x4=xline(-1,'r--','Visible region boundary');
set(x3,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
set(x4,'LineWidth',2,'LabelHorizontalAlignment','center','LabelVerticalAlignment','middle');
grid on;
title('Normalized array factor - discretized source (d=\lambda/2)');
legend ('N=4','N=10','N=20');
xlabel('\beta_z/\beta=cos(\theta)');
ylabel('Relative level [dB]');
