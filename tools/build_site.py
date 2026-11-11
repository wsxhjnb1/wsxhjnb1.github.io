"""Generate the English and Chinese static pages; no third-party packages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://wsxhjnb1.github.io"
PAPER = "https://wsxhjnb1.github.io/Beyond-KV-Cache/paper/Beyond.pdf"
BEYOND = "https://github.com/wsxhjnb1/Beyond-KV-Cache"
EMAIL = "yuhaoxie1999@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/yuhao-xie/"

COPY = {
    "en": {
        "lang": "en", "title": "Yuhao Xie | LLM Inference & GPU Systems",
        "description": "Yuhao Xie, Computer Engineering PhD student at UCF. Research in efficient LLM inference, KV-cache quantization, CUDA kernels and FlashAttention scheduling.",
        "skip": "Skip to content", "brand": "Yuhao Xie", "name": "Yuhao Xie", "native": "谢雨豪",
        "nav": ["Research", "Projects", "Background", "Contact"],
        "eyebrow": "EFFICIENT LLM INFERENCE · GPU SYSTEMS",
        "role": "Computer Engineering PhD student · University of Central Florida",
        "lead": "I work on efficient language model inference, from compact KV caches to GPU scheduling for attention kernels.",
        "cv_en": "English résumé", "cv_zh": "中文简历", "header_cv": "Résumé ↗",
        "figure_label": "ACROSS THE INFERENCE STACK", "figure_caption": "Memory, computation and scheduling across my research interests.",
        "topics": [
            ("Memory", "KV-cache quantization", "Low-bit representations, learnable quantization and memory-efficient decoding."),
            ("Compute", "Fused GPU kernels", "On-the-fly dequantization and attention, with less movement through GPU memory."),
            ("Scheduling", "FlashAttention scheduling", "Constraint-based scheduling with hardware feedback for attention kernels.")],
        "research_label": "01 / RESEARCH", "research_title": "Selected publication",
        "research_note": "From quantization methods to inference systems.",
        "venue": "EMNLP 2026 · Main conference", "first_author": "First author",
        "pub_summary": "Learnable non-uniform KV-cache quantization, studied through the lens of implicit regularization.",
        "paper": "Read paper ↗", "code": "Code ↗", "project": "Project page ↗",
        "projects_label": "02 / ENGINEERING", "projects_title": "Selected systems work",
        "projects_note": "Implementations with measured, explicitly scoped results.",
        "fa2_tag": "CUDA / CuTe", "fa2_title": "TileCadence",
        "fa2_summary": "A constraint solver decides when to release shared-memory buffers so FlashAttention-2 can fit more intermediates on chip or keep them there longer. It schedules probability tiles, output tiles and log-sum-exp values. Device limits and measured latency guide kernel selection. CUDA kernels were validated on an RTX 3080 Laptop GPU and DGX Spark (GB10).",
        "fa2_result": "1.11–1.13× prefill attention speedup",
        "fa2_scope": "Qwen3-4B across 13 shapes at 8K–32K tokens on DGX Spark (GB10), versus default FlashAttention-2.",
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
        "description": "谢雨豪，中佛罗里达大学计算机工程博士在读，研究大模型高效推理、KV Cache 量化、CUDA 内核与 FlashAttention 调度。",
        "skip": "跳转到正文", "brand": "谢雨豪", "name": "谢雨豪", "native": "Yuhao Xie",
        "nav": ["研究", "项目", "经历", "联系"],
        "eyebrow": "大模型高效推理 · GPU 系统",
        "role": "中佛罗里达大学 · 计算机工程博士在读",
        "lead": "我研究如何加速大语言模型推理，包括紧凑的 KV Cache 表示与注意力内核的 GPU 调度。",
        "cv_en": "English résumé", "cv_zh": "中文简历", "header_cv": "简历下载 ↗",
        "figure_label": "内存、计算与调度", "figure_caption": "我的研究方向涵盖推理中的内存、计算与调度。",
        "topics": [
            ("内存", "KV Cache 量化", "低比特表示、可学习量化与节省内存的解码方法。"),
            ("计算", "GPU 融合内核", "融合按需反量化与注意力计算，减少 GPU 显存读写。"),
            ("调度", "FlashAttention 调度", "利用约束求解和硬件反馈优化注意力内核。")],
        "research_label": "01 / 研究", "research_title": "代表论文",
        "research_note": "连接量化方法与推理系统。",
        "venue": "EMNLP 2026 · 主会", "first_author": "第一作者",
        "pub_summary": "从隐式正则化的视角，研究可学习非均匀 KV Cache 量化。",
        "paper": "论文全文 ↗", "code": "开源代码 ↗", "project": "项目主页 ↗",
        "projects_label": "02 / 工程", "projects_title": "代表性系统项目",
        "projects_note": "围绕具体场景实现优化，并注明实测条件。",
        "fa2_tag": "CUDA / CuTe", "fa2_title": "TileCadence",
        "fa2_summary": "为 FlashAttention-2 求解何时释放共享内存，以及如何复用腾出的空间，让概率块、输出块和 softmax 的对数归一化项能在片上存得更多或更久。内核选型参考设备资源限制与实测延迟。CUDA 内核已在 RTX 3080 Laptop GPU 和 DGX Spark（GB10）上验证。",
        "fa2_result": "预填充注意力加速 1.11–1.13 倍",
        "fa2_scope": "在 DGX Spark（GB10）上测试 Qwen3-4B 的 13 个 8K–32K 形状，基线为原生默认 FlashAttention-2。",
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
