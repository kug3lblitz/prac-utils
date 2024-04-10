import os
import re

sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE']
output_file = 'sql_queries.txt'
function_pattern = re.compile(r'(public|private|protected|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\(')

current_function = None

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.cs'):
                with open(os.path.join(root, file), 'r') as code_file:
                    lines = code_file.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        function_match = function_pattern.search(line)
                        if function_match:
                            current_function = function_match.group(2)
                        if any(keyword in line for keyword in sql_keywords):
                            f.write(f'File: {os.path.join(root, file)}\n')
                            f.write(f'Function: {current_function}\n')
                            f.write(f'Line number: {i + 1}\n')
                            f.write(f'Query: {line}\n')
                            if i + 1 < len(lines):
                                f.write(f'Next line: {lines[i + 1]}\n')
                            if i + 2 < len(lines):
                                f.write(f'Next next line: {lines[i + 2]}\n')
                            f.write('-----------------------------------------\n')
