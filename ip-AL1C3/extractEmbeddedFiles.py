# This program was used in the SAIT 2025 summer CTF, AL1C3 1N PWND3RLAND CTF, and was written by me.

# During the challenge, Das Auge sieht ein Geheimnis, a ZIP archive is embedded in a PDF and it needs to be extracted
# Binwalk was used originally to try and extract the file(s), instead could only give me an offset of where they started

offset = 0xA0C6                        # offset where ZIP archive starts from the binwalk output
output_zip = "embedded.zip"            # where the contents would be stored once extracted
input_pdf = "alice_diary_page.pdf"     # the file that would be extracted from

with open(input_pdf, "rb") as f:
    f.seek(offset)
    data = f.read()

eocd_signature = b"PK\x05\x06"      # what ZIP files end with, "End of central directory record" signature: b'PK\x05\x06'
pos = data.rfind(eocd_signature)

if pos != -1:
    zip_data = data[:pos+22]        # eocd record size is usually 22 bytes minimum
else:
    zip_data = data                 # fallback: just dump everything from offset to EOF

with open(output_zip, "wb") as f:
    f.write(zip_data)

print(f"Extracted embedded zip archive to '{output_zip}'")
