# Assignment 1.4 — Git Installation and Fundamentals
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Install and check Git
Install Git from https://git-scm.com/downloads. Open Terminal or Command Prompt and run:
```bash
git --version
```

## 2. Set username and email
```bash
git config --global user.name "Shrey Saidava"
git config --global user.email "YOUR-GITHUB-EMAIL"
git config --global --list
```
Replace the email with the email I use for GitHub.

## 3. Create a local repository
```bash
mkdir MyProject
cd MyProject
git init
```
The `.git` folder stores Git history and configuration for the repository. It is normally hidden.

## 4. Clone a public repository
```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
ls
```
On Windows Command Prompt, `dir` can be used instead of `ls`.

## 5. Create and push a wishlist
Create `wishlist.txt` with a few items, then run:
```bash
git add wishlist.txt
git commit -m "Add wishlist items"
git status
```
Create a new empty GitHub repository, connect it, and push:
```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/wishlist.git
git push -u origin main
```
I should make small commits that describe one clear change each.
