
from urllib.parse import urlparse, unquote

def defang(url):
    try:
        unquote(url)
        u = urlparse()
    except:
        return "Invalid URL"

    # hxxps:\/\/www[dot]cwi[dot]nl
    defanged_url = f"{u.scheme.replace('t', 'x')}:\/\/{u.hostname.replace('.', '[dot]')}"

    if u.port:
        defanged_url += ':' + str(u.port)

    if u.path:
        defanged_url += u.path.replace('/', '\/')

    if u.params:
        defanged_url += u.params.replace('/', '\/').replace('.', '[dot]')

    if u.query:
        defanged_url += '?' + u.query.replace('/', '\/').replace('.', '[dot]')

    if u.fragment:
        defanged_url += '#' + u.fragment

    return defanged_url

def refang(fanged_url):
    try:
        u = urlparse(unquote(fanged_url))
    except:
        return "Invalid URL"

    original_url = f"{u.scheme.replace('x', 't')}:\/\/{u.hostname.replace('[dot]', '.')}"

    if u.port:
        original_url += ':' + str(u.port)

    if u.path:
        original_url += u.path.replace('\/', '/')

    if u.params:
        original_url += u.params.replace('\/', '/').replace('[dot]', '.')

    if u.query:
        original_url += '?' + u.query

    if u.fragment:
        original_url += '#' + u.fragment

    return original_url
