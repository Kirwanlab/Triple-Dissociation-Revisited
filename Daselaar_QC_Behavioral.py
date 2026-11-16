#python3
import numpy as np
import glob

#Define psychopy directory from code location
psychopy_dir = '../psychopy/'

#get all behavioral csv files with glob
csv_files_behavioral = glob.glob('../behavioraldata/*.csv')

#start looping through behavioral files
for behavioral_file in csv_files_behavioral:

	#pull out subject number information 00X
	subj = behavioral_file.split('/')[-1]
	subj = subj.split('_')[0]

	#skip subjects with x in front
	if 'x' in subj:
		break
	else: pass

	#print subject number and psychopy folder name
	print(subj, 'p' + subj)

	#psychopy file path name for current subject
	psychopy_file = psychopy_dir+'p'+subj+'/'+'study.csv'

	#open behavioral data file and psychopy file
	subject_file = np.genfromtxt(behavioral_file, delimiter = ',', unpack = True, dtype =None)
	psychopy_file_data = np.genfromtxt(psychopy_file, delimiter = ',', unpack = True, dtype =None)

	#get words and corans in each file
	psychopy_words = psychopy_file_data[0][1:]
	psychopy_corans = psychopy_file_data[1][1:]
	#print(psychopy_corans)
	behavioral_words = subject_file[0][1:]
	behavioral_corans = subject_file[1][1:]

	#save status for each word
	psychopy_words_1 = []
	psychopy_words_2 = []
	corans_1_status = []
	corans_2_status = []

	#check for corans 1
	for i in range(len(psychopy_words)):
		if psychopy_corans[i] == '1':
			current_word = psychopy_words[i]
			psychopy_words_1.append(current_word)
			#print(current_word)

			word_found = False

			for j in range(len(behavioral_words)):
				if current_word == behavioral_words[j]:
					word_found = True
					break
				else:
					word_found = False
			if word_found:
				#print('Match')
				corans_1_status.append('Match')
			else:
				#print('Check for Error')
				corans_1_status.append('Check for Error')

	#check for corans 2
	for i in range(len(psychopy_words)):
		if psychopy_corans[i] == '2':
			current_word = psychopy_words[i]
			psychopy_words_2.append(current_word)
			#print(current_word)

			word_found = False

			for j in range(len(behavioral_words)):
				if current_word == behavioral_words[j]:
					word_found = True
					break
				else:
					word_found = False
			if word_found:
				#print('Check for Error')
				corans_2_status.append('Check for Error')
			else:
				#print('Match')
				corans_2_status.append("Match")


	filename = '../derivatives/' + 'sub-'+subj + '/qc_psychopy_behavioral.txt'
	print(filename)
	with open(filename,'w') as f:
		for i in range(len(psychopy_words_1)):
			f.write('{0}\t{1}\t{2}\n'.format(psychopy_words_1[i], corans_1_status[i], '1'))
		for i in range(len(psychopy_words_2)):
			f.write('{0}\t{1}\t{2}\n'.format(psychopy_words_2[i], corans_2_status[i], '2'))

	#break




