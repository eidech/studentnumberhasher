import os
import pandas as pd
import hashlib

def generate_salt_dict(salt_file_path):
    salt_df = pd.read_excel(salt_file_path)
    salt_dict = dict(zip(salt_df['student_studentNumber'], salt_df['salt']))
    return salt_dict

def generate_md5_hash(value, salt):
    md5_hash = hashlib.md5()
    value_with_salt = str(value) + str(salt)
    md5_hash.update(value_with_salt.encode('utf-8'))
    return md5_hash.hexdigest()

def generate_sha512_hash(value, salt):
    sha512_hash = hashlib.sha512()
    value_with_salt = str(value) + str(salt)
    sha512_hash.update(value_with_salt.encode('utf-8'))
    return sha512_hash.hexdigest()

def process_excel_file(file_path, salt_dict):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Iterate over the column 'student_studentNumber' and replace values with salted SHA512 hashes
    column_name = 'student_studentNumber'
    df[column_name] = df.apply(lambda row: generate_sha512_hash(row[column_name], salt_dict.get(row[column_name], '')), axis=1)

    # Save the modified DataFrame to a new Excel file
    new_file_path = 'SALTHASHED_' + file_path
    df.to_excel(new_file_path, index=False)
    print(f"Hashed file saved as: {new_file_path}")

def main():
    # Get salt values from salts.xlsx
    salt_file_path = 'salts.xlsx'
    salt_dict = generate_salt_dict(salt_file_path)

    # Get all .xlsx files starting with "export" in the current directory
    files_to_process = [file for file in os.listdir() if file.endswith('.xlsx') and file.startswith('export')]

    # Process each Excel file
    for file_path in files_to_process:
        process_excel_file(file_path, salt_dict)

if __name__ == '__main__':
    main()
