def main() -> None:
    bucket = input("Enter both buckets' contents here, preferably left first: ").upper().split(" ")
    contents = [str(x) for x in bucket[0]]
    contentsToo = [str(x) for x in bucket[1]]
    contents.sort()
    contentsToo.sort()
    
    sortedStringOne = ""
    sortedStringTwo = ""
    
    print("Left Bucket, sorted: " + "".join(contents))
    print("Right Bucket, sorted: " + "".join(contentsToo))

if __name__ == "__main__":
    main()