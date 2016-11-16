
import copy
import math
#min:max
contact = []
 
n = 15
 
x_action = [1,-1,0,0]
y_action = [0,0,1,-1]
 
#set({point:(x,y)})
proteins = []
proteins.append({0:(0,0),1:(1,0),2:(2,0),3:(3,0)})
c = []
contact.append(c)
proteins.append({0:(0,0),1:(1,0),2:(2,0),3:(2,-1)})
c = []
contact.append(c)
proteins.append({0:(0,0),1:(1,0),2:(1,-1),3:(0,-1)})
c = [(0,3)]
contact.append(c)
proteins.append({0:(0,0),1:(1,0),2:(1,-1),3:(1,-2)})
c = []
contact.append(c)
proteins.append({0:(0,0),1:(1,0),2:(1,-1),3:(2,-1)})
c = []
contact.append(c)
#print proteins
for step in range(4,n):
    print step, len(proteins)
    lastAA = step - 1
    temp = []
    temp_c = []
    for i in range(len(proteins)):
        lastAA_pos = proteins[i][lastAA]
 
        for j in range(len(x_action)):
            tentative_pos_x = lastAA_pos[0] + x_action[j]
            tentative_pos_y = lastAA_pos[1] + y_action[j]
            #print (tentative_pos_x, tentative_pos_y)
            found = False
            temp_contact = copy.deepcopy(contact[i])
            for AA in proteins[i].keys():
                if proteins[i][AA] == (tentative_pos_x, tentative_pos_y):
                    found = True
                if math.sqrt((proteins[i][AA][0] - tentative_pos_x)**2 + (proteins[i][AA][1] - tentative_pos_y)**2) == 1 and AA != lastAA:
                    temp_contact.append((AA,step))
                    #print "found"
            if found == False and abs(tentative_pos_x) < 6 and abs(tentative_pos_y) < 5:
                #print (tentative_pos_x, tentative_pos_y)
 
                temp_protein = copy.deepcopy(proteins[i])
                temp_protein[step] = (tentative_pos_x, tentative_pos_y)
                #print temp_protein,proteins[i]
                temp.append(temp_protein)
                #print temp
 
                temp_c.append(temp_contact)
 
    proteins = temp
    contact = temp_c
print len(contact)
