# -*- coding: utf-8 -*-
"""Генератор статического сайта revanite.kz (RU/EN).
Запуск: python3 build.py  ->  папка site/
Чтобы добавить фото: положи файл в site_src/ruslan-khasanov.jpg.
Картинка для соцсетей (1200×630): site_src/og-image.jpg.
"""
import json, os, shutil, datetime

BASE = "https://revanite.kz"
PHOTO = os.path.exists("site_src/ruslan-khasanov.jpg")
PHOTO_URL = BASE + "/assets/ruslan-khasanov.jpg"
TODAY = datetime.date.today().isoformat()
OUT = "site"

IG = "https://www.instagram.com/hasanov5/"
LI = "https://www.linkedin.com/in/ruslan-khassanov-0bb812202"
TG = "https://t.me/messer66"
WA = "https://wa.me/77014584242"
PHONE = "+77014584242"
PHONE_H = "+7 701 458 42 42"
SAME_AS = [IG, LI, TG]
CLIENTS = {
 "ru": ["Бакай Банк (Тумар)", "Глоббинг Казахстан", "Yeko Kazakhstan", "SAGI", "Shanyraq Business Forum", "BI GROUP",
        "Geometry", "Jintropine", "Youtrade", "InnMedia"],
 "en": ["Bakai Bank (Tumar)", "Globbing Kazakhstan", "Yeko Kazakhstan", "SAGI", "Shanyraq Business Forum", "BI GROUP",
        "Geometry", "Jintropine", "Youtrade", "InnMedia"],
}

# Блок клиентов на главной: (заголовок группы, названия)
GROUPS = {
 "ru": [("Клиенты", CLIENTS["ru"]),
        ("Опыт работы", ["re:Kassa", "Alfa Bank", "Home Credit Bank", "Halyk Insurance", "Samsung Kazakhstan"]),
        ("Трекинг и преподавание", ["Astana Hub", "Almaty Hub", "Terricon Valley", "NURIS", "IT Park", "AlmaU", "Qamalladin University"])],
 "en": [("Clients", CLIENTS["en"]),
        ("Previously at", ["re:Kassa", "Alfa Bank", "Home Credit Bank", "Halyk Insurance", "Samsung Kazakhstan"]),
        ("Tracking and teaching", ["Astana Hub", "Almaty Hub", "Terricon Valley", "NURIS", "IT Park", "AlmaU", "Qamalladin University"])],
}

STATS = {
 "ru": [("316%", "ROMI — приложение программы лояльности SAGI"), ("×2,4", "снижение стоимости лида — Yeko Kazakhstan"),
        ("−45%", "стоимость регистрации — Глоббинг Казахстан"), ("1 600+", "обращений за один запуск — Shanyraq Business Forum")],
 "en": [("316%", "ROMI — SAGI loyalty app"), ("×2.4", "lower cost per lead — Yeko Kazakhstan"),
        ("−45%", "cost per sign-up — Globbing Kazakhstan"), ("1,600+", "leads from a single launch — Shanyraq Business Forum")],
}
STATS_NOTE = {
 "ru": "Трекер стартапов в 5 IT-хабах Казахстана · Преподаватель AlmaU, Qamalladin University и колледжа ICB",
 "en": "Startup tracker at 5 Kazakhstan tech hubs · Lecturer at AlmaU, Qamalladin University and ICB College",
}

# Цена экспресс-диагностики: старая (зачёркнутая) и действующая
PRICE_OLD, PRICE = "$200", "$99"
PRICE_HTML = f'<span class="price"><s>{PRICE_OLD}</s> {PRICE}</span>'

# Кейсы: (название, каналы и инструменты, задача, решение, результат)
CASES = {
 "ru": [
  ("Shanyraq Business Forum — бизнес-форум, 3 города", "Meta Ads, WhatsApp, amoCRM, чат-бот",
   "Обеспечить продажи билетов и прозрачность воронки — от клика до оплаты.",
   ["Еженедельный анализ воронки в amoCRM: статусы сделок, источники, эффективность менеджеров, доля квалифицированных заявок.",
    "Аудит коммуникаций отдела продаж в WhatsApp: выявлены 4 системные ошибки, по итогам внедрён чат-бот.",
    "Данные рекламных кабинетов и CRM объединены в единую систему отчётности."],
   "1 600+ заявок и обращений за первый запуск, ROAS 234%. Формат масштабирован на Шымкент и Алматы."),
  ("Глоббинг Казахстан — сервис доставки покупок из-за рубежа", "Meta Ads",
   "Увеличить приток новых пользователей при снижении стоимости привлечения.",
   ["Анализ эффективности по городам: выявлены регионы с низкой отдачей бюджета.",
    "Аудит структуры рекламного кабинета: избыточная фрагментация кампаний ограничивала обучение алгоритма.",
    "Тестирование аудиторий блогеров против гео-таргетинга и перераспределение бюджета по результатам."],
   "+60% новых регистраций при снижении стоимости регистрации на 45%."),
  ("Yeko Kazakhstan — отечественный бренд техники", "Онлайн-реклама, квалификация лидов",
   "Повысить качество входящих заявок, а не только их количество.",
   ["Перестройка онлайн-рекламы под качество лидов: оптимизация по квалифицированным заявкам вместо объёма."],
   "Доля квалифицированных лидов выросла с 30% до 70%, стоимость лида снизилась в 2,4 раза."),
  ("SAGI — приложение программы лояльности", "Онлайн-реклама, продуктовая воронка",
   "Привлекать пользователей в приложение с окупаемостью рекламных вложений.",
   ["Запуск и ведение онлайн-рекламы, управление воронкой от первого касания до целевого действия, оптимизация по возврату инвестиций."],
   "ROMI 316%."),
  ("Карта рассрочки Тумар, Бакай Банк (Кыргызстан)", "Google Ads, Meta Ads, мобильная атрибуция, CRM-маркетинг",
   "Построить цифровой канал с равномерным ежемесячным притоком клиентов.",
   ["Структура кампаний Google Ads и лид-кампании Meta с ежемесячной отчётностью.",
    "Интеграция мобильной атрибуции приложения с рекламными кабинетами.",
    "Программа активации выданных карт с сегментацией базы — «не совершали покупок», «снижают активность», «неактивны» — и партнёрскими предложениями для каждого сегмента."],
   "Стабильный ежемесячный поток новых клиентов банка и отдельная программа активации действующих держателей карт."),
  ("BI GROUP и Geometry — девелопмент", "Meta Ads, юнит-экономика",
   "Выстроить цифровое привлечение с нуля при отсутствии данных о стоимости клиента.",
   ["Построение цифровой воронки, расчёт стоимости привлечения клиента (CAC) и оптимизация рекламы по этой метрике."],
   "Команда получила измеримую стоимость клиента; реклама оптимизируется по CAC, а не по кликам и охватам."),
 ],
 "en": [
  ("Shanyraq Business Forum — business forum, 3 cities", "Meta Ads, WhatsApp, amoCRM, chatbot",
   "Drive ticket sales and make the funnel transparent from click to payment.",
   ["Weekly amoCRM funnel analysis: deal stages, sources, sales rep performance, qualified-lead share.",
    "Audit of the sales team's WhatsApp communication: 4 systemic errors identified, followed by a chatbot rollout.",
    "Ad account and CRM data consolidated into a single reporting system."],
   "1,600+ leads from the first launch, 234% ROAS. The format was scaled to Shymkent and Almaty."),
  ("Globbing Kazakhstan — cross-border shopping delivery", "Meta Ads",
   "Increase new user acquisition while lowering acquisition cost.",
   ["City-level performance analysis: regions with low budget efficiency identified.",
    "Ad account structure audit: excessive campaign fragmentation was limiting algorithm learning.",
    "Blogger-audience vs. geo-targeting test, with budget reallocated based on the results."],
   "+60% new sign-ups with a 45% lower cost per sign-up."),
  ("Yeko Kazakhstan — local electronics brand", "Online ads, lead qualification",
   "Improve the quality of inbound leads, not just their volume.",
   ["Online advertising rebuilt around lead quality: optimizing for qualified leads instead of volume."],
   "Qualified lead share rose from 30% to 70%; cost per lead fell 2.4×."),
  ("SAGI — loyalty app", "Online ads, product funnel",
   "Acquire app users with advertising that pays back.",
   ["Online acquisition launched and managed, funnel managed from first touch to the target action, optimized for return on investment."],
   "316% ROMI."),
  ("Tumar installment card, Bakai Bank (Kyrgyzstan)", "Google Ads, Meta Ads, mobile attribution, CRM marketing",
   "Build a digital channel with a steady monthly inflow of customers.",
   ["Google Ads campaign structure and Meta lead campaigns with monthly reporting.",
    "Mobile app attribution integrated with the ad accounts.",
    "Activation program for issued cards, segmenting the base — no purchases yet, declining activity, inactive — with partner offers for each segment."],
   "A steady monthly flow of new bank customers and a dedicated activation program for existing cardholders."),
  ("BI GROUP and Geometry — real estate", "Meta Ads, unit economics",
   "Build digital acquisition from scratch with no data on the cost of a customer.",
   ["Digital funnel built, customer acquisition cost (CAC) calculated and advertising optimized against that metric."],
   "The team now has a measurable cost per customer; advertising is optimized for CAC rather than clicks and reach."),
 ],
}

