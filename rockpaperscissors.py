"""
This is the Rock Paper Scissors Game
One player game with computer On pop browser 
"""


import random
import simplegui

h_choice = ""
c_choice = ""
H_SCORE = 0
C_SCORE = 0
Tie_score = 0

def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissor'])
def rock():
    global h_choice, c_choice
    h_choice = 'Rock'
    c_choice = computer_choice()
    choice_result(h_choice, c_choice)
def paper():
    global h_choice, c_choice
    h_choice = 'Paper'
    c_choice = computer_choice()
    choice_result(h_choice, c_choice)
def scissor():
    global h_choice, c_choice
    h_choice = 'Scissor'
    c_choice = computer_choice()  
    choice_result(h_choice, c_choice)
def choice_result(H_choice,C_choice):
    global h_choice, c_choice
    global H_SCORE, C_SCORE, Tie_score
    if h_choice == 'Rock' and c_choice == 'Paper':
        C_SCORE += 1
    elif h_choice == 'Rock' and c_choice == 'Scissor':
        H_SCORE += 1
    elif h_choice == 'Paper' and c_choice == 'Scissor':
        C_SCORE += 1
    elif h_choice == 'Paper' and c_choice == 'Rock':
        H_SCORE += 1
    elif h_choice == 'Scissor' and c_choice == 'Rock':
        C_SCORE += 1
    elif h_choice == 'Scissor' and c_choice == 'Paper':
        H_SCORE += 1
    elif h_choice == c_choice:
        Tie_score += 1

def draw(canvas):
    global Tie_flag
    try:
        canvas.draw_text("You: " + h_choice, [10,40], 48, "Cyan")
        canvas.draw_text("Comp: " + c_choice, [10,80], 48, "Yellow")
        canvas.draw_text("Your Score: " + str(H_SCORE), [10,150], 25, "Cyan")
        canvas.draw_text("Computer Score: " + str(C_SCORE), [10,190], 25, "Yellow")
        canvas.draw_text("Tie Score: " + str(Tie_score), [10,230], 35, "Orange")
    except TypeError:
        pass
def play_rps():
    frame = simplegui.create_frame("Rock Paper Scissor", 400, 300)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissor)
    frame.set_draw_handler(draw)
    frame.start()
 
play_rps()