# code wars task
def get_grade(s1, s2, s3):
    grading = {
        'A': (90, 101),
        'B': (80, 90),
        'C': (70, 80),
        'D': (60, 70),
        'F': (0, 60)
    }
    avg_score = (s1 + s2 + s3) / 3
    
    for k, v in grading.items():
        if avg_score >= min(v) and avg_score < max(v):
            return k
        

    