# Трекинг: (цифра, подпись, название, теги, что изменилось)
TRACK = {
 "ru": [
  ("×1,6", "рост выручки", "Youtrade", "Трекинг · Операционные процессы",
   ["Рост выручки в 1,6 раза", "Перестройка операционных процессов", "Выход фаундера из операционного управления"]),
  ("3", "первых контракта в Казахстане", "InnMedia", "Трекинг · Выход на рынок",
   ["Выход на рынок Казахстана", "Первые 3 контракта", "Адаптация продукта под местный рынок"]),
  ("30%", "выручки — недоиспользуемый партнёрский канал", "Онлайн-школа", "Трекинг · Стратегия рынков",
   ["Анализ продаж: зарубежную выручку формирует русскоязычная диаспора",
    "Смена приоритетных рынков: Узбекистан и Турция вместо США",
    "Выявлен недоиспользуемый партнёрский канал, обеспечивавший около 30% выручки"]),
 ],
 "en": [
  ("×1.6", "revenue growth", "Youtrade", "Tracking · Operations",
   ["Revenue up 1.6×", "Operating processes rebuilt", "Founder moved out of day-to-day operations"]),
  ("3", "first contracts in Kazakhstan", "InnMedia", "Tracking · Market entry",
   ["Entry into the Kazakhstan market", "First 3 contracts", "Product adapted for the local market"]),
  ("30%", "of revenue from an under-used affiliate channel", "Online school", "Tracking · Market strategy",
   ["Sales analysis: foreign revenue came from the Russian-speaking diaspora",
    "Priority markets shifted from the US to Uzbekistan and Turkey",
    "Under-used affiliate channel identified, already generating about 30% of revenue"]),
 ],
}

CASES_NOTE = {
 "ru": "Jintropine — сквозная аналитика Meta Ads и amoCRM: источник каждой заявки из WhatsApp фиксируется в CRM, реклама связана с продажами в едином дашборде.",
 "en": "Jintropine — end-to-end analytics across Meta Ads and amoCRM: the source of every WhatsApp lead is recorded in the CRM, and advertising is tied to sales in a single dashboard.",
}

def socials(lang):
    ru = lang == "ru"
    return [("Telegram", "@messer66", TG), ("WhatsApp", "Чат WhatsApp" if ru else "WhatsApp chat", WA),
            ("Телефон" if ru else "Phone", PHONE_H, "tel:" + PHONE), ("Instagram", "@hasanov5", IG),
            ("LinkedIn", "ruslan-khassanov", LI)]

PAGES = ["", "about", "services", "cases", "teaching", "contact"]
NAV = ["", "cases", "services", "teaching", "contact"]

def url(lang, slug):
    prefix = "" if lang == "ru" else "/en"
    return BASE + prefix + "/" + (slug + "/" if slug else "")

def path(lang, slug):
    prefix = "" if lang == "ru" else "/en"
    return prefix + "/" + (slug + "/" if slug else "")

# ---------------------------------------------------------------- TEXT
T = {
 "ru": {
  "name": "Руслан Хасанов",
  "role": "Консультант по росту бизнеса · трекер стартапов · преподаватель",
  "about": [
   "Я консультант по росту бизнеса из Алматы и основатель студии стратегического роста Revanite. Карьеру строил в корпоративном секторе: был CMO фискальной платформы re:Kassa, руководил digital-маркетингом в Home Credit Bank, занимал позицию директора по продукту в Halyk Insurance, отвечал за маркетинг сегмента малого бизнеса в Alfa Bank, участвовал в запуске онлайн-магазина Samsung Kazakhstan.",
   "Сегодня работаю независимо. Как трекер сопровождаю стартапы в Astana Hub, Almaty Hub, Terricon Valley, NURIS и IT Park. Через Revanite веду проекты для компаний Казахстана и Кыргызстана — от стратегии и продаж до маркетинга, CRM и автоматизации процессов. Преподаю digital-маркетинг и веб-аналитику в AlmaU, руковожу направлением «Диджитал» в Qamalladin University.",
   "Мой подход: сначала определить, где бизнес теряет рост и деньги, и только затем инвестировать. Стратегию, продажи, маркетинг и процессы рассматриваю как единую систему, результат которой измеряется выручкой и окупаемостью.",
  ],
  "nav": {"": "Главная", "about": "Обо мне", "services": "Услуги", "cases": "Кейсы", "teaching": "Преподавание", "contact": "Контакты"},
  "home": "Главная",
  "switch": ("EN", "English version"),
  "contact": "Связаться",
  "footer": "Руслан Хасанов · Revanite — студия стратегического роста · Алматы, Казахстан",
  "jobTitle": "Консультант по росту бизнеса",
  "summary": ("Руслан Хасанов — консультант по росту бизнеса из Алматы (Казахстан), основатель студии стратегического роста Revanite. "
              "Находит ограничения роста в стратегии, продажах, маркетинге, процессах и экономике бизнеса и выстраивает систему роста: "
              "от воронки продаж и рекламы до CRM, сквозной аналитики и автоматизации. Был CMO фискальной платформы re:Kassa, "
              "руководил digital-маркетингом в Home Credit Bank, был директором по продукту в Halyk Insurance, отвечал за маркетинг "
              "сегмента малого бизнеса в Alfa Bank. Трекер стартапов в Astana Hub, Almaty Hub, Terricon Valley, NURIS и IT Park, "
              "преподаёт digital-маркетинг в AlmaU и руководит направлением «Диджитал» в Qamalladin University."),
  "org_desc": "Revanite — студия стратегического роста Руслана Хасанова: диагностика бизнеса, трекинг и консалтинг (Revanite Tracking), продажи, маркетинг и автоматизация под ключ (Revanite Studio) для компаний Казахстана, Кыргызстана и СНГ.",
 },
 "en": {
  "name": "Ruslan Khasanov",
  "role": "Business growth consultant · startup tracker · lecturer",
  "about": [
   "I am a business growth consultant based in Almaty and the founder of Revanite, a strategic growth studio. My background is in the corporate sector: CMO at the fiscal technology platform re:Kassa, Head of Digital Marketing at Home Credit Bank, Director of Product at Halyk Insurance, head of SME marketing at Alfa Bank, and part of the team that launched Samsung Kazakhstan's online store.",
   "Today I work independently. As a tracker, I support startups at Astana Hub, Almaty Hub, Terricon Valley, NURIS and IT Park. Through Revanite I run projects for companies in Kazakhstan and Kyrgyzstan — from strategy and sales to marketing, CRM and process automation. I teach digital marketing and web analytics at AlmaU and lead the Digital program at Qamalladin University.",
   "My approach: first identify where the business is losing growth and money, then invest. I treat strategy, sales, marketing and operations as one system, measured by revenue and payback.",
  ],
  "nav": {"": "Home", "about": "About", "services": "Services", "cases": "Case studies", "teaching": "Teaching", "contact": "Contact"},
  "home": "Home",
  "switch": ("RU", "Русская версия"),
  "contact": "Get in touch",
  "footer": "Ruslan Khasanov · Revanite — Strategic Growth Studio · Almaty, Kazakhstan",
  "jobTitle": "Business growth consultant",
  "summary": ("Ruslan Khasanov is a business growth consultant based in Almaty, Kazakhstan, and the founder of Revanite, a strategic growth studio. "
              "He identifies the constraints on growth across a company's strategy, sales, marketing, operations and unit economics and builds a growth system: "
              "from the sales funnel and advertising to CRM, end-to-end analytics and automation. He was CMO at the fiscal technology platform re:Kassa, "
              "Head of Digital Marketing at Home Credit Bank, Director of Product at Halyk Insurance and head of SME marketing at Alfa Bank. "
              "He tracks startups at Astana Hub, Almaty Hub, Terricon Valley, NURIS and IT Park, teaches digital marketing at AlmaU "
              "and leads the Digital program at Qamalladin University."),
  "org_desc": "Revanite is Ruslan Khasanov's strategic growth studio: business check-ups, tracking and advisory (Revanite Tracking), and done-for-you sales, marketing and automation (Revanite Studio) for companies in Kazakhstan, Kyrgyzstan and the CIS.",
 },
}

KNOWS = {
 "ru": ["Стратегия роста", "Трекинг стартапов", "Go-to-market", "Воронка продаж", "Аудит отдела продаж", "Юнит-экономика",
        "CRM: amoCRM, Bitrix24", "Автоматизация процессов", "Оцифровка бизнеса", "Сквозная аналитика", "Веб-аналитика", "GA4",
        "Google Tag Manager", "Мобильная атрибуция", "AppsFlyer", "Performance-маркетинг", "Google Ads", "Meta Ads",
        "AI в маркетинге", "GEO"],
 "en": ["Growth strategy", "Startup tracking", "Go-to-market", "Sales funnel", "Sales team audit", "Unit economics",
        "CRM: amoCRM, Bitrix24", "Process automation", "Business digitization", "End-to-end analytics", "Web analytics", "GA4",
        "Google Tag Manager", "Mobile attribution", "AppsFlyer", "Performance marketing", "Google Ads", "Meta Ads",
        "AI in marketing", "Generative Engine Optimization"],
}

