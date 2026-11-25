# Mission 4 — How programs run

## 1. Mission title
Mission 4 — How programs run

## 2. Task / objective
The objective of this mission was to run a small Python program from Terminal, understand the difference between compilers and interpreters, and explain in my own words when and how translation happens for each approach.

## 3. Work completed
- [x] Run `hello.py` from Terminal using Python 3.
- [x] Complete the compiler/interpreter comparison table.
- [x] Write a three- or four-sentence explanation in my own words.

### Running hello.py

```bash
$ python3 hello.py
Hello from Python
```

The program printed `Hello from Python` as expected. Python 3 found the `print()` statement, evaluated it and displayed the string immediately — no extra build step was needed.

### Compiler vs Interpreter comparison table

| Feature | Compiler | Interpreter |
|---|---|---|
| When translation happens | Before the program runs (at build time) | Line by line as the program runs (at runtime) |
| Typical output | A standalone executable file (e.g. `.exe`, binary) | Runs directly from source code, no separate executable |
| Speed of execution | Generally faster at runtime (pre-translated) | Slower at runtime (translates as it goes) |
| Error reporting | Reports all errors after analysing the whole program | Reports an error on the line it fails and stops |
| Example language | C, C++, Rust | Python, JavaScript, Ruby |
| Example advantage | The finished program runs quickly without needing the compiler | Easier to test and debug; can run code interactively |

> **Note:** Modern language implementations often combine both techniques. Python first compiles source code to bytecode (`.pyc`), then the Python Virtual Machine interprets that bytecode — a hybrid approach.

## 4. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `python3 hello.py` | Run the Python script using the Python 3 interpreter |
| `python3` | The interpreter itself; reads Python source and executes it |
| `print()` | Built-in Python function that sends text to standard output |

## 5. My understanding
A compiler reads the entire source code, checks it all at once, and produces a separate executable file. That file can then run on its own without the compiler. An interpreter reads and executes the program one line (or statement) at a time while it is running, so the source code and interpreter must both be present every time. Python is an interpreted language, which is why I can type `python3 hello.py` and see output immediately — there is no separate compile step. The trade-off is that compiled programs often run faster because the hard translation work was already done, while interpreted languages are more flexible and easier to experiment with.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `hello.py` — the small Python program that prints `Hello from Python`.
- Output from `python3 hello.py` recorded above.

## 9. Commit details
- Commit message: Compare compilers and interpreters
- Short commit hash: (to be updated after commit)
- Pushed to GitHub: Yes
