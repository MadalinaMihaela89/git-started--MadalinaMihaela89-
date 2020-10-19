# Gitting around

## Story

This project is about familiarizing yourself with git. You will move around in a repository with multiple branches (you won't need to create these) to solve different tasks. By solving these tasks you will gain confidence in your knowledge about git repository structure and how to use the more advanced features for profit!

To be able to solve the exercises you will first need to learn how to list branches and switch to them as the exercises for the tasks can be found on the branches.

## What are you going to learn?

You will learn:

- Git history
- Git branch structure
- Shell basics

## Tasks

1. Setup passwordless use of git on your machine and GitHub account by using `SSH`.
    - Executing `git config --get remote.origin.url` in shell in student's repo shows a response that starts with: `git@...`
    - Executing `git fetch` in shell in student's repo doesn't ask for username/password

2. Initialize your repository by running the init script - `bash ./helper/init`
    - Executing the command `git branch` in shell gives the following output:
```
collect-files
find-secret
* development
remote-change
resolve-conflict
size-history
```

3. Switch to `remote-change` branch and pull the changes from the remote
    - After executing `git checkout remote-change` executing `git log` shows a new merge commit starting with: "Merge branch 'remote-change' ..." on the top of the output
    - After executing `git checkout remote-change` executing `git status` shows the following output:
```
On branch remote-change
Your branch is ahead of 'origin/remote-change' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

4. Switch to `resolve-conflict` branch and pull the changes from the remote and resolve conflicts
    - After executing `git checkout resolve-conflict` executing `cat work.txt` should result in:
```
I work
I rest after I work
```
    - After executing `git checkout resolve-conflict` git log should show a new merge commit starting with:
"Merge branch 'resolve-conflict' ..."

5. Find the secret about the meaning of 42 by investigating the git history of the `find-secret` branch
    - Student knows what 42 means in programming

6. On `size-history` branch there are multiple commits changing the `names.txt` file. Find all versions of `names.txt` and collect the size (in bytes) for each version. Collect all sizes of `names.txt` and put all the sizes starting from the oldest version, separated by commas in a file called `result.txt` and commit it.
    - Executing `git log --name-only` after executing `git checkout size-history` shows a new commit adding `result.txt`
    - Commit message is meaningful and describing the action well
    - Executing `cat result.txt` after executing `git checkout size-history` in the shell shows a 5 elements list starting with 35, ending with 89

7. On `collect-files` branch there were several files created, some still exist. Find all file names that ever existed on the branch and put all the names separated by commas in a file called `result.txt` and commit it.
    - After executing `git checkout collect-files` you can see that the last commit message is meaningful and describing the action well
    - Executing `git log --name-only` after executing `git checkout collect-files` shows a new commit adding `result.txt`
    - Executing `cat result.txt` after executing `git checkout collect-files` in the shell shows 12 (or 14 if `.` and `..` are included) lines.

## General requirements

None

## Hints

- Always make sure that you are on the correct branch when working on an exercise
- Think about how to automate repetitive steps
- Git log has several command line arguments, try `git log --oneline` for more succint view of the current branch's history

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/gitting-around/general).

## Background materials

- <i class="far fa-exclamation"></i> [Moving around branches](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)
- <i class="far fa-exclamation"></i> [Branches in a nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- <i class="far fa-exclamation"></i> [Git without password](../pages/git/git-passwordless.md)
- <i class="far fa-exclamation"></i> [Bash commands and arguments](https://mywiki.wooledge.org/BashGuide/CommandsAndArguments)
- <i class="far fa-open_book"></i> [Bash pattern matching](https://mywiki.wooledge.org/BashGuide/Patterns)
- <i class="far fa-open_book"></i> [Mastering git](https://learn.code.cool/full-stack/#/../pages/git/mastering-git)
