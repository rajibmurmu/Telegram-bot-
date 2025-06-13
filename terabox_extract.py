import re, requests

def get_terabox_direct_link(tlink):
    r = requests.get(tlink)
    m = re.search(r'"downloadUrl":"([^"]+)"', r.text)
    if m:
        return m.group(1)
    return None