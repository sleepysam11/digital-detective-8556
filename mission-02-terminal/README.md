# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
<!-- Summarise the mission objective in your own words. -->

## 3. Work completed
- [ ] Practise each command inside this repository only.
- [ ] Create `terminal-practice/`, a text file, a copy and a renamed backup.
- [ ] Add a second line without removing the first line.
- [ ] Compare a normal listing with a detailed listing that includes hidden files and human-readable sizes.
- [ ] Pipe a detailed listing to a command that shows only the first few lines.
- [ ] Check Homebrew only if it is already installed; do not install or uninstall anything.

## 4. Commands / tools used
Command reference to practise one at a time:
```bash
pwd
ls
ls -lah
cd ..
mkdir terminal-practice
touch terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/notes-copy.txt
mv terminal-practice/notes-copy.txt terminal-practice/notes-backup.txt
cat terminal-practice/notes.txt
printf "First line\n" > terminal-practice/notes.txt
printf "Second line\n" >> terminal-practice/notes.txt
ls -lah | head -n 5
brew --version
brew list
```

Do not run `brew list` unless Homebrew is already installed. Record what you actually observed, and do not paste private paths or usernames.

## 5. My understanding
<!-- Explain the concepts in your own words. What did you observe, and why does it matter? -->

## 6. Difficulties faced
<!-- Describe actual errors, confusing steps or unexpected results. If none, write: No major difficulties. -->

## 7. How I resolved them
<!-- Explain what you did to resolve each difficulty. If none, write: Not applicable. -->

## 8. Evidence / files
<!-- List the files, screenshots or privacy-safe outputs included in this folder. -->

## 9. Commit details
- Commit message: <!-- actual message -->
- Short commit hash: <!-- actual hash -->
- Pushed to GitHub: <!-- Yes/No, after verifying -->
