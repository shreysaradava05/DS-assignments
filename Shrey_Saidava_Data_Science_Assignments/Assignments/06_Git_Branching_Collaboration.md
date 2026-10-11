# Assignment 1.6 — Git Branching and Collaboration
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Start FoodieReview
```bash
mkdir FoodieReview
cd FoodieReview
git init
echo "# FoodieReview" > README.md
git add README.md
git commit -m "Initial commit for FoodieReview"
```
Connect the local project to a new GitHub repository and push `main` using the commands from Assignment 1.4.

## 2. Create a rating feature branch
```bash
git switch -c feature-rating
echo "rating = 5" > rating.py
git add rating.py
git commit -m "Add rating feature"
git push -u origin feature-rating
```

## 3. Simulate a conflict
On `main`, edit the same line in `rating.py` and commit it. Then edit that line differently on `feature-rating`. When merging, Git may show conflict markers. I should open the file, choose the correct final content, and remove the markers.

## 4. Resolve and push
```bash
git add rating.py
git commit -m "Resolve rating feature merge conflict"
git push
```
If the merge is in progress, the commit records the resolved file. A pull request can then be opened on GitHub.

## 5. Fork an open-source project
I can fork a project on GitHub, clone my fork, create a branch, add a short `INDIAN_USERS.md` file describing Indian language support, local payment options, and low-bandwidth support, then push the branch and open a pull request. I should follow the original project’s contribution rules.
