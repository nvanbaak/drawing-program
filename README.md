# drawing-program
draws various shapes


# Git workflow

1.  When starting a new feature, use `git checkout main`, then `git pull` to make sure you're current.
2.  Create a new branch with `git checkout -b yourinitials/nameofbranch`
3.  Commit changes as usual while you work.  When your feature is ready, push to github.  `git push -u origin HEAD` will tell Github you're starting a new commit history for your branch; you can just do `git push` afterward.
4.  Before you make a pull request, checkout `main`, do a pull, then checkout your branch again.  Once you're in your branch, `git merge main` will merge main into your branch.  Once the code is merged, do one more push, then make a pull request on the repo.
