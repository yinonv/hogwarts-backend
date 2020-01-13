student_list = [{"existing": [{"skill": "Animation", "level": "2"}, {"skill": "Elemental", "level": "5"}], "desired": [{"skill": "Self-detonation", "level": "4"}], "courses": ["Magic for day-to-day life"], "name":"Yinon", "lastName":"Vahab", "createDate":{"date": "10/1/20", "time": "12:10"}, "id": 1},
                {"existing": [{"skill": "Summoning", "level": "1"}, {"skill": "Water breathing", "level": "1"}], "desired": [{"skill": "Possession", "level": "1"}, {"skill": "Animation", "level": "3"}], "courses": [
                    "Magic for medical professionals", "Alchemy basics"], "name":"Gabe", "lastName":"Gordon", "createDate":{"date": "10/1/20", "time": "12:12"}, "id": 2}
                ]


skills_list = ['Alchemy', 'Animation', 'Conjuror', 'Disintegration', 'Elemental', 'Healing', 'Illusion', 'Immortality', 'Invisibility',
               'Invulnerability', 'Necromancer', 'Omnipresent', 'Omniscient', 'Poison', 'Possession', 'Self-detonation', 'Summoning', 'Water breathing']

courses_list = ["Alchemy basics", "Alchemy advanced", "Magic for day-to-day life",
                "Magic for medical professionals", "Dating with magic"]



def update(all_students, single_student):
    for index, student in enumerate(all_students):
        if student["id"] == single_student["id"]:
            all_students[index] = single_student
    return all_students


def get_id(all_students):
    if len(all_students) == 0:
        return 1
    l1 = []
    for student in all_students:
        l1.append(student["id"])
    l1 = sorted(l1)
    for index, num in enumerate(l1):
        if index + 1 is not num:
            return index + 1
    return len(all_students) + 1


def delete(all_students, id):
    for index, student in enumerate(all_students):
        if student["id"] == id:
            all_students.pop(index)
            return True
    return False
