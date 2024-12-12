import string

def count_char(file):
  count_char = {}
  file = file.lower()
  for char in file:
    if char in string.ascii_lowercase: 
      count_char[char] = count_char.get(char, 0) + 1
  return count_char

def sort_dict_by_value(dict):
  inverted_dict = {}
  sorted_dict = {}

  for k, v in dict.items():
    inverted_dict[v] = k
  for v in sorted(inverted_dict, reverse=True):
    sorted_dict[v] = inverted_dict[v]
  return sorted_dict

def count_words(file):
  return len(file.split())

def main():
  with open('./books/frankenstein.txt') as f: 
    file_contents = f.read()
    print(f'{count_words(file_contents)} words found in the document')
    print('')
    for v, k in sort_dict_by_value(count_char(file_contents)).items():
      print(f"The '{k}' character was found '{v}' times")
    print('--- End report ---')

if __name__ == "__main__":
  main()