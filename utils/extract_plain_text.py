import re


def extract_plain_text(markdown_text):
    # Markdown 문법 제외하고 텍스트만 추출하는 정규 표현식
    pattern = r"#+\s*|```.*?```|`.*?`|\*{1,2}|_{1,2}|~~|\[.*?\]\(.*?\)|\[.*?\]|\(.*?\)"
    plain_text = re.sub(pattern, "", markdown_text)
    # 여러 개의 연속된 공백을 하나의 공백으로 변경
    plain_text = re.sub(r"\s+", " ", plain_text)
    # 양쪽 공백 제거
    plain_text = plain_text.strip()
    return plain_text
