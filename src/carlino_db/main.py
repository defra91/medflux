# src/main.py

from .db import load_db

def main():
    df = load_db()
    print("Database loaded successfully.")
    print(df.head())  # Display the first few rows of the DataFrame

if __name__ == "__main__":
    main()