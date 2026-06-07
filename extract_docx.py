import zipfile, xml.etree.ElementTree as ET

def extract(f):
    z = zipfile.ZipFile(f)
    root = ET.fromstring(z.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    return '\n'.join(n.text for n in root.findall('.//w:t', ns) if n.text)

open('network_project.txt', 'w', encoding='utf-8').write(extract('network_project.docx'))
open('capstone_req.txt', 'w', encoding='utf-8').write(extract('networking_capstone_requirements.docx'))
