% ***************************************
%        Basic Modulations example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example of QAM4 modulation
%

close all
clear all

M = 4; % QAM 4 modulation
b = round(rand(1,1024)); % input bitstream

% ==========================================================
% Parameters
% ==========================================================
f0=10; % Carrier frequency [Hz]
TSimbola=0.3; % Symbol duration [s]
fSample=1000; % Sampling frequency
tSample=1/fSample; % Sampling period
Ns=round(TSimbola/tSample); % Number of samples per one symbol

BBS=log2(M); % Number of bits per one symbol
b=b(:);
L=length(b); % Number of bits to be transmitted
% Symbol forming
Sb=reshape(b,BBS,L/BBS); % Every column one symbol
Ss=2.^(BBS-1:-1:0)*Sb;

% ==========================================================
% Mapping symbols to constellation
% ==========================================================
Constellation=[1+1i, -1+1i, 1-1i, -1-1i]; %Definition of symbol map
Ac=Constellation(Ss+1); %Searching map 

figure;
plot(real(Ac),imag(Ac),'.');
axis([-1.2 1.2 -1.2 1.2]);
axis square
title('Constellation');
xlabel('Real');
ylabel('Imag');

% ==========================================================
% Modulation
% ==========================================================
t=(0:Ns-1)*tSample;
uQAM=[];
for ks=1:length(Ac)
Signal_ks=real(Ac(ks)*exp(-1i*2*pi*f0*t)); % Multiply with complex carrier
uQAM=[uQAM,Signal_ks];
end

figure;
plot(uQAM); %Zoom in to see the waveform
title(['uQAM, ',num2str(Ns),' samples per symbol']);
xlabel('Sample');
ylabel('Amplitude');


% ==========================================================
% Spectrum 
% ==========================================================

figure;
spectrum01(uQAM(1:300),fSample);
title('Symbol spectrum');

figure;
spectrum01(uQAM,fSample);
title('Signal spectrum');
