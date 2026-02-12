def main():
    file = input("Whats your file name?").lower()

    if file.endswith(".gif"):
        print("images/gif")

    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("images/jpeg")

    elif file.endswith(".png"):
        print("images/png")

    elif file.endswith(".pdf"):
        print("applications/pdf")

    elif file.endswith(".txt"):
        print("applications/txt")

    elif file.endswith(".zip"):
        print("applications/zip")
    else:
        print("application/octet-stream")


main()
