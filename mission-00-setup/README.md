# Mission 0 — Create your GitHub workspace

## 1. Mission title
Mission 0 — Create your GitHub workspace

## 2. Task / objective
The objective of this mission was to set up a properly named GitHub repository for the entire assignment, verify that Python 3 and Git are installed and working, confirm all mission folders exist, and push the initial structure to GitHub so all future work can be version-controlled.

## 3. Work completed
- [x] Rename the local folder and GitHub repository to `digital-detective-8556`.
- [x] Check `python3 --version` and `git --version`; record the real outputs.
- [x] Confirm all mission folders and files exist.
- [x] Create a public GitHub repository with the same name and push the initial structure.
- [x] Verify the repository and initial commit on GitHub.

The repository was renamed to `digital-detective-8556` (last four digits of USN: 8556). All nine mission folders plus the evidence folder were created and confirmed present. The initial structure was pushed to GitHub and verified online.

## 4. Commands / tools used

```bash
python3 --version
git --version
pwd
find . -maxdepth 2 -type f
git status
```

**Real outputs recorded:**

```
Python 3.14.7
git version 2.54.0 (Apple Git-157)
```

A repository is a folder tracked by Git that stores every version of every file, along with who changed what and when. The project is organised by mission folder so each topic stays separate and each commit is easy to understand. No setup issues were encountered — Python 3 and Git were already installed on macOS.

## 5. My understanding
A GitHub repository is like a save-history for an entire project. Every time I commit, Git takes a snapshot of the files, so I can always go back to an earlier version if something goes wrong. Organising the work into separate mission folders means each topic is isolated, which makes it easier to review or fix one part without affecting the others.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `find . -maxdepth 2 -type f` confirmed all mission folders and README files are present.
- Repository verified as public on GitHub at `https://github.com/sleepysam11/digital-detective-8556`.

## 9. Commit details
- Commit message: Add mission-00-setup/README.md
- Short commit hash: e887c8d
- Pushed to GitHub: Yes
