import hashlib
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def detect_hash_type(hash_value):
    hash_length = len(hash_value)
    if hash_length == 32:
        return "MD5"
    elif hash_length == 40:
        return "SHA-1"
    elif hash_length == 64:
        return "SHA-256"
    else:
        return "Unknown"

def crack_hash(hash_to_crack, wordlist, hash_type):
    try:
        with open(wordlist, 'r', encoding='ISO-8859-1') as file:
            for word in file:
                word = word.strip()

                if not word.isascii() or len(word) == 0:
                    continue

                if hash_type == "MD5":
                    hash_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "SHA-1":
                    hash_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == "SHA-256":
                    hash_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print(f"Unsupported hash type: {hash_type}")
                    return None

                sys.stdout.write(f"\rTrying: [{Fore.YELLOW}{word:<40}{Style.RESET_ALL}]")
                sys.stdout.flush()

                if hash_word == hash_to_crack:
                    return word

                time.sleep(0.0)

        return None
    except FileNotFoundError:
        print(f"Error: The file '{wordlist}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    hashes_input = input("Enter the list of hashes (comma-separated or file name): ")

    if hashes_input.endswith('.txt'):
        try:
            with open(hashes_input, 'r') as file:
                hashes = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file '{hashes_input}' does not exist.")
            sys.exit(1)
    else:
        hashes = [hash.strip() for hash in hashes_input.split(',') if hash.strip()]

    wordlist_path = input("Enter the path to the wordlist: ")

    results = {}

    for target_hash in hashes:
        target_hash = target_hash.strip()
        hash_type = detect_hash_type(target_hash)

        if hash_type == "Unknown":
            print(f"{Fore.RED}Unknown hash type for hash: {target_hash}. Skipping...{Style.RESET_ALL}")
            continue

        print(f"\n{Fore.RED}Detected hash type: {hash_type} for hash: {target_hash}{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}Cracking hash...{Style.RESET_ALL}")

        result = crack_hash(target_hash, wordlist_path, hash_type)

        if result:
            print(f"\n{Fore.BLUE}Hash cracked! The password for {target_hash} is: {result}{Style.RESET_ALL}")
            results[target_hash] = result
        else:
            print(f"\n{Fore.RED}Failed to crack the hash: {target_hash}{Style.RESET_ALL}")

    print("\nSummary of cracked hashes:")
    for hash_value, password in results.items():
        print(f"{hash_value}: {password}")
