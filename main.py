import pandas as pd
import os

def main():
    # File input loop
    while True:
        filename = input("Enter the filename (CSV): ").strip()
      
        if not filename:
            print("Filename cannot be empty. Please try again.")
            continue
            
        if not os.path.exists(filename):
            print(f"The file '{filename}' does not exist. Please try again.")
            continue
            
        # Extension check
        if not filename.lower().endswith('.csv'):
            print("Warning: File is not a CSV file. Trying to read anyway...")
        
        break
    
    # Error handling while reading the file
    try:
        df = pd.read_csv(filename)
        print(f"Successfully loaded {filename}")
        print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Method selection loop
    while True:
        print('''
        Available Methods:
        1. Dataset Info
        2. Check Missing Values
        3. Show First 5 Rows
        4. Show Data Types
        5. Show Basic Statistics
        6. Exit
        ''')
        
        method = int(input("Enter your choice (1-6): "))
        
        if method == 1:
            print("\n=== Dataset Info ===")
            print(df.info())
            
        elif method == 2:
            print("\n=== Missing Values ===")
            missing = df.isnull().sum()
            if missing.sum() == 0:
                print("No missing values found!")
            else:
                print(missing[missing > 0])
                
        elif method == 3:
            print("\n=== First 5 Rows ===")
            print(df.head())
            
        elif method == 4:
            print("\n=== Data Types ===")
            print(df.dtypes)
            
        elif method == 5:
            print("\n=== Basic Statistics ===")
            print(df.describe())
            
        elif method == 6:
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-6.")
        
        # Ask to continue or exit
        cont = input("\nDo you want to try another method? (y/n): ").strip().lower()
        if cont == 'y':
            continue
        elif cont == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Exiting.")
            break

if __name__ == "__main__":
    main()
