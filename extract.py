import re

# File to extract HTML from
f = open('/yourfile')

# Destination File to write the output in
f2 = open('/destinationfile', 'r+')

# Read the lines from the file
lines = f.read()

# Closing the files when finish reading
f.close()

# Find HTML pattern which could match what we want to extract
matches = re.findall('<div class="example">(.*?)</div>', lines, re.DOTALL)

# Write into file and replace if necessary some parts to improve html
f2.write(str(matches).replace('\\n', '<br />'))

# Closing the destination file when finish writing
f2.close()