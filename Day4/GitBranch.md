|[< Previous (Simple Plotting)](../Day3/SimplePlotting.md) | [Day4](../README.md)| [Next (Data Analysis) >](DataAnalysis.md) |
|----|----|----|
# Git - Collaboration

Git is a powerful tool for collaboration. It allows team members to work on their own copies and then easily combine or ```merge``` their work together.

The biggest challenge of collaboration is making sure everyone's contributions are correctly combined in an orderly fashion. Git enforces this my making sure you commit your changes on the latest version.

If you already have the code cloned, you can get the latest version by using the ```git pull``` command. This is also equivalent to using ```git fetch``` and ```git merge```.

Because team members are working independently, multiple people may make changes and then when you try to merge (pull), you find a ```conflict``` where the same file has been changed. If git determines that the changes are in different parts of the file, it will just combine them. You should still check that the code executes as expected after this type of merge.

Sometimes git isn't sure how to fix the conflict. In this case, an individual needs to manually review the changes from both versions and determine what the combined result should look like. A good tool to show this helps this process. TortoiseGit has a diff tool. Another excellent choice is meld (http://meldmerge.org). You tell git the name of your merge tool with the command ```git mergetool path-to-difftool.exe```

## Branches

Another way to help minimize conflicts, is to create a ```branch``` for your work. So far, we have worked on the ```master``` branch. If each person creates a branch for their work, conflicts don't arise until you *finish* your task and are ready to have everyone adopt it. This also allows you to wait to adopt other people's work until you have completed the task. It is like a limited access highway where you get on and off at specific points in time. You can also have many branches and can easily switch between them without losing work in progress - although trying to juggle too many at once can just be confusing.

To create a branch, use ```git branch newbranchname```, then ```git checkout newbranchname``` or the shortcut that combines these ```git checkout -b newbranchname```

### Exercise

Create a new branch:

```
git branch branchtesting
git checkout branchtesting
git status
```

change some files, then commit them

```
git checkout master
git status
```

check the files changed before - they should be back to their original version.

```
git checkout branchtesting
git push origin branchtesting
git status
```

Check your github repository and see you have branches. Click around the repository to see how to look at the branches.

If you want to keep the changes, create a github pull request to see what the differences from your master branch are.

To understand more about branching, and git, visit (https://services.github.com/on-demand/)
and go through the lessons.

|[< Previous (Simple Plotting)](../Day3/SimplePlotting.md) | [Day4](../README.md)| [Next (Data Analysis) >](DataAnalysis.md) |
|----|----|----|
