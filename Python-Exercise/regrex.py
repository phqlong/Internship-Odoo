# Use regular expressions to check if email is valid or not
"""
Input: ankitrai326@gmail.com
Output: Valid Email
Input: my.ownsite@ourearth.org
Output: Valid Email
Input: ankitrai326.com
Output: Invalid Email
"""
import re
# re.search(<regex>, <string>) -> None / SRE_Match obj: {span: (<int>from, <int>to), match: <string>}
# <regex>: \w = [0-9a-zA-Z], [abcd]: choose 1 in range;
#   \W != \w; \d, \D: [0-9]; \s: space
#   . : any except \n
#   ^ : at the start; [^0-9]: not digit
#   $ : at the end
#   regex{m, n}: regex appear from m to n times.
#   regex{m}: regex appear exactly m times.

emails = ["ankitrai326@gmail.com", "my.ownsite@ourearth.org", "ankitrai326.com"]

for email in emails:
    if re.search(r"[\w._-]+@\w+\.[a-zA-Z]{2,}" ,email):
        print("Valid Email")
    else:
        print("Invalid Email")
