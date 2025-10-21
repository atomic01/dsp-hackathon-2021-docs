% ***************************************
%           Default FFT example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example
%

close all;
clear all;

%% We run DTFT first
example01_dtft;

%% Find FFT

%
% NOTE
% We will now call `fft` with no additional parameters.
%
X_fft = fft(x);

% Bin axis
k = 0:length(X_fft)-1;

%% Plot the spectrum

figure(spectrumFig);

% Amplitude spectrum
subplot(2,1,1);
stem(2*pi*k/length(k), abs(X_fft), 'r');

% Phase spectrum
subplot(2,1,2);
stem(2*pi*k/length(k), angle(X_fft), 'r');
