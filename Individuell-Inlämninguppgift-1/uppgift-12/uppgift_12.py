# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list) -> dict:
    """
    Returnerar en dictionary där namnet är nyckeln och åldern är värdet.
    """
    student_register = {}
    for name, age in students:
        student_register[name] = age
    return student_register

print(create_student_register([("Johan", 30), ("Anna", 25), ("Bobby", 32), ("Viktor", 24)]))
