print("The Love Calculator gonna calculate your score...")
name_1 = input("Name: ").lower().strip()
name_2 = input("Name: ").lower().strip()

name_couple = name_1 + name_2

score_1 = 0
score_2 = 0

for i in list(name_couple):
    match i:
        case 't':
            score_1 += 1
        case 'r':
            score_1 += 1
        case 'u':
            score_1 += 1
        case 'e':
            score_1 += 1
        
for i in list(name_couple):
    match i:    
        case 'l':
            score_2 += 1
        case 'o':
            score_2 += 1
        case 'v':
            score_2 += 1
        case 'e':
            score_2 += 1

love_score = int(str(score_1) + str(score_2))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print("Your score is " + str(love_score)) 
