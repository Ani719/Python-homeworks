text = "pythön is a programming language!"

print("String methods-encode([encoding[,errors]])")

print(text.encode(encoding="UTF-8", errors="strict"))
print(text.encode(encoding="ascii", errors="replace"))
print(text.encode(encoding="ascii", errors="ignore"))
print(text.encode(encoding="UTF-8", errors="xmlcharrefreplace"))
print(text.encode(encoding="UTF-8", errors="backslashreplace"))

print("String methods-endswith(suffix[, start[, end]])")
suffix = "language!"
endswith = text.endswith(suffix, 8,)
print(endswith)
suffix = "language"
endswith = text.endswith(suffix)
print(endswith)
