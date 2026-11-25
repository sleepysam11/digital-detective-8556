# Mission 6 — Git and GitHub

## 1. Mission title
Mission 6 — Git and GitHub

## 2. Task / objective
The objective of this mission was to practise core Git workflow operations — checking status, staging, committing and reading history — then create a feature branch, add content, push the branch to GitHub, and open a Pull Request from that branch into `main`.

## 3. Work completed
- [x] Check repository status, stage a specific README, commit and inspect history.
- [x] Create the `update-about` branch.
- [x] Add a "My Learning" section to the root README.
- [x] Commit and push the branch.
- [x] Create a Pull Request from `update-about` into `main`.
- [x] Record the actual PR URL and whether it was merged.
- [x] Explain each Git command in my own words.

### Commands run

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

$ git add mission-06-git-github/README.md
$ git commit -m "Complete Git and GitHub collaboration mission"
$ git log --oneline
# (shows commit history with short hashes)

$ git switch -c update-about
Switched to a new branch 'update-about'

$ git add README.md
$ git commit -m "Add personal learning summary"
$ git push -u origin update-about
```

A Pull Request was then created on GitHub from the `update-about` branch into `main`.

**Pull Request URL:** `https://github.com/sleepysam11/digital-detective-8556/pull/1`

The PR was left open (not yet merged) as per the instructions — merge only if instructed by the teacher.

### Git command explanations

| Command | What it does |
|---|---|
| `git status` | Shows which files have changed, which are staged and which branch I am on |
| `git add <file>` | Stages a specific file — adds it to the "ready to commit" area (the staging index) |
| `git commit -m "message"` | Saves a permanent snapshot of all staged changes with a descriptive message |
| `git log --oneline` | Shows the commit history as one line per commit — hash + message |
| `git switch -c update-about` | Creates a new branch called `update-about` and immediately switches to it |
| `git push -u origin update-about` | Pushes the branch to GitHub and sets it as the upstream tracking branch |

### Staging vs committing

**Staging** (also called the index) is a holding area where I select exactly which changes to include in the next commit. I can stage some files and leave others unstaged.

**Committing** takes everything in the staging area and saves it as a permanent snapshot in the repository history. The commit stores who made it, when and what message was given.

This two-step process is useful because it lets me group related changes together into one meaningful commit, even if I changed many files in one working session.

### Why branches and Pull Requests help collaboration

A **branch** lets me work on new content or a fix without touching the main stable code. While I work on `update-about`, the `main` branch stays clean and unchanged.

A **Pull Request (PR)** is a formal request to merge one branch into another. It lets a team member review the changes before they enter `main`. This catches mistakes and keeps a clear review history. Even working alone, PRs are good practice.

### Task 6.4 — Git command glossary

| Git operation | Command | What it does in my own words |
|---|---|---|
| Initialise a repository | `git init` | Creates a new empty Git repository in the current folder — sets up the `.git` tracking folder |
| Check status | `git status` | Shows which files have changed, which are staged ready to commit, and which branch I am on |
| Stage changes | `git add <file>` | Adds a file (or all changes with `.`) to the staging area — marks it as ready to be committed |
| Commit changes | `git commit -m "message"` | Saves a permanent snapshot of all staged changes with a description of what was done |
| View history | `git log --oneline` | Shows a compact list of all commits — one line each with the short hash and message |
| Create a branch | `git branch <name>` | Creates a new branch at the current commit without switching to it |
| List branches | `git branch` | Lists all local branches; the current branch is highlighted with `*` |
| Switch branches | `git switch <name>` | Moves to a different branch so I can work on it |
| Publish changes | `git push origin <branch>` | Uploads the local commits on the named branch to the remote repository on GitHub |
| Retrieve remote changes | `git pull` | Downloads the latest commits from GitHub and merges them into the current local branch |

## 4. Commands / tools used

| Command | Purpose |
|---|---|
| `git status` | Check current branch and file states |
| `git add` | Stage specific files |
| `git commit -m` | Record a snapshot with a message |
| `git log --oneline` | View compact commit history |
| `git switch -c` | Create and switch to a new branch |
| `git push -u origin` | Push branch to GitHub and set upstream |
| GitHub web interface | Create the Pull Request visually |

## 5. My understanding
Git is a version-control system that tracks every change I make to files. Each commit is like a save point I can return to. Branches let me experiment or add features without risking the stable version. GitHub hosts the repository online so it is backed up and shareable. The Pull Request workflow is the standard way teams review code before merging — it creates a discussion thread and shows exactly what lines changed.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- Commit history visible in `git log --oneline`.
- `update-about` branch visible on GitHub.
- Pull Request opened at `https://github.com/sleepysam11/digital-detective-8556/pull/1`.

## 9. Commit details
- Commit message: Complete Git and GitHub collaboration mission
- Short commit hash: 0d13673
- Pushed to GitHub: Yes
