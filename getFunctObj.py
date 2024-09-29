import os
import subprocess

# Define the directory containing the .o files
directory = "."

# Output file to store the results
output_file = "local_functions_disassembly.txt"

# Function to run objdump and disassemble the given function
def disassemble_function_objdump(obj_file):
    # Run objdump to disassemble the entire object file
    command = ["objdump", "-d", obj_file]
    
    # Run objdump with the commands
    result = subprocess.run(command, capture_output=True, text=True)

    return result.stdout

# Open the output file for writing
with open(output_file, "w") as outfile:
    outfile.write("Local Functions and Their Full Disassembly from Object Files:\n\n")

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Process only .o files
        if filename.endswith(".o"):
            # Run the nm command to list symbols in the object file
            command = ["nm", "--defined-only", filename]
            result = subprocess.run(command, capture_output=True, text=True)

            # Split the output into lines
            lines = result.stdout.splitlines()

            # Filter local/static functions (symbol type 't')
            local_functions = [line for line in lines if " t " in line]

            # If there are local functions, process them with objdump
            if local_functions:
                outfile.write(f"File: {filename}\n")
                
                # Disassemble the entire object file using objdump
                disassembly = disassemble_function_objdump(filename)

                # Write the full disassembly to the output file
                outfile.write(f"{disassembly}\n")

print(f"Disassembled functions have been written to {output_file}")
