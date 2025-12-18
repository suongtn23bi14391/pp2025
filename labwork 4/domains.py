import numpy as np

class Student:
    def __init__(self, id, name, DoB):
        self._id = id
        self._name = name
        self._DoB = DoB
        self.marks = {} 
        self.gpa = 0.0

    def calculate_gpa(self, courses_list):
        if not self.marks: return 0.0
        scores = []
        credits = []
        course_map = {c.getId(): c.getCredits() for c in courses_list}
        
        for c_id, score in self.marks.items():
            if c_id in course_map:
                scores.append(score)
                credits.append(course_map[c_id])
        
        np_scores = np.array(scores)
        np_credits = np.array(credits)
        self.gpa = np.sum(np_scores * np_credits) / np.sum(np_credits) if np_credits.sum() > 0 else 0.0
        return self.gpa

    def getId(self): return self._id
    def getName(self): return self._name
    class Course:
    def __init__(self, id, name, credits):
        self._id = id
        self._name = name
        self._credits = credits
    
    def getId(self): return self._id
    def getName(self): return self._name
    def getCredits(self): return self._credits