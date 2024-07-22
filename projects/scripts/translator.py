eng = ["bathroom",
"because",
"bike",
"birthday",
"blog",
]



from googletrans import Translator
import json

translator = Translator()

def fu(n):
  with open("result400.txt", "a", encoding="utf-8") as file:
    translate_text = translator.translate(eng[n], dest='ru')
    file.write(eng[n] + "," + translate_text.text + '\n')


def translate():
  for i in range(0,403):
    while True:
      try:
        fu(i)
        break
      except:
        continue

def to_jsn():
  result = {}
  start = 10
  with open(r"E:\GIT\personal\eng\sours\result.txt", "r", encoding='utf-8') as rus:
    rus = [line.strip() for line in rus.readlines()]

    for i in range(len(eng)):
      result[eng[i]] = [rus[i],start]
      start += 10
  return result

translate()