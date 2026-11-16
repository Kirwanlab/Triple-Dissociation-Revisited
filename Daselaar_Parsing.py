#python for test file
import numpy as np
import glob

csv_files = glob.glob('test.csv')

with open('Data_file_all.txt', "w") as f:
	for sub_file in csv_files:

		subj = sub_file.split('_')[0]

		subject_file = np.genfromtxt(sub_file, delimiter = ',', unpack = True, dtype =None)

		run1_stim = subject_file[0][4:64]
		run2_stim = subject_file[0][65:125]
		run3_stim = subject_file[0][126:186]
		run4_stim = subject_file[0][187:247]

		run1_corans = subject_file[1][4:64]
		run2_corans = subject_file[1][65:125]
		run3_corans = subject_file[1][126:186]
		run4_corans = subject_file[1][187:247]

		run1_response = subject_file[43][4:64]
		run2_response = subject_file[43][65:125]
		run3_response = subject_file[43][126:186]
		run4_response = subject_file[43][187:247]

		run1_status = subject_file[44][4:64]
		run2_status = subject_file[44][65:125]
		run3_status = subject_file[44][126:186]
		run4_status = subject_file[44][187:247]

		run1_onset_t = subject_file[48][4:64]
		run2_onset_t = subject_file[48][65:125]
		run3_onset_t = subject_file[48][126:186]
		run4_onset_t = subject_file[48][187:247]

		run1_response_t = subject_file[45][4:64]
		run2_response_t = subject_file[45][65:125]
		run3_response_t = subject_file[45][126:186]
		run4_response_t = subject_file[45][187:247]

		run1_confidence = subject_file[52][4:64]
		run2_confidence = subject_file[52][65:125]
		run3_confidence = subject_file[52][126:186]
		run4_confidence = subject_file[52][187:247]

		run1_con_onset_t = subject_file[54][4:64]
		run2_con_onset_t = subject_file[54][65:125]
		run3_con_onset_t = subject_file[54][126:186]
		run4_con_onset_t = subject_file[54][187:247]

		run1_con_response_t = subject_file[62][4:64]
		run2_con_response_t = subject_file[62][65:125]
		run3_con_response_t = subject_file[62][126:186]
		run4_con_response_t = subject_file[62][187:247]


		f.write('{0:^130}\n'.format('Subject_' + subj))
		#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
		header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
		f.write(header_line)

		for i in range(len(run1_stim)):
			write_status = None
			try:
				if int(run1_response[i]) == 1:
					if int(run1_corans[i]) == 1:
						write_status = 'HIT'
					else: write_status = 'FA'
				elif int(run1_response[i]) == 2:
					if int(run1_corans[i]) == 1:
						write_status = 'CR'
					else: write_status = 'MISS'
			except: write_status = 'None'
			write_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('1', run1_stim[i], run1_corans[i], run1_response[i], run1_status[i], write_status, run1_onset_t[i], run1_response_t[i], run1_confidence[i] ,run1_con_onset_t[i], run1_con_response_t[i])
			f.write(write_line)

		for i in range(len(run2_stim)):
			write_status = None
			try:
				if int(run2_response[i]) == 1:
					if int(run2_corans[i]) == 1:
						write_status = 'HIT'
					else: write_status = 'FA'
				elif int(run2_response[i]) == 2:
					if int(run2_corans[i]) == 1:
						write_status = 'CR'
					else: write_status = 'MISS'
			except: write_status = 'None'
			write_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('2', run2_stim[i], run2_corans[i], run2_response[i], run2_status[i], write_status, run2_onset_t[i], run2_response_t[i], run2_confidence[i] ,run2_con_onset_t[i], run2_con_response_t[i])
			f.write(write_line)

		for i in range(len(run3_stim)):
			write_status = None
			try:
				if int(run3_response[i]) == 1:
					if int(run3_corans[i]) == 1:
						write_status = 'HIT'
					else: write_status = 'FA'
				elif int(run3_response[i]) == 2:
					if int(run3_corans[i]) == 1:
						write_status = 'CR'
					else: write_status = 'MISS'
			except: write_status = 'None'
			write_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('3', run3_stim[i], run3_corans[i], run3_response[i], run3_status[i], write_status, run3_onset_t[i], run3_response_t[i], run3_confidence[i] ,run3_con_onset_t[i], run3_con_response_t[i])
			f.write(write_line)

		for i in range(len(run4_stim)):
			write_status = None
			try:
				if int(run4_response[i]) == 1:
					if int(run4_corans[i]) == 1:
						write_status = 'HIT'
					else: write_status = 'FA'
				elif int(run4_response[i]) == 2:
					if int(run4_corans[i]) == 1:
						write_status = 'CR'
					else: write_status = 'MISS'
			except: write_status = 'None'
			write_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('4', run4_stim[i], run4_corans[i], run4_response[i], run4_status[i], write_status, run4_onset_t[i], run4_response_t[i], run4_confidence[i] ,run4_con_onset_t[i], run4_con_response_t[i])
			f.write(write_line)

		f.write('\n')






# response:
# 1 - old
# 2 - new

# 1 - 1 = HIT
# 1 - 2 = FA
# 2 - 1 = CR
# 2 - 2 = MISS

# for i in range(len(run1_response)):
# 	if int(run1_response[i]) == 1:
# 		if int(run1_corans[i]) == 1:
# 			print(run1_response[i], run1_corans[i], 'HIT')
# 		else: print(run1_response[i], run1_corans[i], 'FA')
# 	if int(run1_response[i]) == 2:
# 		if int(run1_corans[i]) == 1:
# 			print(run1_response[i], run1_corans[i], 'CR')
# 		else: print(run1_response[i], run1_corans[i], 'MISS')



