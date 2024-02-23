# studentnumberhasher
Simple Python script for hashing student numbers in Infinite Campus generated Ad-Hoc reports to anonymize student data

Uses default column values and hashes on student_studentNumber.  Files should be kept with default filename (starting with 'export').

To generate salted hash values, create a file 'salts.xlsx' that contains two columns, student_studentNumber and salt.  The first column should be student numbers and the second column should be randomly generated salt values.  THIS FILE MUST BE RETAINED IF YOU WISH TO DEANONYMIZE AND/OR PERFORM LOOKUPS WITH FUTURE DATA.