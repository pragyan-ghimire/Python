# questions, 2d options, answers, list of guesses, score, question_num

questions = ("What is 32 + 32?",
             "What is the capital of Nepal?",
             "Who is known as Father of Computer Science?",
             "Who is known as the Father of AI?"
             )

# not really needed (only to know some unnecessary things haha)
options = (("A","B","C","D"),
           ("A","B","C","D"),
           ("A","B","C","D"),
           ("A","B","C","D")
           )

answers = ("A","B","B","D")
guesses = [["64","60","74","54"],
           ["Biratnagar","Kathmandu","Chitwan","Pokhara"],
           ["John McCarthy","Alan Turing","Charles Babbage","Nikola Tesla"],
           ["Albert Einstein","Alan Turing","Charles Babbage","John McCarthy"],
           ]
score = 0
questionNum = 1

print("#"*20,end="")
print()
print("Quiz Game:")
print("#"*20,end="")
print()

# print(len(questions))

for question in questions:
    print(f"{questionNum}. {question}") 
    for option, guess in zip(options[questionNum-1], guesses[questionNum-1]):
        print(f"{option}. {guess}")
    userAns = input("Enter your Guess: (A, B, C or D) ").upper()
    if userAns == answers[questionNum-1]:
        score += 10
    if questionNum == len(questions):
        break
    questionNum += 1
    print()

print(f"Total score: {score}")