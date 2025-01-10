import vobject
from typing import List
from models.contact import Contact, Address

class VCFConverter:
    @staticmethod
    def parse_vcf(vcf_content: str) -> List[Contact]:
        contacts = []
        for vcard in vobject.readComponents(vcf_content):
            contact = Contact()
            
            # Extract basic information
            contact.full_name = getattr(vcard, 'fn', '').value if hasattr(vcard, 'fn') else ''
            
            # Extract emails
            if hasattr(vcard, 'email_list'):
                contact.emails = [email.value for email in vcard.email_list]
            
            # Extract phones
            if hasattr(vcard, 'tel_list'):
                contact.phones = [tel.value for tel in vcard.tel_list]
            
            # Extract addresses
            if hasattr(vcard, 'adr_list'):
                for adr in vcard.adr_list:
                    address = Address(
                        street=adr.value.street,
                        city=adr.value.city,
                        region=adr.value.region,
                        postal_code=adr.value.code,
                        country=adr.value.country
                    )
                    contact.addresses.append(address)
            
            # Extract organization and title
            if hasattr(vcard, 'org'):
                contact.organization = vcard.org.value[0]
            if hasattr(vcard, 'title'):
                contact.title = vcard.title.value
            
            contacts.append(contact)
        
        return contacts

    @staticmethod
    def create_vcf(contacts: List[Contact]) -> str:
        vcf_content = []
        for contact in contacts:
            vcard = vobject.vCard()
            
            # Add basic information
            vcard.add('fn').value = contact.full_name
            vcard.add('n').value = vobject.vcard.Name(family='', given=contact.full_name)
            
            # Add emails
            for email in contact.emails:
                vcard.add('email').value = email
            
            # Add phones
            for phone in contact.phones:
                vcard.add('tel').value = phone
            
            # Add addresses
            for addr in contact.addresses:
                vcard.add('adr').value = vobject.vcard.Address(
                    street=addr.street,
                    city=addr.city,
                    region=addr.region,
                    code=addr.postal_code,
                    country=addr.country
                )
            
            # Add organization and title
            if contact.organization:
                vcard.add('org').value = [contact.organization]
            if contact.title:
                vcard.add('title').value = contact.title
            
            vcf_content.append(vcard.serialize())
        
        return ''.join(vcf_content)