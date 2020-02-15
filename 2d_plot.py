from load import * 

t = time[0][0][0][0][0]
Z = trial[0][0][0][0][0]

fig = plt.figure()
plt.title('Electrodes of first trial')
plt.xlabel('Time')
plt.ylabel('Electrode')
plt.grid(True)
plt.plot(t, Z, 'b')
plt.show()