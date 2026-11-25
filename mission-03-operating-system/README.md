# Mission 3 — Understand the operating system

## 1. Mission title
Mission 3 — Understand the operating system

## 2. Task / objective
Identify the operating-system environment, understand processes, paths, storage and permissions, and explain the main responsibilities of an operating system.

## 3. Work completed
- [x] Added explanations of the six core operating-system responsibilities.
- [x] Added safe macOS inspection commands.
- [ ] Run the commands locally and record privacy-safe observations.
- [ ] Inspect permissions for a practice file without changing system permissions.

### Six operating-system responsibilities
| Responsibility | Explanation |
|---|---|
| Process management | Starts, schedules, and stops running programs and shares CPU time between them. |
| Memory management | Allocates RAM to programs and manages memory use. |
| File-system management | Organises files and folders and controls how they are stored and accessed. |
| Device management | Coordinates hardware devices through drivers and system services. |
| Security and access control | Uses accounts and permissions to restrict access to files and resources. |
| User interface and system services | Provides ways to interact with the computer and common services used by applications. |

### Paths
- An **absolute path** identifies a location from the file-system root, for example `/Users/example/project/mission-03-operating-system/README.md`. This is an illustrative path, not a report of the student's actual username or folder.
- A **relative path** identifies a location from the current working directory, for example `mission-03-operating-system/README.md` when run from the repository root.

### Process identifier
A process is a running instance of a program. The PID (process ID) column identifies a process while it is running. PIDs can change after a process exits and is started again.

## 4. Commands / tools used
Run these on macOS:

```bash
sw_vers
whoami
df -h
ps -Ao pid,comm | head -n 12
pwd
ls -l mission-03-operating-system/README.md
```

Do not save or publish the raw output of `whoami`, full paths, device names, or personal storage details. Summarise only what the assignment asks for and redact identifying values.

## 5. My understanding
The operating system is the layer between applications and the computer's hardware. It manages processes, memory, files, devices, security, and the user interface. File permissions help control who can read, write, or execute a file. A PID is a temporary identifier for a running process.

## 6. Difficulties faced
Local OS version, storage usage, account details, process snapshot, and file permissions have not yet been inspected.

## 7. How I resolved them
Use the commands in Section 4 on the Mac. If sharing results, remove account names and personal paths first. Do not change permissions on system files.

## 8. Evidence / files
- This README contains the OS-responsibility table and path explanations.
- Pending: redacted local command observations.

## 9. Commit details
- Commit message: Complete Mission 3 operating system notes
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
