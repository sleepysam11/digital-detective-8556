# The Digital Detective

A mission-based exploration of computer systems, Terminal operations, operating systems, program execution, number representation, Git/GitHub and computer networks.

> Complete each mission in order, document your own work, and commit and push each mission separately. Do not publish private computer or network information.

## Mission index

| Mission | Topic | README |
|---|---|---|
| 0 | Repository and workspace setup | [Mission 0](mission-00-setup/README.md) |
| 1 | Computer fundamentals and IPOS | [Mission 1](mission-01-computer-basics/README.md) |
| 2 | Terminal and file management | [Mission 2](mission-02-terminal/README.md) |
| 3 | Operating system, processes and permissions | [Mission 3](mission-03-operating-system/README.md) |
| 4 | How programs run | [Mission 4](mission-04-programs/README.md) |
| 5 | Number systems, Python and text encoding | [Mission 5](mission-05-numbers-data/README.md) |
| 6 | Git, GitHub, branches and Pull Requests | [Mission 6](mission-06-git-github/README.md) |
| 7 | Computer networks | [Mission 7](mission-07-networking/README.md) |
| 8 | Final review and submission | [Mission 8](mission-08-final-report/README.md) |

## Topics explored

- Input, processing, output and storage (IPOS)
- Hardware, software and computer-based systems
- Command-line navigation and safe file management
- Operating-system processes, storage, paths and permissions
- Program execution, compilers and interpreters
- Decimal, binary and hexadecimal numbers
- ASCII and UTF-8 text encoding
- Git commits, branches and Pull Requests
- LAN, MAN, WAN, DNS, routers, protocols and client-server communication

## Run the number converter

From the repository root:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

The program asks for a positive decimal integer and displays its binary and hexadecimal forms.

## Learning summary

Working through this assignment taught me how every part of a computer system connects to the others. I started by understanding what hardware and software are and how the IPOS model describes every computing task. The Terminal sessions showed me that text commands give much finer control than clicking through menus. Exploring the operating system made me realise how much invisible work the OS does — managing memory, processes and permissions — so that programs never have to worry about those details directly. Learning how compilers and interpreters differ explained why Python is so quick to experiment with. Converting numbers by hand between decimal, binary and hexadecimal made me appreciate why computers only work with 0s and 1s, and why encoding standards like ASCII and UTF-8 are essential for sharing text between systems. Git and GitHub showed me a professional way to save progress and collaborate, and the networking mission joined the final dots by explaining how every web request travels from my browser across the internet to a server and back.

## My Learning

The biggest insight from this assignment is that computers are entirely **logical** — every apparent "magic" (a web page appearing, a program running) has a clear, step-by-step mechanical explanation. Understanding those steps makes me a better problem-solver. I also learned that documentation and version control are not optional extras; they are what make a project understandable to others (and to myself in the future).

## Commit approach

Each mission is documented and committed separately. The repository history should show the actual mission commits and pushes.
