
import json


def is_answer(node):
    return len(node) == 1


f = open('questions.json') #3
#content = f.read()
#node = json.loads(content)
# alternative
node = json.load(f)  #4+5

finished = False

while not finished:  # 1
    print(node['text'])  # 2
    # 6
    if is_answer(node):  # 7
        finished = True
    else:
        answer = input() # 8
        if answer.lower() in ['yes', 'y']: # 9
            node = node['yes'] # 10
        else:
            node = node['no']
