def main():
    x = int(input("What's X? "))
    print("X square is",square(x))
def square(n):
    return pow(n,2)

if __name__=="__main__":
    main()