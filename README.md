# PasswordPolicyChecker
Look for passwords compliant with a giver policy template in a file (rockyou.txt)

Example:
python3 policy_checker.py Teaaaaaaaaaaaaaaaa@1 1 /usr/share/wordlists/rockyou.txt

It will print every password 20 characters long, with uppercases, lowercases, digits and special characters
