# -*- coding: utf-8 -*-
"""Генератор сайта Revanite Studio — revanite.kz/studio/ (RU/EN): Revanite — Strategic Growth Partner.
Запускается из корня репозитория (его вызывает build.py после сборки личного сайта).
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

STATS = {
 "ru": [("316%", "ROMI — приложение программы лояльности SAGI"), ("×2,4", "снижение стоимости лида — Yeko Kazakhstan"),
        ("−45%", "стоимость регистрации — Глоббинг Казахстан"), ("1 600+", "обращений за один запуск — Shanyraq Business Forum")],
 "en": [("316%", "ROMI — SAGI loyalty app"), ("×2.4", "lower cost per lead — Yeko Kazakhstan"),
        ("−45%", "cost per sign-up — Globbing Kazakhstan"), ("1,600+", "leads from a single launch — Shanyraq Business Forum")],
}

# Цена экспресс-диагностики: старая (зачёркнутая) и действующая
PRICE_OLD, PRICE = "$200", "$99"
PRICE_HTML = f'<span class="price"><s>{PRICE_OLD}</s> {PRICE}</span>'

# Кейсы: (название, инструменты, задача, исходная ситуация — "" если не известна, что сделано, результат)
CASES = {
 "ru": [
  ("Shanyraq Business Forum — бизнес-форум, 3 города", "Meta Ads, WhatsApp, amoCRM, чат-бот",
   "Обеспечить продажи билетов и прозрачность воронки — от клика до оплаты.", "",
   ["Еженедельный анализ воронки в amoCRM: статусы сделок, источники, эффективность менеджеров, доля квалифицированных заявок.",
    "Аудит коммуникаций отдела продаж в WhatsApp: выявлены 4 системные ошибки, по итогам внедрён чат-бот.",
    "Данные рекламных кабинетов и CRM объединены в единую систему отчётности."],
   "1 600+ заявок и обращений за первый запуск, ROAS 234%. Формат масштабирован на Шымкент и Алматы."),
  ("Глоббинг Казахстан — сервис доставки покупок из-за рубежа", "Meta Ads",
   "Увеличить приток новых пользователей при снижении стоимости привлечения.",
   "Кампании в рекламном кабинете были раздроблены, и алгоритму не хватало данных для обучения.",
   ["Анализ эффективности по городам: выявлены регионы с низкой отдачей бюджета.",
    "Аудит структуры рекламного кабинета.",
    "Тестирование аудиторий блогеров против гео-таргетинга и перераспределение бюджета по результатам."],
   "+60% новых регистраций при снижении стоимости регистрации на 45%."),
  ("Yeko Kazakhstan — отечественный бренд техники", "Онлайн-реклама, квалификация лидов",
   "Повысить качество входящих заявок, а не только их количество.",
   "Доля квалифицированных лидов составляла 30%.",
   ["Перестройка онлайн-рекламы под качество лидов: оптимизация по квалифицированным заявкам вместо объёма."],
   "Доля квалифицированных лидов выросла с 30% до 70%, стоимость лида снизилась в 2,4 раза."),
  ("SAGI — приложение программы лояльности", "Онлайн-реклама, продуктовая воронка",
   "Привлекать пользователей в приложение с окупаемостью рекламных вложений.", "",
   ["Запуск и ведение онлайн-рекламы, управление воронкой от первого касания до целевого действия, оптимизация по возврату инвестиций."],
   "ROMI 316%."),
  ("Карта рассрочки Тумар, Бакай Банк (Кыргызстан)", "Google Ads, Meta Ads, мобильная атрибуция, CRM-маркетинг",
   "Построить цифровой канал с равномерным ежемесячным притоком клиентов.", "",
   ["Структура кампаний Google Ads и лид-кампании Meta с ежемесячной отчётностью.",
    "Интеграция мобильной атрибуции приложения с рекламными кабинетами.",
    "Программа активации выданных карт с сегментацией базы — «не совершали покупок», «снижают активность», «неактивны» — и партнёрскими предложениями для каждого сегмента."],
   "Стабильный ежемесячный поток новых клиентов банка и отдельная программа активации действующих держателей карт."),
  ("BI GROUP и Geometry — девелопмент", "Meta Ads, юнит-экономика",
   "Выстроить цифровое привлечение с нуля.",
   "Стоимость привлечения клиента не рассчитывалась.",
   ["Построение цифровой воронки, расчёт стоимости привлечения клиента (CAC) и оптимизация рекламы по этой метрике."],
   "Команда получила измеримую стоимость клиента; реклама оптимизируется по CAC, а не по кликам и охватам."),
 ],
 "en": [
  ("Shanyraq Business Forum — business forum, 3 cities", "Meta Ads, WhatsApp, amoCRM, chatbot",
   "Drive ticket sales and make the funnel transparent from click to payment.", "",
   ["Weekly amoCRM funnel analysis: deal stages, sources, sales rep performance, qualified-lead share.",
    "Audit of the sales team's WhatsApp communication: 4 systemic errors identified, followed by a chatbot rollout.",
    "Ad account and CRM data consolidated into a single reporting system."],
   "1,600+ leads from the first launch, 234% ROAS. The format was scaled to Shymkent and Almaty."),
  ("Globbing Kazakhstan — cross-border shopping delivery", "Meta Ads",
   "Increase new user acquisition while lowering acquisition cost.",
   "Campaigns in the ad account were fragmented, so the algorithm lacked data to learn.",
   ["City-level performance analysis: regions with low budget efficiency identified.",
    "Ad account structure audit.",
    "Blogger-audience vs. geo-targeting test, with budget reallocated based on the results."],
   "+60% new sign-ups with a 45% lower cost per sign-up."),
  ("Yeko Kazakhstan — local electronics brand", "Online ads, lead qualification",
   "Improve the quality of inbound leads, not just their volume.",
   "Qualified leads made up 30% of the total.",
   ["Online advertising rebuilt around lead quality: optimizing for qualified leads instead of volume."],
   "Qualified lead share rose from 30% to 70%; cost per lead fell 2.4×."),
  ("SAGI — loyalty app", "Online ads, product funnel",
   "Acquire app users with advertising that pays back.", "",
   ["Online acquisition launched and managed, funnel managed from first touch to the target action, optimized for return on investment."],
   "316% ROMI."),
  ("Tumar installment card, Bakai Bank (Kyrgyzstan)", "Google Ads, Meta Ads, mobile attribution, CRM marketing",
   "Build a digital channel with a steady monthly inflow of customers.", "",
   ["Google Ads campaign structure and Meta lead campaigns with monthly reporting.",
    "Mobile app attribution integrated with the ad accounts.",
    "Activation program for issued cards, segmenting the base — no purchases yet, declining activity, inactive — with partner offers for each segment."],
   "A steady monthly flow of new bank customers and a dedicated activation program for existing cardholders."),
  ("BI GROUP and Geometry — real estate", "Meta Ads, unit economics",
   "Build digital acquisition from scratch.",
   "Customer acquisition cost was not being calculated.",
   ["Digital funnel built, customer acquisition cost (CAC) calculated and advertising optimized against that metric."],
   "The team now has a measurable cost per customer; advertising is optimized for CAC rather than clicks and reach."),
 ],
}

PAGES = ["", "services", "marketing-management", "digital-growth", "business-tracking", "education", "cases", "about", "teaching", "contact"]
NAV = ["", "services", "cases", "education", "about", "contact"]
DIR_SLUGS = ["marketing-management", "digital-growth", "business-tracking", "education"]

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

ROOT = "/studio"  # сайт студии живёт в подпапке, личный сайт — в корне домена

def url(lang, slug):
    return BASE + path(lang, slug)

def path(lang, slug):
    prefix = ROOT + ("" if lang == "ru" else "/en")
    return prefix + "/" + (slug + "/" if slug else "")

# ---------------------------------------------------------------- TEXT
T = {
 "ru": {
  "name": "Руслан Хасанов",
  "brand": "Revanite",
  "tagline": "Strategic Growth Partner",
  "nav": {"": "Главная", "services": "Направления", "cases": "Кейсы", "education": "Обучение", "about": "Основатель", "contact": "Контакты",
          "marketing-management": "Marketing Management", "digital-growth": "Digital Growth", "business-tracking": "Business Tracking",
          "teaching": "Преподавание"},
  "home": "Главная",
  "switch": ("EN", "English version"),
  "discuss": "Обсудить проект",
  "details": "Подробнее",
  "jobTitle": "Основатель Revanite, Strategic Growth Partner",
  "summary": ("Руслан Хасанов — основатель Revanite, стратегический партнёр бизнеса в маркетинге и digital-развитии (Алматы, Казахстан). "
              "Работает с собственниками бизнеса: диагностика маркетинга, стратегия, приоритеты, управление маркетинговыми процессами и контроль результата. "
              "Был CMO фискальной платформы re:Kassa, руководил digital-маркетингом в Home Credit Bank, был директором по продукту в Halyk Insurance, "
              "руководил маркетингом сегмента малого бизнеса в Alfa Bank. Трекер стартапов в Astana Hub, Almaty Hub, Terricon Valley, NURIS и IT Park, "
              "преподаёт digital-маркетинг в AlmaU и руководит направлением «Диджитал» в Qamalladin University."),
  "org_desc": ("Revanite — Strategic Growth Partner: стратегический партнёр бизнеса в маркетинге, digital-развитии и привлечении клиентов с фокусом на росте выручки и прозрачности работы. "
               "Четыре направления: Marketing Management (управление маркетингом), Digital Growth (реклама, сайты и аналитика), "
               "Business Tracking (трекинг бизнеса) и Education (обучение маркетингу). Алматы, Казахстан."),
  "footer_title": "Revanite — Strategic Growth Partner",
  "footer_sub": "Алматы · Работаем с бизнесом в Казахстане, Кыргызстане и СНГ",
  "copy": "Revanite · Основатель — Руслан Хасанов · Алматы, Казахстан",
 },
 "en": {
  "name": "Ruslan Khasanov",
  "brand": "Revanite",
  "tagline": "Strategic Growth Partner",
  "nav": {"": "Home", "services": "Services", "cases": "Case studies", "education": "Education", "about": "Founder", "contact": "Contact",
          "marketing-management": "Marketing Management", "digital-growth": "Digital Growth", "business-tracking": "Business Tracking",
          "teaching": "Teaching"},
  "home": "Home",
  "switch": ("RU", "Русская версия"),
  "discuss": "Discuss a project",
  "details": "Learn more",
  "jobTitle": "Founder of Revanite, Strategic Growth Partner",
  "summary": ("Ruslan Khasanov is the founder of Revanite, a strategic growth partner for businesses in marketing and digital development (Almaty, Kazakhstan). "
              "He works with business owners on marketing diagnostics, strategy, priorities, marketing process management and results control. "
              "He was CMO at the fiscal technology platform re:Kassa, Head of Digital Marketing at Home Credit Bank, Director of Product at Halyk Insurance "
              "and head of SME marketing at Alfa Bank. He tracks startups at Astana Hub, Almaty Hub, Terricon Valley, NURIS and IT Park, "
              "teaches digital marketing at AlmaU and leads the Digital program at Qamalladin University."),
  "org_desc": ("Revanite is a Strategic Growth Partner for businesses in marketing, digital development and customer acquisition, focused on revenue growth and transparent work. "
               "Four practices: Marketing Management, Digital Growth (ads, websites and analytics), Business Tracking and Education. Almaty, Kazakhstan."),
  "footer_title": "Revanite — Strategic Growth Partner",
  "footer_sub": "Almaty · Working with businesses in Kazakhstan, Kyrgyzstan and the CIS",
  "copy": "Revanite · Founder — Ruslan Khasanov · Almaty, Kazakhstan",
 },
}

HOME = {
 "ru": {
  "eyebrow": "Revanite · Strategic Growth Partner",
  "h1": "Your Business Needs More Than a Marketing Agency.",
  "lead": "Мы становимся стратегическим партнёром бизнеса: управляем маркетингом, развиваем digital-каналы и помогаем находить новые точки роста выручки — прозрачно и на связи на каждом этапе.",
  "cta2": "Наши направления",
  "system_title": "Система Revanite",
  "system_steps": [("Strategy", "цели и приоритеты"), ("Management", "управление маркетингом"),
                   ("Execution", "реклама, сайты, аналитика"), ("Tracking & Growth", "результат и новые точки роста")],
  "system_edu": "+ Education — развитие специалистов и команд",
  "problem_h2": "Почему бизнесу недостаточно отдельных маркетинговых услуг",
  "problem_lead": "Реклама, сайт, аналитика и подрядчики часто существуют по отдельности. Каждый элемент может работать, но система в целом не даёт результата.",
  "problems": ["Нет единой маркетинговой стратегии", "Реклама работает отдельно от продаж", "Подрядчики не управляются системно",
               "Нет прозрачной аналитики", "Собственник вынужден контролировать всё самостоятельно"],
  "approach_h3": "Подход Revanite",
  "approach": ("Мы соединяем стратегию, управление, реализацию и аналитику в одну систему. "
               "Каждое маркетинговое действие связано с ростом бизнеса и выручки, а результат измеряется заявками, продажами и окупаемостью. "
               "Вы всегда видите, что сделано и на что потрачен бюджет."),
  "dirs_h2": "Направления работы",
  "dirs_lead": "Четыре самостоятельных направления, объединённых общей методологией.",
  "method_h2": "Методология Revanite",
  "method_lead": ("Авторский подход, который позволяет видеть маркетинг целиком: каждый этап опирается на предыдущий и проверяется следующим, "
                  "поэтому решения в рекламе, на сайте и в продажах не противоречат друг другу."),
  "aud_h2": "Для кого мы работаем",
  "cases_h2": "Кейсы и проекты",
  "cases_all": "Все кейсы",
  "clients": "Клиенты",
  "founder_h2": "Об основателе",
  "founder_more": "Подробнее об основателе",
  "faq_h2": "Частые вопросы",
  "final_h2": "Let's Find Your Next Growth Point.",
  "final_text": "Расскажите о своей задаче. Мы поможем определить, какие маркетинговые инструменты и решения нужны вашему бизнесу на текущем этапе, чтобы расти в выручке.",
 },
 "en": {
  "eyebrow": "Revanite · Strategic Growth Partner",
  "h1": "Your Business Needs More Than a Marketing Agency.",
  "lead": "We become a strategic partner to your business: we manage marketing, develop digital channels and help you find new sources of revenue growth — transparently, and in touch at every stage.",
  "cta2": "What we do",
  "system_title": "The Revanite system",
  "system_steps": [("Strategy", "goals and priorities"), ("Management", "marketing management"),
                   ("Execution", "ads, websites, analytics"), ("Tracking & Growth", "results and new growth points")],
  "system_edu": "+ Education — developing specialists and teams",
  "problem_h2": "Why separate marketing services are not enough",
  "problem_lead": "Ads, the website, analytics and contractors often live separately. Each piece may work, yet the system as a whole does not deliver.",
  "problems": ["No single marketing strategy", "Advertising is disconnected from sales", "Contractors are not managed as a system",
               "No transparent analytics", "The owner has to control everything personally"],
  "approach_h3": "The Revanite approach",
  "approach": ("We connect strategy, management, execution and analytics into one system. "
               "Every marketing action is tied to business and revenue growth, and results are measured in leads, sales and payback. "
               "You always see what has been done and where the budget went."),
  "dirs_h2": "What we do",
  "dirs_lead": "Four independent practices united by one methodology.",
  "method_h2": "The Revanite methodology",
  "method_lead": ("Our own approach to seeing marketing as a whole: each stage builds on the previous one and is tested by the next, "
                  "so decisions in advertising, on the website and in sales do not contradict each other."),
  "aud_h2": "Who we work with",
  "cases_h2": "Case studies and projects",
  "cases_all": "All case studies",
  "clients": "Clients",
  "founder_h2": "About the founder",
  "founder_more": "More about the founder",
  "faq_h2": "FAQ",
  "final_h2": "Let's Find Your Next Growth Point.",
  "final_text": "Tell us about your challenge. We will help you decide which marketing tools and solutions your business needs at its current stage to grow revenue.",
 },
}

PRINCIPLES = {
 "ru": ("Принципы работы", [
   ("Рост выручки — главная метрика", "Оцениваем маркетинг по заявкам, продажам и окупаемости, а не по охватам и кликам."),
   ("Прозрачность процессов", "Вы видите, что сделано, сколько потрачено и какой получен результат: регулярные отчёты, дашборды и понятный план работ."),
   ("Всегда на связи", "Один ответственный контакт, регулярные созвоны и оперативные ответы на всех этапах проекта."),
   ("Ответственность до результата", "Не пропадаем после запуска: доводим задачи до конца и отвечаем за договорённости.")]),
 "en": ("How we work with clients", [
   ("Revenue growth is the main metric", "We judge marketing by leads, sales and payback, not by reach and clicks."),
   ("Transparent processes", "You see what has been done, what has been spent and what it delivered: regular reports, dashboards and a clear work plan."),
   ("Always in touch", "One accountable contact, regular calls and prompt replies at every stage of the project."),
   ("Accountable to the end", "We do not disappear after launch: we see tasks through and stand by our commitments.")]),
}

METHOD = {
 "ru": [("Strategy", "Понимаем бизнес, определяем цели, аудиторию, позиционирование и приоритеты."),
        ("Management", "Выстраиваем систему управления маркетингом, каналами, бюджетами и специалистами."),
        ("Execution", "Реализуем рекламные кампании, создаём сайты, внедряем аналитику и digital-инструменты."),
        ("Tracking & Growth", "Анализируем результаты, проверяем гипотезы и находим новые возможности для роста.")],
 "en": [("Strategy", "We understand the business and define goals, audience, positioning and priorities."),
        ("Management", "We build a system for managing marketing, channels, budgets and specialists."),
        ("Execution", "We run ad campaigns, build websites and implement analytics and digital tools."),
        ("Tracking & Growth", "We analyze results, test hypotheses and find new growth opportunities.")],
}
METHOD_EDU = {
 "ru": ("Education", "Дополняет систему: развиваем специалистов и команды, которые способны эффективно работать с маркетингом."),
 "en": ("Education", "Complements the system: we develop specialists and teams who can work with marketing effectively."),
}

# Направления: карточка на главной и отдельная страница
DIRS = {
 "ru": {
  "marketing-management": {
   "name": "Marketing Management", "label": "Управление маркетингом", "badge": "Ключевое направление",
   "short": "Становимся внешним маркетинговым партнёром компании: стратегия, план, бюджеты, постановка задач специалистам и подрядчикам, контроль и аналитика.",
   "value": "Маркетинг управляется как система и работает на рост выручки.",
   "h1": "Управление маркетингом бизнеса",
   "lead": "Выступаем внешним маркетинговым партнёром компании и берём на себя системное управление маркетингом — от анализа и стратегии до контроля реализации и регулярной аналитики.",
   "blocks": [("Что входит", ["Анализ текущего маркетинга и бизнес-задач", "Разработка маркетинговой стратегии",
                              "Определение целевой аудитории и позиционирования", "Формирование маркетингового плана",
                              "Планирование рекламных каналов и бюджетов",
                              "Постановка задач маркетологам, дизайнерам, подрядчикам и другим специалистам",
                              "Контроль реализации маркетинговых активностей", "Анализ эффективности каналов привлечения",
                              "Работа с воронкой продаж и качеством лидов", "Регулярная аналитика и рекомендации по развитию"])],
   "for_h2": "Для кого",
   "for": ["У бизнеса нет собственного руководителя маркетинга",
           "Собственник сам управляет маркетологами и подрядчиками, но хочет делегировать эту функцию",
           "В компании есть маркетологи, но нет общей стратегии и системы управления",
           "Бизнес хочет развивать маркетинг, но пока не готов нанимать руководителя отдела маркетинга"],
   "result_h2": "Результат",
   "result": "Бизнес получает внешнего стратегического партнёра, который управляет маркетингом, связывает маркетинговые действия с ростом выручки и регулярно отчитывается о результатах.",
   "format": "Ежемесячное сопровождение с еженедельной отчётностью и постоянной связью с собственником.",
   "note": "Реализацию рекламы, сайтов и аналитики берёт на себя направление Digital Growth. Если задача шире маркетинга и касается бизнеса в целом, подходит Business Tracking.",
   "cases": [0, 2, 5], "diag": True,
  },
  "digital-growth": {
   "name": "Digital Growth", "label": "Реклама, сайты и аналитика", "badge": "",
   "short": "Реализуем стратегию на практике: реклама в Meta и Google, сайты и лендинги, GA4, Google Tag Manager, отчёты и дашборды.",
   "value": "Каждый digital-инструмент работает на рост заявок и выручки.",
   "h1": "Digital-маркетинг и развитие онлайн-каналов",
   "lead": "Практическая сторона работы Revanite: мы не только определяем стратегию, но и помогаем её реализовать. Реклама, сайт и аналитика подключаются под конкретную задачу бизнеса и оцениваются по результату.",
   "blocks": [("Онлайн-реклама", ["Meta Ads (Facebook и Instagram)", "Google Ads", "Настройка и оптимизация рекламных кампаний",
                                 "Разработка рекламных гипотез", "Анализ эффективности рекламы", "Управление рекламными бюджетами"]),
              ("Создание сайтов", ["Разработка сайтов для бизнеса", "Лендинги и посадочные страницы", "Сайты для продуктов и услуг",
                                  "Структура и прототипирование", "UX/UI и конверсионная логика",
                                  "Разработка на Tilda и с использованием современных AI-инструментов"]),
              ("Аналитика и digital-инфраструктура", ["Google Analytics 4", "Google Tag Manager", "Настройка событий и конверсий",
                                                     "Отслеживание заявок и действий пользователей", "Интеграция аналитики с рекламными каналами",
                                                     "Мобильная атрибуция: AppsFlyer", "Интеграция с CRM (amoCRM, Bitrix24), чат-боты и автоматизация передачи заявок",
                                                     "Отчёты и дашборды", "Анализ воронки и эффективности привлечения"])],
   "why_h2": "Не отдельные услуги, а система",
   "why": "Настройка рекламы или новый сайт сами по себе не гарантируют продаж. Мы связываем каналы привлечения, сайт, аналитику и CRM, чтобы видеть путь клиента от первого касания до сделки и принимать решения на основе данных.",
   "format": "Проект или ежемесячное ведение с еженедельной отчётностью: расходы, заявки, продажи.",
   "cases": [1, 3, 4], "diag": False,
  },
  "business-tracking": {
   "name": "Business Tracking", "label": "Трекинг и точки роста", "badge": "",
   "short": "Самостоятельный формат работы с предпринимателем: цели и показатели, поиск ограничений, гипотезы, приоритеты и регулярный контроль прогресса.",
   "value": "Предприниматель системно движется к росту бизнеса и выручки.",
   "h1": "Трекинг бизнеса и работа с точками роста",
   "lead": "Отдельное направление для предпринимателей и собственников бизнеса. Трекинг помогает системно развивать компанию: определять ограничения, формулировать и проверять гипотезы, двигаться к поставленным целям.",
   "blocks": [("Что входит", ["Постановка целей и определение ключевых показателей", "Анализ текущей ситуации в бизнесе",
                              "Поиск ограничений и узких мест", "Формирование и проверка гипотез", "Определение приоритетных действий",
                              "Регулярные встречи и контроль прогресса", "Работа с показателями и результатами",
                              "Помощь в принятии управленческих решений"])],
   "why_h2": "Чем трекинг отличается от управления маркетингом",
   "why": ("В Marketing Management мы управляем маркетингом компании. В трекинге работаем с предпринимателем над бизнесом в целом: "
           "целями, показателями, ограничениями и управленческими решениями. Трекер не выполняет работу за команду — он помогает выбрать приоритеты и удерживать фокус."),
   "format": "Трекшн-сессии раз в одну-две недели, трекшн-карта, контроль показателей между сессиями.",
   "exp": "Основатель Revanite — трекер стартапов в Astana Hub, Almaty Hub, Terricon Valley, NURIS и IT Park, линейный трекер акселератора AIpreneurs.",
   "cases": [], "diag": False,
  },
  "education": {
   "name": "Education", "label": "Обучение маркетингу", "badge": "",
   "short": "Практическое обучение для будущих и действующих маркетологов и таргетологов и корпоративные программы для команд.",
   "value": "Специалисты и команды, способные эффективно работать с маркетингом.",
   "h1": "Обучение маркетингу и развитие digital-компетенций",
   "lead": "Самостоятельное направление Revanite. Обучаем практическим навыкам на реальных инструментах — специалистов, которые строят карьеру в digital, и компании, которые развивают свои команды.",
  },
 },
 "en": {
  "marketing-management": {
   "name": "Marketing Management", "label": "Marketing management", "badge": "Core practice",
   "short": "We act as the company's external marketing partner: strategy, plan, budgets, briefing specialists and contractors, control and analytics.",
   "value": "Marketing is managed as a system and drives revenue growth.",
   "h1": "Managing your business's marketing",
   "lead": "We act as the company's external marketing partner and take on the systematic management of marketing — from analysis and strategy to implementation control and regular analytics.",
   "blocks": [("What's included", ["Analysis of current marketing and business objectives", "Marketing strategy development",
                                   "Target audience and positioning", "Marketing plan",
                                   "Planning of ad channels and budgets",
                                   "Briefing and managing marketers, designers, contractors and other specialists",
                                   "Control over marketing activities", "Analysis of acquisition channel performance",
                                   "Sales funnel and lead quality", "Regular analytics and growth recommendations"])],
   "for_h2": "Who it's for",
   "for": ["The business has no in-house head of marketing",
           "The owner manages marketers and contractors personally but wants to delegate this function",
           "The company has marketers but no shared strategy or management system",
           "The business wants to grow its marketing but is not ready to hire a head of marketing yet"],
   "result_h2": "Result",
   "result": "The business gains an external strategic partner who manages marketing, ties marketing actions to revenue growth and reports on results regularly.",
   "format": "Ongoing monthly engagement with weekly reporting and direct, ongoing contact with the owner.",
   "note": "Ads, websites and analytics are implemented by the Digital Growth practice. If the challenge goes beyond marketing and concerns the business as a whole, Business Tracking is the right fit.",
   "cases": [0, 2, 5], "diag": True,
  },
  "digital-growth": {
   "name": "Digital Growth", "label": "Ads, websites and analytics", "badge": "",
   "short": "We put the strategy into practice: Meta and Google ads, websites and landing pages, GA4, Google Tag Manager, reports and dashboards.",
   "value": "Every digital tool works toward more leads and revenue.",
   "h1": "Digital marketing and online channel development",
   "lead": "The hands-on side of Revanite: we do not just define the strategy, we help implement it. Ads, the website and analytics are set up for a specific business objective and judged by results.",
   "blocks": [("Online advertising", ["Meta Ads (Facebook and Instagram)", "Google Ads", "Campaign setup and optimization",
                                     "Ad hypothesis development", "Ad performance analysis", "Ad budget management"]),
              ("Websites", ["Business websites", "Landing pages", "Websites for products and services",
                            "Structure and prototyping", "UX/UI and conversion logic",
                            "Built on Tilda and with modern AI tools"]),
              ("Analytics and digital infrastructure", ["Google Analytics 4", "Google Tag Manager", "Event and conversion setup",
                                                       "Lead and user action tracking", "Analytics integrated with ad channels",
                                                       "Mobile attribution: AppsFlyer", "CRM integration (amoCRM, Bitrix24), chatbots and lead routing automation",
                                                       "Reports and dashboards", "Funnel and acquisition performance analysis"])],
   "why_h2": "Not separate services, but a system",
   "why": "Setting up ads or launching a new website does not guarantee sales on its own. We connect acquisition channels, the website, analytics and the CRM to see the customer journey from first touch to deal and make data-driven decisions.",
   "format": "Project-based or ongoing monthly management with weekly reporting on spend, leads and sales.",
   "cases": [1, 3, 4], "diag": False,
  },
  "business-tracking": {
   "name": "Business Tracking", "label": "Tracking and growth points", "badge": "",
   "short": "A dedicated format for entrepreneurs: goals and metrics, finding constraints, hypotheses, priorities and regular progress reviews.",
   "value": "The entrepreneur moves systematically toward business and revenue growth.",
   "h1": "Business tracking and growth points",
   "lead": "A separate practice for entrepreneurs and business owners. Tracking helps develop the company systematically: identify constraints, frame and test hypotheses and move toward set goals.",
   "blocks": [("What's included", ["Setting goals and key metrics", "Analysis of the current business situation",
                                   "Finding constraints and bottlenecks", "Framing and testing hypotheses", "Defining priority actions",
                                   "Regular sessions and progress reviews", "Working with metrics and results",
                                   "Support with management decisions"])],
   "why_h2": "How tracking differs from marketing management",
   "why": ("In Marketing Management we manage the company's marketing. In tracking we work with the entrepreneur on the business as a whole: "
           "goals, metrics, constraints and management decisions. A tracker does not do the work for the team — a tracker helps choose priorities and keep focus."),
   "format": "Traction sessions every one to two weeks, a traction map, metric reviews between sessions.",
   "exp": "The founder of Revanite is a startup tracker at Astana Hub, Almaty Hub, Terricon Valley, NURIS and IT Park and a line tracker at the AIpreneurs accelerator.",
   "cases": [], "diag": False,
  },
  "education": {
   "name": "Education", "label": "Marketing education", "badge": "",
   "short": "Hands-on training for aspiring and working marketers and media buyers, and corporate programs for teams.",
   "value": "Specialists and teams who can work with marketing effectively.",
   "h1": "Marketing education and digital skills",
   "lead": "An independent Revanite practice. We teach practical skills on real tools — to specialists building a career in digital and to companies developing their teams.",
  },
 },
}

EDU = {
 "ru": {
  "a_tag": "Для специалистов", "a_h2": "Обучение начинающих и действующих специалистов",
  "a_intro": "Для тех, кто хочет освоить профессию маркетолога или таргетолога, начать карьеру в digital или повысить квалификацию и доход.",
  "a_prog_h": "Программы",
  "a_prog": ["Профессия интернет-маркетолог", "Обучение таргетированной рекламе", "Meta Ads с нуля", "Google Ads", "Digital-маркетинг",
             "Веб-аналитика и Google Analytics 4", "Google Tag Manager", "Маркетинговая стратегия", "Работа с воронками продаж",
             "Практическое применение AI в маркетинге", "Повышение квалификации для действующих маркетологов и таргетологов"],
  "a_fmt_h": "Форматы",
  "a_fmt": ["Индивидуальное обучение", "Наставничество", "Практические курсы", "Групповые программы", "Интенсивы и воркшопы"],
  "a_focus": "Главный акцент — практика: реальные рекламные кабинеты, аналитика и задачи, с которыми специалист работает на настоящих проектах.",
  "a_cta": "Узнать о программах",
  "b_tag": "Для компаний", "b_h2": "Корпоративное обучение",
  "b_intro": "Для компаний, предпринимателей и действующих команд, которым нужно повысить компетенции сотрудников, развить внутренний маркетинг и внедрить современные digital- и AI-инструменты.",
  "b_prog_h": "Направления",
  "b_prog": ["Обучение сотрудников digital-маркетингу", "Обучение таргетированной рекламе", "Работа с рекламными кабинетами",
             "Веб-аналитика", "Маркетинговая стратегия", "AI-инструменты для маркетинга",
             "Обучение руководителей и маркетинговых команд", "Практические корпоративные воркшопы"],
  "b_fmt": "Программа собирается под задачи компании и уровень команды: онлайн или очно в Алматы.",
  "b_cta": "Обсудить обучение команды",
  "terms": "Состав программ, формат и стоимость согласуются индивидуально.",
  "exp_h2": "Опыт преподавания",
  "exp": "Основатель Revanite преподаёт digital-маркетинг и веб-аналитику в AlmaU (с 2022 года), руководит направлением «Диджитал» в Qamalladin University, преподаёт в колледже ICB, проводит воркшопы в Astana Hub и выступал с гостевой лекцией в Nazarbayev University. Автор программы курса «AI в маркетинге».",
  "exp_link": "Подробнее о преподавании",
 },
 "en": {
  "a_tag": "For specialists", "a_h2": "Training for aspiring and working specialists",
  "a_intro": "For people who want to become a marketer or media buyer, start a career in digital, or upgrade their skills and income.",
  "a_prog_h": "Programs",
  "a_prog": ["Online marketer career track", "Paid social advertising", "Meta Ads from scratch", "Google Ads", "Digital marketing",
             "Web analytics and Google Analytics 4", "Google Tag Manager", "Marketing strategy", "Sales funnels",
             "Practical AI in marketing", "Advanced training for working marketers and media buyers"],
  "a_fmt_h": "Formats",
  "a_fmt": ["One-to-one training", "Mentoring", "Hands-on courses", "Group programs", "Intensives and workshops"],
  "a_focus": "The focus is practice: real ad accounts, analytics and the tasks a specialist handles on actual projects.",
  "a_cta": "Ask about programs",
  "b_tag": "For companies", "b_h2": "Corporate training",
  "b_intro": "For companies, entrepreneurs and existing teams that need to upskill employees, build in-house marketing and adopt modern digital and AI tools.",
  "b_prog_h": "Topics",
  "b_prog": ["Digital marketing for employees", "Paid social advertising", "Working with ad accounts",
             "Web analytics", "Marketing strategy", "AI tools for marketing",
             "Training for managers and marketing teams", "Hands-on corporate workshops"],
  "b_fmt": "Each program is built around the company's goals and the team's level: online or in person in Almaty.",
  "b_cta": "Discuss team training",
  "terms": "Program content, format and pricing are agreed individually.",
  "exp_h2": "Teaching experience",
  "exp": "The founder of Revanite teaches digital marketing and web analytics at AlmaU (since 2022), leads the Digital program at Qamalladin University, teaches at ICB College, runs workshops at Astana Hub and has given a guest lecture at Nazarbayev University. Author of the “AI in Marketing” course program.",
  "exp_link": "More about teaching",
 },
}

AUDIENCES = {
 "ru": [("Собственники малого и среднего бизнеса", "Нужно больше клиентов и продаж, нет ясности, насколько эффективен текущий маркетинг, и нет желания самостоятельно управлять всеми подрядчиками.", "marketing-management"),
        ("Растущие компании", "Уже инвестируют в рекламу, работают с маркетологами или подрядчиками и хотят улучшить результат за счёт стратегии, управления и аналитики.", "digital-growth"),
        ("Предприниматели", "Ищут точки роста и хотят системнее управлять компанией.", "business-tracking"),
        ("Начинающие и действующие digital-специалисты", "Хотят освоить профессию маркетолога или таргетолога, получить практические навыки и повысить доход.", "education#specialists"),
        ("Компании, которым нужно обучить команду", "Развивают внутреннюю маркетинговую команду и внедряют современные digital- и AI-инструменты.", "education#corporate")],
 "en": [("Small and mid-sized business owners", "Need more customers and sales, are unsure how effective current marketing is, and do not want to manage every contractor themselves.", "marketing-management"),
        ("Growing companies", "Already invest in advertising, work with marketers or contractors, and want better results through strategy, management and analytics.", "digital-growth"),
        ("Entrepreneurs", "Look for growth points and want to run the company more systematically.", "business-tracking"),
        ("Aspiring and working digital specialists", "Want to become a marketer or media buyer, gain practical skills and increase their income.", "education#specialists"),
        ("Companies training their teams", "Develop in-house marketing teams and adopt modern digital and AI tools.", "education#corporate")],
}

FOUNDER = {
 "ru": {
  "role": "Основатель Revanite · Strategic Growth Partner",
  "short": ["Руслан Хасанов работает с собственниками бизнеса: диагностирует маркетинг, разрабатывает стратегию, определяет приоритеты, управляет маркетинговыми процессами и контролирует результат.",
            "Опыт — руководящие позиции в маркетинге и продукте: CMO re:Kassa, руководитель digital-маркетинга Home Credit Bank, директор по продукту Halyk Insurance, руководитель маркетинга сегмента малого бизнеса Alfa Bank. Трекер стартапов в IT-хабах Казахстана, преподаватель digital-маркетинга в AlmaU и Qamalladin University."],
  "chips": ["Маркетинговая стратегия", "Digital", "Управление рекламой", "Аналитика", "Трекинг", "Обучение"],
  "h1": "Руслан Хасанов — основатель Revanite",
  "lead": "Strategic Growth Partner: стратегическое мышление и практический опыт реализации маркетинговых проектов.",
  "role_h2": "Роль в Revanite",
  "roles": ["Работа с собственниками бизнеса", "Диагностика маркетинга", "Разработка стратегии", "Определение приоритетов",
            "Управление маркетинговыми процессами", "Контроль результатов", "Развитие компании и клиентских проектов"],
  "bio_h2": "Опыт",
  "bio": ["Карьера Руслана сложилась в корпоративном маркетинге и продукте: CMO фискальной платформы re:Kassa, руководитель digital-маркетинга Home Credit Bank, директор по продукту Halyk Insurance, руководитель маркетинга сегмента малого бизнеса Alfa Bank, менеджер маркетинговых проектов BI GROUP, участие в запуске онлайн-магазина Samsung Kazakhstan.",
          "Сегодня — основатель Revanite и трекер стартапов в Astana Hub, Almaty Hub, Terricon Valley, NURIS и IT Park. Преподаёт digital-маркетинг и веб-аналитику в AlmaU, руководит направлением «Диджитал» в Qamalladin University, проводит воркшопы в Astana Hub.",
          "Принцип работы: сначала определить, где бизнес теряет рост и деньги, и только затем инвестировать. Маркетинг — это вложение, которое должно окупаться и измеряться."],
  "exp_h2": "Карьера", "skills_h2": "Компетенции",
  "names_h2": "Как пишется имя",
  "names": "Руслан Хасанов (полное имя — Хасанов Руслан Фархадович). Латиницей — Ruslan Khasanov; в LinkedIn используется написание Ruslan Khassanov.",
 },
 "en": {
  "role": "Founder of Revanite · Strategic Growth Partner",
  "short": ["Ruslan Khasanov works with business owners: he diagnoses marketing, develops strategy, sets priorities, manages marketing processes and controls results.",
            "Background — leadership roles in marketing and product: CMO at re:Kassa, Head of Digital Marketing at Home Credit Bank, Director of Product at Halyk Insurance, head of SME marketing at Alfa Bank. Startup tracker at Kazakhstan's tech hubs, digital marketing lecturer at AlmaU and Qamalladin University."],
  "chips": ["Marketing strategy", "Digital", "Ad management", "Analytics", "Tracking", "Education"],
  "h1": "Ruslan Khasanov — founder of Revanite",
  "lead": "Strategic Growth Partner: strategic thinking combined with hands-on experience delivering marketing projects.",
  "role_h2": "Role at Revanite",
  "roles": ["Working with business owners", "Marketing diagnostics", "Strategy development", "Setting priorities",
            "Managing marketing processes", "Results control", "Developing the company and client projects"],
  "bio_h2": "Background",
  "bio": ["Ruslan built his career in corporate marketing and product: CMO at the fiscal technology platform re:Kassa, Head of Digital Marketing at Home Credit Bank, Director of Product at Halyk Insurance, head of SME marketing at Alfa Bank, Marketing Project Manager at BI GROUP, and part of the team that launched Samsung Kazakhstan's online store.",
          "Today he is the founder of Revanite and a startup tracker at Astana Hub, Almaty Hub, Terricon Valley, NURIS and IT Park. He teaches digital marketing and web analytics at AlmaU, leads the Digital program at Qamalladin University and runs workshops at Astana Hub.",
          "His principle: first identify where the business is losing growth and money, then invest. Marketing is an investment that has to pay back and be measurable."],
  "exp_h2": "Career", "skills_h2": "Expertise",
  "names_h2": "Name spelling",
  "names": "Ruslan Khasanov (Russian: Руслан Хасанов; full name Хасанов Руслан Фархадович). LinkedIn uses the spelling Ruslan Khassanov.",
 },
}

FAQ = {
 "ru": [
  ("Что такое Revanite?", T["ru"]["org_desc"]),
  ("Чем Revanite отличается от маркетингового агентства?", "Агентство выполняет отдельные задачи: настраивает рекламу, делает сайт, ведёт соцсети. Revanite работает как стратегический партнёр: определяет приоритеты, управляет маркетингом и подрядчиками, связывает рекламу с продажами и аналитикой. При этом практическая реализация — реклама, сайты, аналитика — тоже входит в работу."),
  ("Как организована работа с клиентом?", "Прозрачно и с постоянной связью: один ответственный контакт, регулярные созвоны, еженедельные отчёты и дашборды по расходам, заявкам, продажам и выручке. Вы всегда знаете, что сделано, сколько потрачено и какой получен результат. Мы не пропадаем после запуска и доводим задачи до конца."),
  ("С кем работает Revanite?", "С малым и средним бизнесом, предпринимателями и растущими компаниями в Казахстане, Кыргызстане и СНГ, а также с начинающими и действующими digital-специалистами и командами, которым нужно обучение. Среди клиентов — Бакай Банк, Глоббинг Казахстан, Yeko Kazakhstan, SAGI, Shanyraq Business Forum, BI GROUP, Geometry, Jintropine, Youtrade, InnMedia."),
  ("Чем Business Tracking отличается от Marketing Management?", "Marketing Management — управление маркетингом компании: стратегия, каналы, бюджеты, подрядчики, аналитика. Business Tracking — работа с предпринимателем над бизнесом в целом: цели, показатели, ограничения, гипотезы и управленческие решения."),
  ("Кто основатель Revanite?", T["ru"]["summary"]),
  ("Как начать работу?", "Напишите в WhatsApp или Telegram: коротко о бизнесе и задаче. Мы обсудим ситуацию и предложим направление и формат работы. Для быстрого старта есть экспресс-диагностика бизнеса — $99 вместо $200. Контакты: +7 701 458 42 42, Telegram @messer66."),
 ],
 "en": [
  ("What is Revanite?", T["en"]["org_desc"]),
  ("How is Revanite different from a marketing agency?", "An agency executes separate tasks: setting up ads, building a website, running social media. Revanite works as a strategic partner: it sets priorities, manages marketing and contractors, and connects advertising with sales and analytics. Hands-on implementation — ads, websites, analytics — is part of the work too."),
  ("How do you work with clients?", "Transparently and in constant contact: one accountable contact, regular calls, weekly reports and dashboards on spend, leads, sales and revenue. You always know what has been done, what has been spent and what it delivered. We do not disappear after launch and see tasks through."),
  ("Who does Revanite work with?", "Small and mid-sized businesses, entrepreneurs and growing companies in Kazakhstan, Kyrgyzstan and the CIS, as well as aspiring and working digital specialists and teams that need training. Clients include Bakai Bank, Globbing Kazakhstan, Yeko Kazakhstan, SAGI, Shanyraq Business Forum, BI GROUP, Geometry, Jintropine, Youtrade and InnMedia."),
  ("How is Business Tracking different from Marketing Management?", "Marketing Management is managing the company's marketing: strategy, channels, budgets, contractors and analytics. Business Tracking is working with the entrepreneur on the business as a whole: goals, metrics, constraints, hypotheses and management decisions."),
  ("Who is the founder of Revanite?", T["en"]["summary"]),
  ("How do I get started?", "Message us on WhatsApp or Telegram with a short note about your business and the challenge. We will discuss the situation and suggest a practice and format. For a quick start there is a business check-up — $99 instead of $200. Contact: +7 701 458 42 42, Telegram @messer66."),
 ],
}

# Экспресс-диагностика: (надзаголовок, заголовок, текст, пункты, кнопка)
DIAG = {
 "ru": ("С чего начать", f"Экспресс-диагностика бизнеса — {PRICE_HTML}",
        "Анализируем ключевые данные компании — продажи, воронку, маркетинг, процессы и экономику. На 60-минутной сессии показываем главное ограничение роста, зоны потерь и приоритетные шаги.",
        ["Доступ к данным в режиме просмотра: продажи, CRM, рекламные кабинеты, отчётность",
         "Сессия 60 минут: ключевое ограничение роста, зоны потерь, приоритеты",
         "Краткий план действий по итогам сессии",
         f"При продолжении работы {PRICE} засчитываются в стоимость проекта"],
        "Записаться на диагностику"),
 "en": ("Where to start", f"Business check-up — {PRICE_HTML}",
        "We analyze your key business data — sales, funnel, marketing, operations and unit economics. In a 60-minute session we show the main constraint on growth, where you are losing money and which steps come first.",
        ["View-only access to your data: sales, CRM, ad accounts, reporting",
         "60-minute session: the key constraint on growth, areas of loss, priorities",
         "A concise action plan after the session",
         f"If we continue, the {PRICE} is credited toward the project"],
        "Book a check-up"),
}

PROCESS = {
 "ru": ("Порядок работы", [
   "Заявка в WhatsApp или Telegram: кратко о бизнесе и задаче",
   "Обсуждение задачи или экспресс-диагностика: анализ данных и определение приоритетов",
   "Предложение: направление, формат, объём работ и стоимость",
   "Работа с прозрачной отчётностью по выручке, заявкам и бюджету — и на связи на каждом этапе"]),
 "en": ("How we work", [
   "Send a request on WhatsApp or Telegram with a short note about your business and the challenge",
   "A discussion or business check-up: data analysis and priorities",
   "Proposal: practice, format, scope and price",
   "Delivery with transparent reporting on revenue, leads and budget — and in touch at every stage"]),
}

SERVICES_PAGE = {
 "ru": ("Четыре самостоятельных направления, объединённых методологией Strategy → Management → Execution → Tracking & Growth.", "Подробнее о направлении"),
 "en": ("Four independent practices united by the Strategy → Management → Execution → Tracking & Growth methodology.", "More about this practice"),
}

CASES_PAGE = {
 "ru": {"intro": "Проекты для бизнеса и трекинг стартапов. По каждому кейсу — задача, исходная ситуация, решение, инструменты и результат.",
        "projects": "Проекты для бизнеса", "tracking": "Трекинг стартапов",
        "h": ("Задача", "Исходная ситуация", "Что сделано", "Инструменты", "Результат"), "changed": "Что изменилось"},
 "en": {"intro": "Client projects and startup tracking. Each case covers the challenge, the starting point, the solution, the tools and the result.",
        "projects": "Client projects", "tracking": "Startup tracking",
        "h": ("Challenge", "Starting point", "What was done", "Tools", "Result"), "changed": "What changed"},
}

META = {
 "ru": {
  "": ("Revanite — Strategic Growth Partner | Маркетинг и рост бизнеса, Алматы",
       "Revanite — стратегический партнёр бизнеса в росте выручки: управление маркетингом, реклама, сайты и аналитика, трекинг и обучение. Алматы."),
  "services": ("Направления работы — Revanite",
               "Четыре направления Revanite: Marketing Management, Digital Growth, Business Tracking и Education. Экспресс-диагностика бизнеса за $99."),
  "marketing-management": ("Marketing Management — управление маркетингом бизнеса | Revanite",
                           "Внешнее управление маркетингом для малого и среднего бизнеса: стратегия, план, бюджеты, управление подрядчиками, аналитика и качество лидов."),
  "digital-growth": ("Digital Growth — реклама, сайты и аналитика | Revanite",
                     "Meta Ads и Google Ads, сайты и лендинги на Tilda, GA4, Google Tag Manager, сквозная аналитика и дашборды как часть системы привлечения клиентов."),
  "business-tracking": ("Business Tracking — трекинг бизнеса | Revanite",
                        "Трекинг для предпринимателей: цели и показатели, поиск ограничений, проверка гипотез, приоритеты и регулярный контроль прогресса."),
  "education": ("Обучение маркетингу и таргетированной рекламе | Revanite",
                "Практическое обучение интернет-маркетингу, Meta Ads, Google Ads и веб-аналитике для специалистов и корпоративные программы для команд."),
  "cases": ("Кейсы и проекты — Revanite",
            "Кейсы Revanite: ROMI 316% для SAGI, лид в 2,4 раза дешевле для Yeko, −45% к стоимости регистрации в Глоббинг, ROAS 234% для Shanyraq."),
  "about": ("Руслан Хасанов — основатель Revanite",
            "Руслан Хасанов — основатель Revanite: экс-CMO re:Kassa, опыт в Home Credit Bank, Halyk Insurance и Alfa Bank, трекер стартапов, преподаватель AlmaU."),
  "teaching": ("Преподавание и выступления — Руслан Хасанов",
               "Руслан Хасанов преподаёт digital-маркетинг в AlmaU, руководит направлением «Диджитал» в Qamalladin University, проводит воркшопы в Astana Hub."),
  "contact": ("Контакты — Revanite",
              "Связаться с Revanite: Telegram @messer66, WhatsApp и телефон +7 701 458 42 42, Instagram, LinkedIn. Алматы, Казахстан."),
 },
 "en": {
  "": ("Revanite — Strategic Growth Partner | Marketing and business growth, Almaty",
       "Revanite is a strategic partner for revenue growth: marketing management, ads, websites and analytics, business tracking and marketing education."),
  "services": ("Services — Revanite",
               "Revanite's four practices: Marketing Management, Digital Growth, Business Tracking and Education. A $99 business check-up to get started."),
  "marketing-management": ("Marketing Management — outsourced marketing leadership | Revanite",
                           "External marketing management for small and mid-sized businesses: strategy, plan, budgets, contractor management, analytics and lead quality."),
  "digital-growth": ("Digital Growth — ads, websites and analytics | Revanite",
                     "Meta Ads and Google Ads, Tilda websites and landing pages, GA4, Google Tag Manager, end-to-end analytics and dashboards as one acquisition system."),
  "business-tracking": ("Business Tracking — tracking for entrepreneurs | Revanite",
                        "Business tracking for entrepreneurs: goals and metrics, finding constraints, testing hypotheses, priorities and regular progress reviews."),
  "education": ("Marketing and paid social training | Revanite",
                "Hands-on training in online marketing, Meta Ads, Google Ads and web analytics for specialists, plus corporate programs for teams."),
  "cases": ("Case studies — Revanite",
            "Revanite case studies: 316% ROMI for SAGI, 2.4× cheaper leads for Yeko, 45% lower cost per sign-up at Globbing, 234% ROAS for Shanyraq."),
  "about": ("Ruslan Khasanov — founder of Revanite",
            "Ruslan Khasanov, founder of Revanite: former CMO at re:Kassa, Home Credit Bank, Halyk Insurance and Alfa Bank, startup tracker, AlmaU lecturer."),
  "teaching": ("Teaching and talks — Ruslan Khasanov",
               "Ruslan Khasanov lectures in digital marketing at AlmaU, leads the Digital programme at Qamalladin University and runs workshops at Astana Hub."),
  "contact": ("Contact — Revanite",
              "Contact Revanite: Telegram @messer66, WhatsApp and phone +7 701 458 42 42, Instagram, LinkedIn. Almaty, Kazakhstan."),
 },
}

# Названия страниц для хлебных крошек и разметки
H1 = {
 "ru": {"services": "Направления работы", "marketing-management": "Marketing Management", "digital-growth": "Digital Growth",
        "business-tracking": "Business Tracking", "education": "Education", "cases": "Кейсы и проекты",
        "about": "Основатель", "teaching": "Преподавание и выступления", "contact": "Контакты"},
 "en": {"services": "Services", "marketing-management": "Marketing Management", "digital-growth": "Digital Growth",
        "business-tracking": "Business Tracking", "education": "Education", "cases": "Case studies",
        "about": "Founder", "teaching": "Teaching and talks", "contact": "Contact"},
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

EXPERIENCE = {
 "ru": [
  ("Revanite", "Основатель · Strategic Growth Partner"),
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
  ("Revanite", "Founder · Strategic Growth Partner"),
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
        "url": BASE + ("/" if lang == "ru" else "/en/"),
        "address": {"@type": "PostalAddress", "addressLocality": "Almaty", "addressCountry": "KZ"},
        "worksFor": [{"@id": BASE + "/#org"}],
        "affiliation": [
            {"@type": "CollegeOrUniversity", "name": "Almaty Management University (AlmaU)", "url": "https://almau.edu.kz"},
            {"@type": "CollegeOrUniversity", "name": "Qamalladin University"},
        ],
        "knowsAbout": KNOWS[lang],
        "knowsLanguage": ["ru", "en"],
        "sameAs": SAME_AS,
    }
    if PHOTO:
        p["image"] = PHOTO_URL
    return p

def org(lang):
    t = T[lang]
    return {
        "@type": "ProfessionalService", "@id": BASE + "/#org",
        "name": "Revanite",
        "alternateName": ["Revanite Strategic Growth Partner"],
        "slogan": t["tagline"],
        "description": t["org_desc"],
        "url": BASE + "/",
        "logo": BASE + "/assets/logo.svg",
        "founder": {"@id": BASE + "/#person"},
        "address": {"@type": "PostalAddress", "addressLocality": "Almaty", "addressCountry": "KZ"},
        "areaServed": ["KZ", "KG", "UZ", "CIS"],
        "telephone": PHONE,
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE, "contactType": "sales",
                         "availableLanguage": ["ru", "en"], "url": WA},
        "knowsAbout": [DIRS[lang][s]["name"] + " — " + DIRS[lang][s]["label"] for s in DIR_SLUGS],
    }

def website(lang):
    return {"@type": "WebSite", "@id": BASE + ROOT + "/#website", "url": url(lang, ""),
            "name": "Revanite", "inLanguage": ["ru", "en"], "publisher": {"@id": BASE + "/#org"}}

def breadcrumbs(lang, slug, title):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": T[lang]["home"], "item": url(lang, "")},
        {"@type": "ListItem", "position": 2, "name": title, "item": url(lang, slug)}]}

def service(lang, s):
    d = DIRS[lang][s]
    return {"@type": "Service", "@id": url(lang, s) + "#service", "name": d["name"] + " — " + d["label"],
            "description": d["short"], "url": url(lang, s), "provider": {"@id": BASE + "/#org"},
            "areaServed": ["KZ", "KG", "CIS"]}

def schema(lang, slug):
    title, desc = META[lang][slug]
    page_type = {"about": "ProfilePage", "cases": "CollectionPage", "contact": "ContactPage"}.get(slug, "WebPage")
    page = {"@type": page_type, "@id": url(lang, slug) + "#webpage", "url": url(lang, slug), "name": title,
            "description": desc, "inLanguage": lang, "isPartOf": {"@id": BASE + ROOT + "/#website"},
            "about": {"@id": BASE + "/#person" if slug in ("about", "teaching") else BASE + "/#org"}, "dateModified": TODAY}
    if slug == "about":
        page["mainEntity"] = {"@id": BASE + "/#person"}
    graph = [org(lang), person(lang), website(lang), page]
    if slug:
        graph.append(breadcrumbs(lang, slug, H1[lang][slug]))
    if slug == "":
        graph.append({"@type": "FAQPage", "@id": url(lang, "") + "#faq", "inLanguage": lang,
                      "mainEntity": [{"@type": "Question", "name": q,
                                      "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang]]})
    if slug in DIR_SLUGS:
        graph.append(service(lang, slug))
    if slug == "services":
        graph += [service(lang, s) for s in DIR_SLUGS]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

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
.hero h1{font-size:clamp(38px,5.4vw,68px);line-height:1.04;letter-spacing:-.03em;background:linear-gradient(180deg,#fff 30%,#AEB9CF);-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:.06em}
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
.footer-title{font-size:clamp(24px,3.2vw,36px);line-height:1.08;margin-bottom:14px;max-width:820px}
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
.system{width:330px;border-radius:20px;border:1px solid transparent;background:linear-gradient(var(--surface2),var(--surface)) padding-box,var(--grad) border-box;padding:24px 24px 18px;box-shadow:0 30px 80px -30px rgba(126,166,255,.45)}
.system-title{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.system ol{list-style:none;counter-reset:sy}
.system li{counter-increment:sy;position:relative;padding:12px 0 12px 42px;border-top:1px solid var(--line)}
.system li:first-child{border-top:0}
.system li::before{content:"0" counter(sy);position:absolute;left:0;top:13px;font-size:13px;font-weight:700;color:var(--accent)}
.system b{display:block;font-weight:700}
.system li span{color:var(--muted);font-size:14px}
.system-edu{margin-top:6px;padding-top:12px;border-top:1px dashed var(--line);color:var(--muted);font-size:13px}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start}
.panel{background:linear-gradient(180deg,var(--surface2),var(--surface));border:1px solid var(--line);border-radius:22px;padding:36px}
.approach{border-color:rgba(126,166,255,.35)}
.issues{list-style:none;margin-top:22px}
.issues li{position:relative;padding:14px 0 14px 30px;border-top:1px solid var(--line)}
.issues li:first-child{border-top:0}
.issues li::before{content:"";position:absolute;left:2px;top:50%;width:14px;height:2px;background:#E2857F}
.check{list-style:none}
.check li{position:relative;padding:7px 0 7px 28px}
.check li::before{content:"";position:absolute;left:2px;top:.95em;width:11px;height:6px;border-left:2px solid var(--accent);border-bottom:2px solid var(--accent);transform:rotate(-45deg)}
.check.cols{columns:2;column-gap:40px}.check.cols li{break-inside:avoid}
.dirs{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.dir{background:linear-gradient(180deg,var(--surface2),var(--surface));border:1px solid var(--line);border-radius:18px;padding:30px;display:flex;flex-direction:column;gap:10px;transition:border-color .25s,transform .25s}
.dir:hover{border-color:rgba(126,166,255,.45);transform:translateY(-3px)}
.dir-top{display:flex;justify-content:space-between;align-items:center;min-height:24px}
.step-n{color:var(--accent);font-weight:700;font-size:14px}
.badge{font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;padding:4px 10px;border-radius:999px;background:var(--grad);color:#0A0C10}
.dir h3{font-size:24px;margin:0}
.dir p{color:var(--muted);font-size:15px}
.dir .dir-label,.dir-label{color:var(--accent);font-weight:600;font-size:15px}
.dir-value,.dir .dir-value{color:var(--text);border-left:2px solid var(--accent);padding-left:12px;font-size:15px}
.dir a{margin-top:auto;padding-top:6px;color:var(--accent);text-decoration:none;font-weight:600;font-size:15px}
.method{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.step{position:relative;background:linear-gradient(180deg,var(--surface2),var(--surface));border:1px solid var(--line);border-radius:18px;padding:24px;display:flex;flex-direction:column;gap:8px}
.step::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;border-radius:18px 18px 0 0;background:var(--grad)}
.step b{font-size:19px}
.step span:last-child{color:var(--muted);font-size:14.5px}
.step:not(:last-child)::after{content:"";position:absolute;right:-17px;top:50%;width:9px;height:9px;border-top:2px solid var(--accent);border-right:2px solid var(--accent);transform:translateY(-50%) rotate(45deg)}
.method-base{margin-top:18px;border:1px dashed rgba(180,140,255,.5);border-radius:14px;padding:16px 20px;color:var(--muted);font-size:15px}
.method-base b{color:var(--accent2)}
.principles{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.principles li{border-top:2px solid var(--accent);padding-top:16px;display:flex;flex-direction:column;gap:8px}
.principles b{font-size:17px}
.principles span{color:var(--muted);font-size:14.5px}
.auds{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.aud{border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:8px}
.aud h3{font-size:17px;margin:0}
.aud p{color:var(--muted);font-size:14.5px;flex:1}
.aud a{color:var(--accent);text-decoration:none;font-size:14px;font-weight:600}
.founder{display:grid;grid-template-columns:auto 1fr;gap:36px;align-items:start}
.founder .portrait{width:200px;height:240px}
.founder h3{font-size:24px;margin:0}
.founder p{color:var(--muted)}
.founder p+p{margin-top:12px}
.founder .role{color:var(--accent);margin:6px 0 16px}
.final{background:radial-gradient(700px 300px at 90% 0,rgba(126,166,255,.16),transparent 60%),linear-gradient(180deg,var(--surface2),var(--surface))}
.final h2{font-size:clamp(30px,4.6vw,52px)}
.edu-split{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:32px}
.edu-card{display:flex;flex-direction:column;gap:8px;text-decoration:none;border-radius:18px;padding:26px;border:1px solid var(--line)}
.edu-card b{font-size:19px}
.edu-card span:last-child{color:var(--muted);font-size:15px}
.edu-card .tag{color:var(--accent);font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}
.edu-card.a,.panel.edu.a{border-color:transparent;background:linear-gradient(var(--surface2),var(--surface)) padding-box,var(--grad) border-box}
.edu-card.b .tag,.panel.edu.b .eyebrow{color:var(--accent2)}
.edu-card.b,.panel.edu.b{border-color:rgba(180,140,255,.35);background:var(--bg)}
.panel.edu.b .check li::before{border-color:var(--accent2)}
.panel h3{margin-bottom:10px}
.mnav{display:none}
.mnav summary{cursor:pointer;list-style:none;border:1px solid var(--line);border-radius:8px;padding:4px 12px;font-size:14px;font-weight:600}
.mnav summary::-webkit-details-marker{display:none}
.mnav[open] summary{border-color:var(--accent)}
.mnav-list{position:absolute;left:0;right:0;top:64px;background:#0A0C10;border-bottom:1px solid var(--line);box-shadow:0 24px 40px rgba(0,0,0,.6);padding:8px 20px 16px;display:flex;flex-direction:column}
.mnav-list a{padding:12px 0;border-top:1px solid var(--line);text-decoration:none;color:var(--muted);font-size:16px}
.mnav-list a:first-child{border-top:0}
.mnav-list a[aria-current]{color:var(--text)}
.foot-nav{list-style:none;display:flex;flex-wrap:wrap;gap:8px 22px;margin-bottom:28px}
.foot-nav a{color:var(--muted);text-decoration:none;font-size:15px}
.foot-nav a:hover{color:var(--text)}
@media (max-width:1000px){
 .hero-grid{grid-template-columns:1fr}
 .system{width:100%;max-width:460px}
 .method{grid-template-columns:repeat(2,1fr)}
 .principles{grid-template-columns:repeat(2,1fr)}
 .step:nth-child(2)::after{display:none}
}
@media (max-width:760px){
 body{font-size:16px}
 .bar{gap:8px}.brand span{display:none}
 nav{display:none}
 .mnav{display:block;margin-left:auto}
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
 .system{max-width:none}
 .split,.founder,.edu-split{grid-template-columns:1fr;gap:24px}
 .dirs{grid-template-columns:1fr}
 .principles{grid-template-columns:1fr;gap:22px}
 .method{grid-template-columns:1fr;gap:28px}
 .step:not(:last-child)::after,.step:nth-child(2)::after{display:block;right:auto;left:30px;top:auto;bottom:-20px;transform:rotate(135deg)}
 .panel{padding:24px}
 .check.cols{columns:1}
 .founder .portrait{width:112px;height:132px}
}
"""

