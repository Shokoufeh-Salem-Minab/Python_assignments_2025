# Jānis Sniedze
# js23127
# Homework 8
# Final edit date: 30/12/2025


from typing import Iterable, Tuple


def fullNameFunctional(first: str, last: str) -> str:  # return a normalized full name with title-casing and trimmed spaces
	return f"{first.strip().title()} {last.strip().title()}"  # strip whitespace then title-case both names and join


def averageFunctional(grades: Iterable[float]) -> float:  # compute the average of an iterable of numbers without side effects
	vals = list(grades)  # copy to list so we can test emptiness and iterate safely
	if not vals:
		return 0.0  # return zero when no grades are present to avoid division-by-zero
	return sum(vals) / len(vals)  # standard arithmetic mean


gradesDb: list[float] = []  # module-level simple storage for function-based approach


def addGrade(grade: float) -> None:  # add a grade to the module-level storage coercing to float
	gradesDb.append(float(grade))  # store as float to keep internal consistency


def getGrades() -> Tuple[float, ...]:  # return a snapshot of stored grades as an immutable tuple
	return tuple(gradesDb)  # tuple protects callers from mutating internal list directly


def averageDb() -> float:  # compute the average from the module-level storage
	if not gradesDb:
		return 0.0  # return zero when storage empty
	return sum(gradesDb) / len(gradesDb)  # compute mean of stored grades


def clearGrades() -> None:  # remove all grades from the module-level storage
	gradesDb.clear()  # clear in place so references remain valid


class student:  # a minimal student object storing name and grades for the OOP example
	def __init__(self, first: str, last: str) -> None:  # construct with normalized name parts
		self.first = first.strip().title()  # normalize and store first name
		self.last = last.strip().title()  # normalize and store last name
		self._grades: list[float] = []  # internal mutable list to hold grades

	@property
	def fullName(self) -> str:  # provide a property combining first and last name
		return f"{self.first} {self.last}"  # return the full display name

	def addGrade(self, grade: float) -> None:  # record a single grade for this student
		self._grades.append(float(grade))  # coerce to float for consistent arithmetic

	def getGrades(self) -> Tuple[float, ...]:  # return stored grades as an immutable tuple
		return tuple(self._grades)  # protect internal list from outside mutation

	def average(self) -> float:  # compute average of this student's grades or return zero when none
		if not self._grades:
			return 0.0  # explicit zero for empty grade list
		return sum(self._grades) / len(self._grades)  # arithmetic mean of internal grades


def demo() -> None:  # small demonstration that runs each approach and prints concise results
	print("Functional approach:")
	print(" Full name:", fullNameFunctional("jane", "doe"))  # pure function usage example
	grades = (90, 80, 70)
	print(" Grades:", grades)
	print(" Average:", averageFunctional(grades))  # average computed without side effects

	print("\nFunction-based approach (module state):")
	clearGrades()
	addGrade(100)
	addGrade(85)
	addGrade(75)
	print(" Grades (db):", getGrades())  # snapshot of module-level storage
	print(" Average (db):", averageDb())  # average computed from module storage

	print("\nOOP approach:")
	s = student("alice", "smith")
	s.addGrade(88)
	s.addGrade(92)
	s.addGrade(79)
	print(" Full name:", s.fullName)  # property access on the instance
	print(" Grades:", s.getGrades())  # instance-level grades
	print(" Average:", s.average())  # instance-level average


if __name__ == "__main__":
	demo()

