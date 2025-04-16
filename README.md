# 四格漫画提示词生成器

一个基于 Streamlit 的应用程序，用于生成 AI 图像生成器所需的四格漫画详细提示词。

## 功能特点

- 交互式四格漫画设计界面
- AI 图像模型的详细提示词生成
- 参考图片支持
- 可自定义漫画风格配置
- 支持文字位置、音效和过渡效果

## 安装说明

1. 安装 [uv](https://github.com/astral-sh/uv) 包管理器
2. 克隆此仓库
3. 创建虚拟环境并安装依赖：
   ```bash
   uv venv
   source .venv/bin/activate  # Windows系统使用: .venv\Scripts\activate
   uv pip install -e .
   ```

## 使用方法

运行应用程序：
```bash
streamlit run src/app.py
```

## 项目结构

```
comic-prompt-gen/
├── src/
│   └── app.py
├── pyproject.toml
└── README.md
```

## 开发环境

本项目使用：
- Python 3.9+
- Streamlit 用于网页界面
- Ruff 用于代码检查
- uv 用于包管理

[English Version](README-EN.md)