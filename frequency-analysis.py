import string

class alphabet:
    def __init__(self,alphabet):
        self.alphabet = alphabet

    def count_freq(self,text):
        self.count = 0
        
        for word in text:
            if word.lower() == self.alphabet:
                self.count += 1

class code:
    def __init__(self):
        print("Word Frequency Analyzer\n")
        encrypted_code = input("Enter string to analyze : ")
        alphabets = [alphabet(i) for i in string.ascii_lowercase]
        # a list of objects containing each letter in A-Z

        temp = {}
        for letter in alphabets:
            letter.count_freq(encrypted_code)
            if letter.count > 0:
                temp[letter.alphabet] = letter.count

        result = sorted(temp.items(), key=lambda x:x[1],reverse=True)
        print("Result : ")
        print("\n".join(["\t"+letter[0]+":"+str(letter[1]) for letter in result]))


if __name__ == "__main__":
    app = code()