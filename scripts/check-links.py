from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'dist'
errors = []

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else page.parent / unquote(url.path)
            if not target.is_file() and not (target / 'index.html').is_file():
                errors.append(f'{page.relative_to(root)}: {value}')

for page in root.rglob('*.html'):
    Links().feed(page.read_text())
if errors:
    raise SystemExit('Broken local links:\n' + '\n'.join(errors))
print('All local links and assets exist.')
