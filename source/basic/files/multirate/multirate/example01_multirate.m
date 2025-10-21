% ***************************************
%           Multirate example
% ***************************************
% Ericsson Nikola Tesla
% DSP Hackaton 2021
% 

close all
clear all

%% Downsampling - aliasing

%create band-limited input signal
f = [0 0.2500 0.5000 0.7500 1.0000];
a = [1.00 0.6667 0.3333 0 0];

nf = 512;
b1 = fir2(nf-1,f,a);
Hx = fftshift(freqz(b1,1,nf,'whole'));

%plot spectrum of input signal
omega = -pi:2*pi/nf:pi-2*pi/nf;
figure
plot(omega/pi,abs(Hx))
grid
xlabel('\times\pi rad/sample')
ylabel('Magnitude')

%Generate decimated signal
y = downsample(b1,2,0);
Hy = fftshift(freqz(y,1,nf,'whole'));

%Plot spectrum of decimated signal (aliasing appears)
hold on
plot(omega/pi,abs(Hy))
hold off
legend('Original','Downsampled')
text(2.5/pi*[-1 1],0.35*[1 1],{'\downarrow Aliasing','Aliasing \downarrow'}, ...
    'HorizontalAlignment','center')

%% Downsampling - decimate

f1 = 1; % frequency of first component in signal
f2 = 2; % frequency of second component in signal
R = 4; % decimation factor 
fs1=50; % sampling frequency of input signal
fs2=fs1/R; % sampling frequency of decimated signal
Nx=50; % number of discrete time points 
nx=0:Nx-1;

x=sin(2*pi*f1/fs1*nx)+sin(2*pi*f2/fs1*nx);
y=decimate(x,R);
ny=0:length(y)-1;

% spectrum of input and decimated signal
Nfft=256;
fk1=fos(Nfft, fs1);
X=fftshift(fft(x, Nfft));
fk2=fos(Nfft, fs2);
Y=fftshift(fft(y, Nfft));

figure;
subplot(2,2,1);
stem(nx,x,'b');
xlabel('n');
ylabel('x[n]');
title(['f_1=',num2str(f1),', f_2=',num2str(f2),...
', f_s_1=',num2str(fs1)]);

subplot(2,2,3);
stem(ny,y,'r'); shg;
xlabel('n');
ylabel('y[n]');
title(['f_1=',num2str(f1),', f_2=',num2str(f2),...
', R=',num2str(R), ' fs2=', fs2]);

subplot(2,2,2);
plot(fk1,20*log10(abs(X)/max(abs(X))),'b'); shg;
xlabel('f[Hz]');
ylabel('Amplitude[dB]');
title('Amplitude spectrum - input signal');
axis([-fs1/2 fs1/2 -50 0]);

subplot(2,2,4);
plot(fk2,20*log10(abs(Y)/max(abs(Y))),'r'); shg;
xlabel('f[Hz]');
ylabel('Amplitude[dB]');
title('Amplitude spectrum - decimated signal');
axis([-fs2/2 fs2/2 -50 0]);

%% Upsampling - aliasing

f = [0 0.250 0.500 0.7500 1];
a = [1.0000 0.5000 0 0 0];

nf = 512;
b = fir2(nf-1,f,a);
Hx = fftshift(freqz(b,1,nf,'whole'));

omega = -pi:2*pi/nf:pi-2*pi/nf;

figure
plot(omega/pi,abs(Hx))
grid
xlabel('\times\pi rad/sample')
ylabel('Magnitude')

y = upsample(b,2);
Hy = fftshift(freqz(y,1,nf,'whole'));

hold on
plot(omega/pi,abs(Hy))
hold off
legend('Original','Upsampled')
text(0.65*[-1 1],0.45*[1 1],{'\leftarrow Imaging','Imaging \rightarrow'}, ...
    'HorizontalAlignment','center')

%% Upsampling - interpolating with zeros

N=40; % samples number 
L=3; % interpolation factor
fs1=10; %sampling frequency input signal
fs2=L*fs1; %sampling frequency interpolated signal

f0=3; % input signal frequency 
t=(0:N-1)/fs1;

%input signal
x=cos(2*pi*f0*t);

%interpolated signal
y=upsample(x,L); % does interpolation with L zeros between each sample

% spectrum of input and interpolated signal
Nfft=256;
fk1=fos(Nfft, fs1);
X=fftshift(fft(x, Nfft));
fk2=fos(Nfft, fs2);
Y=fftshift(fft(y, Nfft));

figure;
subplot(2,2,1);
stem(x, 'b');
title('Input signal');
xlabel('n');
subplot(2,2,3);
% figure;
stem(y,'r');
title(['Zero-interpolated signal, L= ', num2str(L)]);
xlabel('n');
subplot(2,2,2);
plot(fk1,20*log10(abs(X)/max(abs(X))),'b'); shg;
xlabel('f[Hz]');
ylabel('Amplitude[dB]');
title('Amplitude spectrum - input signal');
axis([-fs1/2 fs1/2 -50 0]);
subplot(2,2,4);
plot(fk2,20*log10(abs(Y)/max(abs(Y))),'r'); shg;
xlabel('f[Hz]');
ylabel('Amplitude[dB]');
title(['Amplitude spectrum - interpolated signal, L= ', num2str(L)]);
axis([-fs2/2 fs2/2 -50 0]);