import matplotlib.pyplot as plt
data = {'ENG': 10, 'MATH': 25, 'PHY': 35, 'CHY': 35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize=(10, 5))
plt.bar(courses, values)  # Use plt.barh for a horizontal bar chart
plt.title('Course Grades')
plt.xlabel('Grades')
plt.ylabel('Courses')
plt.show()
