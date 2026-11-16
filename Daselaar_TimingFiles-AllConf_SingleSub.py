#python for test file
import numpy as np
import glob
import subprocess

csv_files = glob.glob('../behavioraldata/*.csv')

skip = ['056']

#---ONSET TIMES TO BE PRINTED SHOULD WORD TIMINGS NOT CONFIDENCE-----#

for sub_file in csv_files:

	subj = sub_file.split('/')[-1]
	subj = subj.split('_')[0]

	print('sub-' +subj)

	if 'x' in subj:
		break
	else: pass

	if subj in skip:

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
		# run3_corans = subject_file[corans][126:186]
		# run4_corans = subject_file[corans][187:247]

		#Study_response.keys
		#print(subject_file[43][0])
		run1_response = subject_file[study_response_keys][4:64]
		run2_response = subject_file[study_response_keys][65:125]
		# run3_response = subject_file[study_response_keys][126:186]
		# run4_response = subject_file[study_response_keys][187:247]

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

		# run3_word_started = subject_file[stim_word_started][126:186]
		# run3_word_started_num = []
		# for i in range(len(subject_file[stim_word_started][126:186])):
		# 	try:
		# 		num = np.round(float(subject_file[stim_word_started][126:186][i]),3)
		# 		run3_word_started_num.append(num)
		# 	except:
		# 		run3_word_started_num.append('*')

		# run4_word_started = subject_file[stim_word_started][187:247]
		# run4_word_started_num = []
		# for i in range(len(subject_file[stim_word_started][187:247])):
		# 	try:
		# 		num = np.round(float(subject_file[stim_word_started][187:247][i]),3)
		# 		run4_word_started_num.append(num)
		# 	except:
		# 		run4_word_started_num.append('*')
		#print(run1_word_started)

		#ISI_text.started first element in each run
		#print(subject_file[41][0])
		run1_run_started = np.round(float(subject_file[isi_text_started][4:64][0]),3)
		run2_run_started = np.round(float(subject_file[isi_text_started][65:125][0]),3)
		# run3_run_started = np.round(float(subject_file[isi_text_started][126:186][0]),3)
		# run4_run_started = np.round(float(subject_file[isi_text_started][187:247][0]),3)
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

		# run3_onset_tw = []
		# for i in range(len(run3_word_started_num)):
		# 	if run3_word_started_num[i] == '*':
		# 		run3_onset_tw.append('*')
		# 	else:
		# 		run3_onset_tw.append(run3_word_started_num[i] - run3_run_started)

		# run4_onset_tw = []
		# for i in range(len(run4_word_started_num)):
		# 	if run4_word_started_num[i] == '*':
		# 		run4_onset_tw.append('*')
		# 	else:
		# 		run4_onset_tw.append(run4_word_started_num[i] - run4_run_started)
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
		# run3_response_t = []
		# for i in range(len(subject_file[study_response_rt][126:186])):
		# 	try:
		# 		num = np.round(float(subject_file[study_response_rt][126:186][i]),3)
		# 		run3_response_t.append(num)
		# 	except:
		# 		run3_response_t.append('*')
		# run4_response_t = []
		# for i in range(len(subject_file[study_response_rt][187:247])):
		# 	try:
		# 		num = np.round(float(subject_file[study_response_rt][187:247][i]),3)
		# 		run4_response_t.append(num)
		# 	except:
		# 		run4_response_t.append('*')

		#Confidence_resp.keys
		#print(subject_file[52][0])
		run1_confidence = subject_file[confidence_resp_keys][4:64]
		run2_confidence = subject_file[confidence_resp_keys][65:125]
		# run3_confidence = subject_file[confidence_resp_keys][126:186]
		# run4_confidence = subject_file[confidence_resp_keys][187:247]

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

		# run3_confidence_started = subject_file[confidence_resp_started][126:186]
		# run3_confidence_started_num = []
		# for i in range(len(subject_file[confidence_resp_started][126:186])):
		# 	try:
		# 		num = np.round(float(subject_file[confidence_resp_started][126:186][i]),3)
		# 		run3_confidence_started_num.append(num)
		# 	except:
		# 		run3_confidence_started_num.append('*')

		# run4_confidence_started = subject_file[confidence_resp_started][187:247]
		# run4_confidence_started_num = []
		# for i in range(len(subject_file[confidence_resp_started][187:247])):
		# 	try:
		# 		num = np.round(float(subject_file[confidence_resp_started][187:247][i]),3)
		# 		run4_confidence_started_num.append(num)
		# 	except:
		# 		run4_confidence_started_num.append('*')
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

		# run3_onset_tc = []
		# for i in range(len(run3_confidence_started_num)):
		# 	if run3_confidence_started_num[i] == '*':
		# 		run3_onset_tc.append('*')
		# 	else:
		# 		run3_onset_tc.append(run3_confidence_started_num[i] - run3_run_started)

		# run4_onset_tc = []
		# for i in range(len(run4_confidence_started_num)):
		# 	if run4_confidence_started_num[i] == '*':
		# 		run4_onset_tc.append('*')
		# 	else:
		# 		run4_onset_tc.append(run4_confidence_started_num[i] - run4_run_started)
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
		# run3_con_response_t = []
		# for i in range(len(subject_file[confidence_resp_rt][126:186])):
		# 	try:
		# 		num = np.round(float(subject_file[confidence_resp_rt][126:186][i]),3)
		# 		run3_con_response_t.append(num)
		# 	except:
		# 		run3_con_response_t.append('*')
		# run4_con_response_t = []
		# for i in range(len(subject_file[confidence_resp_rt][187:247])):
		# 	try:
		# 		num = np.round(float(subject_file[confidence_resp_rt][187:247][i]),3)
		# 		run4_con_response_t.append(num)
		# 	except:
		# 		run4_con_response_t.append('*')

		run1_status = []
		run2_status = []
		# run3_status = []
		# run4_status = []


		#all_con_resp = np.array((run1_confidence, run2_confidence, run3_confidence, run4_confidence))
		all_con_resp = np.array((run1_confidence, run2_confidence))
		#all_onset_tc = np.array((run1_onset_tc, run2_onset_tc, run3_onset_tc, run4_onset_tc))
		all_onset_tc = np.array((run1_onset_tc, run2_onset_tc))
		all_onset_tw = np.array((run1_onset_tw, run2_onset_tw))

		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie

		collect_runs_conf_1 = []
		collect_runs_conf_2 = []
		collect_runs_conf_3 = []
		collect_runs_conf_4 = []
		collect_runs_conf_other = []
		for i in range(len(all_con_resp)):
			#print(all_con_resp[i])
			collect_runs_conf_1.append(all_onset_tc[i][np.where(all_con_resp[i]=='1')])
			collect_runs_conf_2.append(all_onset_tc[i][np.where(all_con_resp[i]=='2')])
			collect_runs_conf_3.append(all_onset_tc[i][np.where(all_con_resp[i]=='3')])
			collect_runs_conf_4.append(all_onset_tc[i][np.where(all_con_resp[i]=='4')])
			collect_runs_conf_other.append(all_onset_tc[i][np.where(all_con_resp[i]=='None')])

		#Create confidence files
		# file_name =file_path +'conf-1.txt'
		# for i in range(len(collect_runs_conf_1)):

		# 	#Save data
		# 	if i== 0:
		# 		option = 'w'
		# 	else: option = 'a'

		# 	with open(file_name,option) as f:
		# 		if len(collect_runs_conf_1[i]) == 0:
		# 			write_line = '*\n'
		# 		else:
		# 			write_line = ''
		# 		for j in range(len(collect_runs_conf_1[i])):
		# 			write_line += str(collect_runs_conf_1[i][j]) + '\t'
		# 		if j == len(collect_runs_conf_1[i]) -1:
		# 			write_line += '\n'
		# 		#print(write_line)
		# 		f.write(write_line)

		# file_name =file_path +'conf-2.txt'
		# for i in range(len(collect_runs_conf_2)):

		# 	#Save data
		# 	if i== 0:
		# 		option = 'w'
		# 	else: option = 'a'

		# 	with open(file_name,option) as f:
		# 		if len(collect_runs_conf_2[i]) == 0:
		# 			write_line = '*\n'
		# 		else:
		# 			write_line = ''
		# 		for j in range(len(collect_runs_conf_2[i])):
		# 			write_line += str(collect_runs_conf_2[i][j]) + '\t'
		# 		if j == len(collect_runs_conf_2[i]) -1:
		# 			write_line += '\n'
		# 		#print(write_line)
		# 		f.write(write_line)

		# file_name =file_path +'conf-3.txt'
		# for i in range(len(collect_runs_conf_3)):

		# 	#Save data
		# 	if i== 0:
		# 		option = 'w'
		# 	else: option = 'a'

		# 	with open(file_name,option) as f:
		# 		if len(collect_runs_conf_3[i]) == 0:
		# 			write_line = '*\n'
		# 		else:
		# 			write_line = ''
		# 		for j in range(len(collect_runs_conf_3[i])):
		# 			write_line += str(collect_runs_conf_3[i][j]) + '\t'
		# 		if j == len(collect_runs_conf_3[i]) -1:
		# 			write_line += '\n'
		# 		#print(write_line)
		# 		f.write(write_line)

		# file_name =file_path +'conf-4.txt'
		# for i in range(len(collect_runs_conf_4)):

		# 	#Save data
		# 	if i== 0:
		# 		option = 'w'
		# 	else: option = 'a'

		# 	with open(file_name,option) as f:
		# 		if len(collect_runs_conf_4[i]) == 0:
		# 			write_line = '*\n'
		# 		else:
		# 			write_line = ''
		# 		for j in range(len(collect_runs_conf_4[i])):
		# 			write_line += str(collect_runs_conf_4[i][j]) + '\t'
		# 		if j == len(collect_runs_conf_4[i]) -1:
		# 			write_line += '\n'
		# 		#print(write_line)
		# 		f.write(write_line)

		# file_name =file_path +'conf-other.txt'
		# for i in range(len(collect_runs_conf_other)):

		# 	#Save data
		# 	if i== 0:
		# 		option = 'w'
		# 	else: option = 'a'

		# 	with open(file_name,option) as f:
		# 		if len(collect_runs_conf_other[i]) == 0:
		# 			write_line = '*\n'
		# 		else:
		# 			write_line = ''
		# 		for j in range(len(collect_runs_conf_other[i])):
		# 			write_line += str(collect_runs_conf_other[i][j]) + '\t'
		# 		if j == len(collect_runs_conf_other[i]) -1:
		# 			write_line += '\n'
		# 		#print(write_line)
		# 		f.write(write_line)

		#Determine HITS, MISS, CR, FA
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

		# for i in range(len(run3_corans)):
		# 	write_status = None
		# 	try:
		# 		if int(run3_response[i]) == 1:
		# 			if int(run3_corans[i]) == 1:
		# 				write_status = 'HIT'
		# 			elif int(run3_corans[i]) == 2: write_status = 'FA'
		# 		elif int(run3_response[i]) == 2:
		# 			if int(run3_corans[i]) == 1:
		# 				write_status = 'MISS'
		# 			elif int(run3_corans[i]) == 2: write_status = 'CR'
		# 	except: write_status = '*'
		# 	run3_status.append(write_status)
		# run3_status = np.array(run3_status)

		# for i in range(len(run4_corans)):
		# 	write_status = None
		# 	try:
		# 		if int(run4_response[i]) == 1:
		# 			if int(run4_corans[i]) == 1:
		# 				write_status = 'HIT'
		# 			elif int(run4_corans[i]) == 2: write_status = 'FA'
		# 		elif int(run4_response[i]) == 2:
		# 			if int(run4_corans[i]) == 1:
		# 				write_status = 'MISS'
		# 			elif int(run4_corans[i]) == 2: write_status = 'CR'
		# 	except: write_status = '*'
		# 	run4_status.append(write_status)
		# run4_status = np.array(run4_status)

		#all_status = np.array((run1_status, run2_status, run3_status, run4_status))
		all_status = np.array((run1_status, run2_status))
		#print(all_status)

		#replace confidence 'None' wit '*'
		for i in range(len(all_con_resp)):
			all_con_resp[i][np.where(all_con_resp[i] == 'None')] = '*'

		#collect HIT, MISS, CR, FA, other by run
		collect_hits = []
		collect_miss = []
		collect_cr = []
		collect_fa = []
		collect_other = []	
		for i in range(len(all_status)):
			#print('run',i+1)

			ALL_HIT = np.where(all_status[i] == 'HIT')
			#print('all hits this run', ALL_HIT)
			ALL_MISS = np.where(all_status[i] == 'MISS')
			ALL_CR = np.where(all_status[i] == 'CR')
			ALL_FA = np.where(all_status[i] == 'FA')
			ALL_OTHER = np.where(all_status[i] == '*')

			onset_tw_hits = all_onset_tw[i][ALL_HIT]
			collect_hits.append(onset_tw_hits)

			onset_tw_miss = all_onset_tw[i][ALL_MISS]
			collect_miss.append(onset_tw_miss)

			onset_tw_cr = all_onset_tw[i][ALL_CR]
			collect_cr.append(onset_tw_cr)

			onset_tw_fa = all_onset_tw[i][ALL_FA]
			collect_fa.append(onset_tw_fa)

			onset_tw_other = all_onset_tw[i][ALL_OTHER]
			collect_other.append(onset_tw_other)
		
		#Create hits files - all hits by run
		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
		file_name =file_path +'hit.txt'

		for i in range(len(collect_hits)):
			#print(collect_hits[i])

			#Save data
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(collect_hits[i]) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(collect_hits[i])):
					write_line += str(collect_hits[i][j]) + '\t'
				if j == len(collect_hits[i]) -1:
					write_line += '\n'
				#print(write_line)
				f.write(write_line)
		#break

		#Create miss files - all miss by run
		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
		file_name =file_path +'miss.txt'

		for i in range(len(collect_miss)):
			#print(collect_miss[i])

			#Save data
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(collect_miss[i]) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(collect_miss[i])):
					write_line += str(collect_miss[i][j]) + '\t'
				if j == len(collect_miss[i]) -1:
					write_line += '\n'
				#print(write_line)
				f.write(write_line)
		#break

		#Create cr files - all cr by run
		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
		file_name =file_path +'cr.txt'

		for i in range(len(collect_cr)):
			#print(collect_cr[i])

			#Save data
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(collect_cr[i]) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(collect_cr[i])):
					write_line += str(collect_cr[i][j]) + '\t'
				if j == len(collect_cr[i]) -1:
					write_line += '\n'
				#print(write_line)
				f.write(write_line)
		#break

		#Create fa files - all fa by run
		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
		file_name =file_path +'fa.txt'

		for i in range(len(collect_fa)):
			#print(collect_fa[i])

			#Save data
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(collect_fa[i]) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(collect_fa[i])):
					write_line += str(collect_fa[i][j]) + '\t'
				if j == len(collect_fa[i]) -1:
					write_line += '\n'
				#print(write_line)
				f.write(write_line)
		#break

		#Create other files - all other by run
		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/timing/' #Fill in with directory path Julie
		file_name =file_path +'other.txt'

		for i in range(len(collect_other)):
			#print(collect_fa[i])

			#Save data
			if i== 0:
				option = 'w'
			else: option = 'a'

			with open(file_name,option) as f:
				if len(collect_other[i]) == 0:
					write_line = '*\n'
				else:
					write_line = ''
				for j in range(len(collect_other[i])):
					write_line += str(collect_other[i][j]) + '\t'
				if j == len(collect_other[i]) -1:
					write_line += '\n'
				#print(write_line)
				f.write(write_line)
		#break

	else: print('skipped')

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



