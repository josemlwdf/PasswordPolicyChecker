## Password Policy Checker

The Password Policy Checker is a Python script that checks for passwords compliant with a given policy template in a file. The script supports checking for passwords that are at least n characters long, contain upper and lowercase characters, digits, and special characters.

# Usage

``python3 policy_checker.py [policy_template] [length] [passwords_file]
policy_template - The policy template for the password.
length - The minimum length of the password.
passwords_file - The path to the file containing the list of passwords.``

The script will print every password that meets the policy requirements and save them to a file named policy_compliant.txt.

# Example

    python3 policy_checker.py Teaaaaaaaaaaaaaaaa@1 20 /usr/share/wordlists/rockyou.txt

This will check for passwords that are at least 20 characters long, contain upper and lowercase characters, digits, and special characters, and are stored in the /usr/share/wordlists/rockyou.txt file. The results will be saved in policy_compliant.txt.

# Dependencies

The script requires Python 3.x to run. No additional libraries or modules are required.
License

This script is licensed under the MIT License. See the LICENSE file for details.
