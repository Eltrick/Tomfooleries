def main() -> None:
    t = int(input("t = "))
    b = int(input("b = "))
    
    while t >= b:
        t -= b
        b += 1
    
    print("Result: " + str([t, b]))

if __name__ == "__main__":
    main()