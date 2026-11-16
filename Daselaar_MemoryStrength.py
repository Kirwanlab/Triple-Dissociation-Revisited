import numpy as np
import glob
#import subprocess

subj_files = glob.glob('../derivatives/sub*')

for i in range(len(subj_files)):
	print(i)
	location = subj_files[i] + '/timing/'
	
	local_files = glob.glob(location+'*.txt')

	##print(local_files)

	hit_files = []
	miss_files = []
	cr_files = []
	fa_files = []

	for j in range(len(local_files)):
		if 'hit-' in local_files[j]:
			hit_files.append(local_files[j])
		if 'miss-' in local_files[j]:
			miss_files.append(local_files[j])
		if 'cr-' in local_files[j]:
			cr_files.append(local_files[j])
		if 'fa-' in local_files[j]:
			fa_files.append(local_files[j])

	#check files
	for j in range(len(hit_files)):
		if j == 0:
			with open(location+'memorystrength1.txt', 'w') as f:
				pass
			with open(location+'memorystrength2.txt', 'w') as f:
				pass
			with open(location+'memorystrength3.txt', 'w') as f:
				pass
			with open(location+'memorystrength4.txt', 'w') as f:
				pass
			with open(location+'memorystrength5.txt', 'w') as f:
				pass
			with open(location+'memorystrength6.txt', 'w') as f:
				pass
		else:
			#print(hit_files[j])
			with open(hit_files[j], 'r') as f:
				temp_lines1 = f.readlines()
			with open(fa_files[j], 'r') as f:
				temp_lines2 = f.readlines()
			with open(miss_files[j], 'r') as f:
				temp_lines3 = f.readlines()
			with open(cr_files[j], 'r') as f:
				temp_lines4 = f.readlines()

			mem_str4_6 = []
			mem_str3_1 = []

			for k in range(len(temp_lines1)):
				write_line = ''
				if '*' not in temp_lines2[k][0:-1]:
					write_line += temp_lines2[k][0:-1]
				if '*' not in temp_lines1[k]:
					write_line += temp_lines1[k]
				if write_line == '':
					write_line = '*\n'
				if write_line[-1] != '\n':
					write_line += '\n'

				# write_line = temp_lines2[k][0:-1] + temp_lines1[k]
				# if write_line == '**\n':
				# 	write_line = '*\n'
				# elif write_line[0] == '*':
				# 	write_line = write_line[0] + '\t' + write_line[1:]
				# print(write_line)
				mem_str4_6.append(write_line)

			for k in range(len(temp_lines3)):
				write_line = ''
				if '*' not in temp_lines4[k][0:-1]:
					write_line += temp_lines4[k][0:-1]
				if '*' not in temp_lines3[k]:
					write_line += temp_lines3[k]
				if write_line == '':
					write_line = '*\n'
				if write_line[-1] != '\n':
					write_line += '\n'
				# if '*' in temp_lines4[k][0:-1]:
				# 	write_line = temp_lines3[k]
				# elif '*' in temp_lines3[k]:
				# 	write_line = temp_lines4[k][0:-1]
				# else:
				# 	write_line = temp_lines4[k][0:-1] + temp_lines3[k]

				# write_line = temp_lines4[k][0:-1] + temp_lines3[k]
				# if write_line == '**\n':
				# 	write_line = '*\n'
				# elif write_line[0] == '*':
				# 	write_line = write_line[0] + '\t' + write_line[1:]
				# print(write_line)
				mem_str3_1.append(write_line)


			#write files
			if 'hit-2' in hit_files[j]:
				#print('make memstr4')
				#print(mem_str4_6)
				with open(location+'memorystrength4.txt', 'a') as f:
					for k in mem_str4_6:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)
			if 'hit-3' in hit_files[j]:
				#print('make memstr5')
				#print(mem_str4_6)
				with open(location+'memorystrength5.txt', 'a') as f:
					for k in mem_str4_6:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)
			if 'hit-4' in hit_files[j]:
				#print('make memstr6')
				#print(mem_str4_6)
				with open(location+'memorystrength6.txt', 'a') as f:
					for k in mem_str4_6:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)

			if 'miss-4' in miss_files[j]:
				#print('make memstr1')
				#print(mem_str3_1)
				with open(location+'memorystrength1.txt', 'a') as f:
					for k in mem_str3_1:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)
			if 'miss-3' in miss_files[j]:
				#print('make memstr2')
				#print(mem_str3_1)
				with open(location+'memorystrength2.txt', 'a') as f:
					for k in mem_str3_1:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)
			if 'miss-2' in miss_files[j]:
				#print('make memstr3')
				#print(mem_str3_1)
				with open(location+'memorystrength3.txt', 'a') as f:
					for k in mem_str3_1:
						if k[0:1] == '\t':
							f.write(k[1:])
						else:
							f.write(k)
	#break
