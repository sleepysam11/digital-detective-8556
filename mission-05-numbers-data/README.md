# Mission 5 — Numbers and data

## 1. Mission title
Mission 5 — Numbers and data

## 2. Task / objective
Perform manual number conversions across decimal, binary, and hexadecimal representations; verify calculations using Python; test the `number_converter.py` program with positive integer inputs; and explain character encoding standards.

## 3. Work completed
- [x] Completed manual step-by-step working for all seven conversion problems.
- [x] Verified conversions in the Python interactive environment.
- [x] Executed `number_converter.py` with test inputs 10, 25, and 255 and recorded verified outputs.
- [x] Explained what Python's `bin()` and `hex()` functions do.
- [x] Identified ASCII decimal codes for uppercase `A` (65) and lowercase `a` (97).
- [x] Explained text encoding and identified a character outside basic ASCII.

### Task 5.1 — Manual number conversions

#### 1. Decimal 13 to binary
- Repeated division by 2:
  - 13 ÷ 2 = 6, remainder **1**
  - 6 ÷ 2 = 3, remainder **0**
  - 3 ÷ 2 = 1, remainder **1**
  - 1 ÷ 2 = 0, remainder **1**
- Reading remainders from bottom to top: **1101₂**
- Check: $(1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) = 8 + 4 + 0 + 1 = 13_{10}$.

#### 2. Decimal 25 to binary
- Repeated division by 2:
  - 25 ÷ 2 = 12, remainder **1**
  - 12 ÷ 2 = 6, remainder **0**
  - 6 ÷ 2 = 3, remainder **0**
  - 3 ÷ 2 = 1, remainder **1**
  - 1 ÷ 2 = 0, remainder **1**
- Reading remainders from bottom to top: **11001₂**
- Check: $(1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (1 \times 1) = 16 + 8 + 1 = 25_{10}$.

#### 3. Binary 1010 to decimal
- Sum of place values ($2^3, 2^2, 2^1, 2^0$):
  - $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$
  - $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$

#### 4. Binary 1101 to decimal
- Sum of place values ($2^3, 2^2, 2^1, 2^0$):
  - $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
  - $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$

#### 5. Hexadecimal A to decimal & Decimal 15 to hexadecimal
- In base 16 (hexadecimal), single digits represent values 0 through 15:
  - A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.
  - Therefore, **$\text{A}_{16} = \mathbf{10_{10}}$**.
  - Similarly, for decimal 15: 15 ÷ 16 = 0 with remainder 15, which is represented by **$\mathbf{F_{16}}$**.

#### 6. Hexadecimal 1F to decimal
- Sum of base-16 place values ($16^1, 16^0$):
  - $(1 \times 16^1) + (15 \times 16^0)$
  - $= 16 + 15 = \mathbf{31_{10}}$

#### 7. Decimal 255 to hexadecimal
- Division by 16:
  - 255 ÷ 16 = 15, remainder **15**
  - In hexadecimal, 15 is denoted by the letter **F**.
  - Since quotient is 15 (F) and remainder is 15 (F):
  - $(15 \times 16^1) + (15 \times 16^0) = 240 + 15 = 255_{10}$.
- Result: **$\mathbf{FF_{16}}$**
- *(Also binary 1111 to hex: $1111_2 = 8 + 4 + 2 + 1 = 15_{10} = \mathbf{F_{16}}$).*

---

### Task 5.2 — Python verification

Tested expressions in interactive Python 3:

```python
>>> bin(13)
'0b1101'
>>> bin(25)
'0b11001'
>>> int("1010", 2)
10
>>> int("1101", 2)
13
>>> hex(10)
'0xa'
>>> hex(15)
'0xf'
>>> int("1F", 16)
31
>>> hex(255)
'0xff'
```

All Python verification results match the manual calculations exactly.

---

### Task 5.3 — Number converter test runs

Program executed:
```bash
python3 number_converter.py
```

**Observed test runs:**

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| **10** | `1010` | `A` |
| **25** | `11001` | `19` |
| **255** | `11111111` | `FF` |

**Function explanations:**
- `bin(number)`: Converts an integer into a binary string prefixed with `0b` (e.g. `bin(10)` returns `'0b1010'`). The script slices `[2:]` to display pure binary digits.
- `hex(number)`: Converts an integer into a hexadecimal string prefixed with `0x` (e.g. `hex(10)` returns `'0xa'`). The script slices `[2:]` and calls `.upper()` to present standard uppercase hex notation.
- `int(text, base)`: Parses a string representation of a number in the given radix (e.g. base 2, base 16) and computes its decimal integer value.

---

### Task 5.4 — Text encoding

- **ASCII codes:**
  - Uppercase `A`: ASCII decimal code **65** (`01000001` in binary)
  - Lowercase `a`: ASCII decimal code **97** (`01100001` in binary)
  - The constant difference of 32 represents a single bit toggle ($2^5$), which allowed early hardware to convert case with simple bitwise operations.
- **Why computers need text encoding:**
  Computers cannot natively store letters or symbols; they exclusively process binary electrical states (bits: 0 and 1). An encoding standard assigns a unique numeric code point to every character so distinct systems, files, and networks reliably store, transmit, and render the exact same text without corruption.
- **Character outside basic ASCII:**
  The Indian Rupee symbol `₹` (Unicode code point `U+20B9`). Basic 7-bit ASCII only defines characters 0–127 (English alphabet, basic digits, and punctuation). Modern standards such as **UTF-8** represent characters like `₹` using 3 bytes (`0xE2 0x82 0xB9`), enabling global multilingual representation.

## 4. Commands / tools used
- `python3 number_converter.py`: Runs the interactive conversion program.
- Python built-in functions: `bin()`, `hex()`, `int()`, `ord()`.

## 5. My understanding
Number representation is determined by the numeric base (radix): decimal is base-10, binary is base-2, and hexadecimal is base-16. Because 16 is $2^4$, each hexadecimal digit maps directly onto an 4-bit binary nibble, making hex a compact representation for binary bytes. Text encoding translates human typographical characters into numeric values that hardware can store and compute.

## 6. Difficulties faced
No major difficulties. All manual conversion steps were verified mathematically and confirmed via Python built-in functions.

## 7. How I resolved them
Cross-checked repeated division remainders against place-value summation to ensure 100% accuracy.

## 8. Evidence / files
- `mission-05-numbers-data/number_converter.py` — working conversion program.
- Conversion calculations and test run outputs recorded in Section 3.

## 9. Commit details
- Commit message: Complete Mission 5 number systems and encoding
- Short commit hash: ca43b90
- Pushed to GitHub: Yes
