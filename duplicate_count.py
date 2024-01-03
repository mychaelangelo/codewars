def duplicate_count(text):
    text = text.lower()
    dups = [item for item in text if (item. isalnum() and text.count(item) > 1)]  
    return len(list(set(dups)))


result_1 = duplicate_count("abcde")
result_2 = duplicate_count("Indivisibilities")
result_3 = duplicate_count("sTiCqmCnIasSTwX3XrqtdvaoTiAaSmAwyITOwA7CYiKWPEjJWwZOO3l2W8mq5TwxNiXfeVvlGsPd1ayD7MDJCSN")

print(f"Result 1 is: {result_1}, and should be 0")
print(f"Result 2 is: {result_2}, and should be 2")
print(f"Result 3 is: {result_2}, and should be 20")