#python for test file
import numpy as np
import glob

csv_files = glob.glob('../behavioraldata/*.csv')

skip = ['056']


for sub_file in csv_files:

	subj = sub_file.split('/')[-1]
	subj = subj.split('_')[0]

	print('sub-' +subj)

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

		file_path = '/Volumes/Yorick/fMRI_Replication/derivatives/sub-' + subj + '/' #Fill in with directory path Julie
		#print(file_path)
		#file_path = ''

		with open(file_path+'sub-'+subj+'_task-RecogConf_run-1_events.tsv', "w") as f:
				#f.write('{0:^130}\n'.format('Subject_' + subj))
				#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
				header_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
				#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
				f.write(header_line)

				for i in range(len(run1_corans)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
					#check for missing values
					if run1_response[i] not in ['1','2']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run1_response[i]
						resp_time = run1_response_t[i]
					#write word line
					word_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run1_onset_tw[i], 3.4, 'Word', stim_response, run1_corans[i], resp_time)
					f.write(word_line)
					#check for missing values
					if run1_confidence[i] not in ['1','2','3','4']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run1_confidence[i]
						resp_time = run1_con_response_t[i]
					#write confidence line
					confidence_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run1_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
					f.write(confidence_line)

		with open(file_path+'sub-'+subj+'_task-RecogConf_run-2_events.tsv', "w") as f:
				#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
				header_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
				#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
				f.write(header_line)

				for i in range(len(run2_corans)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
					#check for missing values
					if run2_response[i] not in ['1','2']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run2_response[i]
						resp_time = run2_response_t[i]
					#write word line
					word_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run2_onset_tw[i], 3.4, 'Word', stim_response, run2_corans[i], resp_time)
					f.write(word_line)
					#check for missing values
					if run2_confidence[i] not in ['1','2','3','4']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run2_confidence[i]
						resp_time = run2_con_response_t[i]
					#write confidence line
					confidence_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run2_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
					f.write(confidence_line)

		with open(file_path+'sub-'+subj+'_task-RecogConf_run-3_events.tsv', "w") as f:
				#f.write('{0:^130}\n'.format('Subject_' + subj))
				#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
				header_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
				#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
				f.write(header_line)

				for i in range(len(run3_corans)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
					#check for missing values
					if run3_response[i] not in ['1','2']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run3_response[i]
						resp_time = run3_response_t[i]
					#write word line
					word_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run3_onset_tw[i], 3.4, 'Word', stim_response, run3_corans[i], resp_time)
					f.write(word_line)
					#check for missing values
					if run3_confidence[i] not in ['1','2','3','4']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run3_confidence[i]
						resp_time = run3_con_response_t[i]
					#write confidence line
					confidence_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run3_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
					f.write(confidence_line)

		with open(file_path+'sub-'+subj+'_task-RecogConf_run-4_events.tsv', "w") as f:
				#f.write('{0:^130}\n'.format('Subject_' + subj))
				#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
				header_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
				#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
				f.write(header_line)

				for i in range(len(run4_corans)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
					#check for missing values
					if run4_response[i] not in ['1','2']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run4_response[i]
						resp_time = run4_response_t[i]
					#write word line
					word_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run4_onset_tw[i], 3.4, 'Word', stim_response, run4_corans[i], resp_time)
					f.write(word_line)
					#check for missing values
					if run4_confidence[i] not in ['1','2','3','4']:
						stim_response = '*'
						resp_time = '*'
					else:
						stim_response = run4_confidence[i]
						resp_time = run4_con_response_t[i]
					#write confidence line
					confidence_line = '{0:<8}\t{1:<10}\t{2:<15}\t{3:<18}\t{4:<15}\t{5:<15} \n'.format(run4_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
					f.write(confidence_line)

print('All runs done!')
# response:
# 1 - old
# 2 - new

# 1 - 1 = HIT
# 1 - 2 = FA
# 2 - 2 = CR
# 2 - 1 = MISS

# for i in range(len(run1_response)):
# 	if int(run1_response[i]) == 1:
# 		if int(run1_corans[i]) == 1:
# 			print(run1_response[i], run1_corans[i], 'HIT')
# 		else: print(run1_response[i], run1_corans[i], 'FA')
# 	if int(run1_response[i]) == 2:
# 		if int(run1_corans[i]) == 1:
# 			print(run1_response[i], run1_corans[i], 'CR')
# 		else: print(run1_response[i], run1_corans[i], 'MISS')



