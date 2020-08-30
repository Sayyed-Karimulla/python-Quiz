name=str(input("Enter your name:"))
question_prompts = ["In Python 3, the maximum value for an integer is 2^63-1:\na true\nb false",
                    "In a Python program,a control structure:\na Manages the input and output of control characters\nb Dictates what happens before the program starts and after it terminates\nc Directs the order of execution of the statements in the program yes\nd Defines program-specific data structures",
                    "Which one of the following if statements will not execute successfully:\na if (1, 2):\n    print('foo')\nb if (1, 2):\n\n   print('foo')\nc if (1, 2):\nprint('foo')\nd if (1, 2):\nprint('foo')",
                    "What signifies the end of a statement block or suite in Python?\na }\nb A comment\nc A line that is indented less than the previous line\nd end",
                    "The value 1.73 rounded to one decimal place using the rounding up  strategy is…\na 1.8\nb 1.7",
                    "In Python, strings are…\na immutable yes\nb str objects\nc changeable\nd char arrays",
                    "The minsplit parameter to split() specifies the minimum number of splits to make to the input string.\na True\nb False"
                   ]


class Question:
    def __init__(self,prompts,answers):        
        self.prompts=prompts
        self.answers=answers
question=[Question(question_prompts[0],"b"),
          Question(question_prompts[1],"a"),
          Question(question_prompts[2],"c"),
          Question(question_prompts[3],"c"),
          Question(question_prompts[4],"a"),
          Question(question_prompts[5],"a"),
          Question(question_prompts[6],"b")]
def run_test(question):
    score=0
    for questions in question:
        answer= input(questions.prompts)
        if answer==questions.answers:
            score+=1
    print(name  + str(score) + "/" + str(len(question)) +"correct")
run_test(question)
 
