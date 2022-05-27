class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def show(self):
        print('The name of the student is', self.name, ',', 'he is', self.age, 'years old,',
              'his selected tracks are: ', self.tracks, 'and he got a score of', self.score,)
        
    # To change student name

    def change_name(self, new_name):
        self.name = str(new_name)
    # To change student age

    def change_age(self, new_age):
        self.age = int(new_age)
    # To add new track to the existing one

    def add_track(self, new_tracks):
        self.tracks.append(new_tracks)
    # To change student score

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
Bob.show()
