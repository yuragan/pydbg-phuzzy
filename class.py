from cdbfuzz import *
import time

cdblocation = "C:\\Program Files\\Debugging Tools for Windows (x86)\\cdb.exe"
programname = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
crashdir = "c:\\logs\\"

fuzz = cdbfuzz(programname,crashdir,cdblocation)

for i in range(1,10):
	f = open('index.html','w')
	
	# add fuzzing code here maybe?
	
	f.close()
	proc = fuzz.startapp('index.html')
	time.sleep(2)
	
	# possibly +1 on every generated index.html, e.g.: index.html, index1.html
	if fuzz.wascrash() == True:
		fuzz.dumpcrash('index.html') 
