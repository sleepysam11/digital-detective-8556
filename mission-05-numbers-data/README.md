# Mission 5 — Numbers and data

## 1. Mission title
Mission 5 — Numbers and data

## 2. Task / objective
Practise converting between decimal, binary, and hexadecimal; verify conversions with Python; and understand ASCII and Unicode text encoding.

## 3. Work completed

### Seven worked conversions
1. Decimal 13 to binary: (13 = 8 + 4 + 1), so (13_{10} = 1101_2).
2. Decimal 25 to binary: (25 = 16 + 8 + 1), so (25_{10} = 11001_2).
3. Binary 1010 to decimal: (1(8) + 0(4) + 1(2) + 0(1) = 10), so (1010_2 = 10_{10}).
4. Binary 1101 to decimal: (1(8) + 1(4) + 0(2) + 1(1) = 13), so (1101_2 = 13_{10}).
5. Decimal 15 to hexadecimal: (15_{10} = F_{16}).
6. Hexadecimal 1F to decimal: (1(16) + 15(1) = 31), so (1F_{16} = 31_{10}).
7. Decimal 255 to hexadecimal: (255 = 15(16) + 15), so (255_{10} = FF_{16}).

**Handwritten-work requirement:** These worked examples are provided for checking. Copy the seven calculations by hand into your own notebook if the instructor requires handwritten working, then attach your own evidence separately.

### Python verification
Try these in the Python prompt:

```python
bin(13)       # '0b1101'
bin(25)       # '0b11001'
int("1010", 2)  # 10
int("1101", 2)  # 13
hex(15)       # '0xf'
int("1F", 16)  # 31
```

### Number converter
Run from this folder:

```bash
python3 number_converter.py
```

The program accepts a positive decimal whole number and prints its binary and hexadecimal forms. It rejects non-integer input and values that are zero or negative.

Test cases to run and record:
| Input | Expected binary | Expected hexadecimal |
|---:|---:|---:|
| 10 | 1010 | A |
| 25 | 11001 | 19 |
| 255 | 11111111 | FF |

### What the functions do
- `bin(number)` returns a string representation of an integer in binary, prefixed with `0b`.
- `hex(number)` returns a string representation in hexadecimal, prefixed with `0x`.
- `int(text, base)` interprets text in the given base and returns a decimal integer.

### ASCII and Unicode
- Uppercase `A` has ASCII decimal code **65**.
- Lowercase `a` has ASCII decimal code **97**.
- ASCII represents a basic set of English letters, digits, punctuation, and control codes.
- Unicode provides code points for characters used by many writing systems and symbols. For example, `₹` (Indian rupee sign) is outside basic ASCII.
- UTF-8 is a Unicode encoding that represents characters using one to four bytes. Encoding standards let different systems store and exchange text consistently.

## 4. Commands / tools used
`python3 number_converter.py` runs the converter. Python's `bin()`, `hex()`, and `int(value, base)` functions verify the calculations.

## 5. My understanding
Binary uses base 2, decimal uses base 10, and hexadecimal uses base 16. Place values depend on powers of the base. ASCII maps a limited set of characters to numbers, while Unicode supports characters from many languages and symbol sets. UTF-8 is a widely used way to store Unicode text.

## 6. Difficulties faced
The three converter test cases have not yet been run locally, and the handwritten calculations still need to be written in the student's notebook if required.

## 7. How I resolved them
Use the worked conversions above to check the handwritten calculations, then run the converter with each listed input and compare the actual output.

## 8. Evidence / files
- `number_converter.py` — decimal-to-binary-and-hexadecimal program.
- This README — worked conversions, test cases, and encoding explanation.
- Pending: handwritten calculations and local test observations.

## 9. Commit details
- Commit message: Complete Mission 5 number systems and encoding
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
