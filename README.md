# Slay Solution — Weave 소개 사이트

정적 사이트 한 장입니다. 빌드 과정이 없고, `index.html`을 그대로 올립니다.

## 파일

| 파일 | 내용 |
|---|---|
| `index.html` | 페이지 전체 (CSS 인라인, 스크립트 없음) |
| `og.png` | 카톡·문자·링크드인에 링크를 붙였을 때 뜨는 미리보기 이미지 |
| `favicon.svg`, `apple-touch-icon.png` | 브라우저 탭 아이콘, 폰 홈 화면 아이콘 |

## 올리는 법 (Vercel)

1. 이 폴더를 GitHub 비공개 리포로 올립니다.
2. Vercel에서 그 리포를 Import 합니다. 프레임워크는 **Other**, 빌드 명령 없음, 출력 폴더는 루트입니다.
3. Vercel 프로젝트 설정 → Domains 에 `slaysolution.com` 과 `www.slaysolution.com` 을 넣습니다.
4. 도메인 등록처(또는 Cloudflare) DNS에 Vercel이 알려주는 A/CNAME 레코드를 넣습니다.

고치는 방법은 `index.html`을 수정하고 GitHub에 push 하는 것뿐입니다. Vercel이 알아서 다시 올립니다.

## 연락처

페이지에 박혀 있는 값입니다. 바꾸려면 `index.html`에서 `info@slaysolution.com` / `571-419-2673` / `JB Yoon` 을 찾습니다.

## 아직 안 정한 것

- 요금 숫자 — 지금은 세 칸 모두 "문의"입니다.
- 영문판 — 푸터 한 줄만 영어입니다.
