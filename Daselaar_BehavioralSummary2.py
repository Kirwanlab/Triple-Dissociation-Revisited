# create new excel file
# subject # on column 1
# use code behavioral_summary

#python for test file
import numpy as np
import glob
import subprocess

csv_files = glob.glob('../behavioraldata/*.csv')

skip = ['056']

#---ONSET TIMES TO BE PRINTED SHOULD WORD TIMINGS NOT CONFIDENCE-----#

count_tracker = []

for sub_file in csv_files:

	subj = sub_file.split('/')[-1]
	subj = subj.split('_')[0]

	#print('sub-' +subj)

	if 'x' in subj:
		break
	else: pass

	if subj not in skip:

		subject_file = np.genfromtxt(sub_file, delimiter = ',', unpack = True, dtype =None)

		for i in range(len(subject_file)):
			#print(subject_file[i][0])
			if subject_file[i][0] == 'corans':
				corans = i
			if subject_file[i][0] == 'Study_response.keys':
				study_response_keys = i
			if subject_file[i][0] == 'Study_response.corr':
				study_response_corr = i
			if subject_file[i][0] == 'stimuli_word.started':
				stim_word_started = i
			if subject_file[i][0] == 'Study_response.rt':
				study_response_rt = i
			if subject_file[i][0] == 'Confidence_resp.keys':
				confidence_resp_keys = i
			if subject_file[i][0] == 'Confidence_resp.started':
				confidence_resp_started = i
			if subject_file[i][0] == 'Confidence_resp.rt':
				confidence_resp_rt = i
			if subject_file[i][0] == 'ISI_text.started':
				isi_text_started = i

		#corans column
		run1_corans = subject_file[corans][4:64]
		run2_corans = subject_file[corans][65:125]
		run3_corans = subject_file[corans][126:186]
		run4_corans = subject_file[corans][187:247]

		#Study_response.keys
		#print(subject_file[43][0])
		run1_response = subject_file[study_response_keys][4:64]
		run2_response = subject_file[study_response_keys][65:125]
		run3_response = subject_file[study_response_keys][126:186]
		run4_response = subject_file[study_response_keys][187:247]

		#stimuli_word.started
		#print(subject_file[48][0])
		run1_word_started = subject_file[stim_word_started][4:64]
		run1_word_started_num = []
		for i in range(len(subject_file[stim_word_started][4:64])):
			try:
				num = np.round(float(subject_file[stim_word_started][4:64][i]),3)
				run1_word_started_num.append(num)
			except:
				run1_word_started_num.append('*')

		run2_word_started = subject_file[stim_word_started][65:125]
		run2_word_started_num = []
		for i in range(len(subject_file[stim_word_started][65:125])):
			try:
				num = np.round(float(subject_file[stim_word_started][65:125][i]),3)
				run2_word_started_num.append(num)
			except:
				run2_word_started_num.append('*')

		run3_word_started = subject_file[stim_word_started][126:186]
		run3_word_started_num = []
		for i in range(len(subject_file[stim_word_started][126:186])):
			try:
				num = np.round(float(subject_file[stim_word_started][126:186][i]),3)
				run3_word_started_num.append(num)
			except:
				run3_word_started_num.append('*')

		run4_word_started = subject_file[stim_word_started][187:247]
		run4_word_started_num = []
		for i in range(len(subject_file[stim_word_started][187:247])):
			try:
				num = np.round(float(subject_file[stim_word_started][187:247][i]),3)
				run4_word_started_num.append(num)
			except:
				run4_word_started_num.append('*')
		#print(run1_word_started)

		#ISI_text.started first element in each run
		#print(subject_file[41][0])
		run1_run_started = np.round(float(subject_file[isi_text_started][4:64][0]),3)
		run2_run_started = np.round(float(subject_file[isi_text_started][65:125][0]),3)
		run3_run_started = np.round(float(subject_file[isi_text_started][126:186][0]),3)
		run4_run_started = np.round(float(subject_file[isi_text_started][187:247][0]),3)
		#print(run1_run_started, run2_run_started, run3_run_started, run4_run_started)

		#ONSET TIME FOR WORD
		run1_onset_tw = []
		for i in range(len(run1_word_started_num)):
			if run1_word_started_num[i] == '*':
				run1_onset_tw.append('*')
			else:
				run1_onset_tw.append(run1_word_started_num[i] - run1_run_started)

		run2_onset_tw = []
		for i in range(len(run2_word_started_num)):
			if run2_word_started_num[i] == '*':
				run2_onset_tw.append('*')
			else:
				run2_onset_tw.append(run2_word_started_num[i] - run2_run_started)

		run3_onset_tw = []
		for i in range(len(run3_word_started_num)):
			if run3_word_started_num[i] == '*':
				run3_onset_tw.append('*')
			else:
				run3_onset_tw.append(run3_word_started_num[i] - run3_run_started)

		run4_onset_tw = []
		for i in range(len(run4_word_started_num)):
			if run4_word_started_num[i] == '*':
				run4_onset_tw.append('*')
			else:
				run4_onset_tw.append(run4_word_started_num[i] - run4_run_started)
		#print(run4_onset_tw)

		#Study_resp.rt
		#print(subject_file[45][0])
		run1_response_t = []
		for i in range(len(subject_file[study_response_rt][4:64])):
			try:
				num = np.round(float(subject_file[study_response_rt][4:64][i]),3)
				run1_response_t.append(num)
			except:
				run1_response_t.append('*')
		run2_response_t = []
		for i in range(len(subject_file[study_response_rt][65:125])):
			try:
				num = np.round(float(subject_file[study_response_rt][65:125][i]),3)
				run2_response_t.append(num)
			except:
				run2_response_t.append('*')
		run3_response_t = []
		for i in range(len(subject_file[study_response_rt][126:186])):
			try:
				num = np.round(float(subject_file[study_response_rt][126:186][i]),3)
				run3_response_t.append(num)
			except:
				run3_response_t.append('*')
		run4_response_t = []
		for i in range(len(subject_file[study_response_rt][187:247])):
			try:
				num = np.round(float(subject_file[study_response_rt][187:247][i]),3)
				run4_response_t.append(num)
			except:
				run4_response_t.append('*')

		#Confidence_resp.keys
		#print(subject_file[52][0])
		run1_confidence = subject_file[confidence_resp_keys][4:64]
		run2_confidence = subject_file[confidence_resp_keys][65:125]
		run3_confidence = subject_file[confidence_resp_keys][126:186]
		run4_confidence = subject_file[confidence_resp_keys][187:247]
		#print(all_con_resp)

		#Confidence_resp.started
		#print(subject_file[54][0])
		run1_confidence_started = subject_file[confidence_resp_started][4:64]
		#print(run1_confidence_started)
		run1_confidence_started_num = []
		for i in range(len(subject_file[confidence_resp_started][4:64])):
			try:
				num = np.round(float(subject_file[confidence_resp_started][4:64][i]),3)
				run1_confidence_started_num.append(num)
			except:
				run1_confidence_started_num.append('*')

		run2_confidence_started = subject_file[confidence_resp_started][65:125]
		run2_confidence_started_num = []
		for i in range(len(subject_file[confidence_resp_started][65:125])):
			try:
				num = np.round(float(subject_file[confidence_resp_started][65:125][i]),3)
				run2_confidence_started_num.append(num)
			except:
				run2_confidence_started_num.append('*')

		run3_confidence_started = subject_file[confidence_resp_started][126:186]
		run3_confidence_started_num = []
		for i in range(len(subject_file[confidence_resp_started][126:186])):
			try:
				num = np.round(float(subject_file[confidence_resp_started][126:186][i]),3)
				run3_confidence_started_num.append(num)
			except:
				run3_confidence_started_num.append('*')

		run4_confidence_started = subject_file[confidence_resp_started][187:247]
		run4_confidence_started_num = []
		for i in range(len(subject_file[confidence_resp_started][187:247])):
			try:
				num = np.round(float(subject_file[confidence_resp_started][187:247][i]),3)
				run4_confidence_started_num.append(num)
			except:
				run4_confidence_started_num.append('*')
		#print(run1_confidence_started)
		#print(run1_confidence_started_num)

		#ONSET TIME FOR CONFIDENCE
		run1_onset_tc = []
		for i in range(len(run1_confidence_started_num)):
			if run1_confidence_started_num[i] == '*':
				run1_onset_tc.append('*')
			else:
				run1_onset_tc.append(run1_confidence_started_num[i] - run1_run_started)
		#print(run1_onset_tc)

		run2_onset_tc = []
		for i in range(len(run2_confidence_started_num)):
			if run2_confidence_started_num[i] == '*':
				run2_onset_tc.append('*')
			else:
				run2_onset_tc.append(run2_confidence_started_num[i] - run2_run_started)

		run3_onset_tc = []
		for i in range(len(run3_confidence_started_num)):
			if run3_confidence_started_num[i] == '*':
				run3_onset_tc.append('*')
			else:
				run3_onset_tc.append(run3_confidence_started_num[i] - run3_run_started)

		run4_onset_tc = []
		for i in range(len(run4_confidence_started_num)):
			if run4_confidence_started_num[i] == '*':
				run4_onset_tc.append('*')
			else:
				run4_onset_tc.append(run4_confidence_started_num[i] - run4_run_started)
		#print(run4_onset_tc)
		#print(all_onset_tc)

		#Confidence_resp.rt
		#print(subject_file[62][0])
		run1_con_response_t = []
		for i in range(len(subject_file[confidence_resp_rt][4:64])):
			try:
				num = np.round(float(subject_file[confidence_resp_rt][4:64][i]),3)
				run1_con_response_t.append(num)
			except:
				run1_con_response_t.append('*')
		run2_con_response_t = []
		for i in range(len(subject_file[confidence_resp_rt][65:125])):
			try:
				num = np.round(float(subject_file[confidence_resp_rt][65:125][i]),3)
				run2_con_response_t.append(num)
			except:
				run2_con_response_t.append('*')
		run3_con_response_t = []
		for i in range(len(subject_file[confidence_resp_rt][126:186])):
			try:
				num = np.round(float(subject_file[confidence_resp_rt][126:186][i]),3)
				run3_con_response_t.append(num)
			except:
				run3_con_response_t.append('*')
		run4_con_response_t = []
		for i in range(len(subject_file[confidence_resp_rt][187:247])):
			try:
				num = np.round(float(subject_file[confidence_resp_rt][187:247][i]),3)
				run4_con_response_t.append(num)
			except:
				run4_con_response_t.append('*')

		run1_status = []
		run2_status = []
		run3_status = []
		run4_status = []

		all_con_resp = np.concatenate((run1_confidence, run2_confidence, run3_confidence, run4_confidence))
		#all_onset_tc = np.concatenate((run1_onset_tc, run2_onset_tc, run3_onset_tc, run4_onset_tc))
		all_onset_tw = np.concatenate((run1_onset_tw, run2_onset_tw, run3_onset_tw, run4_onset_tw))

		#Determine HIT, MISS, CR, FA
		for i in range(len(run1_corans)):
			write_status = None
			try:
				if int(run1_response[i]) == 1:
					if int(run1_corans[i]) == 1:
						write_status = 'HIT'
					elif int(run1_corans[i]) == 2: write_status = 'FA'
				elif int(run1_response[i]) == 2:
					if int(run1_corans[i]) == 1:
						write_status = 'MISS'
					elif int(run1_corans[i]) == 2: write_status = 'CR'
			except: write_status = '*'
			run1_status.append(write_status)
		run1_status = np.array(run1_status)

		for i in range(len(run2_corans)):
			write_status = None
			try:
				if int(run2_response[i]) == 1:
					if int(run2_corans[i]) == 1:
						write_status = 'HIT'
					elif int(run2_corans[i]) == 2: write_status = 'FA'
				elif int(run2_response[i]) == 2:
					if int(run2_corans[i]) == 1:
						write_status = 'MISS'
					elif int(run2_corans[i]) == 2: write_status = 'CR'
			except: write_status = '*'
			run2_status.append(write_status)
		run2_status = np.array(run2_status)

		for i in range(len(run3_corans)):
			write_status = None
			try:
				if int(run3_response[i]) == 1:
					if int(run3_corans[i]) == 1:
						write_status = 'HIT'
					elif int(run3_corans[i]) == 2: write_status = 'FA'
				elif int(run3_response[i]) == 2:
					if int(run3_corans[i]) == 1:
						write_status = 'MISS'
					elif int(run3_corans[i]) == 2: write_status = 'CR'
			except: write_status = '*'
			run3_status.append(write_status)
		run3_status = np.array(run3_status)

		for i in range(len(run4_corans)):
			write_status = None
			try:
				if int(run4_response[i]) == 1:
					if int(run4_corans[i]) == 1:
						write_status = 'HIT'
					elif int(run4_corans[i]) == 2: write_status = 'FA'
				elif int(run4_response[i]) == 2:
					if int(run4_corans[i]) == 1:
						write_status = 'MISS'
					elif int(run4_corans[i]) == 2: write_status = 'CR'
			except: write_status = '*'
			run4_status.append(write_status)
		run4_status = np.array(run4_status)

		all_status = np.concatenate((run1_status, run2_status, run3_status, run4_status))
		#print(all_status)

		#replace confidence 'None' wit '*'
		all_con_resp[np.where(all_con_resp == 'None')] = '*'

		ALL_HIT = np.where(all_status == 'HIT')
		ALL_MISS = np.where(all_status == 'MISS')
		ALL_CR = np.where(all_status == 'CR')
		ALL_FA = np.where(all_status == 'FA')

		HIT_1 = np.where(all_con_resp[ALL_HIT] == '1')
		onset_hit_1 = all_onset_tw[ALL_HIT][HIT_1]
		HIT_2 = np.where(all_con_resp[ALL_HIT] == '2')
		onset_hit_2 = all_onset_tw[ALL_HIT][HIT_2]
		HIT_3 = np.where(all_con_resp[ALL_HIT] == '3')
		onset_hit_3 = all_onset_tw[ALL_HIT][HIT_3]
		HIT_4 = np.where(all_con_resp[ALL_HIT] == '4')
		onset_hit_4 = all_onset_tw[ALL_HIT][HIT_4]

		MISS_1 = np.where(all_con_resp[ALL_MISS] == '1')
		onset_miss_1 = all_onset_tw[ALL_MISS][MISS_1]
		MISS_2 = np.where(all_con_resp[ALL_MISS] == '2')
		onset_miss_2 = all_onset_tw[ALL_MISS][MISS_2]
		MISS_3 = np.where(all_con_resp[ALL_MISS] == '3')
		onset_miss_3 = all_onset_tw[ALL_MISS][MISS_3]
		MISS_4 = np.where(all_con_resp[ALL_MISS] == '4')
		onset_miss_4 = all_onset_tw[ALL_MISS][MISS_4]

		CR_1 = np.where(all_con_resp[ALL_CR] == '1')
		onset_cr_1 = all_onset_tw[ALL_CR][CR_1]
		CR_2 = np.where(all_con_resp[ALL_CR] == '2')
		onset_cr_2 = all_onset_tw[ALL_CR][CR_2]
		CR_3 = np.where(all_con_resp[ALL_CR] == '3')
		onset_cr_3 = all_onset_tw[ALL_CR][CR_3]
		CR_4 = np.where(all_con_resp[ALL_CR] == '4')
		onset_cr_4 = all_onset_tw[ALL_CR][CR_4]

		FA_1 = np.where(all_con_resp[ALL_FA] == '1')
		onset_fa_1 = all_onset_tw[ALL_FA][FA_1]
		FA_2 = np.where(all_con_resp[ALL_FA] == '2')
		onset_fa_2 = all_onset_tw[ALL_FA][FA_2]
		FA_3 = np.where(all_con_resp[ALL_FA] == '3')
		onset_fa_3 = all_onset_tw[ALL_FA][FA_3]
		FA_4 = np.where(all_con_resp[ALL_FA] == '4')
		onset_fa_4 = all_onset_tw[ALL_FA][FA_4]

		OTHER = np.where(all_status == '*')
		onset_other = all_onset_tw[OTHER]

		#counts
		h1_count = len(onset_hit_1)

		h2_count = len(onset_hit_2)

		h3_count = len(onset_hit_3)

		h4_count = len(onset_hit_4)

		m1_count = len(onset_miss_1)

		m2_count = len(onset_miss_2)

		m3_count = len(onset_miss_3)

		m4_count = len(onset_miss_4)

		cr1_count = len(onset_cr_1)

		cr2_count = len(onset_cr_2)

		cr3_count = len(onset_cr_3)

		cr4_count = len(onset_cr_4)

		fa1_count = len(onset_fa_1)

		fa2_count = len(onset_fa_2)

		fa3_count = len(onset_fa_3)

		fa4_count = len(onset_fa_4)

		other_count = len(onset_other)

		count_tracker.append((subj,[h1_count, h2_count, h3_count, h4_count, m1_count, m2_count, m3_count, m4_count, cr1_count, cr2_count, cr3_count, cr4_count, fa1_count, fa2_count, fa3_count, fa4_count, other_count]))

