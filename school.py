class School():
    def __init__(self, name=None):
        self.name = name
        self._roster = {}
    def roster(self):
        return {x:self._roster[x] for x in sorted(self._roster.keys())}
    def add_student(self, student, grade):
        if self._roster.get(grade) != None:
            self._roster[grade].append(student)
        else:
            self._roster.update({grade : [student]})
    def grade(self, grade):
        return self._roster[grade]
    def sort_roster(self):
        return {x:sorted(self._roster[x]) for x in sorted(self._roster.keys())}
            
        