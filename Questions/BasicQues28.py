#WAF that replace all occurence of "Python" with "Java" in the previous question

with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Python", "Java")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)