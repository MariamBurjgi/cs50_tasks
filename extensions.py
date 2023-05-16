gif = "image/gif"
jpg = "image/jpeg"
jpeg = "image/jpeg"
png = "image/png"
pdf = "application/pdf"
txt = "text/plain"
zip = "application/zip"


extension = input("file name: ").lower().strip()


if extension.endswith(".gif"):
    print(gif)
elif extension.endswith(".jpg"):
    print(jpg)
elif  extension.endswith(".jpeg"):
    print(jpg)
elif extension.endswith(".png"):
    print(png)
elif extension.endswith(".pdf"):
    print(pdf)
elif extension.endswith(".txt"):
    print(txt)
elif extension.endswith(".zip"):
    print(zip)
else:
    print("application/octet-stream")