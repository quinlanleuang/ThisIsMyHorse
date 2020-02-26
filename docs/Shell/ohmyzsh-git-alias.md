[Ohmyzsh-git-plugins](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git/)

# git aliases zsh offers
```shell
gst = git status
g = git
ga = git add
gcam = git commit -am 
gco = git checkout
gcb = git checkout -b
gcm = git checkout master
gcd = git checkout develop
gd = git diff
gf = git fetch
gfo = git fetch origin
ggl = git pull origin "$(current_branch)"
ggp = git push origin "$(current_branch)"
gl = git pull
gp = git push
gm = git merge
gmom = git merge origin/master
gsta = git stash save
gstaa = git stash apply
gstl = git stash list
gstp = git stash pop
grh = git reset
grhh = git reset --hard 
```

# suggestions
```shell
git merge --squash newBranch
git commit -am 'packet as an commit'
```