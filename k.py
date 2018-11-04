import shutil,os,zipfile

print('Select:')
print('1.Copy file')
print('2.Permanently delete file')
print('3.Permanently delete folder with content')
print('4.Extract zip')
print('5.Create zip')

choice=input()

if choice=='1':
	print('Enter source file path:')
	src=input()
	print('Enter destination file path:')
	dest=input()
	shutil.copy(src,dest)
elif choice=='2':
	print('Enter file path:')
	src=input()
	print('Do you want to delete file '+src+' y/n:')
	c=input()
	if c=='y':
		os.unlink(src)
elif choice=='3':
	print('Enter directory path:')
	src=input()
	print('Do you want to delete directory '+src+' y/n:')
	c=input()
	if c=='y':
		shutil.rmtree(src)
elif choice=='4':
	print('Enter directory path of source file:')
	src=input()
	srczip=zipfile.ZipFile(src)
	srczip.extractall()
	srczip.close()
elif choice=='5':
	print('Enter path of source file to be zipped:')
	src=input()
	srczip=zipfile.ZipFile('new.zip','w')
	srczip.write(src,compress_type=zipfile.ZIP_DEFLATED)
	srczip.close()