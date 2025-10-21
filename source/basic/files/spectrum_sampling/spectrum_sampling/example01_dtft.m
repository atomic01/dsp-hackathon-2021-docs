% ***************************************
%           DTFT example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example
%

close all;
clear all;

%% Signal generation

% We produce a signal with multiple frequency components
% x(n) = [ series of 10 random integers elem {0..10} ]
%
x = randi(11,1,10)-1;

% Sample axis
n = 1:10;

%% Plot the signal

timeFig = figure;

stem(n,x);

xlabel("n");
ylabel("x(n)");
grid on;
hold on;

%% DTFT

% Frequency axis
w = 0:0.05:2*pi;

%
% NOTE
% The DTFT function `freqz` can only output a sampled spectrum. However,
% we are using a frequency axis which is quite dense. For this purpose,
% we can consider the ouptut of `freqz` as continuous.
%
X_dtft = freqz(x,1,w);

%% Plot the spectrum

spectrumFig = figure;

% Amplitude spectrum
subplot(2,1,1);
plot(w, abs(X_dtft), 'b');

% Formatting the plot
xlim([0 2*pi]);
xticks([0:pi/2:2*pi]);
xticklabels({0;"\pi/2";"\pi";"3\pi/2";"2\pi"});
xlabel("\Omega");
ylabel("|X(\Omega)|");
grid on;
hold on;

% Phase spectrum
subplot(2,1,2);
plot(w, angle(X_dtft), 'b');

% Formatting the plot
xlim([0 2*pi]);
xticks([0:pi/2:2*pi]);
xticklabels({0;"\pi/2";"\pi";"3\pi/2";"2\pi"});
xlabel("\Omega");
ylim([-pi pi]);
yticks([-pi:pi/2:pi]);
yticklabels({"-\pi";"-\pi/2";0;"\pi/2";"\pi"});
ylabel("\angle X(\Omega)");
grid on;
hold on;
