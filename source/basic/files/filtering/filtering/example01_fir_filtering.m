% ***************************************
%         Basic filtering example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Example of basic filtering;
% Extracting 3 frequency components out of a discretes dignal

close all
clear all

N = 1000; % number of samples
n = 1:1000; % samples of a discretised signal 

fs = 1000; % [Hz] sampling frequency
f1 = 10; % [Hz] (digital frequency 0.01)
f2 = 100; % [Hz] (digital frequency 0.1)
f3 = 200; % [Hz] (digital frequency 0.2)

x1 = sin(2*pi*f1/fs*n);
x2 = sin(2*pi*f2/fs*n);
x3 = sin(2*pi*f3/fs*n);

x = x1 + x2 + x3; % creating the signal 

figure;
plot(x);
title('Original signal');
figure;
spectrum01(x,1); % Spectrum of dicrete signals is periodical with period 1 
title('Original signal spectrum');


%% LOW-PASS 

% Designing the low-pass filter
freq1 = [0 0.05 0.15 1];
amp1 = [1 1 0 0];
f1 = firpm(100,freq1,amp1);

figure;
spectrum01(x,1);
hold on
spectrum01(f1,1); 
title('Frequency response of low-pass filter');

% Filtering by convolution
y1 = conv(x,f1);

figure;
plot(x1);
hold on 
plot(y1);
title('Extracted low-pass component of the signal');


%% BAND-PASS

%Designing the bandpass filter
freq2 = [0 0.1 0.2 0.3 0.4 1];
amp2 = [0 0 1 1 0 0];
f2 = firpm(100,freq2,amp2);

figure;
spectrum01(x,1);
hold on
spectrum01(f2,1);
title('Frequency response of band-pass filter');

% Filtering by convolution
y2 = conv(x,f2);

figure;
plot(x2);
hold on 
plot(y2);
title('Extracted band-pass component');

%% HIGH-PASS
%Designing the highpass filter
freq3 = [0 0.2 0.4 1];
amp3 = [0 0 1 1];
f3 = firpm(100,freq3,amp3);

figure;
spectrum01(x,1);
hold on
spectrum01(f3,1);
title('Frequency response of high-pass filter');

% Filtering by convolution
y3 = conv(x,f3);

figure;
plot(x3);
hold on 
plot(y3);
title('Extracted high-pass component');



