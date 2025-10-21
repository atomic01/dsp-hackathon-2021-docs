% ***************************************
%           Mixing example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example of real and complex mixer in digital domain (NCO)
%

close all
clear all

% 1. Generate input cosine signal with little bit of noise and plot the amplitude spectrum

fs=1.024e3; % sampling frequency
N=1024; %number of samples of sine signal
t=(0:N-1)/fs;
f0=32; % signal frequency

% signal
x=cos(2*pi*f0*t);
snr=15;
x=awgn(x,snr);
% spectrum
Nfft=256;
deltaf=fs/Nfft;
f=linspace(-fs/2,fs/2-deltaf,Nfft); %frequency axis in FFT
X=fftshift(fft(x,Nfft));

figure
stem(t,x)
xlabel('time[s]');
ylabel('Amplitude');
title('Input signal');

figure
plot(f,20*log10(abs(X)));
ylabel('dB');
xlabel('f[Hz]');
title('Amplitude spectrum - input signal');

% 2. Do the frequency upconversion with real mixer, fNCO=128Hz
fNCO=128;
xNCO=cos(2*pi*fNCO*t);
xout1=xNCO.*x;
Xout1=fftshift(fft(xout1,Nfft));

figure
plot(f,20*log10(abs(Xout1)));
ylabel('dB');
xlabel('f[Hz]');
title('Amplitude spectrum -  real mixer upconversion');

% with real mixer, 4 spectral components will appear after the upconversion
% a) fNCO+f0 ->  this one we usually need for further processing
% b) fNCO-f0
% c) -fNCO-f0
% d) -fNCO+f0

% 3. Do the frequency upconversion with complex mixer, fNCO=128 Hz
fNCO=128;
xNCO=exp(1i*2*pi*fNCO*t);
xout2=xNCO.*x;
Xout2=fftshift(fft(xout2,Nfft));

figure
plot(f,20*log10(abs(Xout2)));
ylabel('dB');
xlabel('f[Hz]');
title('Amplitude spectrum - complex mixer upconversion');

% with complex mixer, 2 spectral components will appear after the upconversion
% a) fNCO+f0 ->  this one we usually need for further processing
% b) fNCO-f0

% 4. Do the frequency downpconversion with complex mixer, fNCO=-256 Hz
fNCO=-256;
xNCO=exp(1i*2*pi*fNCO*t);
xout3=xNCO.*x;
Xout3=fftshift(fft(xout3,Nfft));

figure
plot(f,20*log10(abs(Xout3)));
ylabel('dB');
xlabel('f[Hz]');
title('Amplitude spectrum - complex mixer downconversion');

% with complex mixer, 2 spectral components will appear after the downconversion
% a) fNCO+f0 ->  this one we usually need for further processing
% b) fNCO-f0
