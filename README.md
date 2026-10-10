# POOPIEMATE — policy pages (legacy address)

This repository serves POOPIEMATE’s privacy policy, terms of service, support page and open-source licenses
at the address that app versions up to 2.0.0 open:

| Page | Korean | English |
|---|---|---|
| Privacy policy | [privacy-ko](https://viva-jinyi.github.io/poopiemate-legal/privacy-ko) | [privacy-en](https://viva-jinyi.github.io/poopiemate-legal/privacy-en) |
| Terms of service | [terms-ko](https://viva-jinyi.github.io/poopiemate-legal/terms-ko) | [terms-en](https://viva-jinyi.github.io/poopiemate-legal/terms-en) |
| Support | [support-ko](https://viva-jinyi.github.io/poopiemate-legal/support-ko) | [support-en](https://viva-jinyi.github.io/poopiemate-legal/support-en) |
| Open-source licenses | [licenses-ko](https://viva-jinyi.github.io/poopiemate-legal/licenses-ko) | [licenses-en](https://viva-jinyi.github.io/poopiemate-legal/licenses-en) |

**These URLs must keep working** — the released app and the store listings link to them.
That is also why this repo stays on this account: a GitHub Pages address belongs to the account that owns the repo.

## Where the content lives

The canonical pages are on **[poopiemate.com](https://poopiemate.com/privacy/)** (`/privacy/`, `/terms/`, `/support/`, `/licenses/` and `/en/…`),
built from [`poopiemate/poopiemate-website`](https://github.com/poopiemate/poopiemate-website) (`src/legal/`).
The pages here are copies of those, with the same text and design, and each one names poopiemate.com as its canonical URL.

## Updating

```bash
# in poopiemate-website
python3 src/build.py
# then here
python3 src/build.py
git add -A && git commit -m "Rebuild policy pages from the latest website" && git push
```

---

<sub>© 2026 Pixelberry · POOPIEMATE · <a href="mailto:poopiemate@pixelberry.io">poopiemate@pixelberry.io</a></sub>
