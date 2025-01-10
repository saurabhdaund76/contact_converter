import pandas as pd
from typing import List
from models.contact import Contact, Address

class ExcelConverter:
    @staticmethod
    def contacts_to_excel(contacts: List[Contact]) -> pd.DataFrame:
        return pd.DataFrame([contact.to_dict() for contact in contacts])

    @staticmethod
    def excel_to_contacts(df: pd.DataFrame) -> List[Contact]:
        contacts = []
        for _, row in df.iterrows():
            # Parse addresses
            addresses = []
            if pd.notna(row['Address']):
                for addr_str in row['Address'].split(';'):
                    parts = addr_str.strip().split(',')
                    if len(parts) >= 5:
                        addresses.append(Address(
                            street=[parts[0].strip()],
                            city=parts[1].strip(),
                            region=parts[2].strip(),
                            postal_code=parts[3].strip(),
                            country=parts[4].strip()
                        ))

            contact = Contact(
                full_name=row['Full Name'] if pd.notna(row['Full Name']) else '',
                emails=row['Email'].split(';') if pd.notna(row['Email']) else [],
                phones=row['Phone'].split(';') if pd.notna(row['Phone']) else [],
                addresses=addresses,
                organization=row['Organization'] if pd.notna(row['Organization']) else '',
                title=row['Title'] if pd.notna(row['Title']) else ''
            )
            contacts.append(contact)
        return contacts