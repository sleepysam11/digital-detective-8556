# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
Practise navigating folders, listing files, creating and copying files, renaming files, displaying text, appending text, and using a pipe. All practice must stay inside this repository.

## 3. Work completed
- [x] Added a safe command sequence for the practice activity.
- [x] Added `terminal-practice/notes.txt` with the required two lines.
- [x] Added `terminal-practice/notes-backup.txt`, representing the renamed backup copy.
- [ ] Run the commands on the Mac and compare the actual Terminal output.
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
printf "First line\n" > terminal-practice/notes.txt
printf "Second line\n" >> terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/notes-copy.txt
mv terminal-practice/notes-copy.txt terminal-practice/notes-backup.txt
cat terminal-practice/notes.txt
ls -lah | head -n 5
```

Expected text in both `notes.txt` and `notes-backup.txt`:

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
No Terminal error has been reported. The command sequence still needs to be run on the Mac so the student can confirm the observed output.

## 7. How I resolved them
The required practice text files are included in this folder. Run the commands in Section 4 locally to practise each command and confirm that the files match the expected contents.

## 8. Evidence / files
- `terminal-practice/notes.txt` — contains the first and second lines.
- `terminal-practice/notes-backup.txt` — renamed backup copy.
- Pending: privacy-safe screenshot or notes of the commands run locally.
- Do not add screenshots containing private paths or usernames.

## 9. Commit details
- Commit message: Add Mission 2 terminal practice files
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
