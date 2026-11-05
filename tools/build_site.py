"""Generate the English and Chinese static pages; no third-party packages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://wsxhjnb1.github.io"
PAPER = "https://wsxhjnb1.github.io/Beyond-KV-Cache/paper/Beyond.pdf"
BEYOND = "https://github.com/wsxhjnb1/Beyond-KV-Cache"
ORBIT = "https://github.com/wsxhjnb1/OrbitCall"
EMAIL = "yuhaoxie1999@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/yuhao-xie/"

COPY = {
    "en": {
        "lang": "en", "title": "Yuhao Xie | LLM Inference & GPU Systems",
        "description": "Yuhao Xie, Computer Engineering PhD student at UCF. Research in efficient LLM inference, KV-cache quantization, CUDA kernels and Agent scoring.",
        "skip": "Skip to content", "brand": "Yuhao Xie", "name": "Yuhao Xie", "native": "谢雨豪",
        "nav": ["Research", "Projects", "Background", "Contact"],
        "eyebrow": "EFFICIENT LLM INFERENCE · GPU SYSTEMS",
        "role": "Computer Engineering PhD student · University of Central Florida",
        "lead": "I work on making language models more efficient—from the memory that holds their context to the GPU kernels and scoring paths that turn it into useful output.",
        "cv_en": "English résumé", "cv_zh": "中文简历", "header_cv": "Résumé ↗",
        "figure_label": "ACROSS THE INFERENCE STACK", "figure_caption": "Memory, computation, decisions. A conceptual map of my research interests.",
        "topics": [
            ("Memory", "KV-cache quantization", "Low-bit representations, learnable quantization and memory-efficient decoding."),
            ("Compute", "Fused GPU kernels", "On-the-fly dequantization and attention, with less movement through GPU memory."),
            ("Decisions", "Agent scoring systems", "Efficient tool-call likelihoods and practical integration into vLLM.")],
        "research_label": "01 / RESEARCH", "research_title": "Selected publication",
        "research_note": "From quantization methods to inference systems.",
        "venue": "EMNLP 2026 · Main conference", "first_author": "First author",
        "pub_summary": "Learnable non-uniform KV-cache quantization, studied through the lens of implicit regularization.",
        "paper": "Read paper ↗", "code": "Code ↗", "project": "Project page ↗",
        "projects_label": "02 / ENGINEERING", "projects_title": "Selected systems work",
        "projects_note": "Implementations with measured, explicitly scoped results.",
        "orbit_tag": "CUDA / vLLM", "orbit_title": "OrbitCall",
        "orbit_summary": "An opt-in vLLM 0.29 plugin for scoring finite JSON key-order tool-call families. It preserves native LM-head projection shapes and complete JSON/EOS likelihoods while reducing normalization, ranking and CPU transfer.",
        "orbit_result": "1.08× complete two-round Agent speedup",
        "orbit_scope": "Qwen2.5-3B · DGX Spark (GB10) · six paired blocks · eight fixed workflows · versus native full scoring.",
        "results": "Measured study ↗",
        "kernel_tag": "GPU KERNELS", "kernel_title": "Attention decoding with quantized KV caches",
        "kernel_summary": "Fused on-the-fly KV dequantization, attention scoring, online softmax and value accumulation. Packed K/V are reconstructed in registers, avoiding full-precision KV materialization in GPU memory.",
        "kernel_result": "40% faster inference in the measured setup",
        "kernel_scope": "Llama 2 7B · one NVIDIA H100 · versus a Hugging Face implementation.",
        "details": "Full details in résumé ↗",
        "background_label": "03 / BACKGROUND", "background_title": "Research meets engineering",
        "education": "Education", "experience": "Industry experience",
        "education_items": [
            ("2023 — 2027 (expected)", "University of Central Florida", "PhD, Computer Engineering"),
            ("2021 — 2023", "University of Florida", "MS, Electrical & Computer Engineering"),
            ("2017 — 2021", "Hangzhou Dianzi University", "BS, Electrical & Computer Engineering")],
        "experience_items": [
            ("May — Aug. 2024", "Hithink RoyalFlush", "LLM Research Intern. CUDA quantization kernels and integration with FlashAttention and paged KV caches."),
            ("Jan. — May 2021", "Rtelligent Technology", "Software Engineer Intern. ARM firmware, G-code processing and FPGA raster-image parallelism.")],
        "service_label": "ACADEMIC SERVICE", "service_title": "ICLR 2027 Reviewer", "service_text": "Peer review for the International Conference on Learning Representations.",
        "honor_label": "FELLOWSHIP", "honor_title": "ORCGS Doctoral Fellowship", "honor_text": "University of Central Florida · 2023–2027",
        "teaching": "Teaching at UCF", "instructor": "Instructor", "assistant": "Teaching Assistant",
        "instructor_items": ["Aug.–Dec. 2026 · Digital Systems (EEE3342C), Computer Organization (EEL3801C)", "Aug. 2024–May 2025 · Computer Organization Lab"],
        "assistant_items": ["Aug.–Dec. 2026 · Hardware Security and Trusted Circuit Design (EEE4346C)", "May–Aug. 2025 · Junior Design"],
        "contact_label": "04 / CONTACT", "contact_title": "Let’s talk about efficient inference.",
        "contact_text": "For research conversations and opportunities in LLM inference and GPU systems, email is the best way to reach me.",
        "source": "Website source ↗", "resume_repo": "Résumé repository ↗"
    },
    "zh": {
        "lang": "zh-CN", "title": "谢雨豪 | 大模型推理与 GPU 系统",
        "description": "谢雨豪，中佛罗里达大学计算机工程博士在读，研究大模型高效推理、KV Cache 量化、CUDA 内核与 Agent 评分系统。",
        "skip": "跳转到正文", "brand": "谢雨豪", "name": "谢雨豪", "native": "Yuhao Xie",
        "nav": ["研究", "项目", "经历", "联系"],
        "eyebrow": "大模型高效推理 · GPU 系统",
        "role": "中佛罗里达大学 · 计算机工程博士在读",
        "lead": "我的研究关注如何让大语言模型更高效：从保存上下文的 KV Cache，到执行解码的 GPU 内核，再到 Agent 的工具调用评分。",
        "cv_en": "English résumé", "cv_zh": "中文简历", "header_cv": "简历下载 ↗",
        "figure_label": "从内存到计算，再到决策", "figure_caption": "内存、计算、决策：研究方向的概念示意。",
        "topics": [
            ("内存", "KV Cache 量化", "低比特表示、可学习量化与节省内存的解码方法。"),
            ("计算", "GPU 融合内核", "融合按需反量化与注意力计算，减少 GPU 显存读写。"),
            ("决策", "Agent 评分系统", "优化工具调用概率评分，并集成至 vLLM 推理流程。")],
        "research_label": "01 / 研究", "research_title": "代表论文",
        "research_note": "连接量化方法与推理系统。",
        "venue": "EMNLP 2026 · 主会", "first_author": "第一作者",
        "pub_summary": "从隐式正则化的视角，研究可学习非均匀 KV Cache 量化。",
        "paper": "论文全文 ↗", "code": "开源代码 ↗", "project": "项目主页 ↗",
        "projects_label": "02 / 工程", "projects_title": "代表性系统项目",
        "projects_note": "围绕具体场景实现优化，并注明实测条件。",
        "orbit_tag": "CUDA / vLLM", "orbit_title": "OrbitCall",
        "orbit_summary": "面向 CUDA GPU 的 vLLM 0.29 工具调用评分插件，用于有限 JSON 键序候选族。保留原生 LM head 投影形状与完整 JSON/EOS 概率，减少归一化、排名计算和 CPU 传输开销。",
        "orbit_result": "完整双轮 Agent 实测加速 1.08 倍",
        "orbit_scope": "Qwen2.5-3B · DGX Spark（GB10）· 六组配对测速 · 八个固定流程 · 相较原生全量评分。",
        "results": "实验报告 ↗",
        "kernel_tag": "GPU 内核", "kernel_title": "量化 KV Cache 的融合注意力解码",
        "kernel_summary": "将 KV 按需反量化、注意力得分计算、在线 Softmax 与 Value 加权累加融合到解码内核，在寄存器中重构压缩 K/V，避免在显存中生成完整的高精度 KV 副本。",
        "kernel_result": "在实测配置下推理加速 40%",
        "kernel_scope": "Llama 2 7B · 单张 NVIDIA H100 · 相较 Hugging Face 实现。",
        "details": "在简历中查看详情 ↗",
        "background_label": "03 / 经历", "background_title": "研究与工程实践",
        "education": "教育背景", "experience": "产业经历",
        "education_items": [
            ("2023 — 2027（预计）", "中佛罗里达大学", "计算机工程博士在读"),
            ("2021 — 2023", "佛罗里达大学", "电气与计算机工程硕士"),
            ("2017 — 2021", "杭州电子科技大学", "电气与计算机工程学士")],
        "experience_items": [
            ("2024.05 — 2024.08", "同花顺", "大语言模型研究实习生。开发 CUDA 量化内核，并集成 FlashAttention 与分页 KV Cache。"),
            ("2021.01 — 2021.05", "Rtelligent Technology", "软件工程实习生。参与 ARM 固件、G-code 处理与 FPGA 光栅图像并行处理。")],
        "service_label": "学术服务", "service_title": "ICLR 2027 审稿人", "service_text": "International Conference on Learning Representations。",
        "honor_label": "奖学金", "honor_title": "ORCGS 博士奖学金", "honor_text": "中佛罗里达大学 · 2023–2027",
        "teaching": "中佛罗里达大学教学经历", "instructor": "讲师", "assistant": "助教",
        "instructor_items": ["2026.08–2026.12 · 数字系统（EEE3342C）、计算机组成（EEL3801C）", "2024.08–2025.05 · 计算机组成实验课程"],
        "assistant_items": ["2026.08–2026.12 · 硬件安全与可信电路设计（EEE4346C）", "2025.05–2025.08 · Junior Design"],
        "contact_label": "04 / 联系", "contact_title": "交流大模型高效推理。",
        "contact_text": "欢迎交流大模型推理与 GPU 系统研究，以及相关合作和工作机会。请通过邮件联系我。",
        "source": "网站源码 ↗", "resume_repo": "简历仓库 ↗"
    }
}

from academic_layout import render


if __name__ == '__main__':
    for key, path in [('en', ROOT/'index.html'), ('zh', ROOT/'zh/index.html')]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(key, COPY[key]) + '\n', encoding='utf-8', newline='\n')
        print(path.relative_to(ROOT))
