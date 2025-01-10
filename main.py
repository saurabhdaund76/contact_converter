from pathlib import Path
from utils.file_handler import FileHandler

def main():
    while True:
        print("\nContact Converter")
        print("1. Convert VCF to Excel")
        print("2. Convert Excel to VCF")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            break
            
        try:
            if choice == '1':
                input_file = input("Enter the path to your VCF file: ")
                output_file = input("Enter the path for the Excel file (e.g., contacts.xlsx): ")
                FileHandler.vcf_to_excel(input_file, output_file)
                print(f"Successfully converted {input_file} to {output_file}")
                
            elif choice == '2':
                input_file = input("Enter the path to your Excel file: ")
                output_file = input("Enter the path for the VCF file (e.g., contacts.vcf): ")
                FileHandler.excel_to_vcf(input_file, output_file)
                print(f"Successfully converted {input_file} to {output_file}")
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()