# ---------------------------------------------------------------- HTML
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

def crumbs(lang, slug):
    return f'<p class="crumbs"><a href="{path(lang,"")}">{T[lang]["home"]}</a> / {H1[lang][slug]}</p>'

def checklist(items):
    return '<ul class="check">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def cta_row(lang, label=None, href=None, second=True):
    t = T[lang]
    out = f'<div class="cta"><a class="btn" href="{href or WA}" rel="noopener" target="_blank">{label or t["discuss"]}</a>'
    if second:
        out += f'<a class="btn ghost" href="{TG}" rel="me noopener" target="_blank">Telegram</a>'
    return out + "</div>"

def case_article(lang, n, case):
    title, tools, task, situation, done, result = case
    h_task, h_sit, h_done, h_tools, h_res = CASES_PAGE[lang]["h"]
    sit = f"<h3>{h_sit}</h3><p>{situation}</p>" if situation else ""
    return (f'<article class="case" id="case-{n}"><h2>{title}</h2>'
            f'<h3>{h_task}</h3><p>{task}</p>{sit}<h3>{h_done}</h3><ul>{"".join(f"<li>{d}</li>" for d in done)}</ul>'
            f'<h3>{h_tools}</h3><p>{tools}</p><h3>{h_res}</h3><p class="result">{result}</p></article>')

