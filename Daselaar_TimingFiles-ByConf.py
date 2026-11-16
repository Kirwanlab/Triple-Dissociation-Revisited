#python for test file
import numpy as np
import glob
import subprocess

csv_files = glob.glob('../behavioraldata/*.csv')

skip = ['056']

#---ONSET TIMES SHOULD BE WORD TIMINGS NOT CONFIDENCE-----#

for sub_file in csv_files:

	subj = sub_file.split('/')[-1]
	subj = subj.split('_')[0]

	print('sub-' +subj)

	if 'x' in subj:
		break
	else: pass

	if subj not in skip:

		#print(sub_file)

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

		#ONSET TIME FOR CONFIDENCE - NOT USED
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


		all_con_resp = np.array((run1_confidence, run2_confidence, run3_confidence, run4_confidence))
		#all_onset_tc = np.array((run1_onset_tc, run2_onset_tc, run3_onset_tc, run4_onset_tc))
		all_onset_tw = np.array((run1_onset_tw, run2_onset_tw, run3_onset_tw, run4_onset_tw))

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

		all_status = np.array((run1_status, run2_status, run3_status, run4_status))
		#print(all_status)

		#replace confidence 'None' wit '*'
		for i in range(len(all_con_resp)):
			all_con_resp[i][np.where(all_con_resp[i] == 'None')] = '*'

		for i in range(len(all_con_resp)):
			#print('run',i+1)

			ALL_HIT = np.where(all_status[i] == 'HIT')
			ALL_MISS = np.where(all_status[i] == 'MISS')
			ALL_CR = np.where(all_status[i] == 'CR')
			ALL_FA = np.where(all_status[i] == 'FA')

			HIT_1 = np.where(all_con_resp[i][ALL_HIT] == '1')
			onset_hit_1 = all_onset_tw[i][ALL_HIT][HIT_1]
			#print(onset_hit_1)
			HIT_2 = np.where(all_con_resp[i][ALL_HIT] == '2')
			onset_hit_2 = all_onset_tw[i][ALL_HIT][HIT_2]
			HIT_3 = np.where(all_con_resp[i][ALL_HIT] == '3')
			onset_hit_3 = all_onset_tw[i][ALL_HIT][HIT_3]
			HIT_4 = np.where(all_con_resp[i][ALL_HIT] == '4')
			onset_hit_4 = all_onset_tw[i][ALL_HIT][HIT_4]

			MISS_1 = np.where(all_con_resp[i][ALL_MISS] == '1')
			onset_miss_1 = all_onset_tw[i][ALL_MISS][MISS_1]
			#print(onset_miss_1)
			MISS_2 = np.where(all_con_resp[i][ALL_MISS] == '2')
			onset_miss_2 = all_onset_tw[i][ALL_MISS][MISS_2]
			MISS_3 = np.where(all_con_resp[i][ALL_MISS] == '3')
			onset_miss_3 = all_onset_tw[i][ALL_MISS][MISS_3]
			MISS_4 = np.where(all_con_resp[i][ALL_MISS] == '4')
			onset_miss_4 = all_onset_tw[i][ALL_MISS][MISS_4]

			CR_1 = np.where(all_con_resp[i][ALL_CR] == '1')
			onset_cr_1 = all_onset_tw[i][ALL_CR][CR_1]
			#print(onset_cr_1)
			CR_2 = np.where(all_con_resp[i][ALL_CR] == '2')
			onset_cr_2 = all_onset_tw[i][ALL_CR][CR_2]
			CR_3 = np.where(all_con_resp[i][ALL_CR] == '3')
			onset_cr_3 = all_onset_tw[i][ALL_CR][CR_3]
			CR_4 = np.where(all_con_resp[i][ALL_CR] == '4')
			onset_cr_4 = all_onset_tw[i][ALL_CR][CR_4]

			FA_1 = np.where(all_con_resp[i][ALL_FA] == '1')
			onset_fa_1 = all_onset_tw[i][ALL_FA][FA_1]
			#print(onset_fa_1)
			FA_2 = np.where(all_con_resp[i][ALL_FA] == '2')
			onset_fa_2 = all_onset_tw[i][ALL_FA][FA_2]
			FA_3 = np.where(all_con_resp[i][ALL_FA] == '3')
			onset_fa_3 = all_onset_tw[i][ALL_FA][FA_3]
			FA_4 = np.where(all_con_resp[i][ALL_FA] == '4')
			onset_fa_4 = all_onset_tw[i][ALL_FA][FA_4]

			OTHER = np.where(all_status[i] == '*')
			onset_other = all_onset_tw[i][OTHER]

			file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
			#file_path = ''

			#Save files
			file_name =file_path +'hit-1.txt'
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(onset_hit_1) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_hit_1)):
					write_line += str(onset_hit_1[j]) + '\t'
				if j == len(onset_hit_1) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'hit-2.txt'
			with open(file_name,option) as f:
				if len(onset_hit_2) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_hit_2)):
					write_line += str(onset_hit_2[j]) + '\t'
				if j == len(onset_hit_2) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'hit-3.txt'
			with open(file_name,option) as f:
				if len(onset_hit_3) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_hit_3)):
					write_line += str(onset_hit_3[j]) + '\t'
				if j == len(onset_hit_3) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'hit-4.txt'
			with open(file_name,option) as f:
				if len(onset_hit_4) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_hit_4)):
					write_line += str(onset_hit_4[j]) + '\t'
				if j == len(onset_hit_4) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'miss-1.txt'
			with open(file_name,option) as f:
				if len(onset_miss_1) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_miss_1)):
					write_line += str(onset_miss_1[j]) + '\t'
				if j == len(onset_miss_1) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'miss-2.txt'
			with open(file_name,option) as f:
				if len(onset_miss_2) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_miss_2)):
					write_line += str(onset_miss_2[j]) + '\t'
				if j == len(onset_miss_2) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'miss-3.txt'
			with open(file_name,option) as f:
				if len(onset_miss_3) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_miss_3)):
					write_line += str(onset_miss_3[j]) + '\t'
				if j == len(onset_miss_3) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'miss-4.txt'
			with open(file_name,option) as f:
				if len(onset_miss_4) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_miss_4)):
					write_line += str(onset_miss_4[j]) + '\t'
				if j == len(onset_miss_4) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'cr-1.txt'
			with open(file_name,option) as f:
				if len(onset_cr_1) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_cr_1)):
					write_line += str(onset_cr_1[j]) + '\t'
				if j == len(onset_cr_1) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'cr-2.txt'
			with open(file_name,option) as f:
				if len(onset_cr_2) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_cr_2)):
					write_line += str(onset_cr_2[j]) + '\t'
				if j == len(onset_cr_2) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'cr-3.txt'
			with open(file_name,option) as f:
				if len(onset_cr_3) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_cr_3)):
					write_line += str(onset_cr_3[j]) + '\t'
				if j == len(onset_cr_3) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'cr-4.txt'
			with open(file_name,option) as f:
				if len(onset_cr_4) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_cr_4)):
					write_line += str(onset_cr_4[j]) + '\t'
				if j == len(onset_cr_4) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'fa-1.txt'
			with open(file_name,option) as f:
				if len(onset_fa_1) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_fa_1)):
					write_line += str(onset_fa_1[j]) + '\t'
				if j == len(onset_fa_1) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'fa-2.txt'
			with open(file_name,option) as f:
				if len(onset_fa_2) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_fa_2)):
					write_line += str(onset_fa_2[j]) + '\t'
				if j == len(onset_fa_2) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'fa-3.txt'
			with open(file_name,option) as f:
				if len(onset_fa_3) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_fa_3)):
					write_line += str(onset_fa_3[j]) + '\t'
				if j == len(onset_fa_3) -1:
					write_line += '\n'
				f.write(write_line)

			file_name =file_path +'fa-4.txt'
			with open(file_name,option) as f:
				if len(onset_fa_4) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(onset_fa_4)):
					write_line += str(onset_fa_4[j]) + '\t'
				if j == len(onset_fa_4) -1:
					write_line += '\n'
				f.write(write_line)

			# file_name =file_path +'other.txt'
			# with open(file_name,option) as f:
			# 	if len(onset_other) == 0:
			# 		write_line = '*\n'
			# 	else:
			# 		write_line = ''
			# 	for j in range(len(onset_other)):
			# 		write_line += str(onset_other[j]) + '\t'
			# 	if j == len(onset_other) -1:
			# 		write_line += '\n'
			# 	f.write(write_line)

	else: 
		print('skipped')
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
# 2 - 2 = CR
# 2 - 1 = MISS

#-------Test output for run 1--------
# for i in range(len(run1_response)):
# 	try:
# 		if int(run1_response[i]) == 1:
# 			if int(run1_corans[i]) == 1:
# 				print(run1_response[i], run1_corans[i], 'HIT')
# 			elif int(run1_corans[i]) == 2: print(run1_response[i], run1_corans[i], 'FA')
# 	except: print('*')
# 	try:
# 		if int(run1_response[i]) == 2:
# 			if int(run1_corans[i]) == 1:
# 				print(run1_response[i], run1_corans[i], 'MISS')
# 			elif int(run1_corans[i]) == 2: print(run1_response[i], run1_corans[i], 'CR')
# 	except: print('*')



