from collections import defaultdict

'''
Initialize each person and hospital to be free.

while (some hospital is free and hasn’t been matched/assigned
       to every applicant) {

    Choose such a hospital h
    a = 1st applicant on h's list to whom h has not been matched

    if (a is free)
        assign h and a
    else if (a prefers h to her/his current assignment h')
        assign a and h, and h' has a slot free
    else
        a rejects h
}
'''

person = defaultdict(list)
hospitals = defaultdict(list)
#Initialized 

person["Xavier"] = [["Shands",False], ["North", False], ["Vetrans",False]]
person["Yancey"] = [["North",False], ["Shands", False], ["Vetrans",False]]
person["Zeus"] = [["Shands",False], ["North", False], ["Vetrans",False]]

hospitals["Shands"] = [["Yancey",False], ["Xavier", False], ["Zeus",False]]
hospitals["North"] = [["Shands",False], ["Yancey", False], ["Zeus",False]]
hospitals["Vetrans"] = [["Xavier",False], ["Yancey", False], ["Zeus",False]]



