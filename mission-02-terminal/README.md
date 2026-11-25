# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
Practise navigating folders, listing files, creating and copying files, renaming files, displaying text, appending text, and using a pipe. All practice must stay inside this repository.

## 3. Work completed
- [x] Added a safe command sequence for the practice activity.
- [ ] Run the commands on the Mac from the repository root.
- [ ] Confirm that the notes file contains both lines and the backup file exists.
- [ ] Compare normal and detailed directory listings.
- [ ] Check Homebrew only if it is already installed.

## 4. Commands / tools used
Run one command at a time from the repository root:

```bash
pwd
ls
ls -lah
cd mission-02-terminal
mkdir -p terminal-practice
touch terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/notes-copy.txt
mv terminal-practice/notes-copy.txt terminal-practice/notes-backup.txt
printf "First line\n" > terminal-practice/notes.txt
printf "Second line\n" >> terminal-practice/notes.txt
cat terminal-practice/notes.txt
ls -lah | head -n 5
```

Expected text in `notes.txt`:

```text
First line
Second line
```

Command meanings:
- `pwd`: prints the current working directory.
- `ls`: lists directory entries.
- `ls -lah`: lists entries in long format, includes hidden entries, and uses human-readable sizes.
- `cd`: changes the current directory.
- `mkdir -p`: creates a directory and does not complain if it already exists.
- `touch`: creates an empty file if it does not exist.
- `cp`: copies a file.
- `mv`: moves or renames a file.
- `>`: writes output and replaces the file's previous contents.
- `>>`: appends output to the end of a file.
- `cat`: prints file contents.
- `|`: sends one command's output to another command.
- `head -n 5`: displays the first five lines.

Check Homebrew safely:

```bash
brew --version
```

Only if that command reports that Homebrew is installed, run:

```bash
brew list
```

Do not install or uninstall software for this task. If `brew` is not found, record that Homebrew is not installed or not on the command path.

## 5. My understanding
The Terminal accepts text commands to work with files and folders. Relative paths are interpreted from the current directory. Redirection controls whether command output replaces or appends to a file, and a pipe connects commands so that one command can process another command's output.

## 6. Difficulties faced
The commands have not yet been run on the student's Mac, so actual errors or difficulties are not recorded here.

## 7. How I resolved them
Run each command from the stated starting directory. If a command fails, check the current directory with `pwd` and the available files with `ls` before trying again.

## 8. Evidence / files
- Pending local evidence: `terminal-practice/notes.txt` and `terminal-practice/notes-backup.txt`.
- Do not add screenshots containing private paths or usernames.

## 9. Commit details
- Commit message: Complete Mission 2 terminal guide
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
