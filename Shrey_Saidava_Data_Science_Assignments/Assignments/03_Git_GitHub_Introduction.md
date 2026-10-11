# Assignment 1.3 — Git and GitHub Introduction
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Three public data-science repositories
Examples to explore:
- **pandas** — tools for working with tables and datasets: https://github.com/pandas-dev/pandas
- **scikit-learn** — machine-learning tools: https://github.com/scikit-learn/scikit-learn
- **matplotlib** — charts and visualisation: https://github.com/matplotlib/matplotlib

## 2. Clone an open repository
```bash
git clone https://github.com/pandas-dev/pandas.git
cd pandas
git status
```
Cloning downloads a copy of the repository to my computer. `git status` shows the current working-tree state.

## 3. Make the first commit for InstaCloneDemo
```bash
mkdir InstaCloneDemo
cd InstaCloneDemo
git init
echo "# InstaCloneDemo" > README.md
git add README.md
git commit -m "Initial commit for InstaCloneDemo"
```
To push it, create an empty GitHub repository named `InstaCloneDemo`, then connect and push:
```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/InstaCloneDemo.git
git push -u origin main
```
Replace `YOUR-USERNAME` with my GitHub username.
