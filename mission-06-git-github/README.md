# Mission 6 — Git and GitHub

## 1. Mission title
Mission 6 — Git and GitHub

## 2. Task / objective
Practise Git status, staging, commits, history, branches, pushing, and Pull Requests.

## 3. Work completed
- [x] Added explanations of the Git workflow.
- [x] Created the `update-about` branch on GitHub for this assignment work.
- [x] Added a “My Learning” section to the root README on the branch.
- [ ] Inspect the branch and commit history in the local clone.
- [ ] Create or review the Pull Request into `main` and record its URL.
- [ ] Merge only if the instructor specifically requires it.

## 4. Commands / tools used
Run these from the repository root in your local clone:

```bash
git status
git add mission-06-git-github/README.md
git commit -m "Document Git and GitHub workflow"
git log --oneline
git switch update-about
git status
git push -u origin update-about
```

The branch and file changes for this prepared work are published on GitHub. If the branch already exists locally, switch to it with `git switch update-about`. If it does not exist locally, use `git fetch origin` followed by `git switch --track origin/update-about`.

### Command explanations
- `git status`: shows changed, staged, and untracked files.
- `git add`: stages selected changes for the next commit.
- `git commit`: saves a snapshot of staged changes in the repository history.
- `git log --oneline`: displays a compact commit history.
- `git switch`: changes the current branch.
- `git push`: sends local commits to the remote repository.
- A **branch** is an independent line of development.
- A **Pull Request (PR)** proposes merging changes from one branch into another and allows review before integration.

Staging selects the changes that will go into a commit; committing records those staged changes in Git history. Pushing publishes commits to a remote host such as GitHub.

## 5. My understanding
Git tracks changes locally, while GitHub hosts remote repositories. Small, meaningful commits make progress easier to understand. Branches allow work to be prepared separately from the main branch, and Pull Requests provide a place to review proposed changes before merging.

## 6. Difficulties faced
Local Git status and the Pull Request review/merge status still need to be checked in the student's clone and GitHub account.

## 7. How I resolved them
Use the commands above and check the Pull Request page. Do not report a PR as merged unless GitHub shows that it has actually been merged.

## 8. Evidence / files
- Root `README.md` — includes the “My Learning” section on this branch.
- This README — Git command explanations.
- Pending: Pull Request URL and status.

## 9. Commit details
- Commit message: Complete Mission 6 Git and GitHub guide
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
