


from collections import defaultdict, deque
import sys
import time
from random import sample



def makeInput(nAmount):
    n = nAmount
    data = []
    '''
    1 2 3
    2 3 1
    2 1 3
    2 1 3
    1 2 3
    1 2 3
    
    data2 = [
        [1, 2, 3],  # hospital 1 prefs
        [1, 2, 3],  # hospital 2 prefs
        [2, 3, 1],  # hospital 3 prefs
        [2, 1, 3],  # student 1 prefs
        [3, 1, 2],  # student 2 prefs
        [1, 2, 3]   # student 3 prefs
    ]
    '''

    for i in range(n):
        data.append(sample(range(1,n+1),n))
    
    for i in range(n):
        data.append(sample(range(1,n+1),n))
    return [n, data]

def fullgs(nAmount):

    n, data = makeInput(nAmount)
    person = defaultdict(list)
    hospitals = defaultdict(list)

    index = 1
    for i in range(n):
        hospitals[index] = [[s, True] for s in data[i]] #change here
        index += 1

    index = 1
    for i in range(n, 2 * n):
        person[index] = [[h, True] for h in data[i]] #change here
        index += 1

    free = {}

    for i in range(n):
        free[i + 1] = True

    studentMatch = {i: None for i in range(1, n+1)}   # student -> hospital
    hospitalMatch = {i: None for i in range(1, n+1)}  # hospital -> student

    def assign(h, a):
        studentMatch[a[0]] = h
        hospitalMatch[h] = a[0]
        free[a[0]] = False


    def swap(h, a):
        oldHospital = studentMatch[a[0]]
        studentMatch[a[0]] = h
        hospitalMatch[h] = a[0]
        hospitalMatch[oldHospital] = None
        unmatchedHospital.append(oldHospital)


    unmatchedHospital = deque(hospitals.keys())

    # If the students have the ranking
    ranking = defaultdict(dict)

    for student, prefernces in person.items():
        for rank, (hospital, _) in enumerate(prefernces):
            ranking[student][hospital] = rank


    def gs(unmatchedHospital):
        while unmatchedHospital:

            hospital = unmatchedHospital.popleft()
            hospitalList = hospitals[hospital]  # -> we get the list

            # applicant = 1st applicant on h's list to whom hospital has not been matched
            # applicant = hospitalList.pop(0)
            applicant = None
            for student in hospitalList:
                if student[1] == True:
                    applicant = student
                    student[1] = False
                    break

            # if there is no applicant
            # this means they all have been matched, so we continue
            if applicant is None:
                continue

            # get the current hospital that the applicant is matched to
            student = applicant[0]
            currentHospital = studentMatch[student]

            if free[student]:
                assign(hospital, applicant)
            # elif a prefers h to her/his current assignment h':
            elif ranking[student][hospital] < ranking[student][currentHospital]:
                swap(hospital, applicant)
            else:
                # a rejects h
                unmatchedHospital.append(hospital)

    start1 = time.perf_counter()
    gs(unmatchedHospital)
    end1 = time.perf_counter()
    #for k,v in hospitalMatch.items():
        #print(f"{k} {v}\n")

    #-------------------------------------------------------------------------------------
    #print(f"Timer for G.S is :{(end1-start1):.10f}")
    #TaskB

    #Check Validity

    def checkValidity(hospitalMatch):
        
        students = set()

        '''
        Checks validity: each hospital and each student is matched to
        exactly one partner, with no duplicates
        
        '''
        for _,a in hospitalMatch.items():
            if a in students:
                return False
            students.add(a)
        return True

    #def checkStability(hosptials, students):

    def valid(hospitalMatch):
        students = set()

        for _,a in hospitalMatch.items():
            if a in students:
                return False
            students.add(a)
        return True

    start2 = time.perf_counter()
    valid(hospitalMatch)
    end2 = time.perf_counter()

    r = f"valid time was: {end2-start2:.10f}"
    print(r)






#-------------------------------------------------------------------------------------
#Task C

#check res/time_gs.txt
different_n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

for n in different_n:
    print(f"For N = {n}")
    fullgs(n)