def track_article(lang, n, tr):
    m, ml, title, tag, points = tr
    return (f'<article class="case" id="track-{n}"><p class="metric-row"><b class="metric">{m}</b><span class="metric-label">{ml}</span></p>'
            f'<h2>{title}</h2><span class="tag">{tag}</span><h3>{CASES_PAGE[lang]["changed"]}</h3>'
            f'<ul>{"".join(f"<li>{x}</li>" for x in points)}</ul></article>')

def case_card(lang, n):
    title, tools, task, situation, done, result = CASES[lang][n - 1]
    return (f'<article class="project"><span class="tag">{tools}</span><h3>{title}</h3><p>{result}</p>'
            f'<a href="{path(lang,"cases")}#case-{n}">{"Открыть кейс" if lang == "ru" else "Open case"} →</a></article>')

def principles(lang):
    title, items = PRINCIPLES[lang]
    cards = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in items)
    return f'<section id="principles"><h2>{title}</h2><ul class="principles">{cards}</ul></section>'

def method_diagram(lang, compact=False):
    steps = "".join(f'<li class="step"><span class="step-n">0{i}</span><b>{name}</b><span>{text}</span></li>'
                    for i, (name, text) in enumerate(METHOD[lang], 1))
    en, et = METHOD_EDU[lang]
    return f'<ol class="method">{steps}</ol><p class="method-base"><b>{en}</b> — {et}</p>'

