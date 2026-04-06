def read_logs():
    with open("log.txt", "r") as f:
        for line in f:
            yield line.strip()


def count_errors():
    count = 0
    for line in read_logs():
        if "ERROR" in line:
            count += 1
    print("🔴 Total Errors:", count)


def show_errors_with_line():
    for i, line in enumerate(read_logs(), start=1):
        if "ERROR" in line:
            print(f"Line {i}: {line}")


def search_logs():
    keyword = input("Enter keyword: ")
    
    found = False
    for line in read_logs():
        if keyword.lower() in line.lower():
            print("🔍", line)
            found = True
    
    if not found:
        print("❌ No match found")


# 🚀 MENU
while True:
    print("\n====== LOG ANALYZER ======")
    print("1. Count Errors")
    print("2. Show Errors with Line Number")
    print("3. Search Logs")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        count_errors()

    elif choice == "2":
        show_errors_with_line()

    elif choice == "3":
        search_logs()

    elif choice == "4":
        break

    else:
        print("❌ Invalid choice")
