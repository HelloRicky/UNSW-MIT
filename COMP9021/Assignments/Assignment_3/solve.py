"""
COMP9021 16S2 Assignment 3
Created by: Fu Zheng
"""


import re
import sys
import os


    
"""
-----------------------------------Defined Function-----------------------------------



"""

def Knight_Knave_check(title, names, L):
    """
    update involved names to be eith Knave or Knight
    
    """
    
    if 'Knave' in title:
        for i in names:
            i_check = Memberal.index(i.strip())
            L[i_check] = 0        
                
    if 'Knight' in title:
        for i in names:
            i_check = Memberal.index(i.strip())
            L[i_check] = 1
            
    return L



def Sentence(flag, key, sent, solution):
    """
    flag     -> '1' indicates Knight, '0' indicates Knave
    key      -> the person that spoke
    sent     -> the sentence content 
    solution -> binary block of all posibility

    scenarios:
    # At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
    # At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
    # Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
    # All/all of us are Knights/Knaves
    # I am a Knight/Knave
    # Sir Sir_Name is a Knight/Knave
    # Disjunction_of_Sirs is a Knight/Knave
    # Conjunction_of_Sirs are Knights/Knaves
    
    """
    
    L = [None]*len(Memberal)                                        # initial empty list
    
    r1 = re.compile('at least one of (Sirs|Sir|us|I)(.*?)is a (.*)', re.I)
    r2 = re.compile('at most one of (Sirs|Sir|us|I)(.*?)is a (.*)', re.I)
    r3 = re.compile('exactly one of (Sirs|Sir|us|I)(.*?)is a (.*)', re.I)
    r4 = re.compile('all of us are (.*)',re.I)
    r5 = re.compile('I am a (.*)',re.I)
    r6 = re.compile('(Sirs|Sir|I)(.*)is a (.*)',re.I)
    r8 = re.compile('(Sirs|Sir|I)(.*)are (.*)',re.I)


# At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
    if r1.search(sent):
        temp1 = r1.search(sent)
        if temp1.group(1) == 'us':                                  # use group(#) to returns matched subgroup
            names = Memberal
        else:
            if temp1.group(1) == 'I':
                names = key + ' ' + temp1.group(2)
            else:
                names = temp1.group(2).replace(' I ', ' ' + key + ' ')
                names = names.replace(' I,', ' ' + key + ',')
            names = names.replace(' Sir ', ' ')
            names = names.replace(' and ', ', ')
            names = names.strip().split(',')
            
        work = temp1.group(3)                                       # record eith Knave or Knight as stated in sentence

        L =  Knight_Knave_check(work, names, L)                     # Update list L
        
        
        if flag == '1':
            for i in range(len(Memberal)):
                if L[i]is not None and int(solution[i]) == L[i]:    # when claim knight,if the possible solution has a knight,return true                 
                    return True                
            return False
        
        if flag == '0':
            for i in range(len(Memberal)):
                if L[i]is not None and int(solution[i]) == L[i]: 
                    return False
            return True
        
# At/at most one of Conjunction_of_Sirs/us is a Knight/Knave           
    if r2.search(sent):
        temp1 = r2.search(sent)
        if temp1.group(1) == 'us':# ' 'if behind us
            names = Memberal
        else:
            if temp1.group(1) == 'I':
                names = key+' '+temp1.group(2)
            else:
                names = temp1.group(2).replace(' I ', ' ' + key + ' ')
                names = names.replace(' I,',' ' + key + ',')     
            names = names.replace(' Sir ',' ')
            names = names.replace(' and ',', ')
            names = names.strip().split(',')
        work = temp1.group(3)

        L =  Knight_Knave_check(work, names, L)
        
        count = 0
        
        if flag == '1':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]: 
                    count += 1
            if count <=1:
                return True
            return False
        
        if flag == '0':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]: 
                    count += 1
            if count <= 1:
                return False
            return True
        
# Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
    if r3.search(sent):
        temp1 = r3.search(sent)
        if temp1.group(1) == 'us':
            names = Memberal
        else:
            if temp1.group(1) == 'I':
                names = key + ' ' + temp1.group(2)
            else:
                names = temp1.group(2).replace(' I ', ' ' + key + ' ')
                names = names.replace(' I,', ' ' + key + ',')
            names = names.replace(' and ', ', ')
            names = names.replace(' Sir ', ' ')
            names = names.strip().split(',')
        work = temp1.group(3)

        L =  Knight_Knave_check(work, names, L)
        
        count = 0
        if flag == '1':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]: 
                    count += 1
            if count == 1:
                return True
            return False
        
        if flag == '0':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]: 
                    count += 1
            if count == 1:
                return False
            return True
        
# All/all of us are Knights/Knaves
    if r4.search(sent):
        temp1 = r4.search(sent)
        work = temp1.group(1)

        L =  Knight_Knave_check(work, names, L)
        
        if flag == '1':
            for i in range(len(Memberal)):
                if int(solution[i]) != L[i]: 
                    return False
            return True
        if flag == '0':
            for i in range(len(Memberal)):
                if int(solution[i]) != L[i]: 
                    return True
            return False
        
# I am a Knight/Knave
    if r5.search(sent):
        temp1 = r5.search(sent)
        names = key.split()
        work=temp1.group(1).strip()

        L =  Knight_Knave_check(work, names, L)

        
        i = Memberal.index(key)
        if flag == '1':
            if int(solution[i]) == L[i]:
                return True
            return False
        if flag == '0':
            if int(solution[i]) == L[i]:
                return False
            return True
  
# Disjunction_of_Sirs is a Knight/Knave  else Sir a is a knight/knave
    if r6.search(sent):
        temp1 = r6.search(sent)
        if re.search(' or ',temp1.group(2)):
            if temp1.group(1) == 'I':
                names = key + ' ' + temp1.group(2)
            else:                     #some sentence like "I or Sir""Sir ab, I, Sir t or...""Sir ab or I is ..."
                names = temp1.group(2).replace(' I ', ' ' + key + ' ')
                names = names.replace(' I,', ' ' + key + ',')
            names = names.replace(' Sir ', ' ')        
            names = names.replace(' or ', ',')
            names = names.strip().split(',')
        else:
            names = temp1.group(2).strip().split()
        work = temp1.group(3).strip()

        L =  Knight_Knave_check(work, names, L)
        
        if flag == '1':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]:                   
                    return True                
            return False
        if flag == '0':
            for i in range(len(Memberal)):
                if int(solution[i]) == L[i]:                   
                    return False               
            return True
        
# Conjunction_of_Sirs are Knights/Knaves
    if r8.search(sent):
        temp1 = r8.search(sent)
        if temp1.group(1) == 'I':
            names = key + ' ' + temp1.group(2)
        else:
            names = temp1.group(2).replace(' I ', ' ' + key + ' ')
            names = names.replace(' I,', ' ' + key + ',')
        names = names.replace(' and ', ', ')
        names = names.replace(' Sir ', ' ')
        names = names.strip().split(',')
        work = temp1.group(3)


        L =  Knight_Knave_check(work, names, L)
        
        
        if flag =='1':
            for i in range(len(Memberal)):
                if L[i]is not None and int(solution[i]) != L[i]:
                    return False
            return True
        if flag == '0':
            for i in range(len(Memberal)):
                if L[i]is not None and int(solution[i]) != L[i]: 
                    return True
            return False

"""
-----------------------------------Main loop-----------------------------------



"""

# initial

num = 0
location = []
detail_sol = []
dic = {}
arrange = ''    # text content of file after replace sentense end mark
Memberal = ''   # All sirs
name_list = ''  # final name list of all Sir

filename = input('Which text file do you want to use for the puzzle?')

if not os.path.exists(filename):                # check if current path contain input file
    sys.exit()                                  # end process if no file found

with open(filename) as file: 
    # extract all content and replace end mark to full stop
    for line in file:
        for k in {'!','?','!"'}:
            line = line.replace(k, '.')

        arrange += ' ' + line.strip()           
    sentences = arrange.strip().split('.')      # split and store each sentences
    
    for i in range(len(sentences)):
        """
        detect a sentence that has been spoken
        case 1: speaker is after he sentence, e.g. "hello," Ricky said
        case 2: speaker is before the sentence, but no finished speaking, e.g. Ricky said: "Hello," but...
        case 3: speaker is before the sentence and finished speaking. e.g. Ricky said: "Hello."
        """
        # find speaking content
        search_at_begin = re.match(r'"(.*),".*', sentences[i].strip())   # case 1
        search_middle = re.search(r'.* "(.*),"', sentences[i])           # case 2
        search_end = re.search(r'\w+.* "(.*)', sentences[i])             # case 3

        # find speaker
        if search_at_begin:
            search_speaker = re.search(r'.*".*Sir (\w*).*', sentences[i])
            speaker = search_speaker.group(1).strip()
            dic.setdefault(speaker,[]).append(search_at_begin.group(1))
            
        elif search_middle:
            if re.search('.*Sir (\w*).*"\w+.*', sentences[i]):           # speaker is before ""
                speaker = re.search('.*Sir (\w*).*"\w+.*', sentences[i])  
            else:
                speaker = re.search('.*".*Sir (\w*).*', sentences[i])
            speaker = speaker.group(1).strip()
            dic.setdefault(speaker,[]).append(search_middle.group(1))
            
        elif search_end:
            speaker = re.search('.*Sir (\w*).*"\w+.*', sentences[i])  
            speaker = speaker.group(1).strip()
            dic.setdefault(speaker,[]).append(search_end.group(1))

        # for multiple Sirs
        if re.search('.*Sirs(.*)and (\w*)', sentences[i]):
            """
            e.g. "I have just met Sirs Frank, Paul and Nina."
            
            member = 'Frank, Paul'
            member2 = 'Nina'
            members = ['Frank', 'Paul']
            
            """
            member = re.search('.*Sirs(.*)and (\w*)', sentences[i]).group(1).strip()
            member2 = re.search('.*Sirs(.*)and (\w*)', sentences[i]).group(2).strip()
            members = member.replace(',', '').split()

            if member2 not in members:          # avoid duplicate names
                members.append(member2)

        # for single Sir
        temp = re.findall('Sir (\w*)', sentences[i])
        if temp:
            for i in temp:
                if i not in members:            # avoid duplicate names
                    members.append(i)

    
    members.sort()                              # alphabetical order
    name_list = ' '.join(members)               # convert name list to string as print result
    
Memberal = sorted(name_list.strip().split())

maxNum = 2**len(Memberal)                       # total numbers of possible set
    
dickey = sorted(list(dic.keys()))               # get all the Sir name that has a sentense


for i in dickey:
    location.append(Memberal.index(i))          #find the dic index in Memberal

for i in range(maxNum):

    # l is the binary digit array. e.g. 8 -> ['1', '0', '0', '0']
    l = list(bin(i)[2:].zfill(len(Memberal)))
    
    
    k = 0
    possible = 1
    
    for key in sorted(dic):
        for j in range (len(dic[key])):
            temp = location[k]
            
            if not Sentence(l[temp],key,dic[key][j],l):
                possible = 0
                break
        if not possible:
            break
        k += 1
    if possible:
        num += 1
        detail_sol.append(l)

"""
-----------------------------------Print results-----------------------------------



"""

# Print out all the Sirs

print('The Sirs are: {}'.format(name_list))

# Print solutions

if num == 0:
    print('There is no solution.')

if num == 1:
    print('There is a unique solution:',)
    for i in range(len(Memberal)):
        if detail_sol[0][i] =='1':
            print('Sir {} is Knight.'.format(Memberal[i]))
        else:
            print('Sir {} is Knave.'.format(Memberal[i]))
if num > 1:
    print('There are {} solutions.'.format(num))
    
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

