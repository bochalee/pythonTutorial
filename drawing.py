import os
def file_rename():
    name_list=os.listdir(r"C:/Users/CFL-32/Desktop/bocha/prank/")
    print(name_list)
    saved_path=os.getcwd()
    print("Current working directory is"+saved_path)
    os.chdir(r"C:/Users/CFL-32/Desktop/bocha/prank/")

    for file_name in name_list:
        print("old name"+file_name)
        print("new name"+file_name.strip("0123456789"))
        os.renames(file_name,file_name.strip("0123456789"))
    os.chdir(saved_path)

file_rename()
print(os.getcwd())