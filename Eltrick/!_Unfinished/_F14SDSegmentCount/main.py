Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

Letters = ["--XXX----XXX-X","-XX-X-X-XX-X--","--XXXXXX-XXXX-","-XX-X-XXXX-X--","--XXXX---XXXX-","--XXXX---XXXXX","--XXXXX--XXX--","X-XXX----XXX-X","-XX-XXXXXX-XX-","XXXXX-XX-XXX--","X-XX-X-X-XX-XX","X-XXXXXX-XXXX-","X--X--XX-XXX-X","X--XX-XX-XX--X","--XXX-XX-XXX--","--XXX----XXXXX","--XXX-XX-XX---","--XXX----XX-XX","--XXXX--XXXX--","-XX-XXXXXX-XXX","X-XXX-XX-XXX--","X-XX-XXX--XXXX","X-XXX-XX--X--X","XX-X-XXXX-X-XX","XX-X-XXXXX-XXX","-XXX-XXXX-XXX-"]

def main() -> None:
    for i in range(0, len(Letters)):
        print(Alphabet[i] + ": " + str(Letters[i].count('-')))

if __name__ == "__main__":
    main()