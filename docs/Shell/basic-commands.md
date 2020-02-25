- Linux的命令很多是英文缩写，所以用英文的方式取理解和解释命令的含义，更能达意且方便记忆

command  |  meaning
-------- | ------- 
ls |  list files and directories
ls -a | list all files and directories
mkdir | make directory
cd directory | change to name directory
cd | change to home-directory
cd ~ | change to home-directory
cd .. | change to parent directory
pwd | display the path of the current directory
cp file1 file2 | copy file1 and call it file2
mv file1 file2 | move or rename file1 to file2
rm file | remove a file
rmdir directory | remove a directory
cat file | display a file
less file | display a file a page at a time
head file | display the first few lines of a file
tail file | display the last few lines of a file
grep 'keyword' file | search a file for keywords
wc file | count number of lines/words/characters in file
command > file | redirect standard output to a file
command >> file | append standard output to a file
command < file | redirect standard input from a file
command1 \| command2 |pip the output of command1 to the input fo command2
cat file1 file2 > file0 | concatenate file11 file2 to file0
sort | sort data
who | list users currently logged in
* | match any number of characters
? | match one character
man command | read the online manual page for a command
whatis command | brief description of a command
apropos command | match commands with keyword in their man pages
chmod | change access rights for named file
command & | run command in backgroud
^C | kill the job running in the foreground
^Z | suspend the job runing in the foreground
bg | background the suspended job
jobs | list current jobs
fg %1 | foreground job number 1
kill %1 | kill job number 1
ps | list current processes
kill 26152 | kill process number 26152

# 参考
1. [UNIX Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/)