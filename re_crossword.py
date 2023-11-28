import re 
import csv 
import argparse 
import string  
import sre_yield

def rate(value): #letter frequency analysis
  count = 0
  for i in range(0,len(value)):
    if value[i] != ".":
      count=count+1
  m = count / len(value)
  return m

def mutual_letter(g,node): #filling in common letters in a pair of words
    word =g[str(node)] #current word
    for cross in word[1]:
      neigh = (g[cross]) # word that intersects 
      positionI = word[1][cross]
      positionShe= (g[cross][1][str(word[0])])
      letterI = word[3][int(positionShe)]
      letterS = neigh[3][int(positionI)]
      if (neigh[2] != 1.0):
        neigh[3] = neigh[3][:int(positionI)] + letterI + neigh[3][int(positionI)+1:] 
      neigh[2] = rate(neigh[3])

def finding_maximum(g): #finding the word with the most found letters
  big = -1
  position = -1
  for key in g:
    if (g[key][2] > float(big)) & (g[key][2] != 1.0):
        big = g[key][2]
        position = key
  return position

def finding_words(g,node,final):
    word =g[str(node)] #the word i am using 
    mikos = len(word[3])
    population = (len(words[mikos]))
    safe = safety[node]
    visited.append(node)
    for i in range(0,population,2): #checking all generated words from regular expr
        flag = True
        madefrom = words[mikos][i+1]
        madefromexpr = words[mikos][i]
        letter = 0
        for key in final:
          if (final[key][1] == madefromexpr):
            flag= False
        if flag:
          for y in range(0,mikos): #checking for common letters
            if (word[3][y] == madefrom[y]) | (word[3][y]== "."):
              letter = letter + 1
          if letter == mikos :
            word[3] = madefrom
            word[2] = rate(word[3])
            for key in final:
              if key == str(node):
                final[key] = [node, madefromexpr,madefrom]
            mutual_letter(g,node)
            user=finding_maximum(g)
            if (user != -1):
              finding_words(g,user,final)
            if finding_maximum(g) == -1:
              return
            else:
              word[3] = safe
              word = g[str(node)]
              word[2] = rate(word[3])
              mutual_letter(g,node)
              for key in final:
                if key == str(node):
                  final[key] = [node, "not", "found"]
              for i in range(0,len(visited)):
                mutual_letter(g,visited[i])
    for key in final:
      if key == str(node):
          final[key] = [node, "not", "found"]
    word[3] = safe
    word[2] = rate(word[3])
    mutual_letter(g,node)
    visited.pop()
    return

if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument('crossword_file')
    ap.add_argument('regular_expressions_file')
    args = vars(ap.parse_args())

    cross_file = args['crossword_file']
    reg_file = args['regular_expressions_file']

    g={}
    with open(cross_file) as graph_input: 
      for line in graph_input:
        parts = [x for x in line[:-1].split(",")]
        pos = {parts[i]: parts[i + 1] for i in range(2, len(parts), 2)}
        per = rate(parts[1])
        g[parts[0]] = [parts[0],pos,per,parts[1]]
    expr = []

    with open(reg_file) as regural_expressions: 
      for line in regural_expressions:
          stripped_line = line.strip()
          expr.append(stripped_line)

    words= {}
    for i in range(0,len(expr)): #generating words in dictionary based on their length
      links = []
      links.append(expr[i])
      flag= True
      for each in sre_yield.AllStrings(expr[i],max_count=5,charset=string.ascii_uppercase):
          if (each in expr) & True:
            links.append(each)
            flag = False
          if (each not in links):
            links.append(each)
      for the in range(1, len(links)):
        length = len(links[the]) 
        l = [links[0], links[the]] 
        if words.get(length):
          l = words.get(length) + l

        words.update({length: l})
    final = {} #initializing dictionary for results
    for key in g:
      final[key] = [key, "not", "found"]
      if g[key][2] == 1.0:
        a= g[key][3]
        b= len(a)
        c= key
        for x in range(0,len(words[b]),2):
          if words[b][x+1] == g[key][3]:
            final[key] = [key, words[b][x],words[b][x+1] ]
      
    safety = {}
    for key in g:
      safety[key] = g[key][3]
    visited = []
    user = finding_maximum(g)
    mutual_letter(g,user)
    visited.append(user)
    finding_words(g,user,final)
    keys = []
    for key in final:
      keys.append(key)
    keys = [int(x) for x in keys]
    keys.sort()
    for key in keys:
      for i in final:
        if i == str(key):
          ini_list = final[str(key)]
          print(*ini_list)
