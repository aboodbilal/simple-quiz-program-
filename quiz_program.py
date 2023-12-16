
print("\n\n")
welc ="welcom to the quiz"
print(f"{welc:*^48}")


quiz = {
    "question1": {"question" : "what is the capital of france?", "answer": "paris"},

    "question2 ":{"question": "what is the capital of germany?", "answer" : "berlin"},

    "question3":{"question":"what is the capital of italy?","answer": "rome" },
    
    "question4":{"question":"what is the capital of spain?","answer": "madrid" },

    "question5":{"question":"what is the capital of palestine?","answer": "jerusalem"},

    "question6":{"question":"what is the capital of jordan?","answer": "amman" },
    
    "question7":{"question":"what is the capital of egypt?","answer": "cairo"},
 }
 
score = 0
for key, value in quiz.items():
    print(f"{key:*^19}")
    print(value["question"])
    answer = input("answer?")

    if answer.lower() == value["answer"].lower():
        print("correct\n")
        score +=1 
        
        

    else:
        print("wrong\n")
        print(f"the answer is {value['answer']}\n")
       


print(f"you got {score} of of 7 cerrectly")
print(f"your perecentage  is {int((score/7)*100)}%")
