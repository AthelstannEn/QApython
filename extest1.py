data = []

for i in range(5):
    data.append(lambda x: x + i)

#задать вопрос Игорю
print(data[+1](10))
print(data[1](10))