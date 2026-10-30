"""Build the static routes and the self-contained customer attachment (stdlib only)."""
import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / 'templates/upgrade.html').read_text()
for route, assets in [('index.html', 'assets'), ('firepi/index.html', '../assets'), ('vigilpoint/index.html', '../assets')]:
    target = ROOT / route
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEMPLATE.replace('{{ASSETS}}', assets))

standalone = re.sub(
    r'<link\s+rel="stylesheet"\s+href="\{\{ASSETS\}\}/site.css"\s*/?>',
    lambda _: '<style>' + (ROOT / 'assets/site.css').read_text() + '</style>',
    TEMPLATE,
)
def embed(match):
    attribute, relative = match.groups()
    file = ROOT / 'assets' / relative
    mime = mimetypes.guess_type(str(file))[0] or 'application/octet-stream'
    uri = 'data:' + mime + ';base64,' + base64.b64encode(file.read_bytes()).decode()
    download = ' download="' + file.name + '"' if attribute == 'href' and relative.startswith('screenshots/') else ''
    return attribute + '="' + uri + '"' + download
standalone = re.sub(r'(src|href)="\{\{ASSETS\}\}/([^"?]+)"', embed, standalone)
(ROOT / 'share').mkdir(exist_ok=True)
(ROOT / 'share/vigilpoint-upgrade.html').write_text(standalone)
print('Built root, /firepi/, /vigilpoint/ and share/vigilpoint-upgrade.html')
