filename = input("File name: ").strip().lower()

images = (".gif", ".jpg", ".jpeg", ".png")
applications = (".pdf", ".zip")
text = (".txt")

if "." in filename:
    extension = filename.rsplit(".", 1)[1]


if filename.endswith(images):
    if extension == "jpg":
        print ("image/jpeg")
    else:
        print("image/", extension, sep="")
elif filename.endswith(applications):
    print("application/", extension, sep="")
elif filename.endswith(text):
    print("text/plain")
else:
    print("application/octet-stream")