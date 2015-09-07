#!/usr/bin/python
import os, time

print "##################################################\n"
print "##      Empty Folder Finder                     ##\n"
print "##################################################\n"

directory = raw_input('Directory: ')

def find_empty_dirs(root_dir):
    for dirpath, dirs, files in os.walk(root_dir):
        if not dirs and not files:
            yield dirpath

folders = list(find_empty_dirs(directory))

for f in folders:
	created = time.ctime(os.path.getctime(f))
	modified = time.ctime(os.path.getmtime(f))
	print f + "\n - Last modified: %s" % modified
	print " - Created: %s" % created

print "\nActions: delete - output - exit\n"
action = raw_input("Action: ")
if 'delete' in action:
	for f in folders:
		os.rmdir(f)

if 'output' in action:
	outfile = raw_input("Output file: ")
	filz = open(outfile, 'w')
	filz.write("\n".join(folders))
	filz.close()

if 'exit' in action:
	exit()
