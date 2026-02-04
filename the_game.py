#!/usr/bin/env python
import challenge
print("Starting game challenge...")

game = challenge.client(ip_address="cybergame.dk", port=29594)
game.login("vich1000","ITSI-F26")


# Question 0 start
ch_num = 0
print(f"Answering {ch_num}")
def answer0(s):
    return s

game.answer(ch_num, answer0(game.data(ch_num)))
# Question 0 end


# Question 1 start
ch_num = 1
print(f"Answering {ch_num}")
def answer1(num):
    return num*2

game.answer(ch_num, answer1(game.data(ch_num)))
# Question 1 end


# Question 2 start
ch_num = 2
print(f"Answering {ch_num}")
def answer2(s):
    return s.upper()

game.answer(ch_num, answer2(game.data(ch_num)))
# Question 2 end


# Question 3 start
ch_num = 3
print(f"Answering {ch_num}")
def answer3(s):
    return s[::-1]

game.answer(ch_num, answer3(game.data(ch_num)))
# Question 3 end


# Question 4 start
ch_num = 4
print(f"Answering {ch_num}")
def answer4(l):
    l.sort()
    return l

game.answer(ch_num, answer4(game.data(ch_num)))
# Question 4 end


# Question 5 start
ch_num = 5
print(f"Answering {ch_num}")
def answer5(l):
    return l[:3]

game.answer(ch_num, answer5(game.data(ch_num)))
# Question 5 end


# Question 6 start
ch_num = 6
print(f"Answering {ch_num}")
def answer6(l):
    for i in range(len(l)):
        l[i] = l[i]*5
    return l

game.answer(ch_num, answer6(game.data(ch_num)))
# Question 6 end


# Question 7 start
ch_num = 7
print(f"Answering {ch_num}")
def answer7(l):
    return l[5]

game.answer(ch_num, answer7(game.data(ch_num)))
# Question 7 end


# Question 8 start
ch_num = 8
print(f"Answering {ch_num}")
def answer8(l):
    l.sort()
    temp_set = set(l)
    l = list(temp_set)
    return l

game.answer(ch_num, answer8(game.data(ch_num)))
# Question 8 end


input("")
print("Scores... ")
game.score()