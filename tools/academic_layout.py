"""Compact academic profile layout; independent HTML implementation."""
from html import escape

BASE = "https://wsxhjnb1.github.io"
PAPER = BASE + "/Beyond-KV-Cache/paper/Beyond.pdf"
BEYOND = "https://github.com/wsxhjnb1/Beyond-KV-Cache"
ORBIT = "https://github.com/wsxhjnb1/OrbitCall"
EMAIL = "yuhaoxie1999@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/yuhao-xie/"

UI = {
    "en": {
        "role": "Ph.D. Student", "department": "Computer Engineering",
        "university": "University of Central Florida", "focus": "LLM inference · GPU systems",
        "about": "About me", "publications": "Publications", "projects": "Projects",
        "background": "Education & experience", "service": "Service & honors", "contact": "Contact",
        "intro": "I am a Ph.D. student in Computer Engineering at the University of Central Florida. My research focuses on efficient large language model inference, especially KV-cache quantization and GPU kernel optimization.",
        "intro_second": "I work across methods and systems: learning compact KV representations, developing fused attention kernels, and integrating scoring optimizations into vLLM. Previously, I worked on LLM inference at Hithink RoyalFlush.",
        "interests_label": "Research interests",
        "interests": ["KV-cache quantization", "CUDA & fused attention", "LLM inference systems"],
        "cv_en": "CV · English", "cv_zh": "简历 · 中文",
        "paper": "Paper", "code": "Code", "project": "Project page", "results": "Results",
        "full_cv": "More in CV", "preview_alt": "First page of the Beyond paper",
        "venue": "EMNLP 2026, main conference", "service_reviewer": "Reviewer, ICLR 2027",
        "service_fellowship": "ORCGS Doctoral Fellowship, UCF (2023–2027)",
        "contact_text": "For research conversations and opportunities in efficient LLM inference and GPU systems, please email me.",
        "source": "Source", "resume_repository": "Résumé repository",
    },
    "zh": {
        "role": "博士研究生", "department": "计算机工程",
        "university": "中佛罗里达大学", "focus": "大模型推理 · GPU 系统",
        "about": "关于我", "publications": "学术论文", "projects": "系统项目",
        "background": "教育与工作经历", "service": "学术服务与荣誉", "contact": "联系",
        "intro": "我是中佛罗里达大学计算机工程博士研究生，研究方向为大模型高效推理，重点关注 KV Cache 量化与 GPU 内核优化。",
        "intro_second": "我的工作覆盖方法与系统：学习紧凑的 KV 表示、开发融合注意力内核，并将评分优化集成到 vLLM。此前曾在同花顺参与大模型推理研究与工程开发。",
        "interests_label": "研究兴趣",
        "interests": ["KV Cache 量化", "CUDA 与融合注意力", "大模型推理系统"],
        "cv_en": "CV · English", "cv_zh": "简历 · 中文",
        "paper": "论文", "code": "代码", "project": "项目主页", "results": "实验报告",
        "full_cv": "简历详情", "preview_alt": "Beyond 论文首页",
        "venue": "EMNLP 2026，主会", "service_reviewer": "ICLR 2027 审稿人",
        "service_fellowship": "ORCGS 博士奖学金，中佛罗里达大学（2023–2027）",
        "contact_text": "欢迎交流大模型高效推理与 GPU 系统研究，以及相关合作和工作机会。请通过邮件联系。",
        "source": "源码", "resume_repository": "简历仓库",
    },
}


def link(url, label, css=""):
    return f'<a href="{escape(url, quote=True)}" class="{css}">{escape(label)}</a>'


def timeline(items):
    return ''.join(
        f'<div class="timeline-entry"><span class="timeline-date">{escape(date)}</span>'
        f'<div class="timeline-content"><h4>{escape(title)}</h4><p>{escape(text)}</p></div></div>'
        for date, title, text in items)


