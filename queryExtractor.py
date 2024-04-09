import os

sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE']
output_file = 'sql_queries.txt'

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.cs'):
                with open(os.path.join(root, file), 'r') as code_file:
                    for line in code_file:
                        if any(keyword in line.upper() for keyword in sql_keywords):
                            f.write(line)
