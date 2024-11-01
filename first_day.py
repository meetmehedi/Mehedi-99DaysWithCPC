
subjects = ['Math', 'Science', 'English', 'History', 'Art']
num_students = 100
data = {
    'Student_ID': [f"S{i+1:03}" for i in range(num_students)],
    'Math': np.random.randint(50, 100, num_students),
    'Science': np.random.randint(50, 100, num_students),
    'English': np.random.randint(50, 100, num_students),
    'History': np.random.randint(50, 100, num_students),
    'Art': np.random.randint(50, 100, num_students),
      }
df = pd.DataFrame(data)
df['Average'] = df[subjects].mean(axis=1)

average_per_subject = df[subjects].mean()
max_per_subject = df[subjects].max()
min_per_subject = df[subjects].min()

top_student = df.loc[df['Average'].idxmax()]
bottom_student = df.loc[df['Average'].idxmin()]

print("Average Grades per Subject:")
print(average_per_subject)
print("\nMaximum Grades per Subject:")
print(max_per_subject)
print("\nMinimum Grades per Subject:")
print(min_per_subject)

print("\nTop Student:")
print(top_student[['Student_ID', 'Average']])
print("\nBottom Student:")
print(bottom_student[['Student_ID', 'Average']])
