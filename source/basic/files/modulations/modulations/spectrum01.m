%Calculates the spectrum of input signal by performing FFT
%Specify 1 as fs to plot a spectrum of digital signal

function [X,f] = spectrum01(x,fs)
   N=length(x);

   Nfft=10*N;
   %p = blackman(N)';
   p = ones(size(x));
   X=fftshift(fft(x.*p,Nfft));
   X=X/N;
   X=X/max(abs(X));
   f=fos(Nfft,fs);
   X=20*log10(abs(X));
   plot(f,X);
   ylabel('Spectrum [dB/(\Delta Hz)]');
   xlabel('Frequency[Hz]');
   ylim([-100 0]);
end

