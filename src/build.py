"""정책 페이지는 poopiemate.com으로 옮겼다 (2026-10-10).
앱·스토어가 이 주소(privacy-ko, terms-en …)를 링크하므로 파일은 남겨 두고 새 주소로 바로 넘긴다.
본문 원본은 poopiemate-website/src/legal/ 에 있다.

python3 src/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = 'https://poopiemate.com'
PAGES = {
    'index': ('ko', '/privacy/', '개인정보 처리방침'), 'privacy-ko': ('ko', '/privacy/', '개인정보 처리방침'), 'privacy-en': ('en', '/en/privacy/', 'Privacy Policy'),
    'terms-ko': ('ko', '/terms/', '이용약관'), 'terms-en': ('en', '/en/terms/', 'Terms of Service'),
    'support-ko': ('ko', '/support/', '고객 지원'), 'support-en': ('en', '/en/support/', 'Support'),
    'licenses-ko': ('ko', '/licenses/', '오픈소스 라이선스'), 'licenses-en': ('en', '/en/licenses/', 'Open-source licenses'),
}

for name, (lang, path, title) in PAGES.items():
    to = NEW + path
    note = '새 주소로 이동하고 있어요.' if lang == 'ko' else 'This page has moved.'
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {"응가메이트" if lang == "ko" else "PoopieMate"}</title>
<link rel="canonical" href="{to}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace({to!r} + location.hash);</script>
</head>
<body>
<main><p>{note} <a href="{to}">{to}</a></p></main>
</body>
</html>
'''
    (ROOT / f'{name}.html').write_text(html, encoding='utf-8')
    print(name, '→', to)
