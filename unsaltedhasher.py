import os
import pandas as pd
import hashlib

def generate_md5_hash(value):
    md5_hash = hashlib.md5()
    md5_hash.update(str(value).encode('utf-8'))
    return md5_hash.hexdigest()

def generate_sha512_hash(value):
    sha512_hash = hashlib.sha512()
    value_with_salt = str(value)
    sha512_hash.update(value_with_salt.encode('utf-8'))
    return sha512_hash.hexdigest()

def process_excel_file(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Iterate over the column 'student_studentNumber' and replace values with SHA512 hashes
    column_name = 'student_studentNumber'
    df[column_name] = df[column_name].apply(generate_sha512_hash)

    # Save the modified DataFrame to a new Excel file
    new_file_path = 'HASHED_' + file_path
    df.to_excel(new_file_path, index=False)
    print(f"Hashed file saved as: {new_file_path}")

def main():
    # Get all .xlsx files starting with "export" in the current directory
    files_to_process = [file for file in os.listdir() if file.endswith('.xlsx') and file.startswith('export')]

    # Process each Excel file
    for file_path in files_to_process:
        process_excel_file(file_path)

if __name__ == '__main__':
    main()
