from load import * 
t = time[0][0][0][0][0]
X = trial[0][0][0][0][0]

# Downsample to 250 Hz
f = signal.resample(X, 250) #fs = 500 / 2

newt = t[::2]
newt = newt[0: len(f)] 
plt.title('Resampled Elecs of first trial')
plt.xlabel('Time')
plt.ylabel('Electrode')
plt.grid(True)
plt.plot(t, X, 'b', newt, f, 'or-')
plt.legend(['data', 'resampled'], loc='best')
plt.show()
