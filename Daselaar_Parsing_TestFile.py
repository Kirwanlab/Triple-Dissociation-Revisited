#python for test file
import numpy as np
import glob

csv_files = glob.glob('Sub*.csv')


for sub_file in csv_files:

	subj = sub_file.split('_')[1]

	subject_file = np.genfromtxt(sub_file, delimiter = ',', unpack = True, dtype =None)

	#stimuli column
	run1_stim = subject_file[0][4:64]
	run2_stim = subject_file[0][65:125]
	run3_stim = subject_file[0][126:186]
	run4_stim = subject_file[0][187:247]

	#corans column
	run1_corans = subject_file[1][4:64]
	run2_corans = subject_file[1][65:125]
	run3_corans = subject_file[1][126:186]
	run4_corans = subject_file[1][187:247]

	#Study_response.keys
	print(subject_file[43][0])
	run1_response = subject_file[43][4:64]
	run2_response = subject_file[43][65:125]
	run3_response = subject_file[43][126:186]
	run4_response = subject_file[43][187:247]

	# run1_status = subject_file[44][4:64]
	# run2_status = subject_file[44][65:125]
	# run3_status = subject_file[44][126:186]
	# run4_status = subject_file[44][187:247]

	#stimuli_word.started
	print(subject_file[48][0])
	run1_word_started = np.array([float(i) for i in subject_file[48][4:64]])
	run2_word_started = np.array([float(i) for i in subject_file[48][65:125]])
	run3_word_started = np.array([float(i) for i in subject_file[48][126:186]])
	run4_word_started = np.array([float(i) for i in subject_file[48][187:247]])
	print(run4_word_started)

	#ISI_text.started first element in each run
	print(subject_file[41][0])
	run1_run_started = float(subject_file[41][4:64][0])
	run2_run_started = float(subject_file[41][65:125][0])
	run3_run_started = float(subject_file[41][126:186][0])
	run4_run_started = float(subject_file[41][187:247][0])
	print(run1_run_started, run2_run_started, run3_run_started, run4_run_started)

	#ONSET TIME FOR WORD
	run1_onset_tw = run1_word_started - run1_run_started
	run2_onset_tw = run2_word_started - run2_run_started
	run3_onset_tw = run3_word_started - run3_run_started
	run4_onset_tw = run4_word_started - run4_run_started
	print(run4_onset_tw)

	#Study_resp.rt
	print(subject_file[45][0])
	run1_response_t = subject_file[45][4:64]
	run2_response_t = subject_file[45][65:125]
	run3_response_t = subject_file[45][126:186]
	run4_response_t = subject_file[45][187:247]

	#Confidence_resp.keys
	print(subject_file[52][0])
	run1_confidence = subject_file[52][4:64]
	run2_confidence = subject_file[52][65:125]
	run3_confidence = subject_file[52][126:186]
	run4_confidence = subject_file[52][187:247]

	#Confidence_resp.started
	print(subject_file[54][0])
	run1_confidence_started = np.array([float(i) for i in subject_file[54][4:64]])
	run2_confidence_started = np.array([float(i) for i in subject_file[54][65:125]])
	run3_confidence_started = np.array([float(i) for i in subject_file[54][126:186]])
	run4_confidence_started = np.array([float(i) for i in subject_file[54][187:247]])
	print(run4_confidence_started)

	#ONSET TIME FOR CONFIDENCE
	run1_onset_tc = run1_confidence_started - run1_run_started
	run2_onset_tc = run2_confidence_started - run2_run_started
	run3_onset_tc = run3_confidence_started - run3_run_started
	run4_onset_tc = run4_confidence_started - run4_run_started
	print(run4_onset_tc)

	#Confidence_resp.rt
	print(subject_file[62][0])
	run1_con_response_t = subject_file[62][4:64]
	run2_con_response_t = subject_file[62][65:125]
	run3_con_response_t = subject_file[62][126:186]
	run4_con_response_t = subject_file[62][187:247]

	file_path = '' #Fill in with directory path Julie

