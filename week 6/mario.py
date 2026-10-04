while True:
    try:
        height = int(input("Enter height: "))
        if 1 <= height <= 8:
            break
        else:
            print("Enter height:")
    except ValueError:
        print("Invalid input.")

for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1))
