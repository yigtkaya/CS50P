import os

file_name, file_extension = os.path.splitext(input("File name: "))
file_extension = file_extension.replace("." , "").lower()

if "png" in file_extension or "gif" in file_extension:
    print("image" + "/" + file_extension)

elif "jpeg" in file_extension or "jpg" in file_extension:
    print("image" + "/jpeg")

elif "pdf" in file_extension or "zip" in file_extension:
    print("application/" + file_extension)

elif "txt" in file_extension:
    print("text/" + file_name)

else:
    print("application/octet-stream")