name, age, score = "Ruwin", 29, 95.5

print("I'm " + name + " and I'm " + str(age) + " years old." + " My score is " + str(score) + ".")

print("I'm %s and I'm %d years old. My score is %.1f." %(name, age, score))
print("I'm %s and I'm %d years old. My score is %.2f." %(name, age, score))

print("I'm {} and I'm {} years old. My score is {}.".format(name, age, score))
print("I'm {2} and I'm {0} years old. My score is {1}.".format(age, score, name))

print(f"I'm {name} and I'm {age} years old. My score is {score}.")