FAQ = {
 "ru": [
  ("Кто такой Руслан Хасанов?", T["ru"]["summary"]),
  ("Что такое Revanite?", "Revanite — студия стратегического роста, основанная Русланом Хасановым. Студия помогает компаниям выявить ограничения роста в стратегии, продажах, маркетинге, процессах и экономике и выстроить систему, которая приносит измеримый результат. Форматы работы: экспресс-диагностика бизнеса ($99 вместо $200), Revanite Tracking — трекинг и консалтинг для стартапов и собственников, Revanite Studio — продажи, маркетинг и автоматизация под ключ. Принцип студии — маркетинг как вложение, а не расход."),
  ("С кем работает Руслан Хасанов?", "С малым и средним бизнесом в Казахстане, Кыргызстане и СНГ, стартапами на ранних стадиях и командами акселераторов. Отраслевой опыт: банки и финтех, страхование, девелопмент, техника, доставка и e-commerce, ивенты, образование. Среди клиентов — Бакай Банк, Глоббинг Казахстан, Yeko Kazakhstan, SAGI, Shanyraq Business Forum, BI GROUP, Geometry, Jintropine, Youtrade, InnMedia."),
  ("Чем трекер отличается от маркетолога-исполнителя?", "Трекер не выполняет работу за команду: он помогает найти ключевое ограничение роста, сформулировать гипотезы, быстро и экономно их проверить и удерживать фокус на метриках. Исполнитель реализует выбранное решение. Руслан работает в обеих ролях: трекинг — в Revanite Tracking и IT-хабах, внедрение — в Revanite Studio, включая продажи, CRM и автоматизацию."),
  ("Где преподаёт Руслан Хасанов?", "В Almaty Management University (AlmaU) — курсы по веб-аналитике, цифровому маркетингу, SMM и инструментам интернет-маркетинга; в Qamalladin University — руководит направлением «Диджитал»; в колледже ICB. Проводит воркшопы в Astana Hub, выступал с гостевой лекцией в Nazarbayev University."),
  ("Как связаться с Русланом Хасановым?", "WhatsApp и телефон: +7 701 458 42 42, Telegram: @messer66. Также Instagram (@hasanov5) и LinkedIn."),
 ],
 "en": [
  ("Who is Ruslan Khasanov?", T["en"]["summary"]),
  ("What is Revanite?", "Revanite is a strategic growth studio founded by Ruslan Khasanov. It helps companies identify the constraints on growth across strategy, sales, marketing, operations and unit economics and build a system that delivers measurable results. Engagement formats: a business check-up ($99 instead of $200), Revanite Tracking — tracking and advisory for startups and business owners, and Revanite Studio — done-for-you sales, marketing and automation. The studio's principle: marketing is an investment, not an expense."),
  ("Who does Ruslan Khasanov work with?", "Small and mid-sized businesses in Kazakhstan, Kyrgyzstan and the CIS, early-stage startups and accelerator teams. Industry experience includes banking and fintech, insurance, real estate, consumer electronics, delivery and e-commerce, events and education. Clients include Bakai Bank, Globbing Kazakhstan, Yeko Kazakhstan, SAGI, Shanyraq Business Forum, BI GROUP, Geometry, Jintropine, Youtrade and InnMedia."),
  ("How is a startup tracker different from a marketing contractor?", "A tracker does not do the work for the team: a tracker helps find the key constraint on growth, frame hypotheses, test them quickly and economically, and keep the team focused on metrics. A contractor implements the chosen solution. Ruslan works in both roles: tracking through Revanite Tracking and tech hubs, implementation through Revanite Studio, including sales, CRM and automation."),
  ("Where does Ruslan Khasanov teach?", "At Almaty Management University (AlmaU) — web analytics, digital marketing, SMM and online marketing tools; at Qamalladin University, where he leads the Digital program; and at ICB college. He runs workshops at Astana Hub and has given a guest lecture at Nazarbayev University."),
  ("How can I contact Ruslan Khasanov?", "WhatsApp and phone: +7 701 458 42 42, Telegram: @messer66. Also Instagram (@hasanov5) and LinkedIn."),
 ],
}

EXPERIENCE = {
 "ru": [
  ("Revanite", "Основатель студии стратегического роста"),
  ("IT-хабы Казахстана", "Трекер стартапов; линейный трекер акселератора AIpreneurs"),
  ("AlmaU, Qamalladin University, колледж ICB", "Преподаватель; руководитель направления «Диджитал» в Qamalladin University"),
  ("re:Kassa", "CMO (до 2026)"),
  ("Halyk Insurance", "Директор по продукту"),
  ("Home Credit Bank", "Руководитель digital-маркетинга"),
  ("Alfa Bank", "Руководитель маркетинга сегмента малого бизнеса"),
  ("BI GROUP", "Менеджер маркетинговых проектов; впоследствии — клиент Revanite"),
  ("Samsung Kazakhstan", "Запуск онлайн-магазина"),
 ],
 "en": [
  ("Revanite", "Founder of a strategic growth studio"),
  ("Kazakhstan tech hubs", "Startup tracker; line tracker at the AIpreneurs accelerator"),
  ("AlmaU, Qamalladin University, ICB College", "Lecturer; head of the Digital program at Qamalladin University"),
  ("re:Kassa", "CMO (until 2026)"),
  ("Halyk Insurance", "Director of Product"),
  ("Home Credit Bank", "Head of Digital Marketing"),
  ("Alfa Bank", "Head of SME Segment Marketing"),
  ("BI GROUP", "Marketing Project Manager; later a Revanite client"),
  ("Samsung Kazakhstan", "Online store launch"),
 ],
}

FORMULA = {
 "ru": [("Инсайт", "понимание клиента, рынка и реальных мотивов покупки"),
        ("Экономика", "юнит-экономика: CAC, LTV, маржинальность, окупаемость"),
        ("Стратегия", "выбор сегментов, каналов и ценностного предложения"),
        ("Гипотезы", "приоритизированный план проверок"),
        ("Исполнение", "быстрый запуск с минимальными затратами"),
        ("Аналитика", "сквозная — от первого касания до оплаты в CRM"),
        ("Масштаб", "инвестиции в окупаемые решения, отказ от неэффективных")],
 "en": [("Insight", "understanding the customer, the market and the real reasons to buy"),
        ("Economics", "unit economics: CAC, LTV, margin, payback"),
        ("Strategy", "choice of segments, channels and value proposition"),
        ("Hypotheses", "a prioritized testing plan"),
        ("Execution", "fast launch at minimal cost"),
        ("Analytics", "end-to-end, from first touch to payment in the CRM"),
        ("Scale", "invest in what pays back, drop what does not")],
}

# Экспресс-диагностика: (надзаголовок на главной, заголовок на главной, текст, заголовок на странице услуг, пункты, кнопка)
DIAG = {
 "ru": ("Первый шаг", f"Экспресс-диагностика бизнеса — {PRICE_HTML}",
        "Анализирую ключевые данные компании — продажи, воронку, маркетинг, процессы и экономику. На 60-минутной сессии показываю главное ограничение роста, зоны потерь и приоритетные шаги. По итогам вы получаете краткий план действий. При продолжении работы стоимость диагностики засчитывается.",
        f"Первый шаг: экспресс-диагностика бизнеса — {PRICE_HTML}",
        ["Доступ к данным в режиме просмотра: продажи, CRM, рекламные кабинеты, отчётность",
         "Сессия 60 минут: ключевое ограничение роста, зоны потерь, приоритеты",
         "Краткий план действий по итогам сессии",
         f"При продолжении работы {PRICE} засчитываются в стоимость проекта"],
        "Записаться на диагностику"),
 "en": ("First step", f"Business check-up — {PRICE_HTML}",
        "I analyze your key business data — sales, funnel, marketing, operations and unit economics. In a 60-minute session I show the main constraint on growth, where you are losing money and which steps come first. You receive a concise action plan afterwards. If we continue working together, the fee is credited.",
        f"First step: business check-up — {PRICE_HTML}",
        ["View-only access to your data: sales, CRM, ad accounts, reporting",
         "60-minute session: the key constraint on growth, areas of loss, priorities",
         "A concise action plan after the session",
         f"If we continue, the {PRICE} is credited toward the project"],
        "Book a check-up"),
}

