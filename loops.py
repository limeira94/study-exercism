"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    list_score = []
    index = 0 
    while index < len(student_scores):
        round_score = round(student_scores[index])
        list_score.append(round_score)
        index += 1
    return list_score
    
def count_failed_students(student_scores):
    
    count = 0
    for student in student_scores:
        if student <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    return [student for student in student_scores if student >= threshold]


def letter_grades(highest):
    
    threashold = round((highest - 41) / 4)
    D = 41 
    C = D + threashold
    B = C + threashold
    A = B + threashold
    return [D, C, B, A]  


def student_ranking(student_scores, student_names):
    ranked_students = zip(student_scores, student_names)    
    list_students = []
    for rank, (score, name) in enumerate(ranked_students):
        list_students.append(f'{rank + 1}. {name}: {score}')
    return list_students


def perfect_score(student_info):
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []