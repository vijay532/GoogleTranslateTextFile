from googletrans import Translator 

f=open('input.txt','r')

contents=f.read()

file_translate = Translator()

result = file_translate.translate(contents, dest='es')
#print(result.text)

with open('output.txt', 'w') as f:
    f.write(result.text)


# import googletrans

# print(googletrans.LANGAUGES) 

# For All the languages that google supports