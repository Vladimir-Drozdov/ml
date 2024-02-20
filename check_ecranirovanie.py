s = "A &amp; B"
import re
matched = re.search(r'&\w+;', s)
if matched:
    print ("escape char '{0}' found in string '{1}'".format(matched.group(), s))