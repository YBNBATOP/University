from cryptography.fernet import Fernet
import zipfile
from io import BytesIO
from docx import Document

# Assuming the key is stored in a variable called 'key'
key = "hfUogC40RsWhbqdeD5Ib6QBE4XQTYEUZAYhaBeOy_bw="
cipher_suite = Fernet(key)

# Open the encrypted file in binary mode
with open('LetterToBank.docx', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Write the decrypted data to a BytesIO object
decrypted_bytesio = BytesIO(decrypted_data)

# Extract the BytesIO object with a ZIP library
with zipfile.ZipFile(decrypted_bytesio, 'r') as zip_ref:
    zip_ref.extractall('extracted_files')

# Read the XML file that contains the text of the document
with open('extracted_files/word/document.xml', 'r', encoding='utf-8') as xml_file:
    xml_text = xml_file.read()

# Create a new Document object and add a paragraph with the text of the document
new_doc = Document()
new_doc.add_paragraph(xml_text)

# Save the new Document object to a file
new_doc.save('decrypted_LetterToBank.docx')