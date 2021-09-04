from os.path import exists
import hashlib

class hasher():

    def __init__(self, file):
        self.file = file

    def checkfile(self):
        """
        Checks if file exists.
        Creates the file if it does not exist.
        """
        if(exists(self.file)):
            print(f"File found {self.file}")
        else:
            with open(self.file, "x") as file:
                print(f"File created: {self.file}")

    def checkword(self, word):
        """
        Checks if a word is in the file.
        If the word is found it will return the word and hash.
        If not it will hash the word and add it to the file.
        It will return the string "added" if the hash is not found.
        """
        found = False
        self.hashedword = hashlib.sha256(word.encode()).hexdigest()
        with open(self.file, "r+") as file:
            for line in file:
                line = line.strip("\n")
                if (self.hashedword == line):
                    return f"Found in file: {line} | {prevline}"
                prevline = line
            
            file.write(f"{word}\n")
            file.write(f"{self.hashedword}\n")
            return "Added"

    def printfile(self):
        """
        Returns the full contents of the file.
        """
        with open(self.file, "r") as file:
            return file.read()

    def gethashes(self):
        """
        Returns a dicitonary from the hashes in the file.
        keys = words
        values = hashes
        """
        hashes = {}
        count = 0
        with open(self.file, "r") as file:
            for line in file:
                if(count == 0):
                    key = line.strip("\n")
                    count = 1
                else:
                    hashes[key] = line.strip("\n")
                    count = 0
        return hashes

    def findhash(self, hashedword):
        """
        Returns the hash if it is found in the file.
        """
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip("\n")
                if(hashedword == line):
                    return prevline
                prevline = line
            return "Not found"