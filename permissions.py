import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

def compare_permissions(dangerous_permissions, permissions):

    result = []
    
    for perm in permissions:
        for att in perm.attrib:
            permission_manifest = perm.attrib[att]

            for dangerous_permission in dangerous_permissions:

                if dangerous_permission in permission_manifest:

                    result.append("Dangerous:\t{}\n".format(permission_manifest))
    
    return result


def check_permissions(manifest):

    try:
        root = ET.parse(manifest).getroot()
        permissions = root.findall("uses-permission")
        dangerous_permissions = make_request()

        compare_result = compare_permissions(dangerous_permissions, permissions)

        print("[+] Found {} dangerous permissions in AndroidManifest.xml\n".format(len(compare_result)))

        for element in compare_result:
            print(element)

    except FileNotFoundError:
        print('[-] Manifest file not found.')
    
    

def make_request():

    url = "https://developer.android.com/reference/android/Manifest.permission"

    print("\n[+] Requesting {}...\n".format(url))

    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html,'html.parser')

    permissions = []

    # perm_filter = ('normal', 'signature', 'dangerous')

    for element in soup.find_all('div', {"data-version-added" : True}):
        permission = element.h3.get("id")

        if "Protection level:" in element.p.text:
            prot_level = element.p.text.split("level:")[1]

            if "dangerous" in prot_level:
                permissions.append(permission)
    
    return permissions


