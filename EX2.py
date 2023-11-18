import os
import re

fichier_txt = "emails_file.txt"
pattern1 = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
pattern = r"([a-zA-Z0-9._-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
pattern2 = r'\b(?![._-])(?!.*\-\-)(?!.*\.\.)[A-Za-z0-9._-]+@(?![._-])[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'


with open(fichier_txt,"r") as f:
  ligne = f.read()
  emails = re.findall(pattern2,ligne)
sorted_emails = emails.sort()
print(emails)
for email in emails:
  ecole_name = email.split("@")[1].split(".")[0]
  with open(ecole_name+".txt","a") as file:
    file.write(f"{email}\n")


# split("@ ") كتقسم الstring  الا كانت  ['hanan.berrachidfpb@estfbs.usms.ac.ma'] اتولي ['hanan.berrachidfpb', 'estfbs.usms.ac.ma']


