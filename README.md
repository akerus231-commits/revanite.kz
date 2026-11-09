# revanite.kz — личный сайт Руслана Хасанова + Revanite Studio

Статический сайт (RU + EN), рассчитанный на индексацию поисковиками и ИИ-системами.

## Структура

На домене два раздельных сайта:

- **revanite.kz/** — личный сайт Руслана Хасанова. Генератор: `build.py`.
- **revanite.kz/studio/** — сайт Revanite Studio (Strategic Growth Partner): четыре направления, методология, кейсы, обучение. Генератор: `studio/build.py`.

Обе части собираются одной командой `python3 build.py` (корневой генератор сам запускает `studio/build.py`). Результат — папка `site/`, студия — в `site/studio/`.

- `site_src/` — исходники: фото `ruslan-khasanov.jpg`, картинка для соцсетей `og-image.jpg` (1200×630). Общие для обоих сайтов.
- `robots.txt` один на домен и ссылается на обе карты сайта: `/sitemap.xml` и `/studio/sitemap.xml`. `llms.txt` — у каждого сайта свой.
- Кейсы студии: `CASES` в `studio/build.py`. Поле «исходная ситуация» показывается, только если заполнено — сейчас пусто у Shanyraq, SAGI и Тумар.

## Как обновить

1. Поправь текст в `build.py` или положи фото в `site_src/ruslan-khasanov.jpg`.
2. Запусти `python3 build.py`. Папка `site/` пересоберётся целиком.
3. Закоммить изменения и залей `site/` на хостинг (GitHub Pages: содержимое `site/` + `CNAME` в ветку `gh-pages`).

## Что внутри для SEO и GEO

- Чистый HTML без JavaScript: ИИ-краулеры видят весь текст.
- JSON-LD schema.org: Person, ProfessionalService (Revanite), FAQPage, Service, BreadcrumbList.
- `llms.txt` с ключевыми фактами на двух языках.
- `sitemap.xml` с hreflang (ru / en / x-default).
- `robots.txt` с разрешением для GPTBot, ClaudeBot, PerplexityBot, Google-Extended, YandexBot, Bingbot и других.

## Открытые вопросы

- Фото (`site_src/ruslan-khasanov.jpg`).
