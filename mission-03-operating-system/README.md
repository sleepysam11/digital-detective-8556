# Mission 3 — Understand the operating system

## 1. Mission title
Mission 3 — Understand the operating system

## 2. Task / objective
The objective of this mission was to explore the operating system environment, understand processes and their IDs, work with absolute and relative paths, inspect file permissions, and explain the six main responsibilities of an operating system.

## 3. Work completed
- [x] Identify the operating system environment.
- [x] Check the current account and available/used storage, then redact identifying details.
- [x] Observe a brief process snapshot and identify the PID column.
- [x] Explain absolute and relative paths using examples from this project.
- [x] Inspect permissions for a file in the practice area without changing system permissions.
- [x] Explain all six OS responsibilities in the assignment table.

### Operating system information

```bash
$ sw_vers
ProductName:    macOS
ProductVersion: 27.2.1
BuildVersion:   26B131
```

### Storage check (redacted)

```
Filesystem        Size    Used   Avail Capacity  Mounted on
/dev/disk3s1s1   926Gi    13Gi   776Gi     2%    /
/dev/disk3s5     926Gi   124Gi   776Gi    14%    /System/Volumes/Data
```

*(Account name, device name and personal paths redacted.)*

The main volume has 776 GiB free out of 926 GiB total.

### Process snapshot — first 12 entries

```
  PID COMM
    1 /sbin/launchd
  530 /usr/libexec/logd
  532 /usr/libexec/smd
  533 /usr/libexec/UserEventAgent
  535 fseventsd
  536 mediaremoted
  539 /usr/sbin/systemstats
  543 /usr/libexec/configd
  545 powerd
  546 /usr/libexec/IOMFB_bics_daemon
  548 /usr/libexec/amfid
```

The PID column is the leftmost column. PID stands for Process Identifier — a unique number the OS assigns to every running process. PID 1 (`launchd`) is always the first process launched by macOS and it is the parent of all other processes.

### Absolute vs relative paths

| Path type | Example in this project | Explanation |
|---|---|---|
| Absolute | `/Users/[username]/projects/digital-detective-8556/mission-02-terminal/notes.txt` | Full path from the root `/`; works from anywhere |
| Relative | `mission-02-terminal/notes.txt` | Path relative to the current directory; shorter but only works from the right starting point |

### File permissions inspection

```bash
$ ls -l terminal-practice/notes.txt
-rw-r--r--@ 1 [user] staff 23B Nov 25 23:51 terminal-practice/notes.txt
```

Breaking down `-rw-r--r--`:

| Part | Meaning |
|---|---|
| `-` | Regular file (not a directory) |
| `rw-` | Owner can read and write, but not execute |
| `r--` | Group members can read only |
| `r--` | Everyone else can read only |

### Six OS responsibilities

| Responsibility | Explanation |
|---|---|
| Process management | The OS starts, schedules and stops programs, giving each a PID and sharing CPU time fairly |
| Memory management | Allocates RAM to running programs and prevents one program from accessing another's memory |
| File system management | Organises files into directories on disk, handles reading and writing, enforces permissions |
| Device management | Communicates with hardware (keyboard, mouse, disk) through drivers so programs do not need to know the hardware details |
| Security and permissions | Controls who can read, write or execute each file and prevents unauthorised access |
| User interface | Provides a way to interact with the system — either graphical (GUI like macOS Finder) or text-based (Terminal) |

## 4. Commands / tools used

| Command | Purpose |
|---|---|
| `sw_vers` | Display macOS product name, version and build |
| `whoami` | Show the current logged-in username |
| `df -h` | Show disk usage in human-readable sizes |
| `ps -Ao pid,comm \| head -n 12` | Show first 12 running processes with their PID and name |
| `pwd` | Print current working directory |
| `ls -l` | Long listing with permissions, owner, size and date |

## 5. My understanding
The operating system is the master manager of the computer. Without it, programs would have to talk directly to hardware, which would be impossibly complex. By sitting between hardware and applications, the OS hides the complexity and lets me run many programs at once without them interfering. Processes each get a PID so the OS can track and control them individually. Permissions (the rwx system) ensure privacy and safety — not every user or program can touch every file.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- Outputs from `sw_vers`, `df -h` and `ps -Ao pid,comm` recorded above with personal details redacted.
- Permission inspection of `terminal-practice/notes.txt` shown above.

## 9. Commit details
- Commit message: Document operating system and file management
- Short commit hash: (to be updated after commit)
- Pushed to GitHub: Yes
