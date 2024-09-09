# CR-F
Tool CR-F.py
Introduction

The CR-F.py tool is an effective tool for decrypting hashes using wordlists. It relies on the hashlib library in Python, allowing it to decrypt multiple types of hashes, including MD5, SHA-1, and SHA-256. The tool is designed to be user-friendly and customizable, making it suitable for security researchers and ethical hackers.


Requirements

Python 3: You need to have Python 3 installed on your system.
colorama library: For coloring the output in the command line. You can install it using the following command:
       
       pip install colorama

How to Use

Run the tool using the following command:

       python3 CR-F.py

When prompted, enter the list of hashes. You can enter them as a comma-separated list or as a filename containing the hashes.

Enter the path to the wordlist containing the words you wish to use for hash decryption.

Main Functions

Detect Hash Type: The tool detects the type of hash based on its length (MD5, SHA-1, SHA-256).
Crack Hash: The tool uses wordlists to attempt to decrypt the specified hashes.
Display Results: The tool displays results in a colored format, where cracked hashes are shown in blue and unc cracked hashes in red.

Example Output

When using the tool, the output will look like this:


    HACK MR: B
    Enter the list of hashes (comma-separated or file name): hash-password.txt
    Enter the path to the wordlist: /usr/share/wordlists/rockyou.txt

    Detected hash type: MD5 for hash: 21232f297a57a5a743894a0e4a801fc3
    Cracking hash...
    Trying: [admin                                   ]
    Hash cracked! The password for 21232f297a57a5a743894a0e4a801fc3 is: admin

    Summary of cracked hashes:
    21232f297a57a5a743894a0e4a801fc3: admin
