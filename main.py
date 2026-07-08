from side import print_file_info

file_path = r"C:\Trivedi\Bharti\GSFC_University\DataSets\Data1.txt"

with open(file_path, "r", encoding="utf-8") as text_file:
    text = text_file.read()

def main():
    #Calling the functions
    #1. Print the file information
    print_file_info(text)
   # print_file_info(text)
   

# This line ensures the script only runs if you run main.py directly
if __name__ == "__main__":
    main()
