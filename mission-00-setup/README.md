# Mission 0 — Create your GitHub workspace

## 1. Mission title
Mission 0 — Create your GitHub workspace

## 2. Task / objective
Prepare an organised project repository, check the installed Python and Git versions, inspect project paths and structure, and verify that the mission structure is published on GitHub.

## 3. Work completed
- [x] Confirmed this public repository exists and uses the `main` default branch.
- [x] Confirmed the repository contains the nine mission folders and their README templates.
- [x] Executed version, path, and folder-inspection commands and recorded real outputs.
- [x] Confirmed the local folder and remote repository are correctly connected.
- [x] Verified the initial commit and current branch in the local Git history.

**Repository naming and privacy:** The repository is named `digital-detective-8556` following the required naming rule (assignment name + hyphen + last four digits of USN). Personal usernames and identifying file system paths are redacted with `[user]` or `[redacted]` to protect privacy.

## 4. Commands / tools used
Commands executed from the local repository root:

```bash
python3 --version
git --version
pwd
find . -maxdepth 2 -type f
git status
git remote -v
```

### Real outputs recorded

**Python & Git versions:**
```text
$ python3 --version
Python 3.14.7

$ git --version
git version 2.54.0 (Apple Git-157)
```

**Current working directory (`pwd`):**
```text
$ pwd
/Users/[user]/.../digital-detective-8556
```

**Project file hierarchy (`find . -maxdepth 2 -type f`):**
```text
$ find . -maxdepth 2 -type f | sort
./.gitignore
./README.md
./evidence/README.md
./mission-00-setup/README.md
./mission-01-computer-basics/README.md
./mission-02-terminal/README.md
./mission-03-operating-system/README.md
./mission-04-programs/README.md
./mission-04-programs/hello.py
./mission-05-numbers-data/README.md
./mission-05-numbers-data/number_converter.py
./mission-06-git-github/README.md
./mission-07-networking/README.md
./mission-08-final-report/README.md
```

**Repository status (`git status`):**
```text
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**Remote configuration (`git remote -v`):**
```text
$ git remote -v
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
- `evidence/mission-00-versions.txt` recorded.
- Repository confirmed public on GitHub at `https://github.com/sleepysam11/digital-detective-8556`.

## 9. Commit details
- Commit message: Complete Mission 0 setup documentation
- Short commit hash: a88cf6d
- Pushed to GitHub: Yes
