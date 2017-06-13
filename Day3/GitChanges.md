|[< Previous (Source Code Management)](../Day2/GitOverview.md) | [Day3](../README.md)| [Next (Arrays) >](../README.md) |
|----|----|----|
# Git - Saving your work

We will need to do three things to save your work:
1) Create a place (repository) to save work.
2) Identify which files we are going to save (Stage).
3) Perform the save (commit).

## Create a repository

The first step to saving your work is to create your own local git repository where you can save changes.

### Exercise - Create a local git repository

Open the Git Bash shell (from Program Menu).
Change to directory where you have been working.
```
git init
git status
```

## Stage files

You can't go back and save all your past edits, but we can start saving work now.
Saving files is actually a 2 step process.

Identify what files you want to save. This is done with the git add command. Do this for each of your python files. This is called ```staging```.

```
git add hello-world.py

git status
```

## Commit files

When you commit files it is good to create a short description of what the changes are. This helps when you look back at your history to find certain changes.

```
git commit -m "learn python examples from day 1 and day 2"

git status
```

## Browse your history

Since we haven't shared your git repository with github, you will have to browse with gitk from your bash shell.

## Github repository

If you create a github account, you can create a repository on github for your work. This will make it easy to share with other people.

Login to github and then click on the + next to your name and choose New repository.
In the dialog, make sure you are the owner and then give your repository a name. 
Since we already have the repository locally, we don't want to initialize it with a README.

If you created the Github repository first & cloned, then you could initialize it with a default README file and clone the repository instead of using git init like we did before.

Click Create repository.

Github will give you the commands for your bash shell. We'll use the "push an existing repository from the command line" option.

Copy each command to your git bash shell.

```
git remote add origin https://github.com/yourgithubusername/your-new-repo-name.git
git push -u origin master
```

You should be prompted for your username and password.

Then browse your github repository!

## More changes

From now on, just use git add, git commit and git push
## Git references
https://education.github.com/git-cheat-sheet-education.pdf


|[< Previous (Git Overview)](../Day2/GitOverview.md) | [Day3](../README.md)| [Next (Arrays) >](../README.md) |
|----|----|----|
