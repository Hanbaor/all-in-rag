# 1. 从 .pdf 模块导入专用的 partition_pdf
from unstructured.partition.pdf import partition_pdf
from collections import Counter

# PDF文件路径
pdf_path = "../../data/C2/pdf/rag.pdf"

# 2. 使用 partition_pdf 函数，并指定 strategy="hi_res"
print("--- 开始使用 hi_res 策略进行解析 ---")
elements_hires = partition_pdf(
    filename=pdf_path,
    strategy="hi_res"  # <-- 关键在这里：指定高精度策略
)

# 打印解析结果
print(f"解析完成 (hi_res): {len(elements_hires)} 个元素, {sum(len(str(e)) for e in elements_hires)} 字符")
types_hires = Counter(e.category for e in elements_hires)
print(f"元素类型 (hi_res): {dict(types_hires)}")
print("=" * 60)