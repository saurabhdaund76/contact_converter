from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: List[str]
    city: str
    region: str
    postal_code: str
    country: str

    def format(self) -> str:
        parts = [
            ', '.join(filter(None, self.street)),
            self.city,
            self.region,
            self.postal_code,
            self.country
        ]
        return ', '.join(filter(None, parts))

@dataclass
class Contact:
    full_name: str = ''
    emails: List[str] = None
    phones: List[str] = None
    addresses: List[Address] = None
    organization: str = ''
    title: str = ''

    def __post_init__(self):
        self.emails = self.emails or []
        self.phones = self.phones or []
        self.addresses = self.addresses or []

    def to_dict(self):
        return {
            'Full Name': self.full_name,
            'Email': '; '.join(self.emails),
            'Phone': '; '.join(self.phones),
            'Address': '; '.join(addr.format() for addr in self.addresses),
            'Organization': self.organization,
            'Title': self.title
        }
