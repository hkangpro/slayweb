#!/usr/bin/env python3
"""소스 한 벌에서 영문(/)과 국문(/ko/) 두 페이지를 만든다.
   소스: ../slay-weave-design/site/index.html  (두 언어가 다 들어 있음)
   고칠 때는 소스를 고치고 python3 build.py 를 돌린다."""
import pathlib, re, sys

SRC = pathlib.Path(__file__).parent.parent / 'slay-weave-design/site/index.html'
OUT = pathlib.Path(__file__).parent
ORIGIN = 'https://www.slaysolution.com'

def strip_lang(html, drop):
    """class="l-<drop>" 인 요소를 여는/닫는 태그 짝을 세어 통째로 지운다."""
    out, i = [], 0
    pat = re.compile(r'<(\w+)([^>]*\bclass="[^"]*\bl-%s\b[^"]*"[^>]*)>' % drop)
    while True:
        m = pat.search(html, i)
        if not m:
            out.append(html[i:]); break
        out.append(html[i:m.start()])
        tag = m.group(1)
        depth, j = 1, m.end()
        open_re = re.compile(r'<%s\b' % tag, re.I)
        close_re = re.compile(r'</%s\s*>' % tag, re.I)
        while depth:
            o, c = open_re.search(html, j), close_re.search(html, j)
            if not c:
                sys.exit(f'닫는 </{tag}> 를 못 찾음')
            if o and o.start() < c.start():
                depth += 1; j = o.end()
            else:
                depth -= 1; j = c.end()
        i = j
    return ''.join(out)

def head_for(lang):
    other = 'ko' if lang == 'en' else 'en'
    self_url = ORIGIN + ('/' if lang == 'en' else '/ko/')
    if lang == 'en':
        title = 'Relai — Your systems stay. The work between them goes.'
        desc = ('Relai connects the accounting, payroll and field systems you already run and takes '
                'over the work between them. Nothing reaches your books until a person approves it. '
                'Retail, restaurants, custom fabrication and construction.')
        ogt = 'Relai — Your systems stay. The work between them goes.'
        ogd = ('We connect the systems you already run and take over the work between them. '
               'Nothing reaches your books until a person approves it.')
        loc, alt = 'en_US', 'ko_KR'
    else:
        title = 'Relai — 쓰던 시스템은 그대로. 그 사이 일은 저희가 합니다.'
        desc = ('지금 쓰시는 Accounting, Payroll, 현장 시스템 그대로 두고 그 사이에서 옮겨 적고 맞춰 보던 일만 '
                '가져갑니다. 장부에 올라가는 건 사람이 한 번 보고 눌러야 들어갑니다. 소매·도매, 식당, '
                '주문 제작, 건설.')
        ogt = 'Relai — 쓰던 시스템은 그대로. 그 사이 일은 저희가 합니다.'
        ogd = '쓰시던 시스템 그대로 두고 그 사이 일만 저희가 맡습니다. 장부에 올라가는 건 사람이 눌러야 들어갑니다.'
        loc, alt = 'ko_KR', 'en_US'
    return f'''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="en" href="{ORIGIN}/">
<link rel="alternate" hreflang="ko" href="{ORIGIN}/ko/">
<link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#f2efe7">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Slay Solution">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{ogd}">
<meta property="og:url" content="{self_url}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{loc}">
<meta property="og:locale:alternate" content="{alt}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Slay Solution","url":"{ORIGIN}/","email":"info@slaysolution.com","telephone":"+1-571-419-2673","areaServed":"US","makesOffer":{{"@type":"Offer","itemOffered":{{"@type":"SoftwareApplication","name":"Relai","applicationCategory":"BusinessApplication","operatingSystem":"Web"}}}}}}
</script>'''

