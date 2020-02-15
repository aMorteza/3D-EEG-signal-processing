from load import * 

t = time[0][0][0][0][0]
n = np.arange(0, len(t), 1)
X = trial[0][0][0][0][0]

def highpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs #The Nyquist frequency is half the sampling rate
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)    
    return signal.filtfilt(b, a, data)

cutoff = 0.1  # Cutoff frequency as a fraction of the sampling rate    

fps = 500
filtered_X = highpass_filter(X, 200, fps)

plt.figure(figsize=(20,10))
plt.subplot(211)
plt.plot(range(len(X)), X)
plt.title('Original signal')
plt.subplot(212)
plt.plot(range(len(filtered_X)),filtered_X)
plt.title('Highpass filtered signal')
plt.show()