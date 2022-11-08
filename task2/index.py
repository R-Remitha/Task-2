import spacy
import traceback
from datetime import date
nlp = spacy.load("en_core_web_sm")
try:
  f = open(r"C:\Users\remit\OneDrive\Desktop\task2\words.txt", "r")
  f1 = open(r"C:\Users\remit\OneDrive\Desktop\task2\result.txt", "w")
  noun=0
  adjective=0
  verb=0
  if f.read(1)!='':
    f.seek(0)
    l=[]
    text = nlp(f.read())
    for t in text:
      s=[]
      s.append(t)
      s.append(t.pos_)
      l.append(s)
    for i in l:
      if i[1]=='NOUN':
        noun+=1
      elif i[1]=='ADJ':
        adjective+=1
      elif i[1]=='VERB':
        verb+=1
      elif i[1]=='PROPN':
        noun+=1
    res='Noun= '+str(noun)+'\nAdjective= '+str(adjective)+'\nVerb= '+str(verb)
    f1.write(res)
    print("Result is successfully written in 'result.txt' file.")
    f.close()
    f1.close()
  else:
    print("File is empty.")
except Exception as e:
  print("Error happened")
  f3 = open(r"C:\Users\remit\OneDrive\Desktop\task2\logfile.txt", "a")
  today = date.today()
  d1 = today.strftime("%d/%m/%Y")+'\n'
  f3.write(str(d1))
  t=str(e)
  f3.write(t)
  f3.write('\n\n')
  f3.close()
