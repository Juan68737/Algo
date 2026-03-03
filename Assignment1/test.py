from collections import deque

person = {}
hospitals = {}

matchedHospitals = set()
# Initialize all students as unmatched
matchedStudents = {i: None for i in range(1, 4)}

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

# Fill hospital preferences and add all hospitals to unmatched queue
index = 1
for i in range(0, n):
    hospitals[index] = data[i]
    unmatchedHospitals.append(index)
    index += 1

# Fill student preferences
index = 1
for i in range(n, 2*n):
    person[index] = data[i]
    index += 1

# Track which student each hospital will propose to next
next_proposal_index = {h: 0 for h in hospitals}

# Main loop
while unmatchedHospitals:
    h = unmatchedHospitals.popleft()
    hList = hospitals[h]
    i = next_proposal_index[h]

    if i >= n:
        # Hospital has proposed to everyone
        continue

    s = hList[i]
    next_proposal_index[h] += 1  # move to next student for future proposals

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

            # Remove old hospital from matched and put it back to queue
            matchedHospitals.remove(current_hospital)
            unmatchedHospitals.append(current_hospital)
        else:
            # Student rejects new hospital → hospital stays unmatched
            unmatchedHospitals.append(h)

# Print final matches
for student, hospital in matchedStudents.items():
    print(f"Hospital {hospital} is matched with Student {student}")
