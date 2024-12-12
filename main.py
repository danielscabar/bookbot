def count_char(file):
  count_char = {}
  file = file.lower()
  for char in file:
    count_char[char] = count_char.get(char, 0) + 1
  return count_char

def count_words(file):
  return len(file.split())

def main():
  with open('./books/frankenstein.txt') as f: 
    file_contents = f.read()
    #print(count_words(file_contents))
    print(count_char(file_contents))

if __name__ == "__main__":
  main()