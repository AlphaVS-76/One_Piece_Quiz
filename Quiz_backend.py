from One_Piece_Quiz.Questions_class import Questions

question_prompt = [
    "Q1: What is the thing that Zoro Loves the most?\n(a) Swords\n(b) Sake\n(c) Maps\n",
    "Q2: What is the thing that Luffy Loves the most?\n(a) Bon Chan\n(b) Meat\n(c) More Meat\n",
    "Q3: What is the thing that Sanji Loves the most?\n(a) Girls\n(b) Queers\n(c) Cooking\n(d) Vinsmoke Family\n",
    "Q4: What do One Piece Fans want to know ASAP?\n(a) What is Raftel/LaughTale\n(b) When will we get to see Shanks?\n(c) Who is JoyBoy?\n(d) Who is Imu?\n",
    "Q5: The Best Arc in One Piece?\n(a) Dressrosa\n(b) Whole Cake Island\n(c) MarineFord\n(d) Wano Country\n",
    "Q6: Total number of Poneglyphs?\n(a) 4\n(b) 40\n(c) 30\n(d) 20\n",
    "Q7: Total number of Straw Hat Crew?\n(a) 8\n(b) 9\n(c) 10\n(d) 11\n",
    "Q8: Which is the Monster Trio?\n(a) Borsalino/Issho/Ryukogu\n(b) Luffy/Zoro/Sanji\n(c) Roger/Rayleigh/Oden\n(d) Ace/Luffy/Sabo\n",
    "Q9: Who is the Strongest in Straw Hat Pirates?\n(a) Luffy\n(b) Go D. Usopp\n(c) Zoro\n(d) Sanji\n",
    "Q10: Total Bounty of Straw Hat Pirates?(Approx.)\n(a) 2.0 Billion Berries\n(b) 2.5 Billion Berries\n(c) 3.0 Billion Berries\n(d) 3.5 Billion Berries\n"
]

questions = [
    Questions(question_prompt[0], "b"),
    Questions(question_prompt[1], "c"),
    Questions(question_prompt[2], "a"),
    Questions(question_prompt[3], "b"),
    Questions(question_prompt[4], "d"),
    Questions(question_prompt[5], "c"),
    Questions(question_prompt[6], "c"),
    Questions(question_prompt[7], "b"),
    Questions(question_prompt[8], "b"),
    Questions(question_prompt[9], "c")
]

def run_tests(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("Your Score is = " + str(score) + "/" + str(len(questions)))

run_tests(questions)