def build(lang):
    s = SRC.read_text()
    s = strip_lang(s, 'ko' if lang == 'en' else 'en')
    s = re.sub(r'\sclass="l-(?:en|ko)"', '', s)
    s = re.sub(r'\sclass="l-(?:en|ko) ', ' class="', s)

    # <head>
    s = re.sub(r'<title>.*?</script>\n', head_for(lang) + '\n', s, count=1, flags=re.S)
    s = s.replace('<html lang="en" data-lang="en">', f'<html lang="{lang}" data-lang="{lang}">', 1)

    # 언어 전환을 버튼에서 링크로
    home = '/' if lang == 'en' else '/ko/'
    en_cls, ko_cls = ('on', '') if lang == 'en' else ('', 'on')
    s = s.replace('<div class="lang"><button data-l="en" class="on">EN</button><button data-l="ko">KO</button></div>',
                  f'<div class="lang"><a href="/" class="{en_cls}" hreflang="en">EN</a>'
                  f'<a href="/ko/" class="{ko_cls}" hreflang="ko">KO</a></div>', 1)
    s = s.replace('.lang button{', '.lang a{').replace('.lang button.on{', '.lang a.on{')
    s = s.replace('.lang button:hover:not(.on){', '.lang a:hover:not(.on){')
    s = s.replace('.lang{display:inline-flex;border:1px solid rgba(242,239,231,.26)}',
                  '.lang{display:inline-flex;border:1px solid rgba(242,239,231,.26)}\n'
                  '.lang a{display:block;min-width:46px;text-align:center}')

    # 로고를 홈 링크로
    s = s.replace('<div class="badge">', f'<a class="badge" href="{home}" aria-label="Relai — home">', 1)
    s = s.replace('</svg></div>\n  <nav class="rnav">', '</svg></a>\n  <nav class="rnav">', 1)

    # 전환 스크립트 제거 (링크가 대신한다)
    s = re.sub(r"document\.querySelectorAll\('\.lang button'\).*?\n\}\) ?;\n", '', s, count=1, flags=re.S)
    s = re.sub(r"try \{\n  const saved = localStorage.*?\n\} catch \(e\) \{\}\n", '', s, count=1, flags=re.S)

    # 인트로는 한 방문에 한 번만. 로고로 돌아오거나 언어를 바꿀 땐 바로 화면이 뜬다.
    # (깜빡임이 없도록 <head> 에서 먼저 판단한다)
    s = s.replace('</head>', '''<script>
try { if (sessionStorage.getItem('relai-intro') === '1') document.documentElement.setAttribute('data-intro','skip');
      else sessionStorage.setItem('relai-intro','1'); } catch (e) {}
</script>
</head>''', 1)
    s = s.replace('</script>\n</body>', '''(function () {
  const el = document.getElementById('intro');
  if (!el) return;
  const kill = () => { el.remove(); };
  if (document.documentElement.getAttribute('data-intro') === 'skip') { kill(); return; }
  // animationend 는 자식 애니메이션에서도 올라온다. 마지막 퇴장 동작만 본다.
  el.addEventListener('animationend', (e) => {
    if (e.target === el && e.animationName === 'introOut') kill();
  });
  setTimeout(kill, 3850);
})();
</script>
</body>''', 1)
    s = s.replace('#intro{position:fixed;inset:0;z-index:80;',
                  '#intro{position:fixed;inset:0;z-index:80;pointer-events:none;', 1)
    s = s.replace('@keyframes introOut{to{opacity:0;visibility:hidden}}',
                  '@keyframes introOut{to{opacity:0;visibility:hidden}}\n'
                  'html[data-intro="skip"] #intro{display:none}', 1)
    return s

en = build('en'); ko = build('ko')
(OUT / 'index.html').write_text(en)
(OUT / 'ko').mkdir(exist_ok=True)
(OUT / 'ko/index.html').write_text(ko)

(OUT / 'sitemap.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{ORIGIN}/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{ORIGIN}/"/>
    <xhtml:link rel="alternate" hreflang="ko" href="{ORIGIN}/ko/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{ORIGIN}/"/>
  </url>
  <url><loc>{ORIGIN}/ko/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{ORIGIN}/"/>
    <xhtml:link rel="alternate" hreflang="ko" href="{ORIGIN}/ko/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{ORIGIN}/"/>
  </url>
</urlset>
''')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n')
print(f'EN {len(en):,}b  ·  KO {len(ko):,}b  ·  sitemap.xml  ·  robots.txt')
