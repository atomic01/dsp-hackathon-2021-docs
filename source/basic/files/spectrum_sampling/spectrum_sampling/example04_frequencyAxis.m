% ***************************************
%     Discrete frequency axis example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example
%

% Here we present how the frequency of a continuous signal maps
% to its discrete signal counterpart on the [-pi,pi> frequency axis.


%% Generate a sine signal with some noise 

fs=1.024e3; % Sampling frequency
N=1024; % Number of samples of sine signal
f0=32; % Signal frequency

% Time axis, normalized to fs
t=(0:N-1)/fs; 

% Signal
x=cos(2*pi*f0*t);

snr=15;
x=awgn(x,snr);

%% Calculate spectrum
Nfft=256;

% Spacing between each FFT bin
deltaf=fs/Nfft;

% Frequency axis
f=linspace(-fs/2,fs/2-deltaf,Nfft);

% FFT
X=fftshift(fft(x,Nfft));

%% Plots

% Time domain
figure;
stem(t,x);
xlabel('Time [s]');
ylabel('Amplitude');
title('Time domain');

% Amplitude spectrum
figure;
plot(f,20*log10(abs(X)));
ylabel('|X| [dB]');
xlabel('f [Hz]');
title('Amplitude spectrum');

%% Discussion
% The second figure shows the amplitude spectrum of a sine signal.
% The signal was generated with central frequency of 32. (We interpret
% the time scale as being in seconds, so we say the frequency is in
% units of Hertz.)
% After discretization in 1024 points, with a sampling frequency fs, we
% obtain a discrete signal for which we observe the frequency axis in
% interval [-pi, pi>. However, knowing the sampling frequency, this axis
% can be interpreted as [-fs/2,fs/2>, which we then used when plotting
% the spectrum.
