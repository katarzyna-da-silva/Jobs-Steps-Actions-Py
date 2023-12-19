# script.py
import os

def main():
    try:
        os.system("ponysay 'Hello DevOps ;) !'")
    except FileNotFoundError:
        print("Ponysay est mort.")

if __name__ == "__main__":
    main()
