|[< Previous (Debugging)](Debugging.md) | [Day2](../README.md)| [Next (Day 3) >](../README.md) |
|----|----|----|
# Source code management

Developing software is an iterative and collaborative process. It is easy to break something that use to work and there can be lots of files to share. E-mail and even share drives are not the best way to keep track of different versions. Software developers use tools called "version control system" or "source code control system" to do this. You might hear about systems like ```Git```, ```SVN``` (or Subversion), ```Perforce``` and ```CVS``` (Concurrent Versions System). ```Github``` provides Git features and a web interface for some operations, especially browsing the repository.

The ```repository``` is the location where you save versions of your software using specialized commands. 

## Git
One of the current, powerful and popular tools is Git. Git is a distributed, version control system. It is distributed because developers can share code in many different ways, but we'll focus on just some simple basic commands.

Most people start by ```cloning``` an existing repository. Cloning is making your local copy.

### Exercise - Clone a repository

Open the Git Bash shell (from Program Menu).
Change to directory where you want to copy the course materials.
```
cd
mkdir GRC-SummerSchool
cd GRC-SummerSchool
```

Clone the presentation materials from github.com.
```
git clone https://github.com:GRC-SummerSchool/learn-python.git
```

Browse the new directory with Windows Explorer.
Now move into the new directory:
```
cd learn-python
```

## Browsing a repository

There are git tools to look back at past work and compare versions. Every version is called a ```commit```. They are referenced by hexadecimal strings, but most people will use github or a git client tool to browse. 


### Exercise - Browse history
In github, click on the <> Code tab and then on the "## commits" to see the history or work creating this tutorial.

From you Git bash shell, type gitk to open a client window to browse as well.

## Changing files

Changing code locally only affects you. You can change the code and then look at your changes. If you don't want to keep them, you can ```checkout``` the repository again to clean up (or even delete your directory & clone again).

### Exercise - Check changes
Make a change, add a file, edit an existing file, create a new directory.

From your git bash shell window, let's see what changes you made:
```
git status
```

This will return information about files you changed or added.

## Git references
https://education.github.com/git-cheat-sheet-education.pdf


|[< Previous (Debugging)](Debugging.md) | [Day2](../README.md)| [Next (Day 3) >](../README.md) |
|----|----|----|
