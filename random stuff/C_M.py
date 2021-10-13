########################################
## KRBL-PRJ software                  ##
## Module name: Check_module          ##
## Module's coder:Sukhoroslov Aretmiy ##
########################################

def check(blocks):
    values = []  # сюда записываем типы переменных
    for y in blocks:
        for x in y:
            if x.count("while") != 0:
                if x.count("<") != 0 or x.count(">") != 0: # проверка на int
                    x1 = x.split()
                    x2 = x1.index('while')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'while' and a !=  '+' and a !=  '=' and a !=  '-' and a !=  '/' and a !=  '*'and a !=  '>' and a !=  '<'  and a !=  '1' and a !=  '0' and a !=  '2' and a !=  '3' and a !=  '4' and a !=  '5' and a !=  '6' and a !=  '7' and a !=  '8' and a !=  '9' and a.count(':') == 0:
                            values.append({a: 'int'})
                elif x.count('str') != 0: # проверка на str
                    x1 = x.split()
                    x2 = x1.index('while')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'while' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                            values.append({a: 'expr'})
                elif x.count('list') != 0 or x.count('split') != 0: # проверка на list
                    x1 = x.split()
                    x2 = x1.index('while')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'while' and a != 'list' and a != 'split' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                            values.append({a: 'list'})
                elif x.count('dict') != 0: # проверка на dict
                    x1 = x.split()
                    x2 = x1.index('while')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'while' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                            values.append({a: 'dict'})
            elif x.count('for') != 0:
                if x.count('range') != 0 and x.count('len') == 0:
                    x1 = x.split()
                    x2 = x1.index('for')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9' and a != 'for' and a != 'in' and a != 'range':
                            values.append({a: 'int'})
                elif x.count('str') != 0:  # проверка на str
                    x1 = x.split()
                    x2 = x1.index('for')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'in' and a != 'str' and a != 'for' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                               values.append({a: 'expr'})
                elif x.count('list') != 0 or x.count('split') != 0:  # проверка на list
                    x1 = x.split()
                    x2 = x1.index('for')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'in' and a != 'list' and a != 'split' and a != 'for' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                            values.append({a: 'list'})
                elif x.count('dict') != 0:  # проверка на dict
                    x1 = x.split()
                    x2 = x1.index('for')
                    x2 += 1
                    values.append({x1[x2]: 'int'})
                    x1.remove(x1[x2])
                    for a in x1:
                        if a.count(':') != 0:
                            a.replace(':', '')
                        if a != 'in' and a != 'dict' and a != 'for' and a != '+' and a != '=' and a != '-' and a != '/' and a != '*' and a != '1' and a != '0' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7' and a != '8' and a != '9':
                            values.append({a: 'dict'})

    return values


blocks = []
line = input()
while line != "": # получаем код и заносим его в блоки
    if line.count('while') != 0 or line.count('for') != 0 or line.count('def') != 0 or line.count('if') != 0:
        blocks.append([])
        blocks[len(blocks) - 1].append(line)
        line = input()
        while line.count('\t') != 0:
            blocks[len(blocks) - 1].append(line)
            line = input()
    else:
        blocks.append([])
        blocks[len(blocks) - 1].append(line)
        line = input()
vals = check(blocks)
print(blocks)
print(vals)