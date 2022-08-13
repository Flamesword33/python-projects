# old example data
lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], \
"quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], \
"quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = { "name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], \
"quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}


#subject
mat_alj = {'class': 'Linear Aljabra',\
           'homework':[0.9, 0.95, 0.88, 0.89, 0.83], 'quizzes':[1, 0.95], 'tests':[0.82, 0.5], 'final':[0], 'labs':[0],\
           'h': [.1] 'q': [.1], 't': [.35], 'f': [.45],'l':[0]}
mat_cal = {'class': 'Advanced Calculus',\
           'homework':[1, 0.95, 0.94, 0.64, 0.89], 'quizzes':[0.8, 0.75, 0.75], 'tests':[0.74], 'final':[0], 'labs': [0],\
           'h': [.12], 'q': [.24], 't': [.24], 'f': [.4], 'l':[0]}
phy = {'class': 'Physics',\
       'homework':[0.72, 0.8, 0.8, 0.72, 0.96], 'quizzes':[0], 'tests':[0.73,0.68], 'labs':[0.7], 'final':[0], \
       'h': [.15], 'q': [0], 't': [.3], 'l': [.2], 'f': [.35]}
csc = {'class': 'Java Computer Science', \
       'homework':[0.91, 0.55, 0.79, 0.6,0.8], 'quizzes':[0], 'tests':[0.98, 0.71],'final':[0] ,'labs':[0]\
       'h':[.2], 'q':[0], 't':[.4],'f':[.4],'l': [0]}

def average(numbers):
    'basic averaging of numbers'
    total = sum(numbers)
    total = float(total)
    average = total / len(numbers)
    return average

def get_average(student):
    'calculates weighted averages'
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    labs = average(student['labs'])
    final_test = average(student['final'])
    # single letters stand for grade weighting
    final = (homework * student['h']) + (quizzes * student['q'])\
            + (tests * student['t']) + (labs * student['l']) + (final_test * student['f'])
    return final
    
def get_letter_grade(score):
    'converts marks into letter grades'
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
        
def get_class_average(students):
    'uses a list of class'
    results = []
    for individual in students:
        results.append(get_average(individual))
    return average(results)