def diag_section(lang, sid="diagnostics"):
    eyebrow, title, text, items, btn = DIAG[lang]
    return (f'<section id="{sid}"><div class="panel"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2><p class="answer">{text}</p>'
            f'{checklist(items)}{cta_row(lang, btn, second=False)}</div></section>')

def dir_card(lang, s, n):
    d = DIRS[lang][s]
    badge = f'<span class="badge">{d["badge"]}</span>' if d["badge"] else ""
    return (f'<article class="dir"><div class="dir-top"><span class="step-n">0{n}</span>{badge}</div>'
            f'<h3>{d["name"]}</h3><p class="dir-label">{d["label"]}</p><p>{d["short"]}</p>'
            f'<p class="dir-value">{d["value"]}</p><a href="{path(lang, s)}">{T[lang]["details"]} →</a></article>')

def founder_block(lang, full_link=True):
    f = FOUNDER[lang]
    ps = "".join(f'<p>{p}</p>' for p in f["short"])
    chips = "".join(f"<li>{c}</li>" for c in f["chips"])
    link = f'<p class="card-links"><a href="{path(lang,"about")}">{HOME[lang]["founder_more"]} →</a><a href="{LI}" rel="me noopener" target="_blank">LinkedIn</a></p>' if full_link else ""
    return (f'<div class="founder">{portrait(lang)}<div><h3>{T[lang]["name"]}</h3><p class="role">{f["role"]}</p>{ps}'
            f'<ul class="chips" style="margin-top:18px">{chips}</ul>{link}</div></div>')

