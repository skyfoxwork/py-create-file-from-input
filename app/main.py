def main() -> None:
    crate_file_string = input("Enter name of the file: ")
    open_file = open(f"{crate_file_string}.txt", "a")

    while True:
        content_string = input("Enter new line of content: ")
        if content_string == "stop":
            break
        open_file.write(content_string + "\n")


if __name__ == "__main__":
    main()
