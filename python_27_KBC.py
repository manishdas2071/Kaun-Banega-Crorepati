# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

from playsound import playsound


Q1 = ['What is the capital of India?', 'A. Mumbai', 'B. Chennai', 'C. Kolkata', 'D. New Delhi'] #D - 1000
Q2 = ['Who wrote the Indian national anthem?', 'A. Bankim Chandra Chatterjee', 'B. Harivansh Rai Bachchan', 'C. Rabindranath Tagore', 'D. Subramania Bharati'] #C - 2000
Q3 = ['Which planet is known as the red planet?', 'A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'] #B - 3000
Q4 = ['Which gas do humans need to breathe?', 'A. Carbon Dioxide', 'B. Hydrogen', 'C. Oxygen', 'D. Nitrogen'] #C - 5000
Q5 = ['What is the currency of Japan?', 'A. Yen', 'B. Won','C. Ringgit','D. Baht'] #A - 10,000
Q6 = ['What is the chemical symbol of water?', 'A. CO2','B. H2O','C. NaCl','D. O2'] #B - 20,000
Q7 = ['Who invented the telephone?','A. Thomas Edison','B. Alexander Graham Bell','C. Nikola Tesla', 'D. Isaac Newton'] #B - 40,000
Q8 = ['In which year did India gain independence?','A. 1945','B. 1950','C. 1947','D. 1935'] #C - 80,000
Q9 = ['Who was the first President of India?','A. Sardar Vallabhbhai Patel','B. Rajendra Prasad','C. Dr. Rajendra Prasad','D. Zakir Husain'] #C - 1,60,000
Q10 = ['Which is the longest river in the world?', 'A. Amazon','B. Yangtze','C. Mississippi','D. Nile'] #D - 3,20,000
Q11 = ['What is the main source of energy for the Earth?', 'A. Sun', 'B. Moon', 'C. Fire', 'D. Coal'] #A - 6,40,000
Q12 = ['How many players are there in a cricket team?','A. 10', 'B. 11', 'C. 12', 'D. 9'] #B - 12,50,000
Q13 = ['What is the national flower of India?', 'A. Rose', 'B. Lotus','C. Marigold','D. Jasmine'] #B - 25,00,000
Q14 = ['Who wrote the Ramayana?', 'A. Valmiki', 'B. Vyasa', 'C. Tulsidas', 'D. Kalidasa'] #A - 50,00,000
Q15 = ['Which Indian city is known as the Pink City?','A. Udaipur','B. Bhopal','C. Jaipur', 'D. Jodhpur'] #C - 1,00,00,000
Q16 = ['Who is the President of India?', 'A. Narendra Modi','B. Droupadi Murmu','C. Nirmala Sitharaman','D. Nitin Jairam Gadkari'] #B - 7,00,00,000

kbc = 'Welcome to Kaun Banega Crorepati'
print(kbc.center(50))
playsound(r"Audio/Intro.mp3")

price = '₹ 1000'                                                #1st Question
print(price.center(50))
for i in range(5):
    print(Q1[i])
ans = input('Enter your choice: ')
if ans == 'D':
    print('CONGRATULATIONS!! \nYou Won 1000')
else :
    print('SORRY, YOU LOST!!')
    exit()

price = '₹ 2000'                                                #2nd Question
print(price.center(50))
for i in range(5):
    print(Q2[i])
ans = input('Enter your choice: ')
if ans == 'C':
    print('CONGRATULATIONS!! \nYou Won 2000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 1000')
    exit()

price = '₹ 3000'                                                #3rd Question
print(price.center(50))
for i in range(5):
    print(Q3[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 3000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 2000')
    exit()

price = '₹ 5000'                                                #4th Question
print(price.center(50))
for i in range(5):
    print(Q4[i])
ans = input('Enter your choice: ')
if ans == 'C':
    print('CONGRATULATIONS!! \nYou Won 5000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 3000')
    exit()

price = '₹ 10,000'                                               #5th Question
print(price.center(50))
for i in range(5):
    print(Q5[i])
ans = input('Enter your choice: ')
if ans == 'A':
    print('CONGRATULATIONS!! \nYou Won 10,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 5000')
    exit()

price = '₹ 20,000'                                               #6th Question
print(price.center(50))
for i in range(5):
    print(Q6[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 20,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 10,000')
    exit()

price = '₹ 40,000'                                              #7th Question
print(price.center(50))
for i in range(5):
    print(Q7[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 40,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 20,000')
    exit()

price = '₹ 80,000'                                              #8th Question
print(price.center(50))
for i in range(5):
    print(Q8[i])
ans = input('Enter your choice: ')
if ans == 'C':
    print('CONGRATULATIONS!! \nYou Won 80,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 40,000')
    exit()

price = '₹ 1,60,000'                                            #9th Question
print(price.center(50))
for i in range(5):
    print(Q9[i])
ans = input('Enter your choice: ')
if ans == 'C':
    print('CONGRATULATIONS!! \nYou Won 1,60,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 80,000')
    exit()

price = '₹ 3,20,000'                                            #10th Question
print(price.center(50))
for i in range(5):
    print(Q10[i])
ans = input('Enter your choice: ')
if ans == 'D':
    print('CONGRATULATIONS!! \nYou Won 3,20,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 1,60,000')
    exit()

price = '₹ 6,40,000'                                            #11th Question
print(price.center(50))
for i in range(5):
    print(Q11[i])
ans = input('Enter your choice: ')
if ans == 'A':
    print('CONGRATULATIONS!! \nYou Won 6,40,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 3,20,000')
    exit()

price = '₹ 12,50,000'                                           #12th Question
print(price.center(50))
for i in range(5):
    print(Q12[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 12,50,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 6,40,000')
    exit()

price = '₹ 25,00,000'                                           #13th Question
print(price.center(50))
for i in range(5):
    print(Q13[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 25,00,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 12,50,000')
    exit()

price = '₹ 50,00,000'                                            #14th Question
print(price.center(50))
for i in range(5):
    print(Q14[i])
ans = input('Enter your choice: ')
if ans == 'A':
    print('CONGRATULATIONS!! \nYou Won 50,00,000')
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 25,00,000')
    exit()

price = '₹ 1 Crore'                                             #15th Question
print(price.center(50))
for i in range(5):
    print(Q15[i])
ans = input('Enter your choice: ')
if ans == 'C':
    print('CONGRATULATIONS!! \nYou Won 1 Crore')
    playsound(r"Audio\Last Question.mp3")
else :
    print('SORRY, YOU LOST!! \n The Won Amount is ₹ 50,00,000')
    exit()

price = '₹ 7 Crore'                                             #16th Question
print(price.center(50))
for i in range(5):
    print(Q16[i])
ans = input('Enter your choice: ')
if ans == 'B':
    print('CONGRATULATIONS!! \nYou Won 7 Crore')
    playsound(r"Audio\Winner.mp3")
    print('You are welcomed for the Next Season of Kaun Banega Crorepati')
else :
    print('SORRY, IT WAS A WRONG ANSWER AND YOU NEED TO BE HAPPY WITH 1,00,00,000')
    exit()
