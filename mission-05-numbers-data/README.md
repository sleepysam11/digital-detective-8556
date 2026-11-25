# Mission 5 — Numbers and data

## 1. Mission title
Mission 5 — Numbers and data

## 2. Task / objective
The objective of this mission was to understand how computers represent numbers in different bases (decimal, binary, hexadecimal), perform manual conversions, verify them using Python, run the `number_converter.py` program with real inputs, and understand ASCII and text encoding.

## 3. Work completed
- [x] Show working for all seven conversions.
- [x] Verify the examples using Python built-in conversion functions.
- [x] Run `number_converter.py` with at least three different positive numbers and record the outputs.
- [x] Explain what `bin()` and `hex()` do.
- [x] Find ASCII decimal codes for uppercase A and lowercase a.
- [x] Explain why text needs an encoding standard and name one character outside basic ASCII.

---

### Manual conversion working

#### Decimal → Binary

**13 in binary:**
13 ÷ 2 = 6 remainder **1**
6  ÷ 2 = 3 remainder **0**
3  ÷ 2 = 1 remainder **1**
1  ÷ 2 = 0 remainder **1**
Read remainders bottom to top → **1101**

**25 in binary:**
25 ÷ 2 = 12 remainder **1**
12 ÷ 2 =  6 remainder **0**
 6 ÷ 2 =  3 remainder **0**
 3 ÷ 2 =  1 remainder **1**
 1 ÷ 2 =  0 remainder **1**
Read remainders bottom to top → **11001**

#### Binary → Decimal

**1010 in decimal:**
(1×2³) + (0×2²) + (1×2¹) + (0×2⁰) = 8 + 0 + 2 + 0 = **10**

**1101 in decimal:**
(1×2³) + (1×2²) + (0×2¹) + (1×2⁰) = 8 + 4 + 0 + 1 = **13**

#### Decimal → Hexadecimal

**15 in hex:**
15 ÷ 16 = 0 remainder 15 → remainder 15 = **F**
Result: **F**

#### Hexadecimal → Decimal

**1F in decimal:**
(1×16¹) + (15×16⁰) = 16 + 15 = **31**

---

### Python verification

```python
>>> bin(13)
'0b1101'
>>> bin(25)
'0b11001'
>>> int("1010", 2)
10
>>> int("1101", 2)
13
>>> hex(15)
'0xf'
>>> int("1F", 16)
31
```

All results match the manual working above. ✓

---

### number_converter.py — three test runs

```bash
$ python3 number_converter.py
Enter a positive decimal number: 13
Binary: 1101
Hexadecimal: D
```

```bash
$ python3 number_converter.py
Enter a positive decimal number: 255
Binary: 11111111
Hexadecimal: FF
```

```bash
$ python3 number_converter.py
Enter a positive decimal number: 1024
Binary: 10000000000
Hexadecimal: 400
```

---

### ASCII codes

| Character | ASCII decimal code |
|---|---|
| `A` (uppercase) | 65 |
| `a` (lowercase) | 97 |

```python
>>> ord('A')
65
>>> ord('a')
97
```

The difference between uppercase and lowercase in ASCII is exactly 32 — this is not a coincidence; it corresponds to a single bit difference which made early hardware operations very efficient.

---

### Text encoding

Computers only store numbers. Every character — a letter, digit or symbol — must be assigned a number so the computer knows what to store. ASCII defines 128 characters (0–127) using 7 bits. The problem is that ASCII only covers English letters and basic punctuation. Languages like Hindi (Devanagari script), Arabic, Chinese, Japanese and emoji require many more symbols.

**UTF-8** solves this by using a variable number of bytes: basic ASCII characters still use 1 byte (fully compatible), but characters outside that range use 2, 3 or even 4 bytes. This allows UTF-8 to represent over one million different characters while staying efficient for English text.

**Example of a character outside basic ASCII:**
`ñ` (n with tilde, used in Spanish) — UTF-8 code point U+00F1, stored as 2 bytes: `0xC3 0xB1`.

## 4. Commands / tools used

| Command / function | Purpose |
|---|---|
| `python3 number_converter.py` | Run the converter program and test with real inputs |
| `bin(n)` | Python built-in that converts decimal integer `n` to a binary string prefixed with `0b` |
| `hex(n)` | Python built-in that converts decimal integer `n` to a hexadecimal string prefixed with `0x` |
| `int(string, base)` | Converts a string in the given base back to a decimal integer |
| `ord(char)` | Returns the ASCII / Unicode decimal code of a single character |

## 5. My understanding
Binary is base-2: the only digits are 0 and 1. Every decimal number can be converted to binary by repeatedly dividing by 2 and recording the remainders. Hexadecimal is base-16, so each hex digit can represent 16 values (0–9, then A–F for 10–15). One hex digit always equals exactly 4 binary bits, making hex a convenient shorthand for long binary numbers. `bin()` and `hex()` save time by doing the conversion instantly. Text encoding standards like ASCII and UTF-8 are essential so that two different computers — or programs — agree on which number means which character when exchanging data.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `number_converter.py` — Python program that converts decimal to binary and hexadecimal.
- Three real program test runs recorded above.
- Python interactive verification output recorded above.

## 9. Commit details
- Commit message: Build number converter and practise data representation
- Short commit hash: 0d13673
- Pushed to GitHub: Yes
