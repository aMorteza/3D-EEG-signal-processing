from load import * 

t = time[0][0][0][0][0]
n = np.arange(0, len(t), 1)
X = trial[0][0][0][0][0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(t, n, X, zdir='z', c= 'blue')
plt.title('Electrodes frist trial')
plt.xlabel('Time')
plt.ylabel('Electrode')
plt.grid(True)
plt.show()