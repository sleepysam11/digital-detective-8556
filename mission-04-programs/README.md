# Mission 4 — How programs run

## 1. Mission title
Mission 4 — How programs run

## 2. Task / objective
Create and execute a Python program from the Terminal and compare how compilers and interpreters translate and execute software.

## 3. Work completed
- [x] Created `hello.py` inside `mission-04-programs/` with the required one-line print statement.
- [x] Executed `hello.py` from Terminal using `python3` and confirmed the output message.
- [x] Completed the compiler versus interpreter comparison table across all required dimensions.
- [x] Wrote a concise explanation comparing the two execution models.

### Task 4.1 — Program execution

Command executed from the mission directory:
```bash
$ python3 hello.py
Hello from Python
```

The program ran successfully and displayed `Hello from Python` as expected.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates the entire source code into machine code or an intermediate format prior to execution (at build time) | Translates and executes source statements line-by-line or statement-by-statement at runtime |
| Typical output | A standalone binary executable file (e.g. `.exe`, `.bin`, ELF binary) or intermediate object file | Direct execution of statements in memory; no standalone machine-code binary is saved |
| One example | C / C++ / Rust compiler (e.g. `gcc`, `clang`, `rustc`) | Python / Ruby / JavaScript runtime (e.g. `python3`, `ruby`, Node.js) |
| One advantage | Higher runtime execution speed because all translation and optimization occur beforehand | Rapid prototyping and debugging because code can be tested immediately without a separate compilation step |

### Explanation of differences
A compiler processes an entire program's source code in advance, performing syntax verification and machine-level optimization to produce a standalone executable file that runs directly on the CPU. In contrast, an interpreter reads, translates, and executes instructions sequentially at runtime, requiring the language interpreter to be present each time the program runs. Modern programming environments frequently employ hybrid techniques; for example, Python compiles source code into intermediate bytecode (`.pyc` files), which is then interpreted by the Python Virtual Machine (PVM).

## 4. Commands / tools used
- `python3 hello.py`: Invokes the Python 3 interpreter to parse and execute the script.
- `print("Hello from Python")`: Built-in Python function that outputs the given string to standard output.

## 5. My understanding
Computers can only directly execute native machine code instructions. Compilers translate high-level source code into native binary ahead of time, providing peak performance. Interpreters translate instructions dynamically during execution, providing superior flexibility and immediate interactive feedback.

## 6. Difficulties faced
No major difficulties. The Python 3 interpreter executed `hello.py` directly without errors.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `mission-04-programs/hello.py` — contains `print("Hello from Python")`.
- Observed Terminal output recorded in Section 3.

## 9. Commit details
- Commit message: Complete Mission 4 program execution notes
- Short commit hash: fb04b38
- Pushed to GitHub: Yes