def body_home(lang):
    h = HOME[lang]
    t = T[lang]
    system = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in h["system_steps"])
    problems = "".join(f"<li>{p}</li>" for p in h["problems"])
    dirs = "".join(dir_card(lang, s, i) for i, s in enumerate(DIR_SLUGS, 1))
    aud = "".join(f'<article class="aud"><h3>{a}</h3><p>{b}</p><a href="{path(lang, l.split("#")[0])}{"#" + l.split("#")[1] if "#" in l else ""}">'
                  f'{DIRS[lang][l.split("#")[0]]["name"]} →</a></article>' for a, b, l in AUDIENCES[lang])
    stats = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in STATS[lang])
    cases = "".join(case_card(lang, n) for n in range(1, len(CASES[lang]) + 1))
    clients = " · ".join(CLIENTS[lang])
    faq = "".join(f'<details class="qa"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ[lang])
    return f"""
<section class="hero"><div class="hero-grid"><div>
<p class="eyebrow">{h["eyebrow"]}</p>
<h1 lang="en">{h["h1"]}</h1>
<p class="lead">{h["lead"]}</p>
<div class="cta"><a class="btn" href="{WA}" rel="noopener" target="_blank">{t["discuss"]}</a><a class="btn ghost" href="#directions">{h["cta2"]}</a></div>
</div><div class="system" aria-hidden="true"><p class="system-title">{h["system_title"]}</p><ol>{system}</ol><p class="system-edu">{h["system_edu"]}</p></div></div></section>
<section id="problem"><div class="split"><div><h2>{h["problem_h2"]}</h2><p class="answer">{h["problem_lead"]}</p><ul class="issues">{problems}</ul></div>
<div class="panel approach"><p class="eyebrow">Revanite</p><h3>{h["approach_h3"]}</h3><p>{h["approach"]}</p></div></div></section>
<section id="directions">{head(h["dirs_h2"], path(lang,"services"), "Все направления" if lang == "ru" else "All services")}<p class="answer" style="margin:-8px 0 28px">{h["dirs_lead"]}</p><div class="dirs">{dirs}</div></section>
<section id="method"><h2>{h["method_h2"]}</h2><p class="answer" style="margin-bottom:32px">{h["method_lead"]}</p>{method_diagram(lang)}</section>
{principles(lang)}
<section id="audience"><h2>{h["aud_h2"]}</h2><div class="auds">{aud}</div></section>
<section id="cases">{head(h["cases_h2"], path(lang,"cases"), h["cases_all"])}<ul class="stats">{stats}</ul>
<div class="projects two" style="margin-top:18px">{cases}</div><p class="note"><b>{h["clients"]}:</b> {clients}</p></section>
<section id="founder"><h2>{h["founder_h2"]}</h2>{founder_block(lang)}</section>
<section id="faq">{head(h["faq_h2"])}{faq}</section>
<section id="contact-cta"><div class="panel final"><h2 lang="en">{h["final_h2"]}</h2><p class="answer">{h["final_text"]}</p>{cta_row(lang)}</div></section>"""

def body_services(lang):
    t = T[lang]
    lead, more = SERVICES_PAGE[lang]
    p_title, p_steps = PROCESS[lang]
    out = [f'<section class="page">{crumbs(lang,"services")}<h1>{H1[lang]["services"]}</h1><p class="lead">{lead}</p></section>']
    for i, s in enumerate(DIR_SLUGS, 1):
        d = DIRS[lang][s]
        badge = f' · {d["badge"]}' if d["badge"] else ""
        out.append(f'<section id="{s}"><p class="eyebrow">0{i} · {d["name"]}{badge}</p><h2>{d["label"]}</h2><p class="answer">{d["short"]}</p>'
                   f'<p class="dir-value" style="margin-top:14px">{d["value"]}</p><p class="card-links"><a href="{path(lang, s)}">{more} →</a></p></section>')
    out.append(f'<section id="method"><h2>{HOME[lang]["method_h2"]}</h2>{method_diagram(lang)}</section>')
    out.append(principles(lang))
    out.append(diag_section(lang))
    out.append(f'<section id="process"><h2>{p_title}</h2><ol class="steps">{"".join(f"<li><span>{x}</span></li>" for x in p_steps)}</ol>{cta_row(lang)}</section>')
    return "".join(out)

def body_direction(lang, slug):
    d = DIRS[lang][slug]
    t = T[lang]
    ru = lang == "ru"
    badge = f' · {d["badge"]}' if d["badge"] else ""
    out = [f'<section class="page">{crumbs(lang, slug)}<p class="eyebrow">{d["name"]}{badge}</p><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>{cta_row(lang)}</section>']
    blocks = d["blocks"]
    if len(blocks) == 1:
        out.append(f'<section><h2>{blocks[0][0]}</h2>{checklist(blocks[0][1])}</section>')
    else:
        cards = "".join(f'<article class="card"><h3>{h}</h3>{checklist(items)}</article>' for h, items in blocks)
        out.append(f'<section><h2>{"Что входит" if ru else "What we do"}</h2><div class="cards">{cards}</div></section>')
    if "for" in d:
        out.append(f'<section><div class="split"><div><h2>{d["for_h2"]}</h2>{checklist(d["for"])}</div>'
                   f'<div class="panel approach"><p class="eyebrow">{d["result_h2"]}</p><p class="answer">{d["result"]}</p></div></div></section>')
    if "why" in d:
        out.append(f'<section><h2>{d["why_h2"]}</h2><p class="answer">{d["why"]}</p></section>')
    fmt = f'<p class="note"><b>{"Формат" if ru else "Format"}:</b> {d["format"]}</p>'
    extra = f'<p class="note">{d["exp"]}</p>' if "exp" in d else ""
    note = f'<p class="note">{d["note"]}</p>' if "note" in d else ""
    out.append(f'<section style="padding-top:0">{fmt}{extra}{note}</section>')
    if d.get("diag"):
        out.append(diag_section(lang))
    if d["cases"]:
        cards = "".join(case_card(lang, n + 1) for n in d["cases"])
        out.append(f'<section>{head("Кейсы направления" if ru else "Related case studies", path(lang,"cases"), HOME[lang]["cases_all"])}<div class="projects">{cards}</div></section>')
    if slug == "business-tracking":
        out.append(f'<section><h2>{CASES_PAGE[lang]["tracking"]}</h2>' + "".join(track_article(lang, n, tr) for n, tr in enumerate(TRACK[lang], 1)) + "</section>")
    out.append(f'<section><div class="panel final"><h2 lang="en">{HOME[lang]["final_h2"]}</h2><p class="answer">{HOME[lang]["final_text"]}</p>{cta_row(lang)}</div></section>')
    return "".join(out)

def body_education(lang):
    d = DIRS[lang]["education"]
    e = EDU[lang]
    ru = lang == "ru"
    split = (f'<div class="edu-split"><a class="edu-card a" href="#specialists"><span class="tag">{e["a_tag"]}</span><b>{e["a_h2"]}</b><span>{e["a_intro"]}</span></a>'
             f'<a class="edu-card b" href="#corporate"><span class="tag">{e["b_tag"]}</span><b>{e["b_h2"]}</b><span>{e["b_intro"]}</span></a></div>')
    a_prog = "".join(f"<li>{p}</li>" for p in e["a_prog"])
    b_prog = "".join(f"<li>{p}</li>" for p in e["b_prog"])
    a_fmt = "".join(f"<li>{p}</li>" for p in e["a_fmt"])
    return f"""
<section class="page">{crumbs(lang,"education")}<p class="eyebrow">{d["name"]}</p><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>{split}</section>
<section id="specialists"><div class="panel edu a"><p class="eyebrow">{e["a_tag"]}</p><h2>{e["a_h2"]}</h2><p class="answer">{e["a_intro"]}</p>
<div class="split" style="margin-top:28px"><div><h3>{e["a_prog_h"]}</h3><ul class="check">{a_prog}</ul></div><div><h3>{e["a_fmt_h"]}</h3><ul class="check">{a_fmt}</ul>
<p class="note">{e["a_focus"]}</p></div></div>{cta_row(lang, e["a_cta"], second=False)}</div></section>
<section id="corporate"><div class="panel edu b"><p class="eyebrow">{e["b_tag"]}</p><h2>{e["b_h2"]}</h2><p class="answer">{e["b_intro"]}</p>
<h3 style="margin-top:28px">{e["b_prog_h"]}</h3><ul class="check cols">{b_prog}</ul><p class="note">{e["b_fmt"]}</p>{cta_row(lang, e["b_cta"], second=False)}</div></section>
<section style="padding-top:0"><p class="note">{e["terms"]}</p></section>
<section><h2>{e["exp_h2"]}</h2><p class="answer">{e["exp"]}</p><p class="card-links"><a href="{path(lang,"teaching")}">{e["exp_link"]} →</a></p></section>"""

def body_cases(lang):
    c = CASES_PAGE[lang]
    stats = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in STATS[lang])
    out = [f'<section class="page">{crumbs(lang,"cases")}<h1>{H1[lang]["cases"]}</h1><p class="lead">{c["intro"]}</p></section>',
           f'<section style="padding-top:0"><ul class="stats">{stats}</ul></section>',
           f'<section><h2>{c["projects"]}</h2>']
    out += [case_article(lang, n, case) for n, case in enumerate(CASES[lang], 1)]
    out.append(f'</section><section id="tracking"><h2>{c["tracking"]}</h2>')
    out += [track_article(lang, n, tr) for n, tr in enumerate(TRACK[lang], 1)]
    out.append(f'<p class="note">{CASES_NOTE[lang]}</p></section>')
    return "".join(out)

