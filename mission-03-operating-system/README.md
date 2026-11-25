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

### Task 3.1 — Operating system information table

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| Operating system / system details | The name and version of the OS running on this computer | macOS, ProductVersion: 27.2.1, BuildVersion: 26B131 |
| Current account identity | Which user account is logged in | [redacted] — personal username not published |
| Available and used storage | How much disk space is free vs used | Main volume: 926 GiB total, 124 GiB used, 776 GiB free (14% used) |
| System activity snapshot | Which programs (processes) are currently running and their PIDs | launchd (PID 1), logd, UserEventAgent, fseventsd, configd and others — all system background processes |

**Raw command outputs (personal details redacted):**

```bash
$ sw_vers
ProductName:    macOS
ProductVersion: 27.2.1
BuildVersion:   26B131
```

```
Filesystem        Size    Used   Avail Capacity  Mounted on
/dev/disk3s1s1   926Gi    13Gi   776Gi     2%    /
/dev/disk3s5     926Gi   124Gi   776Gi    14%    /System/Volumes/Data
```

*(Account name, device name and personal paths redacted.)*

### Task 3.2 — Processes

**Process snapshot — first 12 entries:**

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

- **What is a process?** A process is a program that is currently running. When I open a browser or text editor, the OS creates a process for it and assigns it a PID.
- **What does the PID column represent?** PID stands for Process Identifier — a unique number the OS assigns to every running process so it can track, control and schedule it.
- **Two example processes:** `launchd` (PID 1) — the system's first process and parent of all others; `logd` — the system log daemon that records system events.

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

### Task 3.4 — Six OS responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| Process management | The OS starts, schedules and stops programs, giving each a PID and sharing CPU time fairly between them | Opening Safari creates a process; the OS ensures it gets CPU time alongside other apps |
| Memory management | Allocates RAM to running programs and prevents one program from accessing another's memory | When I open VS Code, the OS gives it its own memory space; it cannot read Chrome's memory |
| Device management | Communicates with hardware through drivers so programs do not need to know the hardware details | The keyboard driver translates key presses into characters my text editor can receive |
| File system management | Organises files into directories on disk, handles reading and writing, enforces permissions | Saving a document stores it on the SSD in a folder I can find later |
| Security and permissions | Controls who can read, write or execute each file and prevents unauthorised access | The `-rw-r--r--` permission means only the owner can write to `notes.txt` |
| User interface / shell | Provides a way to interact with the system — either graphical (GUI like macOS Finder) or text-based (Terminal) | I use Terminal to navigate folders; other users use Finder's graphical windows |

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
- Short commit hash: 0d13673
- Pushed to GitHub: Yes
