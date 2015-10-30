#! /usr/bin/python
import os,sys,re
import time,string 
s='mfsdata_'
e='bcdefg'
def rmdir():
	for i in range(len(e)-1):
		file_name='/root/'+s+e[i]
		os.rmdir(file_name)


def mkdir():
	for i in range(len(e)-1):
		file_name='/root/'+s+e[i]
		os.mkdir(file_name)
def mount():
	for i in range(len(e)-1):
		cmd='mount /dev/sd'+e[i]+'1'+' '+'/mnt/hgfs'
		os.system(cmd)
#t=time(5.0,mkdir)
#t.start()
#rmdir()
def test():
	os.system('pwd')
	os.system('pwd')

#test()
def modify():
	dir='/etc/yum.repos.d/'
	filenamelist=os.listdir(dir)
	number=len(filenamelist)
	print 'number is'+str(number)
	for i in range(number):
		print 'round'+str(i)
		filename=filenamelist[i]
		s=re.findall('.repo',filename)
		num=len(s)
		print 'num:'+str(num)
		if num!=0:
			filename_modify=filename.replace('.repo.repo','.repo')
			if filename != filename_modify:
				#filename_modify=filename[:-4]
				cmd='mv'+' '+dir+filename+' '+dir+filename_modify
				print 'find'
				os.system(cmd)
modify()

