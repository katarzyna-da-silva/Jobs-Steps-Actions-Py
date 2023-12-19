# script.py
import subprocess

def main():
    try:
        subprocess.run(["ponysay", "Hello DevOps ;) !"], check=True)
    except FileNotFoundError:
        print("Ponysay ne fonctionne pas.")

if __name__ == "__main__":
    main()
