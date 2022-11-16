from dotenv import load_dotenv
import time
import os
import re

load_dotenv()

def main():
    file_path = os.environ['FILE_PATH'] # Path to the dictionary file

    in_file = open(file_path, encoding = "ISO-8859-1")

    usable_lines = []

    lines_to_process = 10000 # Number of lines to process

    for count, line in enumerate(in_file):
        if count == lines_to_process:
            break

        if re.match('^[a-zA-Zñ\[\]{}*.`!@#$%^&*()\-=_+;/?><|\\áéíóúÁÉÍÓÚ ]+$', str(line)):
            usable_lines.append(line)
        

    in_file.close()

    if os.path.exists(os.environ['OUTPUT_PATH']):
        out_file = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        out_file = open(os.environ['OUTPUT_PATH'], 'x')

    out_file.writelines(usable_lines)
    out_file.close()

start = time.time()
main()
end = time.time()
print('Total Time: ' + str(end - start))