# Mission 0 — Create your GitHub workspace

## 1. Mission title
Mission 0 — Create your GitHub workspace

## 2. Task / objective
Prepare an organised project repository, check the installed Python and Git versions, and verify that the mission structure is available on GitHub.

## 3. Work completed
- [x] Confirmed this public repository exists and uses the `main` default branch.
- [x] Confirmed the repository contains the nine mission folders and their README templates.
- [x] On the Mac, run the version and folder-inspection commands below and record the actual results.
- [x] Confirm the local folder and remote repository are correctly connected.
- [x] Verify the initial commit and current branch in the local Git history.

**Repository naming and privacy:** The repository is named `digital-detective-8556` following the naming rule (assignment name + hyphen + last four digits of USN). In public documentation, personal usernames and identifying paths are redacted to protect privacy.

## 4. Commands / tools used
Commands executed from the local repository folder:

```bash
python3 --version
git --version
pwd
find . -maxdepth 2 -type f
git status
git remote -v
```

**Real outputs recorded:**

```
Python 3.14.7
git version 2.54.0 (Apple Git-157)
```

Remote configuration verified:
```
origin  https://github.com/sleepysam11/digital-detective-8556 (fetch)
origin  https://github.com/sleepysam11/digital-detective-8556 (push)
```

A repository stores project files together with their change history. Git records changes as commits, while GitHub hosts a remote copy so work can be backed up and shared. Mission folders keep work organised by topic and make progress easier to review.

## 5. My understanding
A repository is a tracked folder that preserves every version of every file alongside commit descriptions and author metadata. Organising the project into mission-specific directories prevents accidental cross-topic contamination and enables clear, incremental commits corresponding to each stage of the assignment.

## 6. Difficulties faced
No major difficulties. Both Python 3 and Git were pre-installed and available on the macOS system path.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- Confirmed all 9 mission folders (`mission-00-setup` through `mission-08-final-report`) and `evidence/` directory exist.
- Python 3.14.7 and Git 2.54.0 outputs verified.
- Repository confirmed public on GitHub at `https://github.com/sleepysam11/digital-detective-8556`.

## 9. Commit details
- Commit message: Complete Mission 0 setup documentation
- Short commit hash: a88cf6d
- Pushed to GitHub: Yes
