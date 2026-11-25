# Mission 3 — Understand the operating system

## 1. Mission title
Mission 3 — Understand the operating system

## 2. Task / objective
Explore the operating system environment, running processes, available storage, absolute and relative paths, and file permissions, and describe the primary responsibilities of an operating system.

## 3. Work completed
- [x] Identified operating system environment and version using `sw_vers`.
- [x] Inspected storage capacity and volume mounting points using `df -h` with personal identifiers redacted.
- [x] Observed a running process snapshot, identified the PID column, and explained processes.
- [x] Explained differences between absolute and relative paths using project examples.
- [x] Inspected file permissions on `terminal-practice/notes.txt` without changing system settings.
- [x] Explained all six core OS responsibilities with practical examples in the required table.

### Task 3.1 — Operating system information table

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| Operating system / system details | The OS family, version release, and build number | macOS, ProductVersion: 27.2.1, BuildVersion: 26B131 |
| Current account identity | The active user account executing shell processes | `[user]` (standard non-root user account) |
| Available and used storage | Total, allocated, and free disk blocks on mounted storage volumes | Data Volume (`/System/Volumes/Data`): 926 GiB total, 124 GiB used, 776 GiB available (14% utilised). Root Volume (`/`): 926 GiB total, 13 GiB used, 776 GiB available (2% utilised) |
| System activity snapshot | Currently running tasks, their process names, and system PIDs | `launchd` (PID 1), `logd`, `fseventsd`, `powerd`, and system daemons |

**Terminal commands used (privacy-safe outputs):**

```bash
$ sw_vers
ProductName:    macOS
ProductVersion: 27.2.1
BuildVersion:   26B131
```
*(Note: Output obtained directly by executing `sw_vers` in Terminal on this Mac).*

```bash
$ df -h
Filesystem        Size    Used   Avail Capacity  Mounted on
/dev/disk3s1s1   926Gi    13Gi   776Gi     2%    /
/dev/disk3s5     926Gi   124Gi   776Gi    14%    /System/Volumes/Data
```

*(Personal paths, account names, and hardware serials redacted.)*

### Task 3.2 — Understand processes

**Process snapshot:**
```bash
$ ps -Ao pid,comm | head -n 12
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

**Questions answered:**
- **What is a process?** A process is an actively executing instance of a program loaded in memory. When a program file is launched, the operating system allocates memory, CPU time, and system resources to turn the static code into an active process.
- **What does the PID column represent?** PID stands for Process Identifier. It is a unique integer assigned by the kernel to identify and track each running process. Operating systems use PIDs to manage priorities, monitor resource consumption, and send control signals (e.g. terminate).
- **Two examples of processes running on this computer:**
  1. `/sbin/launchd` (PID 1): The root parent process on macOS that initializes and manages all other system and user processes.
  2. `/usr/libexec/logd`: The system logging daemon responsible for collecting and indexing system logs.

### Task 3.3 — Understand paths and permissions

**Path differences:**
- **Absolute path:** Specifies the location of a file or folder starting all the way from the root directory `/`. It is independent of the current directory.
  - *Example in assignment folder:* `/Users/[user]/.../digital-detective-8556/mission-02-terminal/terminal-practice/notes.txt`
- **Relative path:** Specifies the location relative to the current working directory.
  - *Example from repository root:* `mission-02-terminal/terminal-practice/notes.txt`

**File permissions inspection:**
```bash
$ ls -l mission-02-terminal/terminal-practice/notes.txt
-rw-r--r--@ 1 [user] staff 23B Nov 26 00:41 mission-02-terminal/terminal-practice/notes.txt
```

**Owner permissions breakdown:**
- The first character `-` indicates a regular file.
- The next three characters `rw-` represent the owner's permissions:
  - `r` (Read): **Allowed** — The owner can view and read the file's contents.
  - `w` (Write): **Allowed** — The owner can edit, modify, and append to the file.
  - `-` (Execute): **Not set** — The file cannot be executed as a program or script.
- Group and others have `r--` (Read-only access).

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows reading the file contents or listing directory contents | Opening a text file with `cat` or an editor |
| `w` — Write | Allows modifying, truncating, or appending to the file | Editing a file or appending text using `>>` |
| `x` — Execute | Allows running the file as a program; on a directory, allows entering/traversing it | Running a shell script or entering a folder with `cd` |

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| Process management | Allocates CPU time slices, schedules active threads, creates, and terminates processes | Multitasking between a browser, terminal, and code editor simultaneously without freezing |
| Memory management | Dynamically allocates blocks of RAM to programs and prevents processes from overwriting each other's memory | Allocating memory to Python when running a script, and reclaiming that memory when the script finishes |
| Device management | Communicates with hardware components using device drivers, abstracting low-level hardware details | Communicating with an external SSD or display using standard file and graphics interfaces |
| File management | Organises data into hierarchical directories, maps file names to physical disk blocks, and maintains metadata | Creating folders, saving files to disk, and managing directory trees |
| User interface / shell | Provides an interactive bridge (command-line shell or graphical desktop) between user and system | The Terminal shell (zsh) accepting typed commands, and the macOS Finder graphical interface |
| Security and permissions | Restricts access to files and resources based on user accounts, roles, and read/write/execute permissions | Preventing non-administrator accounts from modifying core system files in `/System` |

## 4. Commands / tools used
- `sw_vers` (OS details), `whoami` (account identity), `df -h` (storage status), `ps -Ao pid,comm | head -n 12` (running processes), `pwd` (current path), `ls -l` (permissions inspection).

## 5. My understanding
The operating system is the master resource manager of the computer. It provides hardware abstraction so programs do not need bespoke logic for specific hardware brands. By isolating process memory and enforcing access permissions, the OS guarantees system stability and multi-user security.

## 6. Difficulties faced
No major difficulties. All personal identifiers, home paths, and hostnames were redacted in accordance with the assignment's privacy rules.

## 7. How I resolved them
Used privacy-safe placeholders (`[user]`, `[redacted]`) in command output logs.

## 8. Evidence / files
- Privacy-safe outputs of `sw_vers`, `df -h`, `ps`, and `ls -l` recorded in this README and in `evidence/mission-03-system-snapshot.txt`.

## 9. Commit details
- Commit message: Complete Mission 3 operating system notes
- Short commit hash: f9d4c08
- Pushed to GitHub: Yes
