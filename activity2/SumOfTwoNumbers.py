import sys


def main():
    while True:
        try:
            mynum1 = float(input("Enter your first number: "))
            mynum2 = float(input("Enter your second number: "))
            if not (mynum1 or mynum2 < 0):
                raise ValueError()

            print(mynum1, " + ", mynum2, "is", (mynum1 + mynum2))
            sys.exit(0)

        except Exception as j:
            print(j)


if __name__ == "__main__":
    main()
    sys.exit(0)
