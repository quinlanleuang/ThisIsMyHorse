- Linux的命令很多是英文缩写，所以用英文的方式取理解和解释命令的含义，更能达意且方便记忆

# directory
command  |  meaning
-------- | ------- 
ls |  list files and directories
ls -a | list all files and directories
mkdir | make directory
cd directory | change to name directory
cd | change to home-directory
cd ~ | change to home-directory
cd .. | change to parent directory
pwd | print working directory

# file
command  |  meaning
-------- | ------- 
cp file1 file2 | copy file1 and call it file2
mv file1 file2 | move or rename file1 to file2
rm file | remove a file
rmdir directory | remove an empty directory
clear | clear screen（equal to '^L'）
cat file | display a file
less file | display a file a page at a time
head file | display the first few lines of a file
tail file | display the last few lines of a file
grep 'keyword' file | search a file for keywords
wc file | count number of lines/words/characters in file

# redirectory
command  |  meaning
-------- | ------- 
command > file | redirect standard output to a file
command >> file | append standard output to a file
command < file | redirect standard input from a file
command1 \| command2 |pip the output of command1 to the input fo command2
cat file1 file2 > file0 | concatenate file11 file2 to file0
sort | sort data
who | list users currently logged in


# wildcard and help
command  |  meaning
-------- | ------- 
* | match any number of characters
? | match one character
man command | read the online manual page for a command
whatis command | brief description of a command
apropos command | match commands with keyword in their man pages


# file access rights
command  |  meaning
-------- | ------- 
chmod | change a file mode, change access rights for named file

```shell
ls -l command result meaning 

-rwxr-xr-x      1            quinlan staff   0B     1  7 13:29    favicon.ico
[access rights] [file count] [owner] [group] [size] [update time] [file name]
```

chmod option  |  meaning
-------- | ------- 
u | user
g | group
o | other
a | all, include u & g & o
r | read file or list directory
w | write file or create/move/delete file in the directory
x | execute or change into the directory 
+ | add permission
- | take away permission

# processes and jobs
command  |  meaning
-------- | ------- 
command & | run command in backgroud
^C | kill the job running in the foreground
^Z | suspend the job runing in the foreground
bg %jobnumber | background the suspended job number jobnumber
jobs | list current jobs
fg %jobnumber | foreground job number jobnumber
kill %jobnumber | kill job number jobnumber
ps | list current processes
kill 26152 | kill process number 26152

# check disk
command | meaning
-|-
quota| current user‘s quota disk space
df . | disk left, how much space left on the file systems
du -s * | disk used, ls the number of kilobytes used by each subdirectory
gzip science.txt | compress science.txt file and named science.txt.gz
gunzip science.txt.gz | uncompress science.txt.gz file and named science.txt
zcat science.txt.gz | read gzipped file without uncompressing
file * | list all files and their type

# variables
command | meaning 
-|-
printenv | print environment variables 
setenv | set environment variables
unsetenv | unset environment variables
set | print shell variables
set p = 1 | set shell variable p store value 1
unset | unset shell variables

 
# 参考
1. [UNIX Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/)