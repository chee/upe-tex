import os

output_filename = 'chap.cat'

outf = open(output_filename, 'w')
for each in os.listdir('.'):
	if each.endswith('.txt'):
		f = open(each)
		page = f.read()
		f.close()
		header = ('page ' + each.replace('.txt', '')).center(80, '-')
		outf.write(header)
		outf.write(page)
	
		