def body_about(lang):
    f = FOUNDER[lang]
    exp = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in EXPERIENCE[lang])
    bio = "".join(f"<p>{p}</p>" for p in f["bio"])
    chips = "".join(f"<li>{k}</li>" for k in KNOWS[lang])
    return f"""
<section class="page">{crumbs(lang,"about")}<h1>{f["h1"]}</h1><p class="lead">{f["lead"]}</p></section>
<section style="padding-top:0">{founder_block(lang, full_link=False)}</section>
<section><div class="split"><div><h2>{f["role_h2"]}</h2>{checklist(f["roles"])}</div><div><h2>{f["bio_h2"]}</h2>{bio}</div></div></section>
<section><h2>{f["exp_h2"]}</h2><ul class="exp">{exp}</ul></section>
<section><h2>{f["skills_h2"]}</h2><ul class="chips">{chips}</ul></section>
<section><h2>{f["names_h2"]}</h2><p>{f["names"]}</p></section>"""

def body_contact(lang):
    ru = lang == "ru"
    lead = ("Расскажите о задаче в Telegram или WhatsApp: коротко о бизнесе и цели. Мы ответим, предложим направление и формат работы и останемся на связи на всех этапах."
            if ru else "Tell us about your challenge on Telegram or WhatsApp: a few lines about your business and goal. We will reply with a suggested practice and format, and stay in touch at every stage.")
    note = ("Алматы, Казахстан. Работаем с бизнесом в Казахстане, Кыргызстане, СНГ и онлайн."
            if ru else "Almaty, Kazakhstan. Working with businesses in Kazakhstan, Kyrgyzstan, the CIS and online.")
    return f"""
<section class="page">{crumbs(lang,"contact")}<h1>{H1[lang]["contact"]}</h1><p class="lead">{lead}</p></section>
<section>{social_list(lang)}<p class="note">{note}</p></section>"""

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

