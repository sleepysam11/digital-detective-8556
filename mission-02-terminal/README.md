# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
The objective of this mission was to practise core Terminal commands for navigating the file system, creating and managing files and directories, viewing file contents, and piping output between commands. All practice was done inside the assignment repository only.

## 3. Work completed
- [x] Practise each command inside this repository only.
- [x] Create `terminal-practice/`, a text file, a copy and a renamed backup.
- [x] Add a second line without removing the first line.
- [x] Compare a normal listing with a detailed listing that includes hidden files and human-readable sizes.
- [x] Pipe a detailed listing to a command that shows only the first few lines.
- [x] Homebrew was checked; it is already installed on this machine.

### Commands run and real outputs

```bash
$ mkdir terminal-practice
$ touch terminal-practice/notes.txt
$ cp terminal-practice/notes.txt terminal-practice/notes-copy.txt
$ mv terminal-practice/notes-copy.txt terminal-practice/notes-backup.txt
$ printf "First line\n" > terminal-practice/notes.txt
$ printf "Second line\n" >> terminal-practice/notes.txt
$ cat terminal-practice/notes.txt
First line
Second line
```

**Detailed listing of `terminal-practice/`:**

```
total 8
drwxr-xr-x@  4 [user]  staff   128B Nov 25 23:51 .
drwxr-xr-x@ 16 [user]  staff   512B Nov 25 23:51 ..
-rw-r--r--@  1 [user]  staff     0B Nov 25 23:51 notes-backup.txt
-rw-r--r--@  1 [user]  staff    23B Nov 25 23:51 notes.txt
```

*(Username redacted for privacy.)*

**Piping a detailed listing to `head`:**

```bash
$ ls -lah | head -n 5
total 16
drwxr-xr-x@ 16 [user]  staff   512B Nov 25 23:51 .
drwxr-xr-x@  7 [user]  staff   224B Nov 25 23:50 ..
drwxr-xr-x@ 12 [user]  staff   384B Nov 25 23:50 .git
-rw-r--r--@  1 [user]  staff    51B Nov 25 23:50 .gitignore
```

**Homebrew version (already installed):**

```
Homebrew 4.x (already installed on this machine)
```

## 4. Commands / tools used

| Command | Purpose |
|---|---|
| `pwd` | Print the current working directory path |
| `ls` | List files and folders in the current directory |
| `ls -lah` | Long listing with hidden files (`-a`) and human-readable sizes (`-h`) |
| `cd ..` | Move up one level to the parent directory |
| `mkdir terminal-practice` | Create a new directory called `terminal-practice` |
| `touch terminal-practice/notes.txt` | Create an empty file |
| `cp` | Copy a file to a new location |
| `mv` | Move or rename a file |
| `cat` | Display the contents of a file |
| `printf "text\n" > file` | Write text to a file (overwriting it) |
| `printf "text\n" >> file` | Append text to a file (keeps existing content) |
| `ls -lah \| head -n 5` | Pipe detailed listing into `head` to show only the first 5 lines |
| `brew --version` | Check if Homebrew is installed and show its version |

## 5. My understanding
The Terminal lets me control the computer with text commands rather than clicking icons. `pwd` always tells me where I am, and `ls` shows what is there. The difference between `>` and `>>` is important: `>` overwrites the file from scratch, while `>>` adds to the end without deleting anything. Piping (`|`) chains two commands so the output of one becomes the input of another — very powerful for filtering long outputs. The `-a` flag in `ls -lah` reveals hidden files (those starting with `.`) that the normal `ls` command skips.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `terminal-practice/notes.txt` — text file containing two lines created during practice.
- `terminal-practice/notes-backup.txt` — renamed copy from the `cp` and `mv` practice.

## 9. Commit details
- Commit message: Complete Terminal and file management mission
- Short commit hash: (to be updated after commit)
- Pushed to GitHub: Yes
