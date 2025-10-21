% ***************************************
%           Zero-padding example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example
%

close all;
clear all;

%% We run FFT first
example02_fft;

%% Discussion
% At this point, it is evident that the DFT (found by using the FFT
% algorithm, samples the continous spectrum found by FFT.
%
% An important assumption we've made to achieve this is that the
% analyzed signal is now constrained (and periodic) in time domain.
%
% For DTFT, the signal was defined only on samples n=1:10. For all other
% samples n=-infty:infty, we had to assume a zero value.
%
% Let's put this claim to the test.

%% Zero-pad the signal

x_zp = [x zeros(1,10)];

% Sample axis
n_zp = 1:20;

%% Plot the signal

figure(timeFig);

stem(n_zp, x_zp, 'g');

% Reorder plots so we see the original signal
set(gca, 'Children', flipud(get(gca, 'Children')));

%% Find FFT

X_zp = fft(x_zp);

% Bin axis
k = 0:length(X_zp)-1;

%% Plot the spectrum

figure(spectrumFig);

% Amplitude spectrum
subplot(2,1,1);
stem(2*pi*k/length(k), abs(X_zp), 'g');

% Reorder plots so we see the original spectrum
set(gca, 'Children', flipud(get(gca, 'Children')));

% Phase spectrum
subplot(2,1,2);
stem(2*pi*k/length(k), angle(X_zp), 'g');

% Reorder plots so we see the original spectrum
set(gca, 'Children', flipud(get(gca, 'Children')));
