# Mission 4 — How programs run

## 1. Mission title
Mission 4 — How programs run

## 2. Task / objective
Run a small Python program and compare compiled and interpreted approaches to executing programs.

## 3. Work completed
- [x] Confirmed `hello.py` contains the required print statement.
- [x] Added the compiler/interpreter comparison.
- [ ] Run the program locally and confirm the output.

### Compiler and interpreter comparison
| Feature | Compiler approach | Interpreter approach |
|---|---|---|
| When translation happens | Usually translates a source program (or a large part of it) before execution. | Usually translates or executes instructions as the program runs. |
| Typical output | Often creates a separate executable or intermediate code. | Often produces program behaviour directly without a separate native executable. |
| Example | A C program compiled with a C compiler. | A Python script run with the Python interpreter (although Python implementations also compile to bytecode). |
| Advantage | Compiled programs can run efficiently and can be distributed without the original source in some workflows. | Interactive execution and quick testing can make development convenient. |

### Run the program
From this folder:

```bash
python3 hello.py
```

Expected output:

```text
Hello from Python
```

### Explanation
A compiler translates source code into another form before the program runs, commonly machine code or bytecode. An interpreter executes a program by reading and carrying out instructions at runtime. The distinction is not absolute: modern language implementations often combine both techniques. Python commonly compiles source into bytecode, which its virtual machine executes.

## 4. Commands / tools used
`python3 hello.py` — starts Python 3 and runs the file named `hello.py`.

## 5. My understanding
A program must be translated into operations the computer can execute. Compilers and interpreters are two approaches to this process. They differ in when translation occurs and how the resulting instructions are executed, but real language systems may combine the approaches.

## 6. Difficulties faced
The local execution result has not yet been observed.

## 7. How I resolved them
Run `python3 hello.py` from this directory. If Python is not found, check `python3 --version` and use the Python 3 installation provided for the course.

## 8. Evidence / files
- `hello.py` — prints the required greeting.
- This README — comparison table and explanation.
- Pending: local terminal output.

## 9. Commit details
- Commit message: Complete Mission 4 program execution notes
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
