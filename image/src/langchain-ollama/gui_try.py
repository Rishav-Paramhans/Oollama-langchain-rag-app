import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory of the script's directory
src_dir = os.path.dirname(script_dir)

image_dir = os.path.dirname(src_dir)
# Use the parent directory for relative paths
relative_path = os.path.join(src_dir, "my_file.txt")

print("Script directory:", script_dir)
print("Src dir:", src_dir)
print("image_dir", image_dir)
print("Relative path to file in parent directory:", relative_path)
