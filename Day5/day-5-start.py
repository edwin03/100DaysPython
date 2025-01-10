fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
	print(fruit)

stu_scores = [100,1,2,3,101]
total_exam_score = sum(stu_scores)
print(f"This is the sum {total_exam_score}")

summ = 0
for score in stu_scores:
	summ += score

print(f"sum is {summ}")

#Find the max number
maxs = max(stu_scores)
print(f"This is the maxs {maxs}")

highest = 0
for score in stu_scores:
	if score > highest:
		highest = score
print(f"highest number is {highest}")

for number in range(1,10):# this does not print the 10
	print(number)

# This is for stepping. The last parameter is the stepper.
for number in range(1,10, 2):# this does not print the 10
	print(number)

 #Gauss Challange
summer = 0
for num in range(1, 101):
	summer += num
print(summer)

#FizzBuzz game

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)