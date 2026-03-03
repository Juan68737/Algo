from collections import deque
from collections import defaultdict, deque
from re import A

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

# if the file is empty, is an edge case we need to check
# one hospital, one student
# equal number of hospitals and students

# person = defaultdict(list)
# hospitals = defaultdict(list)
person = {}
hospitals = {}

matchedHospitals = set()
# Initialize all students as unmatched
matchedStudents = {i: None for i in range(1, n+1)}

unmatchedHospitals = deque()

n = 3  # example
data = [
    [1, 2, 3],
    [2, 3, 1],
    [2, 1, 3],
    [2, 1, 3],
    [1, 2, 3],
    [1, 2, 3]
]

index = 1
for i in range(0, n):
    hospitals[index] = list(data[i])
    unmatchedHospitals.append(index)
    index += 1

"""
hospitals = {
    1: [1, 2, 3],
    2: [2, 3, 1],
    3: [2, 1, 3]
}
"""

index = 1
for i in range(n, 2*n):
    person[index] = data[i]
    index += 1

"""
persons = {
    1: [2, 1, 3],
    2: [1, 2, 3],
    3: [1, 2, 3]
}
"""

while unmatchedHospitals:
    h = unmatchedHospitals.popleft()
    hList = hospitals[h]

    if not hList:
        # Hospital has no students left to propose to
        continue

    # Propose to the next student (pop from front of list)
    s = hList.pop(0)

    if matchedStudents[s] is None:
        # Student is free → accept
        matchedStudents[s] = h
        matchedHospitals.add(h)
    else:
        # Student already matched → maybe trade up
        current_hospital = matchedStudents[s]
        sList = person[s]

        # Check if student prefers new hospital
        if sList.index(h) < sList.index(current_hospital):
            # Student trades up
            matchedStudents[s] = h
            matchedHospitals.add(h)

            # Remove old hospital from matched set and put it back to queue
            matchedHospitals.remove(current_hospital)
            unmatchedHospitals.append(current_hospital)
        else:
            # Student rejects new hospital → hospital stays unmatched, try next later
            unmatchedHospitals.append(h)

# Print final matches in hospital → student format
for student, hospital in matchedStudents.items():
    print(f"{hospital} {student}")


"""
index = 1
while unmatchedHospitals:
    hList = hospitals[index]  # get the hospital list prefence
    s = hList[0]  # get the first student prefence

    
    for cs in range(len(hList)):
        if matchedStudents[s] is None:  # if the student have not matched
            matchedStudents[s] = index
            matchedHospitals.add(index)

            unmatchedHospitals.popleft()  # remove hospital from queue?
        else:
            sList = person[s]  # get the student list prefence

            # if the student has already matched
            # check to see if the student want to trade up
            assignedHospitalIndex = 0
            for i in range(len(sList)):
                if sList[i] == matchedStudents[s]:
                    assignedHospitalIndex = i

                if sList[i] == index:
                    if assignedHospitalIndex < i:
                        # student does not want to trade
                        break

                    else:
                        # student wants to trade
                        # remove the hospital from the set
                        matchedHospitals.remove(assignedHospitalIndex)

                        # add the new assigned hospital to the set
                        matchedHospitals.add(index)

                        # update the matched students dictionary
                        matchedStudents[s] = index

                        # add the unmatched hospital back to the queue
                        unmatchedHospitals.append(assignedHospitalIndex)

        # else
        # check the next student in the hospital list


"""


"""
hp1 = [1, 2, 3]
hp2 = [2, 3, 1]
hp3 = [2, 1, 3]

sp1 = [2, 1, 3]
sp2 = [1, 2, 3]
sp3 = [1, 2, 3]
"""

"""
hp1 to s1, s1 accepts
hp2 to s2, s2 accepts
hp3 to s2, s2 declines
hp3 to s1, s1 declines
hp3 to s3, s3 accepts

1, 1
2, 2
3, 3
"""