file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/'
#Save counting file
file_name = file_path + 'behavioral_summary2.csv'
with open(file_name, 'w') as f:
	f.write('{0:10}, {1:5}, {2:5}, {3:5}, {4:5}, {5:5}, {6:5}, {7:5}, {8:5}, {9:5}, {10:5}, {11:5}, {12:5}, {13:5}, {14:5}, {15:5}, {16:5}, {17:5}\n'.format('','H1', 'H2', 'H3', 'H4', 'M1', 'M2', 'M3', 'M4', 'CR1', 'CR2', 'CR3', 'CR4', 'FA1', 'FA2', 'FA3', 'FA4', 'OT'))
	for i in range(len(count_tracker)):
		f.write('{0:<10}, {1:<5}, {2:<5}, {3:<5}, {4:<5}, {5:<5}, {6:<5}, {7:<5}, {8:<5}, {9:<5}, {10:<5}, {11:<5}, {12:<5}, {13:<5}, {14:<5}, {15:<5}, {16:<5}, {17:5}\n'.format("sub-"+count_tracker[i][0], count_tracker[i][1][0],
			count_tracker[i][1][1],
			count_tracker[i][1][2],
			count_tracker[i][1][3],
			count_tracker[i][1][4],
			count_tracker[i][1][5],
			count_tracker[i][1][6],
			count_tracker[i][1][7],
			count_tracker[i][1][8],
			count_tracker[i][1][9],
			count_tracker[i][1][10],
			count_tracker[i][1][11],
			count_tracker[i][1][12],
			count_tracker[i][1][13],
			count_tracker[i][1][14],
			count_tracker[i][1][15],
			count_tracker[i][1][16]))
	# f.write('{0:5} {1:5} {2:5} {3:5} {4:5} {5:5} {6:5} {7:5} {8:5} {9:5} {10:5} {11:5} {12:5} {13:5} {14:5} {15:5} {16:5}\n'.format('H1', 'H2', 'H3', 'H4', 'M1', 'M2', 'M3', 'M4', 'CR1', 'CR2', 'CR3', 'CR4', 'FA1', 'FA2', 'FA3', 'FA4', 'OT'))
	# f.write('{0:<5} {1:<5} {2:<5} {3:<5} {4:<5} {5:<5} {6:<5} {7:<5} {8:<5} {9:<5} {10:<5} {11:<5} {12:<5} {13:<5} {14:<5} {15:<5} {16:<5}\n'.format(h1_count, h2_count, h3_count, h4_count, m1_count, m2_count, m3_count, m4_count, cr1_count, cr2_count, cr3_count, cr4_count, fa1_count, fa2_count, fa3_count, fa4_count, other_count))
	#break

print('All runs done!')

#Check values against output files
# for i in range(len(all_onset_tc)):
# 	print('{0:10} {1:10} {2:10} '.format(all_status[i], all_con_resp[i], all_onset_tc[i]))

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



