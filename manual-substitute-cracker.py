#!/usr/bin/env python3
import frequency_analysis
import sys
import os

class code:
    def __init__(self,encrypted_code):
        if 'nux' in sys.platform:
            self.clear = lambda: os.system("clear")
        else:
            self.clear = lambda: os.system("cls")

        self.code = encrypted_code
        self.history = []
        self.original = self.code

        helpmsg =  "\nx y : replace x with y in the string" 
        helpmsg += "\nfreq : display frequency" 
        helpmsg += "\nback : go back one version"
        helpmsg += "\nreset : go back to original version"
        helpmsg += "\nclear : clear the screen"
        helpmsg += "\nexit : get out of the program\n"

        while True:
            try:
                print()
                cmd = input(">> ")
                if cmd == "?" or cmd == "help":
                    print(helpmsg)
                elif cmd == "freq":
                    frequency_analysis.code(self.code)
                elif cmd == "back":
                    self.goback()
                elif cmd == "reset":
                    self.code = self.original
                    print("\nReset to original\n")
                    print(self.code)
                    print()
                elif cmd == "clear":
                    self.clear()
                elif cmd == "exit":
                    exit()
                else:
                    self.replace(cmd.split(" ")[0],cmd.split(" ")[1])

            # except ValueError:
            #     pass

            except IndexError:
                # Means the splitting failed
                # which means command invalid
                print()
                print(self.code)

            except KeyboardInterrupt:
                print()
                exit()

    def goback(self):
        """
        Revert the code back into the version which is lower than this
        """
        try:
            self.code = self.history[-1]
            # Set the code into the last entry in the history
            self.history.pop()
            # Removes the last entry
            print()
            print(self.code)
            print()
        except IndexError:
            print("[!] This is the original version cannot go back anymore\n")
            print()
            print(self.code)
            print()

    def replace(self,old,new):
        """Replace the occurance of 'old' with 'new' and print"""
        self.change = True if old in self.code else False
        # Checks if it is possible to replace
        if self.change:
            self.code = self.code.lower().replace(old,new)
            self.history.append(self.code)
            print("\n[+] Replaced : {} with {}".format(old,new))
            print()
            print(self.code)

        else:
            print("\n[-] No occurance of [{}]".format(old))

if __name__ == "__main__":
    print("Manual Substitute Cracker")
    print("=========================")
    text = input("\nEnter encrypted string : ").lower()
    app = code(text)