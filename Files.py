import os
# joins string to path
os.path.join('d:\\','github','Scripts')
# current dir
os.getcwd()
# change current dir
os.chdir('C:\\Windows\\System32')
#create all dirs
os.makedirs('C:\\delicious\\walnut\\waffles')
# returns absolut path
os.path.abspath('.')
# check's if path is absolute
os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))
# relational length to path to a certian file\ dir
os.path.relpath('C:\\Windows', 'C:\\')
os.path.relpath('C:\\Windows', 'C:\\Windows\\System32\\calc.exe')
path = 'C:\\Windows\\System32\\calc.exe'
#get first file or dir name
os.path.basename(path)
# get full dir path
os.path.dirname(path)
# splits dir from file name
os.path.split(path)
(os.path.dirname(path), os.path.basename(path))
# seperate path to list by partion, dirs,
path.split(os.path.sep)
'C:\\Windows\\System32\\calc.exe'.split(os.path.sep)
# get file size or dir size of file
os.path.getsize('C:\\Windows\\System32\\calc.exe')
# list all files in a dir
os.listdir('C:\\Windows\\System32')
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
# check if dir exists
os.path.exists('C:\\Windows')
os.path.exists('C:\\some_made_up_folder')
# check if its a dir o file
os.path.isdir('C:\\Windows\\System32')
os.path.isfile('C:\\Windows\\System32')
os.path.isdir('C:\\Windows\\System32\\calc.exe')
os.path.isfile('C:\\Windows\\System32\\calc.exe')
# check if file exists
os.path.exists('C:\\Windows\\System32\\calc.exe')