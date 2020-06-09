import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

"""
  Example: input in bash: python3 sysarg.py 34 234 23423
  output: 
  sysarg.py
  ['34', '234', '23423']
  3
"""
print(program_name)
print(arguments)
print(count)
