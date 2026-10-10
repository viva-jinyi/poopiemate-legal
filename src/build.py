"""정책 페이지 — 원본(src/pages)의 본문은 그대로 두고 응가메이트 웹 디자인(초록 헤더·토큰 색·나눔스퀘어 네오)으로 다시 감싼다.
주소(privacy-ko, terms-en …)는 앱·스토어가 링크하므로 바꾸지 않는다.

python3 src/build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = 'https://poopiemate.com'
PAIR = {'privacy': '개인정보 처리방침', 'terms': '이용약관', 'support': '고객 지원', 'licenses': '오픈소스 라이선스'}
PAIR_EN = {'privacy': 'Privacy Policy', 'terms': 'Terms of Service', 'support': 'Support', 'licenses': 'Open-source licenses'}

CSS = '''
@font-face{font-family:"NanumSquareNeo";src:url("https://poopiemate.com/assets/fonts/NanumSquareNeo-cBd.woff2") format("woff2");font-weight:700 900;font-display:swap}
:root{--brand:#18955A;--brand-deep:#0E7041;--brand-subtle:#E5F8F0;--on-color:#FFFFFF;--fg:#191F28;--fg-2:#4E5968;--fg-3:#6B7684;--fg-4:#8B95A1;--line:#E5E8EB;--surface:#F2F4F6;--surface-soft:#F9FAFB}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#FFFFFF;color:var(--fg);font-family:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;line-height:1.75;word-break:keep-all;overflow-wrap:break-word;-webkit-font-smoothing:antialiased}
a{color:var(--brand-deep)}
:focus-visible{outline:3px solid var(--brand);outline-offset:3px;border-radius:6px}
.bar{position:sticky;top:0;z-index:5;height:64px;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);box-shadow:0 1px 0 var(--line);color:var(--fg)}
.bar-in{max-width:1120px;height:100%;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.bar img{height:24px;width:auto;display:block}
.bar nav{display:flex;align-items:center;gap:14px;font-size:13px;font-weight:700}
.bar nav a{color:var(--fg-3);text-decoration:none}
.bar nav a[aria-current="true"]{color:var(--fg)}
.bar .home{display:inline-flex;align-items:center;height:36px;padding:0 16px;border-radius:999px;background:var(--fg);color:var(--on-color)}
.container{max-width:760px;margin:0 auto;padding:clamp(40px,6vw,72px) 20px 40px}
header{margin-bottom:36px;padding-bottom:28px;border-bottom:1px solid var(--line)}
.app-name{font-size:15px;font-weight:700;color:#127F4A}
.lang-switch{display:none}
h1,h2,h3,.contact-card .value{font-family:"NanumSquareNeo","Pretendard Variable",Pretendard,sans-serif}
h1{margin:10px 0 0;font-size:clamp(26px,3.4vw,36px);line-height:1.32;font-weight:700;letter-spacing:-.025em}
.date,.subtitle{margin:12px 0 0;font-size:15px;color:var(--fg-3)}
section{margin-bottom:36px}
h2{margin:0 0 12px;font-size:clamp(18px,1.8vw,20px);line-height:1.45;font-weight:700;letter-spacing:-.015em}
h3{margin:0 0 4px;font-size:16px;font-weight:700}
p{margin:0 0 10px;font-size:16px;color:var(--fg-2)}
ul,ol{margin:0 0 10px;padding-left:20px}
li{margin:6px 0;font-size:16px;color:var(--fg-2)}
strong{color:var(--fg)}
.highlight{padding:16px 20px;border-radius:16px;background:var(--brand-subtle)}
.highlight p{margin:0}
.contact-card{margin:0 0 12px;padding:18px 20px;border-radius:16px;background:var(--surface-soft)}
.contact-card .label{font-size:13px;font-weight:700;color:var(--fg-2)}
.contact-card .value{margin-top:4px;font-size:17px;font-weight:700}
.item{margin-bottom:20px}
.item p{margin-bottom:2px;font-size:15px}
.meta{color:var(--fg-3)}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--line);vertical-align:top;color:var(--fg-2)}
th{font-weight:700;color:var(--fg);white-space:nowrap}
td:nth-child(2){white-space:nowrap}
td:first-child{word-break:break-all}
details{margin-bottom:12px;border-radius:14px;background:var(--surface-soft)}
summary{cursor:pointer;padding:14px 18px;font-size:15px;font-weight:700}
.used-by{padding:0 18px;font-size:13px;color:var(--fg-3)}
pre{margin:0;padding:12px 18px 18px;font-size:12px;line-height:1.6;white-space:pre-wrap;word-break:break-word;color:var(--fg-2)}
.feather{background:none;margin:2px 0 0}
.feather summary{padding:0;font-size:13px;font-weight:400;color:var(--fg-3)}
.feather p{font-size:13px;color:var(--fg-3);margin:4px 0 0}
@media (max-width:600px){thead{display:none}table,tbody,tr,td{display:block;width:100%}tr{padding:10px 0;border-bottom:1px solid var(--line)}td{border:0;padding:0}td:nth-child(2){display:inline;font-size:12px}td:nth-child(3){font-size:12px;color:var(--fg-3)}td:first-child a{display:inline-block;padding:4px 0;min-height:24px}}
.foot{margin-top:24px;padding:40px 20px 48px;background:var(--surface-soft);font-size:13px;color:var(--fg-2)}
.foot-in{max-width:1120px;margin:0 auto;display:flex;flex-wrap:wrap;gap:10px 22px;justify-content:space-between}
.foot a{color:var(--fg-2);text-decoration:none}
.foot nav{display:flex;flex-wrap:wrap;gap:8px 18px}
'''


def build(name):
    src = (ROOT / 'src/pages' / name).read_text(encoding='utf-8')
    lang = 'en' if re.search(r'<html lang="en"', src) else 'ko'
    base = 'privacy' if name == 'index.html' else name.rsplit('-', 1)[0]
    cur = lambda l: ' aria-current="true"' if l == lang else ''
    head = src[:src.index('<style>')] + '<link rel="icon" href="https://poopiemate.com/favicon.ico" sizes="48x48">\n  <meta name="theme-color" content="#18955A">\n  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">\n  <style>' + CSS + '  </style>\n</head>\n'
    m = re.search(r'<div class="container">(.*)</div>\s*(<script>.*?</script>)?\s*</body>', src, re.S)
    body, script = m.group(1), m.group(2) or ''
    body = re.sub(r'\s*<footer>.*?</footer>', '', body, flags=re.S)
    labels = PAIR if lang == 'ko' else PAIR_EN
    links = ''.join(f'<a href="./{k}-{lang}">{v}</a>' for k, v in labels.items())
    bar = (f'<div class="bar" role="banner"><div class="bar-in"><a href="{WEB}{"/" if lang == "ko" else "/en/"}"><img src="{WEB}/assets/brand/wordmark-{lang}-green.svg" alt="{"응가메이트" if lang == "ko" else "PoopieMate"}" width="120" height="32"></a>'
           f'<nav aria-label="{"언어" if lang == "ko" else "Language"}">'
           f'<a href="./{base}-ko" lang="ko" hreflang="ko"{cur("ko")}>KO</a><a href="./{base}-en" lang="en" hreflang="en"{cur("en")}>EN</a>'
           f'<a class="home" href="{WEB}{"/" if lang == "ko" else "/en/"}">{"홈페이지" if lang == "ko" else "Website"}</a></nav></div></div>')
    sns = [('YouTube', 'https://www.youtube.com/@poopiemate'), ('TikTok', 'https://www.tiktok.com/@poopiemate'),
           ('Instagram', 'https://www.instagram.com/poopiemate_kr' if lang == 'ko' else 'https://www.instagram.com/poopiemate'),
           ('LinkedIn', 'https://www.linkedin.com/company/poopiemate')]
    sns_nav = ''.join(f'<a href="{h}" rel="noopener">{n}</a>' for n, h in sns)
    foot = (f'<footer class="foot"><div class="foot-in"><nav>{links}</nav><nav aria-label="SNS">{sns_nav}</nav>'
            f'<span>© 2026 {"픽셀베리 · 응가메이트" if lang == "ko" else "Pixelberry · PoopieMate"} · <a href="mailto:poopiemate@pixelberry.io">poopiemate@pixelberry.io</a></span></div></footer>')
    out = head + '<body>\n' + bar + '\n<main class="container">' + body + '</main>\n' + foot + '\n' + script + '\n</body>\n</html>\n'
    (ROOT / name).write_text(out, encoding='utf-8')


if __name__ == '__main__':
    for f in sorted((ROOT / 'src/pages').glob('*.html')):
        build(f.name)
        print(f.name)