SERVICES = {
 "ru": [
  ("studio", "Revanite Studio", "Продажи, маркетинг и автоматизация под ключ",
   "Для малого и среднего бизнеса, которому нужен измеримый рост продаж, а не охваты.",
   ["Стратегия роста и медиаплан с расчётом окупаемости",
    "Аудит воронки и отдела продаж: этапы сделки, конверсии, коммуникации с клиентами",
    "Оцифровка и автоматизация: CRM (amoCRM, Bitrix24), интеграции, чат-боты",
    "Performance-маркетинг: Google Ads, Meta Ads, TikTok Ads",
    "Сквозная аналитика: GA4, Google Tag Manager, Яндекс Метрика, Meta Pixel и Conversions API, AppsFlyer — от рекламы до продажи в CRM",
    "Дашборды в Looker Studio и отчётность план-факт"],
   "проектная работа или ежемесячное сопровождение с еженедельной отчётностью."),
  ("tracking", "Revanite Tracking", "Трекинг и стратегия",
   "Для стартапов и собственников бизнеса, чей рост вышел на плато.",
   ["Диагностика ключевых ограничений роста",
    "Проверка продуктовых, коммерческих и маркетинговых гипотез",
    "Go-to-market, построение воронки продаж, привлечение первых клиентов",
    "Операционные процессы и работа с фаундером: фокус, приоритеты, делегирование"],
   "трекшн-сессии раз в одну-две недели, трекшн-карта, контроль метрик между сессиями."),
  ("mentoring", "Обучение и менторство", "Для маркетологов и команд", "",
   ["Индивидуальная программа: digital-маркетинг, аналитика, AI-инструменты",
    "Корпоративные воркшопы: go-to-market, лидогенерация, воронки продаж",
    "Выступления и гостевые лекции"],
   "онлайн или очно в Алматы."),
 ],
 "en": [
  ("studio", "Revanite Studio", "Done-for-you sales, marketing and automation",
   "For small and mid-sized businesses that need measurable sales growth, not reach.",
   ["Growth strategy and media plan with payback modeling",
    "Sales funnel and sales team audit: deal stages, conversion rates, customer communication",
    "Digitization and automation: CRM (amoCRM, Bitrix24), integrations, chatbots",
    "Performance marketing: Google Ads, Meta Ads, TikTok Ads",
    "End-to-end analytics: GA4, Google Tag Manager, Yandex Metrica, Meta Pixel and Conversions API, AppsFlyer — from ad to sale in the CRM",
    "Looker Studio dashboards and plan-vs-actual reporting"],
   "project-based or ongoing monthly engagement with weekly reporting."),
  ("tracking", "Revanite Tracking", "Tracking & strategy",
   "For startups and business owners whose growth has plateaued.",
   ["Diagnosis of the key constraints on growth",
    "Testing product, commercial and marketing hypotheses",
    "Go-to-market, sales funnel design, first customer acquisition",
    "Operations and founder work: focus, priorities, delegation"],
   "traction sessions every one to two weeks, a traction map, metric tracking between sessions."),
  ("mentoring", "Teaching & mentoring", "For marketers and teams", "",
   ["Individual program: digital marketing, analytics, AI tools",
    "Corporate workshops: go-to-market, lead generation, sales funnels",
    "Talks and guest lectures"],
   "online or in person in Almaty."),
 ],
}

PROCESS = {
 "ru": ("Порядок работы", [
   "Заявка в WhatsApp или Telegram: кратко о бизнесе и задаче",
   "Экспресс-диагностика: анализ данных и определение зон потерь",
   "Предложение: формат, объём работ и стоимость — Studio, Tracking или отдельный проект",
   "Работа с еженедельной отчётностью по финансовым показателям, а не по кликам"]),
 "en": ("How we work", [
   "Send a request on WhatsApp or Telegram with a short note about your business and the challenge",
   "Business check-up: data analysis and identification of areas of loss",
   "Proposal: format, scope and price — Studio, Tracking or a standalone project",
   "Delivery with weekly reporting on financial metrics, not clicks"]),
}
TEACH = {
 "ru": [
  ("Almaty Management University (AlmaU)", "Преподаватель с 2022 года",
   ["Веб-аналитика", "Цифровой маркетинг", "SMM и социальные сети", "Инструменты интернет-маркетинга",
    "Автор программ курсов «AI в маркетинге» и «SEO-оптимизация и веб-аналитика»"]),
  ("Qamalladin University", "Руководитель направления «Диджитал»",
   ["Управление маркетинговыми проектами", "Лидогенерация и оптимизация воронки продаж"]),
  ("Колледж ICB", "Преподаватель", []),
  ("Astana Hub", "Воркшопы",
   ["Go-to-market и первые шаги привлечения клиентов в AI, цифровых и традиционных продуктах",
    "Growth hacking", "Лидогенерация и воронки продаж"]),
  ("Nazarbayev University", "Гостевая лекция", ["Основы маркетинга и его роль в современном мире"]),
  ("Акселераторы и IT-хабы", "Трекер стартапов",
   ["Astana Hub, Almaty Hub, Terricon Valley, NURIS, IT Park", "AIpreneurs — линейный трекер"]),
 ],
 "en": [
  ("Almaty Management University (AlmaU)", "Lecturer since 2022",
   ["Web analytics", "Digital marketing", "SMM and social media", "Online marketing tools",
    "Author of the course programmes “AI in Marketing” and “SEO and Web Analytics”"]),
  ("Qamalladin University", "Head of the Digital programme",
   ["Marketing project management", "Lead generation and sales funnel optimisation"]),
  ("ICB college", "Instructor", []),
  ("Astana Hub", "Workshops",
   ["Go-to-market and first customer acquisition for AI, digital and traditional products",
    "Growth hacking", "Lead generation and sales funnels"]),
  ("Nazarbayev University", "Guest lecture", ["Fundamentals of marketing and its role in the modern world"]),
  ("Accelerators and tech hubs", "Startup tracker",
   ["Astana Hub, Almaty Hub, Terricon Valley, NURIS, IT Park", "AIpreneurs — line tracker"]),
 ],
}

AI_COURSE = {
 "ru": ("Курс «AI в маркетинге»", ["AI в маркетинге без мифов: типы моделей, LLM, промптинг, инструменты",
        "AI, SEO и GEO: оптимизация под поисковики и генеративные ответы",
        "AI в маркетинговой аналитике и прогнозировании",
        "Сквозная аналитика: реклама → сайт → CRM → продажи, расчёт ROAS и CAC",
        "Vibe coding: от исследования конкурентов до живого сайта",
        "Маркетинговая воронка: построение и стресс-тест с помощью AI"]),
 "en": ("“AI in Marketing” course", ["AI in marketing demystified: model types, LLMs, prompting, tools",
        "AI, SEO and GEO: optimising for search engines and generative answers",
        "AI in marketing analytics and forecasting",
        "End-to-end analytics: ads → website → CRM → sales, ROAS and CAC",
        "Vibe coding: from competitor research to a live website",
        "Marketing funnel: building and stress-testing it with AI"]),
}

META = {
 "ru": {
  "": ("Руслан Хасанов — консультант по росту бизнеса | Алматы",
       "Руслан Хасанов — консультант по росту бизнеса в Алматы: стратегия, продажи, маркетинг, CRM и автоматизация. Экс-CMO re:Kassa, трекер стартапов."),
  "about": ("Обо мне — Руслан Хасанов",
            "Биография Руслана Хасанова: CMO re:Kassa, Home Credit Bank, Halyk Insurance, Alfa Bank, Samsung Kazakhstan; трекинг стартапов, преподавание в AlmaU."),
  "services": ("Услуги: диагностика бизнеса, продажи и маркетинг, трекинг — Руслан Хасанов",
               "Экспресс-диагностика бизнеса за $99, Revanite Studio, Revanite Tracking и обучение: продажи, маркетинг, CRM, автоматизация и трекинг стартапов."),
  "cases": ("Кейсы — Руслан Хасанов, Revanite",
            "Кейсы Руслана Хасанова: ROMI 316% для SAGI, лид в 2,4 раза дешевле для Yeko, −45% к стоимости регистрации в Глоббинг, ROAS 234% для Shanyraq."),
  "teaching": ("Преподавание и выступления — Руслан Хасанов",
               "Руслан Хасанов преподаёт digital-маркетинг в AlmaU, руководит направлением «Диджитал» в Qamalladin University, проводит воркшопы в Astana Hub."),
  "contact": ("Контакты — Руслан Хасанов, Revanite",
              "Как связаться с Русланом Хасановым: Telegram @messer66, WhatsApp и телефон +7 701 458 42 42, Instagram, LinkedIn. Алматы, Казахстан."),
 },
 "en": {
  "": ("Ruslan Khasanov — business growth consultant | Almaty",
       "Ruslan Khasanov, business growth consultant in Almaty: strategy, sales, marketing, CRM and automation. Former CMO at re:Kassa, startup tracker."),
  "about": ("About — Ruslan Khasanov",
            "Biography of Ruslan Khasanov: CMO at re:Kassa, Home Credit Bank, Halyk Insurance, Alfa Bank, Samsung Kazakhstan; startup tracking, lecturing at AlmaU, Revanite."),
  "services": ("Services: business check-up, sales and marketing, tracking — Ruslan Khasanov",
               "A $99 business check-up, Revanite Studio, Revanite Tracking and training: sales, marketing, CRM, automation and startup tracking."),
  "cases": ("Case studies — Ruslan Khasanov, Revanite",
            "Ruslan Khasanov's case studies: 316% ROMI for SAGI, 2.4× cheaper leads for Yeko, 45% lower cost per sign-up at Globbing, 234% ROAS for Shanyraq."),
  "teaching": ("Teaching and talks — Ruslan Khasanov",
               "Ruslan Khasanov lectures in digital marketing at AlmaU, leads the Digital programme at Qamalladin University and runs workshops at Astana Hub."),
  "contact": ("Contact — Ruslan Khasanov, Revanite",
              "How to reach Ruslan Khasanov: Telegram @messer66, WhatsApp and phone +7 701 458 42 42, Instagram, LinkedIn. Almaty, Kazakhstan."),
 },
}

