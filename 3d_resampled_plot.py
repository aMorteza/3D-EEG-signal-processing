from load import * 

t = time[0][0][0][0][0]
n = np.arange(0, len(t), 1)
X = trial[0][0][0][0][0]

# Downsample to 250 Hz
f = signal.resample(X, 250) #fs = 500 / 2 

newt = t[::2]
newt = newt[0: len(f)] 
newn = np.arange(0, len(newt), 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(t, n, X, zdir='z', c= 'blue')
ax.scatter(newt, newn, f, zdir='z', c= 'red')
plt.title('Electrodes frist trial')
plt.xlabel('Time')
plt.ylabel('Electrode')
plt.legend(['data', 'resampled'], loc='best')
plt.grid(True)
plt.show()