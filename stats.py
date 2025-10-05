def get_num_words(string):
  words = string.split()
  return len(words)

def get_chars_dict(string):
  chars = {}
  for i in string.lower():
    chars[i] = chars.get(i, 0) + 1
  return chars

def get_num_for_sort(items):
  return items["num"]

def sort_characters(dict):
  sorted_dict = []
  for char, count in dict.items():
    sorted_dict.append({"char": char, "num": count})
  sorted_dict.sort(key=get_num_for_sort, reverse=True)
  return sorted_dict