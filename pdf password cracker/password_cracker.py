import pikepdf    #pip install pikepdf

# set the path to the password-protected PDF file
pdf_file = "example.pdf"
# set the path to the password list file
password_list = "password.txt"
# read in the password list file and try each password to unlock the PDF
with open(password_list, "r") as f:
    for line in f:
        password = line.strip()
        try:
            with pikepdf.open(pdf_file, password=password) as pdf:
                print("*********************************")
                print(f"Password found: {password}")
                print("*********************************")
                break
        except:
            print(f"Password failed: {password}")
