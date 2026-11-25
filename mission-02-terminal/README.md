# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
Use the command-line interface (CLI) to inspect directories, create and manage practice files safely, understand flags and pipes, and explain package managers. All file-management practice was performed strictly inside this repository.

## 3. Work completed
- [x] Practised navigation, listing, creation, copying, moving, viewing, and appending commands one at a time.
- [x] Created `terminal-practice/` inside `mission-02-terminal/`.
- [x] Created `notes.txt` inside `terminal-practice/`, added first line, then appended second line without removing the first.
- [x] Made a copy (`notes-copy.txt`) and renamed it to `notes-backup.txt`. Both files contain the verified two lines.
- [x] Compared basic `ls` with detailed `ls -lah` including hidden entries and human-readable sizes.
- [x] Piped detailed directory listing to `head -n 5` and explained the pipeline mechanism.
- [x] Checked Homebrew package manager version and verified package manager utility.

### Task 2.1 — Basic Terminal operations table

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (`pwd`) | Displays the absolute file system path of the current working directory | Displayed `/Users/.../digital-detective-8556` confirming the active working folder |
| Directory listing (`ls`) | Lists visible files and folders in the current directory | Displayed directory names and README files in simple column format |
| Detailed listing (`ls -lah`) | Lists all entries including hidden files with file permissions, owner, size, and timestamp | Displayed permissions (`drwxr-xr-x`), file sizes (e.g. `23B`), dates, and hidden entries like `.git` and `.gitignore` |
| Change directory (`cd ..` / `cd <dir>`) | Changes the current working directory to the target path | Terminal prompt updated and `pwd` reflected the new relative location |
| Create directory (`mkdir -p terminal-practice`) | Creates a new directory at the specified path | Folder `terminal-practice/` was created without error |
| Create empty file (`touch notes.txt`) | Creates a new empty file or updates the modification timestamp | Created `notes.txt` with initial size of 0 bytes |
| Copy file (`cp notes.txt notes-copy.txt`) | Duplicates the source file to a new target path | Created an identical second file leaving the original intact |
| Move / rename file (`mv notes-copy.txt notes-backup.txt`) | Moves or renames a file to a new path | `notes-copy.txt` was renamed to `notes-backup.txt` at the same location |
| Display file contents (`cat notes.txt`) | Concatenates and prints file contents to standard output | Output both lines ("First line" and "Second line") to the terminal screen |

### Task 2.2 — Practise file changes safely & Questions answered

Commands executed:
```bash
cd mission-02-terminal
mkdir -p terminal-practice
touch terminal-practice/notes.txt
printf "First line\n" > terminal-practice/notes.txt
printf "Second line\n" >> terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/notes-copy.txt
mv terminal-practice/notes-copy.txt terminal-practice/notes-backup.txt
cat terminal-practice/notes.txt
```

Verified file contents in both `notes.txt` and `notes-backup.txt`:
```text
First line
Second line
```

**Questions answered:**
- **Replacing vs adding to end:** The `>` redirection operator overwrites (replaces) any existing content in the destination file with new output. The `>>` redirection operator appends new output to the end of the destination file while preserving all existing lines.
- **Copying vs moving:** Copying (`cp`) creates a separate, independent duplicate of the source file, preserving the original at its source location. Moving (`mv`) renames or transfers the file to a new location without creating a duplicate; the original location no longer contains the file under its previous name.
- **What `pwd` provides:** `pwd` (print working directory) returns the complete, unambiguous absolute path from the root directory `/` to the current folder, ensuring the user knows exactly where subsequent relative commands will take effect.
- **Why directory listing is useful:** `ls` confirms file presence, names, hierarchy, permissions, and sizes before executing modifications, deletions, or program executions, preventing mistakes.

### Task 2.3 — Flags and pipes explained

**Comparison of `ls` vs `ls -lah`:**
- A simple `ls` lists only visible file names.
- Flags modify command behaviour: `-l` produces long-format listing (permissions, link count, owner, group, byte size, timestamp); `-a` includes hidden files (entries starting with `.`, such as `.gitignore` and `.git`); `-h` renders byte counts into human-readable units (e.g. `23B`, `4.0K`, `1.2M`).

**Pipes demonstration (`ls -lah | head -n 5`):**
```bash
$ ls -lah | head -n 5
total 16
drwxr-xr-x@ 15 [user]  staff   480B Nov 26 00:34 .
drwxr-xr-x@  7 [user]  staff   224B Nov 25 23:50 ..
drwxr-xr-x@ 14 [user]  staff   448B Nov 26 00:34 .git
-rw-r--r--@  1 [user]  staff    51B Nov 25 23:50 .gitignore
```
- The pipe operator (`|`) redirects the standard output (stdout) of the command on the left into the standard input (stdin) of the command on the right without writing to an intermediate temporary file.
- The left side (`ls -lah`) generates the complete detailed directory stream.
- The right side (`head -n 5`) filters the stream and outputs only the first 5 lines.

### Task 2.4 — Package managers

Homebrew inspection output on macOS:
```bash
$ brew --version
Homebrew 7.0.12
```

**Why package managers are useful:**
A package manager automates the downloading, dependency resolution, installation, updating, and uninstallation of software libraries and command-line tools from centralised repositories. Instead of manually searching websites, compiling binaries, and managing shared library conflicts, a package manager ensures software packages and their prerequisites remain consistent, secure, and up to date with simple commands.

## 4. Commands / tools used
- `pwd`, `ls`, `ls -lah`, `cd`, `mkdir -p`, `touch`, `cp`, `mv`, `cat`, `>`, `>>`, `|`, `head -n 5`, `brew --version`.

## 5. My understanding
The command line provides direct, scriptable control over files and directories. Redirection symbols (`>` vs `>>`) distinguish between destructive overwriting and cumulative appending. Pipes permit composition of simple single-purpose tools into powerful processing chains. Flags adjust the depth and format of command responses.

## 6. Difficulties faced
No major difficulties. All file modifications were tested and confirmed inside `mission-02-terminal/terminal-practice/`.

## 7. How I resolved them
Verified file contents using `cat` after each write and append step, and confirmed directory listings with `ls -lah`.

## 8. Evidence / files
- `mission-02-terminal/terminal-practice/notes.txt` (contains two lines).
- `mission-02-terminal/terminal-practice/notes-backup.txt` (renamed copy, contains two lines).

## 9. Commit details
- Commit message: Complete Mission 2 terminal guide
- Short commit hash: cece8d5
- Pushed to GitHub: Yes
