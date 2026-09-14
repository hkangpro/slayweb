# Slay Solution — Weave 소개 사이트

정적 사이트 한 장입니다. 빌드 과정이 없고, `index.html`을 그대로 올립니다.

## 파일

| 파일 | 내용 |
|---|---|
| `index.html` | 페이지 전체. CSS와 스크립트 인라인. 배경 천은 canvas, 영한 전환은 `data-lang` 하나로 |
| `og.png` | 카톡·문자·링크드인에 링크를 붙였을 때 뜨는 미리보기 이미지 |
| `favicon.svg`, `apple-touch-icon.png` | 브라우저 탭 아이콘, 폰 홈 화면 아이콘 |

## 올리는 법 (Vercel)

1. 이 폴더를 GitHub 비공개 리포로 올립니다.
2. Vercel에서 그 리포를 Import 합니다. 프레임워크는 **Other**, 빌드 명령 없음, 출력 폴더는 루트입니다.
3. Vercel 프로젝트 설정 → Domains 에 `slaysolution.com` 과 `www.slaysolution.com` 을 넣습니다.
4. 완료 — Zoho DNS에 A(apex)와 CNAME(www)이 들어가 있습니다. MX·SPF는 Microsoft 365용이니 건드리지 마십시오.

고치는 방법은 `index.html`을 수정하고 GitHub에 push 하는 것뿐입니다. Vercel이 알아서 다시 올립니다.

## 연락처

페이지에 박혀 있는 값입니다. 바꾸려면 `index.html`에서 `info@slaysolution.com` / `571-419-2673` / `JB Yoon` 을 찾습니다.

## 아직 안 정한 것

- DKIM — Microsoft 365 관리자에서 켜야 합니다 (SPF·DMARC는 완료).
- 영문판 — 푸터 한 줄만 영어입니다.

## 로고와 색

마크는 **점으로 이은 W**입니다. 실이 엮이는 모양이면서, 점과 선으로 이어진 형태가 AI를 암시합니다. `logo-mark.svg`가 원본이고, 같은 모양이 파비콘·폰 아이콘·링크 카드에 들어갑니다.

| 쓰임 | 값 |
|---|---|
| 초록 (강조) | `#0f5c4a` |
| 종이 | `#f2efe7` |
| 기둥 | `#0e1c17` |
| 바탕 | `#f3f5f0` |
| 글자 | `#151d18` |
| 흐린 글자 | `#4d5a51` · `#7d8a80` |
| 선 | `#d2d9cd` |
| 제목 서체 | Bebas Neue (영문) · Noto Sans KR 700 (국문) |
| 본문 서체 | Open Sans · Noto Sans KR |
| 라벨 서체 | Open Sans 600, 대문자, 자간 넓게 |

마크는 초록 단색으로만 씁니다. 그라데이션이나 그림자를 넣지 마십시오.
