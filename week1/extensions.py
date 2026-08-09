# File Extensions

input_file = input("Enter you file with type: ")
input_file = input_file.lower().strip()

if input_file.endswith(".jpeg") or input_file.endswith(".jpg"):
    print("image/jpeg")
elif input_file.endswith(".gif"):
    print("image/gif")
elif input_file.endswith(".png"):
    print("image/png")
elif input_file.endswith(".pdf"):
    print("application/pdf")
elif input_file.endswith(".txt"):
    print("text/plain")
elif input_file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")