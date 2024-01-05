def main():
    print_column(3)
    print_row(4)
    print_square(5)

def print_column(n):
    print("#\n"*n,end="")

def print_row(width):
    print("?"*width)

def print_square(size):
    for i in range(size):
        print_row(size)

main()