H1 = {
 "ru": {"about": "Руслан Хасанов — обо мне", "services": "Услуги", "cases": "Кейсы", "teaching": "Преподавание и выступления", "contact": "Контакты"},
 "en": {"about": "Ruslan Khasanov — about me", "services": "Services", "cases": "Case studies", "teaching": "Teaching and talks", "contact": "Contact"},
}

# ---------------------------------------------------------------- SCHEMA
def person(lang):
    t = T[lang]
    p = {
        "@type": "Person", "@id": BASE + "/#person",
        "name": t["name"],
        "alternateName": ["Руслан Хасанов", "Ruslan Khasanov", "Ruslan Khassanov", "Хасанов Руслан Фархадович", "Ruslan Farkhadovich Khasanov"],
        "givenName": "Руслан" if lang == "ru" else "Ruslan",
        "familyName": "Хасанов" if lang == "ru" else "Khasanov",
        "jobTitle": t["jobTitle"],
        "description": t["summary"],
        "url": url(lang, ""),
        "address": {"@type": "PostalAddress", "addressLocality": "Almaty", "addressCountry": "KZ"},
        "worksFor": [{"@id": BASE + "/#org"}],
        "affiliation": [
            {"@type": "CollegeOrUniversity", "name": "Almaty Management University (AlmaU)", "url": "https://almau.edu.kz"},
            {"@type": "CollegeOrUniversity", "name": "Qamalladin University"},
        ],
        "knowsAbout": KNOWS[lang],
        "knowsLanguage": ["ru", "en"],
        "sameAs": SAME_AS,
        "telephone": PHONE,
    }
    if PHOTO:
        p["image"] = PHOTO_URL
    return p

def org(lang):
    return {
        "@type": "ProfessionalService", "@id": BASE + "/#org",
        "name": "Revanite",
        "alternateName": ["Revanite Strategic Growth Studio", "Revanite Studio", "Revanite Tracking"],
        "slogan": "Маркетинг как вложение, а не расход." if lang == "ru" else "Marketing as an investment, not an expense.",
        "description": T[lang]["org_desc"],
        "url": BASE + "/",
        "logo": BASE + "/assets/logo.svg",
        "founder": {"@id": BASE + "/#person"},
        "address": {"@type": "PostalAddress", "addressLocality": "Almaty", "addressCountry": "KZ"},
        "areaServed": ["KZ", "KG", "UZ", "CIS"],
        "telephone": PHONE,
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE, "contactType": "sales",
                         "availableLanguage": ["ru", "en"], "url": WA},
    }

def website(lang):
    return {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/",
            "name": T[lang]["name"], "inLanguage": ["ru", "en"], "publisher": {"@id": BASE + "/#person"}}

def breadcrumbs(lang, slug, title):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": T[lang]["home"], "item": url(lang, "")},
        {"@type": "ListItem", "position": 2, "name": title, "item": url(lang, slug)}]}

