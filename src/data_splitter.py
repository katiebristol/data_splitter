# Import libraries
import os.path
from os import path

line_number = 0
header = ''
add_header = False 

# Place your CryoPC3 file in the data directory and replace
# "YOUR_FILE.dat" with your file name below. 
with open("data/YOUR_FILE.dat", "r") as cryopc3_file:
    for line in cryopc3_file:
        line_number+=1
        next_line = line.strip()

        if line_number < 6:
            header = header + next_line + '\n'
            continue
       
        sample_name = next_line[:next_line.find(' ')]
        print(sample_name)

        # Create seperate sample files 
        add_header = not path.exists('results/' + sample_name + '.txt')


        # Fill the sample files with data stripped from main file
        samples_file = open('results/' + sample_name + '.txt', 'a+')
        if add_header:
            samples_file.write(header)
        samples_file.write((next_line)+'\n')
        samples_file.close()