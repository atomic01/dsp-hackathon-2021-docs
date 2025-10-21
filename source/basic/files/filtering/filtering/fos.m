%Calculates the frequency axis for the spectral samples obtained by FFT
function [ f ] = fos( N, fs )
narginchk(2,2); %Check the size of parameters

if (N <= 0)
   error('Number of samples must be a positive number greater than 0');
end

if (fs <= 0)
    error('Number of samples must be a positive number greater than 0');
end

deltaf = fs/N;

if mod(N,2)==0  % even N
    f = linspace(-fs/2,fs/2-deltaf, N);
else % odd N
    f = linspace(-(fs-deltaf)/2,(fs-deltaf)/2,N);
end

end