BODIES = {"": body_home, "services": body_services, "education": body_education, "cases": body_cases,
          "about": body_about, "teaching": body_teaching, "contact": body_contact}
for _s in ("marketing-management", "digital-growth", "business-tracking"):
    BODIES[_s] = (lambda s: lambda lang: body_direction(lang, s))(_s)

def render(lang, slug):
    t = T[lang]
    title, desc = META[lang][slug]
    other = "en" if lang == "ru" else "ru"
    cur = ' aria-current="page"'
    active = "services" if slug in DIR_SLUGS[:3] else slug
    nav = "".join(
        f'<a href="{path(lang,s)}"{cur if s == active else ""}{"" if s else ' class="nav-home"'}>{t["nav"][s]}</a>'
        for s in NAV)
    # пункт меню на личный сайт основателя
    nav += f'<a href="{"/" if lang == "ru" else "/en/"}">{"Личный сайт" if lang == "ru" else "Personal site"}</a>'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Revanite">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url(lang,slug)}">
<link rel="alternate" hreflang="ru" href="{url("ru",slug)}">
<link rel="alternate" hreflang="en" href="{url("en",slug)}">
<link rel="alternate" hreflang="x-default" href="{url("ru",slug)}">
<link rel="alternate" type="text/plain" title="llms.txt" href="/studio/llms.txt">
<meta property="og:type" content="{"profile" if slug == "about" else "website"}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang,slug)}">
<meta property="og:locale" content="{"ru_RU" if lang=="ru" else "en_US"}">
<meta property="og:site_name" content="Revanite">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
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
<nav aria-label="{"Основное меню" if lang=="ru" else "Main menu"}">{nav}</nav><details class="mnav"><summary>{"Меню" if lang=="ru" else "Menu"}</summary><div class="mnav-list">{nav}</div></details><a class="lang" href="{path(other,slug)}" hreflang="{other}" lang="{other}" title="{t["switch"][1]}">{t["switch"][0]}</a>
</div></header>
<main class="wrap">{BODIES[slug](lang)}</main>
<footer id="contact"><div class="wrap">
<h2 class="footer-title">{t["footer_title"]}</h2>
<p class="footer-sub">{t["footer_sub"]}</p>
<ul class="foot-nav">{"".join(f'<li><a href="{path(lang, s)}">{DIRS[lang][s]["name"]}</a></li>' for s in DIR_SLUGS)}<li><a href="{path(lang,"cases")}">{t["nav"]["cases"]}</a></li><li><a href="{path(lang,"about")}">{t["nav"]["about"]}</a></li></ul>
{social_list(lang)}
<p class="copy">© {datetime.date.today().year} {t["copy"]}</p>
</div></footer>
</body>
</html>
"""

# ---------------------------------------------------------------- EXTRA FILES
def llms_txt():
    ru, en = T["ru"], T["en"]
    lines = [
        "# Revanite — Strategic Growth Partner",
        "",
        f"> {ru['org_desc']}",
        "",
        f"> {en['org_desc']}",
        "",
        "## Ключевые факты / Key facts",
        "- Revanite — стратегический партнёр малого и среднего бизнеса в маркетинге, digital-развитии и привлечении клиентов; Алматы, Казахстан",
        "- Ключевая идея: не просто выполнять маркетинговые задачи, а думать вместе с бизнесом, определять приоритеты и управлять развитием",
        "- Методология: Strategy → Management → Execution → Tracking & Growth; Education дополняет систему",
        "- Принципы работы: рост выручки как главная метрика; прозрачность процессов (регулярные отчёты и дашборды по расходам, заявкам, продажам); всегда на связи (один ответственный контакт, регулярные созвоны); ответственность до результата",
        "- Marketing Management: внешнее управление маркетингом — стратегия, план, бюджеты, постановка задач специалистам и подрядчикам, контроль, аналитика, качество лидов",
        "- Digital Growth: Meta Ads, Google Ads, сайты и лендинги (Tilda, AI-инструменты), GA4, Google Tag Manager, интеграция с CRM, отчёты и дашборды",
        "- Business Tracking: трекинг для предпринимателей — цели и показатели, ограничения, гипотезы, приоритеты, регулярный контроль прогресса",
        "- Education: обучение начинающих и действующих маркетологов и таргетологов; корпоративное обучение команд",
        "- Экспресс-диагностика бизнеса: $99 вместо $200, засчитывается при продолжении работы",
        f"- Основатель: {ru['summary']}",
        "- Опыт основателя: re:Kassa (CMO, до 2026), Home Credit Bank (руководитель digital-маркетинга), Halyk Insurance (директор по продукту), Alfa Bank (руководитель маркетинга сегмента малого бизнеса), BI GROUP (менеджер маркетинговых проектов), Samsung Kazakhstan (запуск онлайн-магазина)",
        "- Клиенты: " + ", ".join(CLIENTS["ru"]),
        "- Кейсы: SAGI — ROMI 316%; Yeko Kazakhstan — доля квалифицированных лидов с 30% до 70%, стоимость лида ниже в 2,4 раза; Глоббинг Казахстан — +60% новых регистраций, стоимость регистрации ниже на 45%; Shanyraq Business Forum — 1 600+ заявок и обращений за первый запуск, ROAS 234%; карта рассрочки Тумар (Бакай Банк) — стабильный ежемесячный поток новых клиентов и программа активации карт; BI GROUP и Geometry — расчёт CAC с нуля и оптимизация рекламы по нему; Jintropine — сквозная аналитика Meta Ads и amoCRM",
        "- Трекинг: Youtrade — рост выручки в 1,6 раза, перестройка операционных процессов; InnMedia — выход на рынок Казахстана, первые 3 контракта; онлайн-школа — смена приоритетных рынков, партнёрский канал около 30% выручки",
        "",
        "## Страницы / Pages",
    ]
    for s in PAGES:
        lines.append(f"- [{META['ru'][s][0]}]({url('ru', s)}): {META['ru'][s][1]}")
    for s in PAGES:
        lines.append(f"- [{META['en'][s][0]}]({url('en', s)}): {META['en'][s][1]}")
    lines += ["", "## Профили / Profiles", f"- Instagram: {IG}", f"- LinkedIn: {LI}", f"- Telegram: {TG}", "", "## Контакты / Contact", f"- WhatsApp / телефон: {PHONE_H} ({WA})", "- Telegram: @messer66", ""]
    return "\n".join(lines)

def sitemap():
    items = []
    for lang in ("ru", "en"):
        for s in PAGES:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l,s)}"/>' for l in ("ru", "en"))
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("ru",s)}"/>'
            items.append(f"<url><loc>{url(lang,s)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(items) + "\n</urlset>\n")

def write(p, content):
    full = os.path.join(OUT, p.lstrip("/"))
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # robots.txt, 404, логотип и фото пишет корневой build.py; здесь только страницы студии
    shutil.rmtree(os.path.join(OUT, ROOT.lstrip("/")), ignore_errors=True)
    for lang in ("ru", "en"):
        for s in PAGES:
            write(path(lang, s) + "index.html", render(lang, s))
    write(ROOT + "/llms.txt", llms_txt())
    write(ROOT + "/sitemap.xml", sitemap())
    print("built", OUT + ROOT)
