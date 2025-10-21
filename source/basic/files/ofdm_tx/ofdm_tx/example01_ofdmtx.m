% ***************************************
%           OFDM tx example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 
% Basic level example for OFDM tx simbol generation
%

close all 
clear all

%% 0. Message (bitstream) creation 

% in this example, we will use OAM-16 modulation for coding the subcarriers
% in OFDM simbol
% note difference between "simbol" and "OFDM simbol"
% simbol is part of tx message, in this case carrying 4 bit length information (possible values 0-15)
% Each simbol is coded into amplitude and phase of specific OFDM subcarrier
% Together specific number of OFDM subcarriers make OFDM simbol 

simbolsTx=[...
     8,     9,    12,    12,     3,     2,     9,     8,    13      8,     4,     8,     4,     2,     0,    11,     9,     8,     3,     7,     3,     7,    11, ...
     0,    10,    12,    15,     0,    14,    14,     3,    15,     8,     3,     3,     7,    15,     2,     2,     0,    10,     2,     3,     4,     3,     9, ...
     2,     4,     7,     0,     8,     6,     8,    10,     1,    12,     1,     1,    15,     9,     5,    15,     6,     4,    13,     9,     0,    13,     0, ...
    12,     0,     8,     6,     4,     8,     7,    14,     0,     5,     3,     3,     3,     1,     5,     9,     3,     7,     4,    14,    13,     1,     6, ...
    14,     1,    14,    14,     4,     0,    15,     9,     4,     9,     8,     4,     8,    13,    15,    13,     0,     3,    15,     7,     4,     9,    14, ...
     6,     7,     0,    15,    14,     7,     0,     9,     6,    11,    10,     1,     6,     0,     2,    12,     2,     7,     5,     5,     7,    15,    11, ...
    15,     2,     0,    11,     3,     5,     4,     6,    13,     3,     2,    13,    10,     3,    10,     0,    11,    15,    11,    15,    12,     3,     0, ...
     8];

%% 1. OFDM parameters  

% total 256 OFDM bins
Nfft=256; % total number of OFDM sub-carriers 
Ng=Nfft/4; % length of guard interval
fs=30.72e6; %sampling frequency of the system 

%frequency axis of the OFDM simbol
f=fos(Nfft, fs);

activeSubcarriersPos=[-103:103];
% pilots
pilotSubcarriersPos=[(-103:5:0), 3:5:103];
pilotAmplitude=1;
pilotPhase=0;
% DC subcarriers - not used 
subCarriersAroundDcPos=[-1:1];

%position of data subcarriers are the rest of active subcarrier positions, that are not pilot or DC positions
dataSubcarriersPos=activeSubcarriersPos(~or(ismember(activeSubcarriersPos,pilotSubcarriersPos),ismember(activeSubcarriersPos,subCarriersAroundDcPos)));

%% 2. Simbols mapping 

constellation = ...
[ 1+1*i,  ... % 0='0000'
  1+3*i,  ... % 1='0001'
  3+1*i,  ... % 2='0010'
  3+3*i,  ... % 3='0011'
  1-1*i,  ... % 4='0100'
  1-3*i,  ... % 5='0101'
  3-1*i,  ... % 6='0110'
  3-3*i,  ... % 7='0111'
  -1+1*i, ... % 8='1000'
  -1+3*i, ... % 9='1001'
  -3+1*i, ... %10='1010'
  -3+3*i, ... %11='1011'
  -1-1*i, ... %12='1100'
  -1-3*i, ... %13='1101'
  -3-1*i, ... %14='1110'
  -3-3*i, ... %15='1111'
  ];

Aph_dataSubcarriers=constellation(simbolsTx+1);

%% 3. Create OFDM simbol

OFDMsimbol_f=zeros(1,Nfft);
indexOffset=Nfft/2+1;

% first place pilot subcarriers
OFDMsimbol_f(pilotSubcarriersPos+indexOffset)=pilotAmplitude*exp(1i*pilotPhase);

%then place data subcarriers
OFDMsimbol_f(dataSubcarriersPos+indexOffset)=Aph_dataSubcarriers;

% Plot amplitude and phase spectrum of OFDM simbol
figure
subplot(2,1,1);
stem(f/10^6, abs(OFDMsimbol_f));
title('OFDM simbol - amplitude spectrum');
xlabel('f [MHz]');
ylabel('Amplitude');
subplot(2,1,2);
stem(f/10^6, angle(OFDMsimbol_f)*180/pi);
title('OFDM simbol - phase spectrum');
xlabel('f [MHz]');
ylabel('Phase [deg]');

%% 4. Perform IFFT modulation and add Cylcic prefix 
OFDMsimbol_t=ifft(ifftshift(OFDMsimbol_f));

% add cyclic prefix 
OFDMsimbol_t=[OFDMsimbol_t(end-Ng+1:end) OFDMsimbol_t]; 

It=real(OFDMsimbol_t); % in-phase component sent in time domain
Qt=imag(OFDMsimbol_t); % quadrature-phase component sent in time domain

t=(0:length(It)-1)/fs; 
figure
subplot(2,1,1);
plot(t*10^6, It);
title('OFDM in-phase component I(t)');
xlabel('t[\mus]');
ylabel('Amplitude [db]');
subplot(2,1,2);
plot(t*10^6, Qt);
title('OFDM quad-phase component Q(t)');
xlabel('t[\mus]');
ylabel('Phase [deg]');
