raw_dict = "4-letter-words-processed-new.txt"
output_file = "dictionary.json"
with open(raw_dict, 'r', encoding='utf-8') as file:
  words = (file.read().split())
with open(output_file, "w", encoding="utf-8") as file:
  file.write("[\n")
  for word in words:
    file.write(f"  \"{word.lower()}\",\n")
  file.write("]")

  