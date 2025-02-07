def extract_numbers(input_str):
    input_str = input_str.replace('all', '').replace('#', '')
    result = []
    for part in input_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return result

# Get HW title
section_number = input("Enter the HW section number: ")
section_title  = input("Enter the HW section title : ")
page_n         = input("Enter the page number: ")

# Get user input for problem numbers
user_num_input = input("Enter problem numbers separated by commas and dashes: ")

# Split the input string into a list of integers
problem_nums = extract_numbers(user_num_input)

# Convert the list to a string for printing
problem_nums_str = ', '.join(map(str, problem_nums))

with open('HW ' + section_number + ' ' + section_title + '.tex', 'w') as f:

    f.write("\\documentclass[12pt]{exam}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\usepackage{amssymb}\n")
    f.write("\\usepackage[T1]{fontenc}\n")
    f.write("\\usepackage[table]{xcolor}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\begin{document}\n")
    f.write(f"HW {section_number}\n\n")

    #HW info
    f.write(
        "\\begin{center}\n"
        "MA 224 Discrete Mathematics \\\ \n"
        "Andrew Malone \\\ \n"
        f"HW {section_number} {section_title} \\\ \n"
        f"{section_number} pg {page_n} \\#{problem_nums_str} \\\ \n"
        "\\end{center}\n\n"
    )

    # Centered line
    f.write("\\rule{\\textwidth}{0.5pt}\n")
    f.write("\\vspace{1mm}\n\n")

    # Begin numbering the problems
    f.write("\\begin{enumerate}\n\n")
    for num in problem_nums:
        
        f.write(f"% Problem {num}\n")

        # Individual problem start
        f.write(f"\t\\setcounter{{enumi}}{{{num-1}}}\n")
        f.write("\t\\item\n")
        f.write("\t\\begin{enumerate}\n")

        # Sub-problems a, b, c
        f.write("\t\t\\item\n")
        f.write("\t\t\\item\n")
        f.write("\t\t\\item\n")

        #Individual problem end
        f.write("\t\\end{enumerate}\n\n")
 
    # Stop numbering the problems
    f.write("\\end{enumerate}\n")
    f.write("\\end{document}")
