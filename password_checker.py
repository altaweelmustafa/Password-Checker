import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

score = 0
iscapital = False
isspecial = False

# Special char
special_chars = {'!', '@', '#', '$', '%' , '^', '&', '*', '(' , ')', '-', '_', '+', '=', ';', ':', ',', '.', '"', '~', '`'}
# Check args
if len(sys.argv) > 2:
    print(f"{RED}[ERROR]{RESET} Invalid number of args, enter just one password please.")

# Save password text
password = sys.argv[1]

# Check length
if len(password) < 8 or len(password) > 26:
    print(f"{RED}[INVALID]{RESET} Length must be between 8 and 26.")

# Check capitals and specials
for ch in password:
    if(ch.isupper()):
        iscapital = True
        score += 1
    if ch in special_chars:
        isspecial = True
        score += 1

if not iscapital:
    print(f"{RED}[INVALID]{RESET} No uppercase characters.")

if not isspecial:
    print(f"{RED}[INVALID]{RESET} No special characters.")
    

if score >= 2 and iscapital and isspecial and sys.argv[1].isalnum() == False and len(sys.argv) == 2:
    print(f"{GREEN}[STRONG]{RESET} Your password is strong.")
else:
    print(f"{YELLOW}[WEAK]{RESET} Your password is weak.")
