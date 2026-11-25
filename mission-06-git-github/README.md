# Mission 6 — Git and GitHub

## 1. Mission title
Mission 6 — Git and GitHub

## 2. Task / objective
Understand version control, inspect repository status, stage and commit changes, create a feature branch, publish a Pull Request, and document the collaborative Git workflow.

## 3. Work completed
- [x] Inspected repository status, staged specific changes, committed, and verified commit history.
- [x] Created the `update-about` feature branch.
- [x] Added the required "My Learning" section to the root `README.md`.
- [x] Committed the changes and published `update-about` to GitHub.
- [x] Opened Pull Request #1 comparing `update-about` with `main` on GitHub.
- [x] Recorded Pull Request URL (`https://github.com/sleepysam11/digital-detective-8556/pull/1`) and kept it open as instructed.
- [x] Completed the Git workflow comparison and the full 10-operation Git command glossary.

### Task 6.1 — Git workflow operations

| Git operation | What it does in your own words |
|---|---|
| Check repository status (`git status`) | Displays which branch is checked out, which files have been modified or staged, and any untracked files |
| Stage selected changes (`git add <file>`) | Places specific modified or new files into the staging index, preparing them for the next commit snapshot |
| Create a commit (`git commit -m "msg"`) | Records a permanent point-in-time snapshot of the staged changes into the local Git history with a message |
| View commit history (`git log --oneline`) | Displays chronological commits in a condensed single-line format showing short commit hashes and titles |

**Difference between staging and committing:**
Staging (`git add`) acts as a selective preparation area (the index). It allows a developer to choose exactly which modified files or changes should belong to the upcoming logical update. Committing (`git commit`) takes everything currently staged and writes a permanent, cryptographic snapshot into the repository's history along with author information, timestamp, and explanation.

### Task 6.2 — Feature branch `update-about`

Commands used:
```bash
git switch -c update-about
# Added '## My Learning' section to root README.md
git add README.md
git commit -m "Add personal learning summary"
git push -u origin update-about
```

### Task 6.3 — Pull Request

- **Pull Request URL:** `https://github.com/sleepysam11/digital-detective-8556/pull/1`
- **PR Status:** **Open** (kept open as instructed; per assignment guidelines, merge only if specifically directed by the instructor).
- **Why branches and Pull Requests are useful:**
  - A **branch** isolates new features, experiments, or documentation updates from the stable `main` branch. This ensures that ongoing work does not break production code.
  - A **Pull Request (PR)** provides a formal collaborative space where team members review proposed code diffs, leave comments, run automated tests, and ensure code quality before merging into the main codebase.

### Task 6.4 — Git command glossary

| Git operation | Command | What it does in my own words |
|---|---|---|
| Initialise a repository | `git init` | Creates a new empty Git repository in the current folder by setting up the internal `.git` tracking directory |
| Check status | `git status` | Shows which files are modified, untracked, or staged, and identifies the current active branch |
| Stage changes | `git add <file>` | Adds modified or new files to the staging index ready for the next commit |
| Commit changes | `git commit -m "message"` | Saves a permanent snapshot of all staged changes with an explanatory message |
| View history | `git log --oneline` | Displays a clean, chronological history showing commit hashes and commit messages |
| Create a branch | `git branch <name>` | Creates a new branch reference without immediately switching to it |
| List branches | `git branch` | Lists all local branches and marks the currently active branch with an asterisk (`*`) |
| Switch branches | `git switch <name>` | Checks out and switches the working tree to the specified branch |
| Publish changes | `git push origin <branch>` | Uploads local branch commits to the remote repository on GitHub |
| Retrieve remote changes | `git pull` | Fetches the latest commits from the remote repository and integrates them into the local branch |

## 4. Commands / tools used
- `git status`, `git add`, `git commit`, `git log --oneline`, `git switch -c`, `git branch`, `git push -u origin <branch>`, `git pull`.
- GitHub web interface for creating and reviewing Pull Request #1.

## 5. My understanding
Git is a distributed version control system that records changes as an immutable graph of commit snapshots. Branches enable parallel development without conflicts, and Pull Requests facilitate peer review and code quality control before integration into the primary branch.

## 6. Difficulties faced
No major difficulties. The feature branch was published and the Pull Request was successfully opened on GitHub.

## 7. How I resolved them
Followed the standard GitHub compare-and-pull-request flow to open PR #1 and kept it open for review.

## 8. Evidence / files
- Root `README.md` containing the "My Learning" section.
- Pull Request #1: `https://github.com/sleepysam11/digital-detective-8556/pull/1` (visible and open on GitHub).

## 9. Commit details
- Commit message: Complete Mission 6 Git and GitHub guide
- Short commit hash: 47d1d5d
- Pushed to GitHub: Yes
