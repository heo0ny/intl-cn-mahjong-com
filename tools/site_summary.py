import os
import json
from datetime import datetime

# 内置站点资料
SITES = [
    {
        "name": "国际麻将乐园",
        "url": "https://intl-cn-mahjong.com",
        "keywords": ["麻将胡了", "在线麻将", "中国麻将"],
        "tags": ["娱乐", "棋牌", "多人游戏"],
        "description": "提供正宗中国麻将玩法，支持好友对战与随机匹配。"
    },
    {
        "name": "胡牌大师",
        "url": "https://mahjong.example.com",
        "keywords": ["麻将胡了", "麻将技巧", "胡牌公式"],
        "tags": ["教学", "攻略", "工具"],
        "description": "收录最新麻将规则与胡牌概率计算，助你快速提升牌技。"
    }
]

def load_sites(path: str = None) -> list:
    """从 JSON 文件加载站点资料，若无文件则返回内置数据"""
    if path and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return SITES

def format_tags(tags: list) -> str:
    """将标签列表格式化为带 # 前缀的字符串"""
    return " ".join(f"#{tag}" for tag in tags)

def generate_summary(site: dict) -> str:
    """为单个站点生成结构化摘要"""
    name = site.get("name", "未命名站点")
    url = site.get("url", "无链接")
    keywords = site.get("keywords", [])
    tags = site.get("tags", [])
    desc = site.get("description", "暂无描述")

    lines = [
        f"【站点名称】{name}",
        f"【网址】{url}",
        f"【核心关键词】{'、'.join(keywords)}",
        f"【标签】{format_tags(tags)}",
        f"【简介】{desc}",
    ]
    return "\n".join(lines)

def build_report(sites: list) -> str:
    """将所有站点摘要合并为一份报告"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"站点摘要报告（生成时间：{now}）"
    separator = "=" * 40
    parts = [header, separator]

    for i, site in enumerate(sites, 1):
        summary = generate_summary(site)
        parts.append(f"#{i} 站点摘要")
        parts.append(summary)
        parts.append("-" * 30)

    parts.append("报告结束")
    return "\n".join(parts)

def export_report(report: str, path: str = "site_summary_report.txt"):
    """将报告写入文本文件"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"报告已保存至 {path}")

def main():
    # 可选的 JSON 配置文件路径（若存在则覆盖内置数据）
    config_path = "sites_data.json"
    sites = load_sites(config_path)

    report = build_report(sites)
    print(report)

    # 输出到文件供 GitHub 仓库使用
    export_report(report)

if __name__ == "__main__":
    main()