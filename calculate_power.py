from load import * 
import seaborn as sns
from scipy.integrate import simps

def signal_power(data, sf, shift = 0):
	# Define window length
	win = sf + shift
	freqs, psd = signal.welch(X, sf, nperseg=win)

	# Plot the power spectrum
	# sns.set(font_scale=1.2, style='white')
	# plt.plot(freqs, psd, color='k', lw=2)
	# plt.xlabel('Frequency (Hz)')
	# plt.ylabel('Power spectral density (V^2 / Hz)')
	# plt.ylim([0, psd.max() * 1.1])
	# plt.title("Welch's periodogram")
	# plt.xlim([0, freqs.max()])
	# sns.despine()
	# plt.show()

	low, high = 0.5 , 20
	# Find intersecting values in frequency vector
	idx_delta = np.logical_and(freqs >= low, freqs <= high)

	# Frequency resolution
	freq_res = freqs[1] - freqs[0]  # = 1 / 3 = 0.33

	# Compute the absolute power by approximating the area under the curve
	delta_power = simps(psd[idx_delta], dx=freq_res)
	return delta_power


sf = 125  #samplig freq
shift = 0 # window move
for electrode_idx in range(0, 12):
	window_mean_power_dict = dict()
	print("Electrode:", electrode_idx + 1)
	for trial_idx in range(0, 192):
		print("----------------------------------")
		X = trial[0][0][0][trial_idx][electrode_idx]
		print("trial:", trial_idx + 1)
		for shift in range(0, len(X), sf):
			power = signal_power(X, sf, shift)
			window = sf + shift
			print("Window:", window,"Hz  Absolute delta power: %.3f uV^2" % power)
			if window not in window_mean_power_dict:
				window_mean_power_dict[window] = power 
			window_mean_power_dict[window] = (power + window_mean_power_dict[window]) / 2.0
	print("Electode ", electrode_idx + 1, "Windows Mean power:")
	for key, value in window_mean_power_dict.items():
		print("Window:", key, "Hz : %.3f" % float(value), "uV^2")			
	print("#################################################################################################")



