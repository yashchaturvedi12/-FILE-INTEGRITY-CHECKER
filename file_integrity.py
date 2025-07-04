import hashlib

def generate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found!")
        return None

def save_hash(file_path, hash_value):
    try:
        with open("hash_record.txt", "w") as f:
            # Using "||" as separator to avoid Windows path issue
            f.write(f"{file_path}||{hash_value}")
        print("✅ Original hash saved successfully.\n")
    except Exception as e:
        print(f"❌ Error saving hash: {e}")

def check_file_integrity(file_path):
    current_hash = generate_file_hash(file_path)
    if current_hash is None:
        return

    try:
        with open("hash_record.txt", "r") as f:
            saved_data = f.read()
            saved_file, saved_hash = saved_data.strip().split("||")

            if saved_file != file_path:
                print("\n⚠️ Warning: The saved hash was for a different file!")

            if current_hash == saved_hash:
                print("\n✅ File Integrity Check Passed: No changes detected.")
            else:
                print("\n❌ File Integrity Check Failed: File has been modified!")

    except FileNotFoundError:
        print("❌ No saved hash found. Please run option 1 first to save hash.")
    except ValueError:
        print("❌ Hash file format error. Please regenerate the hash using option 1.")

def main():
    while True:
        print("\n--- File Integrity Checker ---")
        print("1. Generate and Save File Hash")
        print("2. Check File Integrity")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            file_path = input("Enter file path: ")
            file_hash = generate_file_hash(file_path)
            if file_hash:
                save_hash(file_path, file_hash)
        elif choice == '2':
            file_path = input("Enter file path to check: ")
            check_file_integrity(file_path)
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
