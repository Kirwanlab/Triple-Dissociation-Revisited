import numpy as np
import glob

directory = '../derivatives/'

derivatives_files = glob.glob(directory+'*')

for j in range(len(derivatives_files)):
	if 'sub' in derivatives_files[j]:

		behavior_file = glob.glob(derivatives_files[j]+'/'+'behavioral_summary.txt')

		if len(behavior_file) == 1:

			load_file = np.genfromtxt(behavior_file[0], unpack=True, dtype=None)

			confidence_bins = np.zeros(6)
			print(derivatives_files[j].split('/')[-1])
			for i in range(len(load_file)):
				#print(load_file[i])
				status = load_file[i][0]
				count = load_file[i][1]

				if status == 'H2' or status == 'FA2':
					confidence_bins[3] += float(count)
				elif status == 'H3' or status == 'FA3':
					confidence_bins[4] += float(count)
				elif status == 'H4' or status == 'FA4':
					confidence_bins[5] += float(count)
				elif status == 'M2' or status == 'CR2':
					confidence_bins[2] += float(count)
				elif status == 'M3' or status == 'CR3':
					confidence_bins[1] += float(count)
				elif status == 'M4' or status == 'CR4':
					confidence_bins[0] += float(count)

			print(confidence_bins)