def schema(lang, slug):
    title, desc = META[lang][slug]
    page_type = {"": "WebPage", "about": "ProfilePage", "services": "WebPage", "cases": "CollectionPage", "teaching": "WebPage", "contact": "ContactPage"}[slug]
    page = {"@type": page_type, "@id": url(lang, slug) + "#webpage", "url": url(lang, slug), "name": title,
            "description": desc, "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"},
            "about": {"@id": BASE + "/#person"}, "dateModified": TODAY}
    if slug == "about":
        page["mainEntity"] = {"@id": BASE + "/#person"}
    graph = [person(lang), org(lang), website(lang), page]
    if slug:
        graph.append(breadcrumbs(lang, slug, H1[lang][slug]))
    if slug == "":
        graph.append({"@type": "FAQPage", "@id": url(lang, "") + "#faq", "inLanguage": lang,
                      "mainEntity": [{"@type": "Question", "name": q,
                                      "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang]]})
    if slug == "services":
        for key, name, sub, who, items, fmt in SERVICES[lang]:
            graph.append({"@type": "Service", "@id": url(lang, "services") + "#" + key, "name": f"{name} — {sub}",
                          "description": who + " " + "; ".join(items) + ".", "provider": {"@id": BASE + "/#org"},
                          "areaServed": ["KZ", "CIS"]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- HTML
LOGO = ('<svg class="logo" viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M10 26V6h7.5a5 5 0 0 1 0 10H10"/><path d="M15.5 16 22 26"/>'
        '<path d="M4 29 28 3" stroke="#5B82C9" stroke-width="1.2"/></svg>')

CSS = """
:root{--bg:#0A0C10;--surface:#11141B;--surface2:#171B25;--line:#232937;--text:#F1F3F7;--muted:#9AA3B2;--accent:#7EA6FF;--accent2:#B48CFF;--grad:linear-gradient(135deg,var(--accent),var(--accent2));--max:1120px}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{background:var(--bg) radial-gradient(1100px 600px at 85% -10%,rgba(126,166,255,.13),transparent 60%) no-repeat;color:var(--text);font:400 17px/1.65 Manrope,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:inherit}
.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(10,12,16,.78);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);z-index:5}
.bar{display:flex;align-items:center;gap:20px;height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;letter-spacing:.01em;white-space:nowrap}
.logo{width:28px;height:28px}
nav{display:flex;gap:22px;margin-left:auto;min-width:0;align-items:center;overflow-x:auto;scrollbar-width:none}
nav::-webkit-scrollbar{display:none}
nav a{text-decoration:none;color:var(--muted);font-size:15px;white-space:nowrap;transition:color .2s}
nav a:hover,nav a[aria-current]{color:var(--text)}
.lang{flex:none;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:3px 9px;font-size:13px;color:var(--text)}
main section{padding:84px 0}
.eyebrow{color:var(--accent);font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:18px}
h1{font-size:clamp(34px,5vw,52px);line-height:1.08;font-weight:700;letter-spacing:-.025em}
h2{font-size:clamp(28px,4vw,40px);line-height:1.15;font-weight:700;letter-spacing:-.02em;margin-bottom:28px}
h3{font-size:19px;line-height:1.35;font-weight:600;margin-bottom:8px}
p+p{margin-top:14px}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:clamp(19px,2.3vw,23px);color:var(--muted);max-width:700px;margin-top:22px}
.hero{padding:104px 0 56px}
.hero h1{font-size:clamp(46px,8.4vw,92px);line-height:1;letter-spacing:-.035em;background:linear-gradient(180deg,#fff 30%,#AEB9CF);-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:.06em}
.hero-grid{display:grid;grid-template-columns:1fr auto;gap:48px;align-items:center}
.portrait{width:240px;height:290px;border-radius:20px;border:1px solid transparent;background:linear-gradient(var(--surface2),var(--surface)) padding-box,var(--grad) border-box;object-fit:cover;display:flex;align-items:center;justify-content:center;font-size:60px;font-weight:700;letter-spacing:.04em;color:var(--accent);box-shadow:0 30px 80px -30px rgba(126,166,255,.45)}
.role{font-size:clamp(16px,2vw,19px);font-weight:600;margin-top:18px}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:36px}
.btn{display:inline-block;padding:14px 24px;border-radius:12px;background:var(--grad);color:#0A0C10;text-decoration:none;font-weight:700;font-size:15px;box-shadow:0 10px 30px -10px rgba(126,166,255,.6);transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 16px 40px -12px rgba(126,166,255,.75)}
.btn.ghost{background:rgba(255,255,255,.03);border:1px solid var(--line);color:var(--text);box-shadow:none}
.btn.ghost:hover{border-color:var(--accent)}
.stats{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.stats li{background:var(--surface);padding:26px 24px}
.stats b{display:block;font-size:clamp(34px,4.6vw,50px);line-height:1;font-weight:700;letter-spacing:-.03em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:10px}
.stats span{color:var(--muted);font-size:14px;line-height:1.5;display:block}
.answer{font-size:clamp(18px,2vw,21px);max-width:860px;line-height:1.7}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.card,.project,.case{background:linear-gradient(180deg,var(--surface2),var(--surface));border:1px solid var(--line);border-radius:18px;transition:border-color .25s,transform .25s}
.card{padding:28px}
.card:hover,.project:hover{border-color:rgba(126,166,255,.45);transform:translateY(-3px)}
.card .tag,.project .tag,.case .tag{color:var(--accent);font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;margin-bottom:12px;display:block}
.card h3{font-size:21px}
.card p{color:var(--muted);font-size:15px}
.card ul{margin-top:14px;padding-left:18px;color:var(--muted);font-size:15px}
.card li+li{margin-top:6px}
.exp{list-style:none}
.exp li{display:grid;grid-template-columns:240px 1fr;gap:24px;padding:18px 0;border-top:1px solid var(--line)}
.exp li:first-child{border-top:0}
.exp b{font-weight:700}
.exp span{color:var(--muted)}
.case{padding:32px;margin-bottom:18px}
.case h2{font-size:clamp(22px,2.6vw,26px);margin-bottom:8px}
.case h3{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin:22px 0 8px}
.case ul{padding-left:18px}
.case li+li{margin-top:6px}
.result{border-left:2px solid var(--accent);padding-left:16px}
.price{white-space:nowrap}
s{opacity:.55;font-weight:500;margin-right:.1em}
.note{color:var(--muted);font-size:15px;margin-top:18px}
footer{border-top:1px solid var(--line);padding:84px 0 36px;background:radial-gradient(900px 400px at 10% 0,rgba(180,140,255,.10),transparent 60%),var(--surface)}
.footer-title{font-size:clamp(30px,5vw,54px);line-height:1.08;margin-bottom:14px;max-width:820px}
.footer-sub{color:var(--muted);margin-bottom:32px}
.copy{color:var(--muted);font-size:14px;margin-top:40px}
.socials{list-style:none;display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px}
.socials a{display:block;text-decoration:none;border:1px solid var(--line);border-radius:14px;padding:16px 18px;background:rgba(10,12,16,.6);transition:border-color .2s}
.socials a:hover{border-color:var(--accent)}
.socials b{display:block;font-weight:700}
.socials span{color:var(--muted);font-size:14px;overflow-wrap:anywhere}
.section-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:28px}
.section-head h2{margin-bottom:0}
.more{color:var(--accent);text-decoration:none;font-size:15px;font-weight:600;white-space:nowrap}
.projects{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.project{padding:28px;display:flex;flex-direction:column;gap:10px}
.project .tag{margin-bottom:2px}
.project h3{margin:0;font-size:20px}
.project p{color:var(--muted);font-size:15px;flex:1}
.project a{color:var(--accent);text-decoration:none;font-size:15px;font-weight:600}
.projects.two{grid-template-columns:repeat(2,1fr)}
.metric{display:block;font-size:clamp(40px,5.4vw,60px);line-height:1;font-weight:700;letter-spacing:-.035em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.metric-label{display:block;color:var(--muted);font-size:14px;margin-bottom:10px}
.project ul{padding-left:18px;color:var(--muted);font-size:15px;flex:1}
.project li+li{margin-top:6px}
.metric-row{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 14px;margin-bottom:14px}
.metric-row .metric-label{margin:0}
main section > h2 + .case{margin-top:4px}
.trust{padding-top:24px !important}
.trust h2{font-size:12px;color:var(--muted);font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin-bottom:22px}
.trust ul{list-style:none;display:flex;flex-wrap:wrap;gap:14px 36px}
.trust ul+h2{margin-top:36px}
.trust li{font-size:clamp(18px,2.4vw,24px);font-weight:700;letter-spacing:-.01em;color:#C9D0DC}
.card-links{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:18px;font-size:15px}
.card-links a{color:var(--accent);text-decoration:none;font-weight:600}
.knowledge{display:grid;grid-template-columns:1fr 1fr;gap:56px}
.knowledge h2{font-size:clamp(24px,3vw,30px)}
.chips{list-style:none;display:flex;flex-wrap:wrap;gap:8px}
.chips li{border:1px solid var(--line);background:var(--surface);border-radius:999px;padding:6px 14px;font-size:14px}
.steps{list-style:none;counter-reset:s}
.steps li{counter-increment:s;display:grid;grid-template-columns:38px 1fr;gap:10px;padding:10px 0;border-top:1px solid var(--line);color:var(--muted);font-size:15px}
.steps li:first-child{border-top:0}
.steps li::before{content:"0" counter(s);color:var(--accent);font-weight:700;font-size:14px;padding-top:1px}
.steps b{color:var(--text);font-weight:700}
.rows{list-style:none}
.rows li{display:grid;grid-template-columns:240px 1fr;gap:24px;padding:20px 0;border-top:1px solid var(--line)}
.rows li:first-child{border-top:0}
.rows .when{color:var(--accent);font-size:14px;font-weight:600;padding-top:3px}
.rows h3{margin-bottom:4px}.rows p{color:var(--muted);font-size:15px}
details summary{cursor:pointer;list-style:none}
details summary::-webkit-details-marker{display:none}
.more-box summary{color:var(--accent);font-size:15px;font-weight:600;margin-top:14px}
.more-box[open] summary{margin-bottom:4px}
.qa{border-top:1px solid var(--line);padding:20px 0}
.qa:last-child{border-bottom:1px solid var(--line)}
.qa summary{font-weight:600;font-size:18px;display:flex;justify-content:space-between;gap:16px}
.qa summary::after{content:"+";color:var(--accent);font-size:22px;line-height:1}
.qa[open] summary::after{content:"−"}
.qa p{color:var(--muted);margin-top:12px;max-width:820px}
.page{padding-bottom:24px !important}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:18px}
.crumbs a{text-decoration:none}
@media (max-width:760px){
 body{font-size:16px}
 .bar{gap:8px}.brand span{display:none}
 nav{gap:10px}nav a{font-size:13px}nav .nav-home{display:none}
 .hero{padding:52px 0 40px}
 .hero-grid{grid-template-columns:1fr;gap:28px}
 .portrait{width:112px;height:132px;font-size:30px;border-radius:16px;order:-1}
 main section{padding:56px 0}
 .stats{grid-template-columns:1fr 1fr}
 .stats li{padding:20px 18px}
 .exp li,.rows li{grid-template-columns:1fr;gap:2px}
 .knowledge{grid-template-columns:1fr;gap:44px}
 .projects.two{grid-template-columns:1fr}
 .card,.project,.case{padding:22px}
}
"""

def portrait(lang):
    alt = T[lang]["name"]
    if PHOTO:
        return f'<img class="portrait" src="/assets/ruslan-khasanov.jpg" alt="{alt}" width="220" height="260">'
    return f'<div class="portrait" role="img" aria-label="{alt}">{"РХ" if lang=="ru" else "RK"}</div>'

def head(title, link=None, label=None):
    more = f'<a class="more" href="{link}">{label} →</a>' if link else ""
    return f'<div class="section-head"><h2>{title}</h2>{more}</div>'

def social_list(lang):
    out = []
    for name, handle, href in socials(lang):
        ext = "" if href.startswith("tel:") else ' rel="me noopener" target="_blank"'
        out.append(f'<li><a href="{href}"{ext}><b>{name}</b><span>{handle}</span></a></li>')
    return '<ul class="socials">' + "".join(out) + "</ul>"

def body_home(lang):
    t = T[lang]
    ru = lang == "ru"
    eyebrow = "Руслан Хасанов · Revanite · Алматы" if ru else "Ruslan Khasanov · Revanite · Almaty"
    h1 = "Системный рост бизнеса" if ru else "Business growth as a system"
    lead = ("Анализирую бизнес целиком — стратегию, продажи, маркетинг, процессы и экономику — и выстраиваю систему роста: "
            "от воронки продаж и рекламы до CRM, сквозной аналитики и автоматизации. Опыт руководителя в банках, страховании и финтехе; "
            "трекер стартапов в IT-хабах Казахстана."
            if ru else
            "I analyze the whole business — strategy, sales, marketing, operations and unit economics — and build a growth system: "
            "from the sales funnel and advertising to CRM, end-to-end analytics and automation. Former executive in banking, insurance "
            "and fintech; startup tracker at Kazakhstan's tech hubs.")
    btn_diag = f"Диагностика бизнеса — {PRICE_HTML}" if ru else f"Business check-up — {PRICE_HTML}"
    btn_tg = "Написать в Telegram" if ru else "Message on Telegram"
    cta = "Обсудить проект" if ru else "Discuss a project"
    stats = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in STATS[lang])
    open_case = "Открыть кейс" if ru else "Open case"
    cases = "".join(
        f'<article class="project"><span class="tag">{channels}</span><h3>{title}</h3><p>{result}</p>'
        f'<a href="{path(lang,"cases")}#case-{n}">{open_case} →</a></article>'
        for n, (title, channels, task, done, result) in enumerate(CASES[lang], 1))
    track = "".join(
        f'<article class="project"><b class="metric">{m}</b><span class="metric-label">{ml}</span>'
        f'<span class="tag">{tag}</span><h3>{title}</h3><ul>{"".join(f"<li>{x}</li>" for x in points)}</ul></article>'
        for m, ml, title, tag, points in TRACK[lang])
    groups = "".join(f'<h2>{g}</h2><ul>{"".join(f"<li>{c}</li>" for c in items)}</ul>' for g, items in GROUPS[lang])
    d_eyebrow, d_title, d_text, _, _, d_btn = DIAG[lang]
    services = "".join(
        f'<article class="card"><span class="tag">{name}</span><h3>{sub}</h3>' + (f"<p>{who}</p>" if who else "") +
        f'<p class="card-links"><a href="{WA}" rel="noopener" target="_blank">{cta}</a>'
        f'<a href="{path(lang,"services")}#{key}">{"Подробнее" if ru else "Details"} →</a></p></article>'
        for key, name, sub, who, items, fmt in SERVICES[lang])
    about = "".join(f'<p class="answer">{p}</p>' for p in t["about"])
    chips = "".join(f"<li>{k}</li>" for k in KNOWS[lang])
    formula = "".join(f"<li><span><b>{a}</b> — {b}</span></li>" for a, b in FORMULA[lang])
    teach = "".join(
        f'<li><span class="when">{role}</span><div><h3>{place}</h3>'
        + (f'<p>{" · ".join(items)}</p>' if items else "") + "</div></li>"
        for place, role, items in TEACH[lang])
    rows = [f"<li><b>{a}</b><span>{b}</span></li>" for a, b in EXPERIENCE[lang]]
    exp = ('<ul class="exp">' + "".join(rows[:4]) + "</ul>"
           f'<details class="more-box"><summary>{"Показать ещё опыт" if ru else "Show more experience"}</summary>'
           '<ul class="exp">' + "".join(rows[4:]) + "</ul></details>")
    faq = "".join(f'<details class="qa"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ[lang])
    return f"""
<section class="hero"><div class="hero-grid"><div>
<p class="eyebrow">{eyebrow}</p>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
<div class="cta"><a class="btn" href="{WA}" rel="noopener" target="_blank">{btn_diag}</a><a class="btn ghost" href="{TG}" rel="me noopener" target="_blank">{btn_tg}</a></div>
</div>{portrait(lang)}</div></section>
<section style="padding:0 0 8px"><ul class="stats">{stats}</ul><p class="note">{STATS_NOTE[lang]}</p></section>
<section>{head("Ключевые проекты" if ru else "Key projects", path(lang,"cases"), "Все кейсы" if ru else "All case studies")}<div class="projects two">{cases}</div></section>
<section>{head("Трекинг стартапов" if ru else "Startup tracking", path(lang,"cases") + "#tracking", "Подробнее" if ru else "Details")}<div class="projects">{track}</div></section>
<section class="trust">{groups}</section>
<section id="diagnostics"><p class="eyebrow">{d_eyebrow}</p><h2>{d_title}</h2><p class="answer">{d_text}</p>
<div class="cta"><a class="btn" href="{WA}" rel="noopener" target="_blank">{d_btn}</a></div></section>
<section>{head("Форматы работы" if ru else "Engagement formats")}<div class="cards">{services}</div></section>
<section><h2>{"Обо мне" if ru else "About me"}</h2>{about}
<p class="card-links"><a href="{path(lang,"about")}">{"Подробная биография" if ru else "Full biography"} →</a><a href="{IG}" rel="me noopener" target="_blank">Instagram</a><a href="{LI}" rel="me noopener" target="_blank">LinkedIn</a></p></section>
<section><div class="knowledge">
<div><h2>{"Инструменты и компетенции" if ru else "Skills and tools"}</h2><ul class="chips">{chips}</ul></div>
<div><h2>{"Как я работаю: Revanite Growth Formula" if ru else "How I work: Revanite Growth Formula"}</h2><ol class="steps">{formula}</ol></div>
</div></section>
<section>{head("Где я преподаю" if ru else "Where I teach", path(lang,"teaching"), "Подробнее" if ru else "Details")}<ul class="rows">{teach}</ul></section>
<section>{head("Карьера" if ru else "Career", path(lang,"about"), "Обо мне" if ru else "About me")}{exp}</section>
<section id="faq">{head("Частые вопросы" if ru else "FAQ")}{faq}</section>"""

def body_contact(lang):
    ru = lang == "ru"
    lead = ("Напишите в Telegram или WhatsApp: коротко о бизнесе и задаче. Отвечу и предложу формат работы."
            if ru else "Message me on Telegram or WhatsApp with a short note about your business and the challenge. I will reply with a suggested format.")
    note = ("Алматы, Казахстан. Работаю с клиентами в Казахстане, СНГ и онлайн."
            if ru else "Almaty, Kazakhstan. Working with clients across Kazakhstan, the CIS and online.")
    return f"""
<section class="page">{crumbs(lang,"contact")}<h1>{H1[lang]["contact"]}</h1><p class="lead">{lead}</p></section>
<section>{social_list(lang)}<p class="note">{note}</p></section>"""

def crumbs(lang, slug):
    return f'<p class="crumbs"><a href="{path(lang,"")}">{T[lang]["home"]}</a> / {H1[lang][slug]}</p>'

def body_about(lang):
    ru = lang == "ru"
    t = T[lang]
    exp = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in EXPERIENCE[lang])
    bio = "".join(f"<p>{p}</p>" for p in t["about"])
    if ru:
        names = "Как пишется имя"
        names_p = "Руслан Хасанов (полное имя — Хасанов Руслан Фархадович). Латиницей — Ruslan Khasanov; в LinkedIn используется написание Ruslan Khassanov."
    else:
        names = "Name spelling"
        names_p = "Ruslan Khasanov (Russian: Руслан Хасанов; full name Хасанов Руслан Фархадович). LinkedIn uses the spelling Ruslan Khassanov."
    kn = ", ".join(KNOWS[lang])
    return f"""
<section class="page">{crumbs(lang,"about")}<h1>{H1[lang]["about"]}</h1><p class="lead">{t["role"]}</p></section>
<section>{bio}</section>
<section><h2>{"Опыт" if ru else "Experience"}</h2><ul class="exp">{exp}</ul></section>
<section><h2>{"Компетенции" if ru else "Expertise"}</h2><p>{kn}</p></section>
<section><h2>{names}</h2><p>{names_p}</p></section>"""

def body_services(lang):
    ru = lang == "ru"
    _, _, _, d_title, d_items, d_btn = DIAG[lang]
    p_title, p_steps = PROCESS[lang]
    lead = ("Работа начинается с экспресс-диагностики бизнеса. Далее — один из форматов: продажи, маркетинг и автоматизация под ключ, трекинг или обучение команды."
            if ru else "Every engagement starts with a business check-up, followed by one of three formats: done-for-you sales, marketing and automation, tracking, or team training.")
    out = [f'<section class="page">{crumbs(lang,"services")}<h1>{H1[lang]["services"]}</h1><p class="lead">{lead}</p></section>',
           f'<section id="diagnostics"><h2>{d_title}</h2><div class="card" style="margin-top:20px"><ul>{"".join(f"<li>{i}</li>" for i in d_items)}</ul></div>'
           f'<div class="cta"><a class="btn" href="{WA}" rel="noopener" target="_blank">{d_btn}</a></div></section>']
    for key, name, sub, who, items, fmt in SERVICES[lang]:
        li = "".join(f"<li>{i}</li>" for i in items)
        out.append(f'<section id="{key}"><p class="eyebrow">{name}</p><h2>{sub}</h2>' + (f"<p>{who}</p>" if who else "") +
                   f'<div class="card" style="margin-top:20px"><h3>{"Что входит" if ru else "What is included"}</h3><ul>{li}</ul>'
                   f'<p style="margin-top:14px"><b>{"Формат" if ru else "Format"}:</b> {fmt}</p></div></section>')
    out.append(f'<section id="process"><h2>{p_title}</h2><ol class="steps">{"".join(f"<li><span>{s}</span></li>" for s in p_steps)}</ol></section>')
    return "".join(out)

def body_cases(lang):
    ru = lang == "ru"
    intro = ("Проекты для бизнеса и трекинг стартапов. По каждому кейсу — каналы и инструменты, задача, решение и результат."
             if ru else "Client projects and startup tracking. Each case covers the channels and tools, the challenge, the solution and the result.")
    ch_h, task_h, done_h, res_h = ("Каналы и инструменты", "Задача", "Решение", "Результат") if ru else ("Channels and tools", "Challenge", "Solution", "Result")
    out = [f'<section class="page">{crumbs(lang,"cases")}<h1>{H1[lang]["cases"]}</h1><p class="lead">{intro}</p></section>',
           f'<section><h2>{"Ключевые проекты" if ru else "Key projects"}</h2>']
    for n, (title, channels, task, done, result) in enumerate(CASES[lang], 1):
        li = "".join(f"<li>{d}</li>" for d in done)
        out.append(f'<article class="case" id="case-{n}"><h2>{title}</h2>'
                   f'<h3>{ch_h}</h3><p>{channels}</p><h3>{task_h}</h3><p>{task}</p><h3>{done_h}</h3><ul>{li}</ul>'
                   f'<h3>{res_h}</h3><p class="result">{result}</p></article>')
    out.append(f'</section><section id="tracking"><h2>{"Трекинг стартапов" if ru else "Startup tracking"}</h2>')
    for n, (m, ml, title, tag, points) in enumerate(TRACK[lang], 1):
        li = "".join(f"<li>{x}</li>" for x in points)
        out.append(f'<article class="case" id="track-{n}"><p class="metric-row"><b class="metric">{m}</b><span class="metric-label">{ml}</span></p>'
                   f'<h2>{title}</h2><span class="tag">{tag}</span>'
                   f'<h3>{"Что изменилось" if ru else "What changed"}</h3><ul>{li}</ul></article>')
    out.append(f'<p class="note">{CASES_NOTE[lang]}</p></section>')
    return "".join(out)

def body_teaching(lang):
    ru = lang == "ru"
    cards = ""
    for place, role, items in TEACH[lang]:
        li = "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>" if items else ""
        cards += f'<article class="card"><span class="tag">{role}</span><h3>{place}</h3>{li}</article>'
    ctitle, citems = AI_COURSE[lang]
    cli = "".join(f"<li>{i}</li>" for i in citems)
    lead = ("Преподаю digital-маркетинг в университетах Алматы и провожу воркшопы для стартапов."
            if ru else "I teach digital marketing at Almaty universities and run workshops for startups.")
    return f"""
<section class="page">{crumbs(lang,"teaching")}<h1>{H1[lang]["teaching"]}</h1><p class="lead">{lead}</p></section>
<section><div class="cards">{cards}</div></section>
<section><h2>{ctitle}</h2><p>{"Я написал эту программу для AlmaU: от основ LLM до сквозной аналитики и создания сайта с AI. Задания устроены так, что студент сначала делает работу сам, а потом проверяет её с помощью AI." if ru else "I wrote this programme for AlmaU, from LLM basics to end-to-end analytics and building a website with AI. Students do each assignment by hand first, then check it with AI."}</p>
<div class="card" style="margin-top:20px"><ol style="padding-left:20px">{cli}</ol></div></section>"""

BODIES = {"": body_home, "about": body_about, "services": body_services, "cases": body_cases, "teaching": body_teaching, "contact": body_contact}

def render(lang, slug):
    t = T[lang]
    title, desc = META[lang][slug]
    other = "en" if lang == "ru" else "ru"
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{path(lang,s)}"{cur if s == slug else ""}{"" if s else ' class="nav-home"'}>{t["nav"][s]}</a>'
        for s in NAV)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{t["name"]}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url(lang,slug)}">
<link rel="alternate" hreflang="ru" href="{url("ru",slug)}">
<link rel="alternate" hreflang="en" href="{url("en",slug)}">
<link rel="alternate" hreflang="x-default" href="{url("ru",slug)}">
<link rel="alternate" type="text/plain" title="llms.txt" href="/llms.txt">
<meta property="og:type" content="{"profile" if slug in ("", "about") else "website"}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang,slug)}">
<meta property="og:locale" content="{"ru_RU" if lang=="ru" else "en_US"}">
<meta property="og:site_name" content="{t["name"]}">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0A0C10">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap&subset=cyrillic" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">
{schema(lang,slug)}
</script>
</head>
<body>
<header><div class="wrap bar">
<a class="brand" href="{path(lang,"")}">{LOGO}<span>Revanite</span></a>
<nav aria-label="{"Основное меню" if lang=="ru" else "Main menu"}">{nav}</nav><a class="lang" href="{path(other,slug)}" hreflang="{other}" lang="{other}" title="{t["switch"][1]}">{t["switch"][0]}</a>
</div></header>
<main class="wrap">{BODIES[slug](lang)}</main>
<footer id="contact"><div class="wrap">
<h2 class="footer-title">{"Маркетинг как вложение, а не расход." if lang=="ru" else "Marketing as an investment, not an expense."}</h2>
<p class="footer-sub">{"Алматы · Работаю с бизнесом в Казахстане, Кыргызстане и СНГ" if lang=="ru" else "Almaty · Working with businesses in Kazakhstan, Kyrgyzstan and the CIS"}</p>
{social_list(lang)}
<p class="copy">© {datetime.date.today().year} {t["footer"]}</p>
</div></footer>
</body>
</html>
"""

# ---------------------------------------------------------------- EXTRA FILES
def llms_txt():
    ru, en = T["ru"], T["en"]
    lines = [
        "# Руслан Хасанов (Ruslan Khasanov)",
        "",
        f"> {ru['summary']}",
        "",
        f"> {en['summary']}",
        "",
        "## Ключевые факты / Key facts",
        "- Имя: Руслан Хасанов (Хасанов Руслан Фархадович); латиницей Ruslan Khasanov, в LinkedIn — Ruslan Khassanov",
        "- Город: Алматы, Казахстан / Almaty, Kazakhstan",
        "- Роль: консультант по росту бизнеса, трекер стартапов, преподаватель digital-маркетинга, основатель Revanite; экс-CMO re:Kassa",
        "- Позиционирование: системный рост бизнеса — диагностика стратегии, продаж, маркетинга, процессов и экономики; внедрение от воронки продаж и рекламы до CRM, сквозной аналитики и автоматизации",
        "- Revanite — студия стратегического роста: экспресс-диагностика бизнеса ($99 вместо $200, засчитывается при продолжении работы), Revanite Tracking (трекинг и консалтинг), Revanite Studio (продажи, маркетинг и автоматизация под ключ). Принцип: маркетинг как вложение, а не расход",
        "- Метод: Revanite Growth Formula — Инсайт → Экономика → Стратегия → Гипотезы → Исполнение → Аналитика → Масштаб",
        "- Трекер стартапов: Astana Hub, Almaty Hub, Terricon Valley, NURIS, IT Park; акселератор AIpreneurs",
        "- Преподавание: Almaty Management University (AlmaU), Qamalladin University (руководитель направления «Диджитал»), колледж ICB; воркшопы Astana Hub; гостевая лекция Nazarbayev University",
        "- Опыт: Home Credit Bank (руководитель digital-маркетинга), Halyk Insurance (директор по продукту), Alfa Bank (тимлид маркетинга, сегмент малого бизнеса), Samsung Kazakhstan (запуск онлайн-магазина), BI GROUP (менеджер маркетинговых проектов), re:Kassa (CMO, до 2026)",
        "- Клиенты: " + ", ".join(CLIENTS["ru"]),
        "- Кейсы: SAGI — ROMI 316%; Yeko Kazakhstan — доля квалифицированных лидов с 30% до 70%, стоимость лида ниже в 2,4 раза; Глоббинг Казахстан — +60% новых регистраций, стоимость регистрации ниже на 45%; Shanyraq Business Forum — 1 600+ заявок и обращений за первый запуск, ROAS 234%; карта рассрочки Тумар (Бакай Банк) — стабильный ежемесячный поток новых клиентов и активация выданных карт; BI GROUP и Geometry — стоимость привлечения клиента рассчитана с нуля, реклама оптимизируется по ней; Jintropine — сквозная аналитика Meta Ads + amoCRM",
        "- Трекинг: Youtrade — рост выручки в 1,6 раза, перестройка операционных процессов, выход фаундера из операционного управления; InnMedia — выход на рынок Казахстана, первые 3 контракта; онлайн-школа — смена приоритетных рынков с США на Узбекистан и Турцию, выявлен партнёрский канал, обеспечивавший около 30% выручки",
        "- Компетенции: " + ", ".join(KNOWS["ru"]),
        "",
        "## Страницы / Pages",
    ]
    for s in PAGES:
        lines.append(f"- [{META['ru'][s][0]}]({url('ru', s)}): {META['ru'][s][1]}")
    for s in PAGES:
        lines.append(f"- [{META['en'][s][0]}]({url('en', s)}): {META['en'][s][1]}")
    lines += ["", "## Профили / Profiles", f"- Instagram: {IG}", f"- LinkedIn: {LI}", f"- Telegram: {TG}", "", "## Контакты / Contact", f"- WhatsApp / телефон: {PHONE_H} ({WA})", "- Telegram: @messer66", ""]
    return "\n".join(lines)

def robots():
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Applebot-Extended", "YandexBot", "Bingbot", "CCBot"]
    out = ["User-agent: *", "Allow: /", ""]
    for b in bots:
        out += [f"User-agent: {b}", "Allow: /", ""]
    out.append(f"Sitemap: {BASE}/sitemap.xml")
    out.append(f"Sitemap: {BASE}/studio/sitemap.xml")
    return "\n".join(out) + "\n"

def sitemap():
    items = []
    for lang in ("ru", "en"):
        for s in PAGES:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l,s)}"/>' for l in ("ru", "en"))
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("ru",s)}"/>'
            items.append(f"<url><loc>{url(lang,s)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(items) + "\n</urlset>\n")

def page404():
    return render("ru", "").replace("<title>", "<title>404 · ", 1).replace(
        '<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')

LOGO_FILE = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#0E1014"/>'
             '<g fill="none" stroke="#ECEEF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
             '<path d="M10 26V6h7.5a5 5 0 0 1 0 10H10"/><path d="M15.5 16 22 26"/></g>'
             '<path d="M4 29 28 3" stroke="#5B82C9" stroke-width="1.2" stroke-linecap="round"/></svg>')

def write(p, content):
    full = os.path.join(OUT, p.lstrip("/"))
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    for lang in ("ru", "en"):
        for s in PAGES:
            write(path(lang, s) + "index.html", render(lang, s))
    write("/llms.txt", llms_txt())
    write("/robots.txt", robots())
    write("/sitemap.xml", sitemap())
    write("/404.html", page404())
    write("/assets/logo.svg", LOGO_FILE)
    if PHOTO:
        shutil.copy("site_src/ruslan-khasanov.jpg", os.path.join(OUT, "assets/ruslan-khasanov.jpg"))
    if os.path.exists("site_src/og-image.jpg"):
        shutil.copy("site_src/og-image.jpg", os.path.join(OUT, "og-image.jpg"))
    print("built", OUT, "photo:", PHOTO)
    # сайт Revanite Studio — отдельный генератор, пишет в site/studio/
    import runpy
    runpy.run_path("studio/build.py", run_name="__main__")
