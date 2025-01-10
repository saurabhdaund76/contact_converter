import pandas as pd
from pathlib import Path
from typing import List
from models.contact import Contact
from converters.vcf_converter import VCFConverter
from converters.excel_converter import ExcelConverter

class FileHandler:
    @staticmethod
    def vcf_to_excel(input_path: str, output_path: str):
        # Read VCF file
        with open(input_path, 'r', encoding='utf-8') as file:
            vcf_content = file.read()
        
        # Convert to contacts
        contacts = VCFConverter.parse_vcf(vcf_content)
        
        # Convert to DataFrame and save
        df = ExcelConverter.contacts_to_excel(contacts)
        df.to_excel(output_path, index=False)

    @staticmethod
    def excel_to_vcf(input_path: str, output_path: str):
        # Read Excel file
        df = pd.read_excel(input_path)
        
        # Convert to contacts
        contacts = ExcelConverter.excel_to_contacts(df)
        
        # Convert to VCF and save
        vcf_content = VCFConverter.create_vcf(contacts)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(vcf_content)
