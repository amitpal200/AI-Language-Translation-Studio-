def guess_language(text):
    if not text:
        return "auto"
    if any("\u0900" <= char <= "\u097f" for char in text):
        return "hi"
    if any("\u3040" <= char <= "\u30ff" for char in text):
        return "ja"
    if any("\u4e00" <= char <= "\u9fff" for char in text):
        return "zh-CN"
    return "en"
