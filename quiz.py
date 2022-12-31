import socket 
from threading import Thread
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

server.bind((ip_address,port))

server.listen()

print("Server is running")

students = []
questions = ["What is the Italian word for PIE? \n a.Mozarellain \n b. Pastyin \n c.Patty \n d.pizza", "Water boils at 212 Units at which scale? a.Fahrenheitin b.Celsiusin c.Rankinen d.Kelvin \n","Which sea creature has three hearts? \n a.Dolphin\n b.Octopusin \n c.Walrusin \n d.Seal", "Who was the character famous in our childhood rhymes associated with a Lamb? In a.Mary\n b. Jack \n c. Johnny\n d.Mukesh", "How many bones does an adult human have? In a.206\n b.208\n c.201\n d.196", "How many wonders are there in the world? In a.7\n b.8\n c.10\n d.4", "What element does not exist? In a.Xf\n b.Rein c.Si\n d. Pa", "How many states are there in India? In a.24\n b.29\n c.30\n d.31", "Who invented the telephone? In a.A.G Bell\n b.John Wick \n c. Thomas Edison\n d.G Marconi", "Who is Loki? \n a.God of Thunder \n b.God of Dwarves in c.God of Mischief in d.God of Goda", "Who was the first Indian female astronaut ? \n a.Smita Williams\n b.Kalpana Chavla\n c.Hone of them\n d. Both of them ", "What is the mallest continent? In a.Asia\n b.Antarcticin c.Africain 4.Australia", "The beaver is the national embeles of which country? In a.Zimbabwe in b.Iceland in c.Argentina in d.Canada", "Bow many players are on the field in baseball? In a.6\n b. 7\n c.9\n Bg stands for? \n a.Mercuryn b.Bulgeriumin a.Argeninela d.Halfnium"]
answers = ["d","a","b","a","a","a","a","b","a","c","b","d","d","c","a","b","a"]

def client_thread(con,addr):
    score = 0

    con.send("Welcome to the QUIZ".encode("utf-8"))
    con.send("Each Questions answer should be given in chat. Either A,B,C or D should be entered.".encode("utf-8"))
    con.send("GOOD LUCK".encode("utf-8"))

    index, question, answer = get_random_question_answer(con)

    while True:
        try:
            message = con.recv(2048).decode("utf-8")
            if message:
                if message.lower() == answer:
                    score += 1
                    con.send("Correct answer! Your score is: {score}\n\n".encode("utf-8"))
                else:
                    con.send("Incorrect answer!".encode("utf-8"))
                remove_question(index)
                index,question,answer = get_random_question_answer(con)
            else:
                remove(con)
        except:
            continue


def remove(con):
    if con in students: 
        students.remove(con)

def remove_question(index):
    questions.pop(index)
    answers.pop(index)


def get_random_question_answer():
    random_index = random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    con.send(random_question.encode("utf-8"))
    return random_index,random_question,random_answer



def brodcast(messageToSend,con):
    for student in students:
        if student != con:
            try:
                student.send(messageToSend.encode("utf-8"))
            except:
                remove(student)

while True:
    con,addr = server.accept()
    students.append(con)

    print(addr[0]+"Connected")

    new_thread = Thread(target=client_thread,args=(con,addr))
    new_thread.start()