def render(key, c):
    u = UI[key]
    prefix = "../" if key == "zh" else ""
    canonical = BASE + ("/zh/" if key == "zh" else "/")
    cv_en = prefix + "assets/resume/yuhao_xie_resume_en.pdf"
    cv_zh = prefix + "assets/resume/yuhao_xie_resume_zh.pdf"
    primary_cv = cv_zh if key == "zh" else cv_en
    nav = ''.join(link('#' + slug, u[label]) for slug, label in (
        ('about', 'about'), ('research', 'publications'), ('projects', 'projects'),
        ('background', 'background'), ('contact', 'contact')))
    en_current = ' aria-current="page"' if key == 'en' else ''
    zh_current = ' aria-current="page"' if key == 'zh' else ''
    interests = ''.join(f'<li>{escape(item)}</li>' for item in u['interests'])
    teaching = ''.join(
        f'<div class="teaching-group"><h3>{escape(c[role])}</h3><ul>'
        + ''.join(f'<li>{escape(item)}</li>' for item in c[role + '_items'])
        + '</ul></div>' for role in ('instructor', 'assistant'))
    result_stop = '。' if key == 'zh' else '.'
    return f'''<!doctype html>
<html lang="{c['lang']}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(c['title'])}</title><meta name="description" content="{escape(c['description'], quote=True)}">
  <meta name="theme-color" content="#1d4ed8"><meta name="color-scheme" content="light">
  <link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="zh-CN" href="{BASE}/zh/"><link rel="alternate" hreflang="x-default" href="{BASE}/">
  <meta property="og:type" content="website"><meta property="og:title" content="{escape(c['title'], quote=True)}"><meta property="og:description" content="{escape(c['description'], quote=True)}"><meta property="og:url" content="{canonical}">
  <link rel="icon" href="{prefix}assets/favicon.svg?v=academic-20261105" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/styles.css?v=portrait-20261105">
</head>
<body>
<a class="skip-link" href="#main">{c['skip']}</a>
<div class="page-shell">
  <aside class="profile-sidebar" aria-label="{'个人信息' if key == 'zh' else 'Profile'}">
    <img class="profile-photo" src="{prefix}assets/yuhao-xie.jpg" alt="{'谢雨豪的照片' if key == 'zh' else 'Portrait of Yuhao Xie'}" width="3652" height="5489" fetchpriority="high" decoding="async">
    <h1 class="profile-name">{c['name']}</h1><p class="profile-native">{c['native']}</p>
    <p class="profile-role">{u['role']}</p><p class="profile-affiliation">{u['department']}<br>{u['university']}</p>
    <p class="profile-focus">{u['focus']}</p>
    <div class="profile-links">{link('mailto:' + EMAIL, EMAIL)}{link('https://github.com/wsxhjnb1', 'GitHub')}{link(LINKEDIN, 'LinkedIn')}</div>
    <div class="cv-links">{link(primary_cv, u['cv_zh'] if key == 'zh' else u['cv_en'], 'blue-button')}{link(cv_en if key == 'zh' else cv_zh, u['cv_en'] if key == 'zh' else u['cv_zh'], 'outline-button')}</div>
    <nav class="profile-nav" aria-label="{'导航' if key == 'zh' else 'Navigation'}">{nav}</nav>
    <p class="profile-note">{link('https://github.com/wsxhjnb1/resume', u['resume_repository'])}</p>
  </aside>
  <main class="content-column" id="main">
    <div class="site-tools"><div class="language-switch" aria-label="Language"><a href="{prefix or './'}" lang="en"{en_current}>EN</a><span aria-hidden="true">/</span><a href="{'./' if key == 'zh' else 'zh/'}" lang="zh-CN"{zh_current}>中文</a></div></div>
    <section class="cv-section section-intro" id="about"><h2>{u['about']}</h2>
      <p class="intro-lead">{u['intro']}</p><p>{u['intro_second']}</p>
      <p class="interests-label">{u['interests_label']}</p><ul class="interest-list">{interests}</ul>
    </section>
    <section class="cv-section" id="research"><h2>{u['publications']}</h2>
      <article class="paper-entry">
        <a class="paper-cover-link" href="{PAPER}"><img class="paper-cover" src="{prefix}assets/beyond-paper-preview.png" alt="{u['preview_alt']}" width="495" height="700"></a>
        <div class="paper-content"><h3 class="paper-title">{link(PAPER, 'Beyond: Better-than-Full-Precision KV Caches via Learnable Non-Uniform Quantization as Implicit Regularization')}</h3>
          <p class="paper-authors"><strong>Yuhao Xie</strong>, Mingjie Lin</p><p class="paper-venue">{u['venue']} · {c['first_author']}</p>
          <p class="paper-summary">{c['pub_summary']}</p>
          <div class="resource-links">{link(PAPER,u['paper'])}{link(BEYOND,u['code'])}{link(BASE+'/Beyond-KV-Cache/',u['project'])}</div>
        </div>
      </article>
    </section>
    <section class="cv-section" id="projects"><h2>{u['projects']}</h2>
      <article class="project-entry"><div class="project-heading"><h3>{link(ORBIT,c['orbit_title'])}</h3><span class="project-category">{c['orbit_tag']}</span></div>
        <p class="project-desc">{c['orbit_summary']}</p><p class="project-result"><strong>{c['orbit_result']}{result_stop}</strong> {c['orbit_scope']}</p>
        <div class="resource-links">{link(ORBIT,u['code'])}{link(ORBIT+'/blob/main/evidence/vllm_agent/RESULTS.md',u['results'])}</div>
      </article>
      <article class="project-entry"><div class="project-heading"><h3>{c['kernel_title']}</h3><span class="project-category">{c['kernel_tag']}</span></div>
        <p class="project-desc">{c['kernel_summary']}</p><p class="project-result"><strong>{c['kernel_result']}{result_stop}</strong> {c['kernel_scope']}</p>
        <div class="resource-links">{link(primary_cv,u['full_cv'])}</div>
      </article>
    </section>
    <section class="cv-section" id="background"><h2>{u['background']}</h2>
      <div class="background-grid"><div><h3>{c['education']}</h3>{timeline(c['education_items'])}</div><div><h3>{c['experience']}</h3>{timeline(c['experience_items'])}</div></div>
    </section>
    <section class="cv-section" id="service"><h2>{u['service']}</h2>
      <ul class="service-list"><li><strong>{u['service_reviewer']}</strong></li><li>{u['service_fellowship']}</li></ul>
      <details class="teaching-details"><summary>{c['teaching']}</summary><div class="teaching-columns">{teaching}</div></details>
    </section>
    <section class="cv-section contact-section" id="contact"><h2>{u['contact']}</h2><p>{u['contact_text']}</p><p>{link('mailto:'+EMAIL,EMAIL)}</p></section>
    <footer class="site-footer">© 2026 Yuhao Xie · 谢雨豪 <span aria-hidden="true">/</span> {link('https://github.com/wsxhjnb1/wsxhjnb1.github.io',u['source'])}</footer>
  </main>
</div>
</body></html>'''
