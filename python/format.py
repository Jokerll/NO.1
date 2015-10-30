#! /usr/bin/python
import os,sys,re
import time,string 
dirname='mfsdata_'
e='bcdefghijklmnop'
def rmdir():
	for i in range(len(e)-1):
		file_name='/root/'+dirname+e[i]
		os.rmdir(file_name)


def mkdir():
	for i in range(len(e)-1):
		file_name='/root/'+dirname+e[i]
		print file_name
		#os.mkdir(file_name)
def mount():
	for i in range(len(e)-1):
		cmd='mount /dev/sd'+e[i]+'1'+' '+'/root/'+dirname+e[i]
		print cmd
		#os.system(cmd)

def parted():
	s1='bcdefghijklnmop'
	for i in range(len(s1)):
		cmd='parted /dev/sd'+s1[i]+'1'+' -s mklabel GPT -s unit TB -s mkpart primary 0.00 4.00'
		print cmd
	print '####parted complete!####'
def format():
	s1='bcdefghijklmnop'
	for i in range(len(s1)):
		cmd='mkfs -t ext4 /dev/sd'+s1[i]+'1'
		print cmd
	print '####format complete!####'

def diskcheck():
	print '####check disk!####'
	s1=e
	os.system('df -h >> 1.tt ')
	f=open('1.tt','r')
	disklist=[]
	modify_disklist=[]
	i=0
	line=f.readline()
	while line!='':
		x=line[7]
		disklist.append(x)
		line=f.readline()
		i=i+1
	#	print 'round '+str(i)+':'+str(disklist)
	f.close()
	del disklist[0]
	#print disklist
	#print 'disklist'+' '+''.join(disklist)
	modify_disklist=sorted(disklist)
	#print modify_disklist
	m=modify_disklist
	#print m
	###compile disk_number
	while m[0]==' ':
		del m[0]
	#print m
	while m[0].isdigit()==True:
		del m[0]
	#print m
	#while m[0]=='a':
	#	del m[0]
	

	s2=''.join(m)
	#print 's2:'+''.join(s2)
	while s2[0]=='a':
		s2=s2.replace('a','')
		if len(s2)==0:
			break
	
	for i in range(len(s2)):
		cmd='disk sd'+s2[i]+'1'+' '+'mounted successfully!'
		print cmd
	#print s2
	
	#common=[]
	#for x in s1:
	#if x in s2:
	#		common.append(x)
	#for x in range(len(common)):
	#	cmd='disk sd'+common[x]+'mounted successfully!'
	#	print cmd
	if ''.join(s2)==e:
		print 'Congratulitions,mounted sucessfully!'
		sys.exit()
	else:
		s3=list(s1)
		for i in range(len(s2)):
			s3.remove(s2[i])

		for i in range(len(s3)):
			umount='disk sd'+s3[i]+'1'+' '+'umounted!'
			print umount
		print 'mkfs again!'
		for i in range(len(s1)):
			cmd='mkfs -t ext4 /dev/sd'+s1[i]+'1'
			#os.system(cmd)
			print cmd
		os.system('rm -rf 1.tt')
mkdir()
parted()
format()
mount()
diskcheck()
