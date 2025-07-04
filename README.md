# -FILE-INTEGRITY-CHECKER
This is a simple project where i try to build a file integrity checker using python library hashlib which provides an interface to various secure hash and message digest algorithms. Go through the readme section to deeply analyze this project. Thanks✌️

## 📂 File Integrity Checker:

A simple Python-based tool to **detect unauthorized modifications in files** by generating and comparing their hash values.

🔒 Purpose

This tool helps in:

* Detecting file tampering or corruption
* Monitoring integrity of sensitive files
* Learning hashing in cybersecurity

⚙️ Features

* Generates SHA-256 hash of any file
* Saves the hash as a baseline
* Compares the current hash to detect file changes
* User-friendly **menu-based interface**
* Clear success and warning messages

 🛠️ How It Works

1. **Option 1: Generate and Save File Hash**

   * Takes file path input
   * Calculates SHA-256 hash
   * Saves it in `hash_record.txt`

2. **Option 2: Check File Integrity**

   * Recalculates the file hash
   * Compares with saved hash
   * Displays whether the file is modified

3. **Option 3: Exit**

   * Ends the program

 🐍 Requirements

* Python 3.6 or higher (tested on Python 3.13)
* No external libraries needed

### 📦 How to Run

bash
python file_integrity.py
```

📁 Example

```text
--- File Integrity Checker ---
1. Generate and Save File Hash
2. Check File Integrity
3. Exit
Enter your choice (1/2/3): 1
Enter file path: E:\yash.txt
✅ Original hash saved successfully.

--- File Integrity Checker ---
Enter your choice (1/2/3): 2
Enter file path to check: E:\yash.txt
✅ File Integrity Check Passed: No changes detected.
```

🧪 Tip for Testing

* Save the original hash (Option 1)
* Modify the file (change or delete/add content)
* Use Option 2 to verify if it detects the change


📁 File Structure

```
📁 Task1/
│
├── file_integrity.py        # Main script
├── hash_record.txt          # Stores file path and hash (auto-created)
├── yash.txt                 # Sample test file
```

### 📚 Learning Outcome

* Practical use of hashing (SHA-256)
* Working with file I/O
* Building real-world cybersecurity tools

