"""정책 페이지 원본과 디자인은 poopiemate.com(poopiemate-website)에 있다 (2026-10-10 이관).
앱·스토어가 이 주소(privacy-ko, terms-en …)를 링크하므로, 이 주소에서도 같은 페이지가 그대로 열리게 한다.
웹사이트를 빌드한 뒤 그 결과(privacy/index.html …)를 가져와, 사이트 안 경로(/assets/…, /privacy/ …)만 poopiemate.com 절대 주소로 바꾼다.
검색엔진에는 canonical로 poopiemate.com 쪽이 원본이라고 알려 준다.

python3 src/build.py     (../poopiemate-website 를 먼저 빌드)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT.parent / 'poopiemate-website'
SITE = 'https://poopiemate.com'
PAGES = {
    'index': '/privacy/', 'privacy-ko': '/privacy/', 'privacy-en': '/en/privacy/',
    'terms-ko': '/terms/', 'terms-en': '/en/terms/',
    'support-ko': '/support/', 'support-en': '/en/support/',
    'licenses-ko': '/licenses/', 'licenses-en': '/en/licenses/',
}

for name, path in PAGES.items():
    html = (WEB / path.strip('/') / 'index.html').read_text(encoding='utf-8')
    # 사이트 안 경로를 poopiemate.com 절대 주소로 (//로 시작하는 외부 주소는 그대로)
    html = re.sub(r'(\s(?:src|href|poster|content)=")/(?!/)', rf'\1{SITE}/', html)
    html = re.sub(r'(srcset="[^"]*)', lambda m: re.sub(r'(^srcset="|,\s*)/(?!/)', rf'\1{SITE}/', m.group(1)), html)
    (ROOT / f'{name}.html').write_text(html, encoding='utf-8')
    print(name, '←', SITE + path)
