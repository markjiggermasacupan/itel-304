import sys


def main():
    while True:
        try:
            # Make a Python program to find the area of Triangle

            # a, b, and c is the three sides of triangle:
            a = float(input("Enter first side:  "))
            b = float(input("Enter second side: "))
            c = float(input("Enter third side: "))
            if a and b and c < 0:
                myError = ValueError("\n" "SHOULD BE A POSITIVE NUMBER, PLEASE RE-ENTER!")
                raise myError

            if not (a or b or c < 0):
                raise ValueError()
                assert a or b or c > 0
            # Triangle Perimeter computation:
            p = (a + b + c)

            # Triangle Semi-perimeter computation:
            smp = (a + b + c / 2)

            # calculating the area:
            area = (smp * (smp - a) * (smp - b) * (smp - c)) ** 0.5
            print("THE AREA OF TRIANGLE IS: %0.2f" % area, "\n")

            # Additional Info
            print("ADDITIONAL INFO OF TRIANGLE")
            print("Semi-perimeter: ", smp)
            print("Perimeter: ", p)
            sys.exit(0)

        except Exception as j:
            print(j)


if __name__ == "__main__":
    main()
    sys.exit(0)