with open(file_path+'Sub-'+subj+'_task-RecogConf_run-1_events.tsv', "w") as f:
		#f.write('{0:^130}\n'.format('Subject_' + subj))
		#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
		header_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
		#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
		f.write(header_line)

		for i in range(len(run1_stim)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
			#check for missing values
			if run1_response[i] not in ['1','2']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run1_response[i]
				resp_time = run1_response_t[i]
			#write word line
			word_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run1_onset_tw[i], 3.4, 'Word', stim_response, run1_corans[i], resp_time)
			f.write(word_line)
			#check for missing values
			if run1_confidence[i] not in ['1','2','3','4']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run1_confidence[i]
				resp_time = run1_con_response_t[i]
			#write confidence line
			confidence_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run1_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
			f.write(confidence_line)

with open(file_path+'Sub-'+subj+'_task-RecogConf_run-2_events.tsv', "w") as f:
		#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
		header_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
		#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
		f.write(header_line)

		for i in range(len(run2_stim)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
			#check for missing values
			if run2_response[i] not in ['1','2']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run2_response[i]
				resp_time = run2_response_t[i]
			#write word line
			word_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run2_onset_tw[i], 3.4, 'Word', stim_response, run2_corans[i], resp_time)
			f.write(word_line)
			#check for missing values
			if run2_confidence[i] not in ['1','2','3','4']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run2_confidence[i]
				resp_time = run2_con_response_t[i]
			#write confidence line
			confidence_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run2_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
			f.write(confidence_line)

with open(file_path+'Sub-'+subj+'_task-RecogConf_run-3_events.tsv', "w") as f:
		#f.write('{0:^130}\n'.format('Subject_' + subj))
		#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
		header_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
		#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
		f.write(header_line)

		for i in range(len(run3_stim)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
			#check for missing values
			if run3_response[i] not in ['1','2']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run3_response[i]
				resp_time = run3_response_t[i]
			#write word line
			word_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run3_onset_tw[i], 3.4, 'Word', stim_response, run3_corans[i], resp_time)
			f.write(word_line)
			#check for missing values
			if run3_confidence[i] not in ['1','2','3','4']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run3_confidence[i]
				resp_time = run3_con_response_t[i]
			#write confidence line
			confidence_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run3_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
			f.write(confidence_line)

with open(file_path+'Sub-'+subj+'_task-RecogConf_run-4_events.tsv', "w") as f:
		#f.write('{0:^130}\n'.format('Subject_' + subj))
		#run, stimuli, corans, response, status, onset_t, response_t, confidence, con_onset_t, con_response_t
		header_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format('Onset', 'Duration', 'Trial_Type', 'Stimuli_Response', 'Correct_Answer', 'Reaction_Time')
		#header_line = '{0:10} {1:10} {2:15} {3:10} {4:10} {5:10} {6:30} {7:30} {8:15} {9:30} {10:30} \n'.format('run', 'stimuli', 'correct_answer', 'response', 'accuracy', 'status', 'onset_time', 'response_time', 'confidence', 'confidence_onset', 'confidence_rt')
		f.write(header_line)

		for i in range(len(run4_stim)):											#ONSET / DURATION /TRIAL_TYPE /STIM RESPONSE /CORRECT ANS / REACTION TIME
			#check for missing values
			if run4_response[i] not in ['1','2']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run4_response[i]
				resp_time = run4_response_t[i]
			#write word line
			word_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run4_onset_tw[i], 3.4, 'Word', stim_response, run4_corans[i], resp_time)
			f.write(word_line)
			#check for missing values
			if run4_confidence[i] not in ['1','2','3','4']:
				stim_response = '*'
				resp_time = '*'
			else:
				stim_response = run4_confidence[i]
				resp_time = run4_con_response_t[i]
			#write confidence line
			confidence_line = '{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} \n'.format(run4_onset_tc[i], 1.7, 'Confidence', stim_response, 'n/a', resp_time)
			f.write(confidence_line)


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



