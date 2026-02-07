#!/usr/bin/env python
import challenge
import hashlib
import ast
print("Starting game challenge...")

game = challenge.client(ip_address="cybergame.dk", port=29594)
game.login("vich1000","ITSI-F26")
"""
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


# Question 9 start
ch_num = 9
print(f"Answering {ch_num}")
def answer9(s):
    s = s.replace("be","python")
    return s

game.answer(ch_num, answer9(game.data(ch_num)))
# Question 9 end


# Question 10 start
ch_num = 10
print(f"Answering {ch_num}")
def answer10(s):
    s = s[:33] + "star"[::-1]
    return s

game.answer(ch_num, answer10(game.data(ch_num)))
# Question 10 end


# Question 11 start
ch_num = 11
print(f"Answering {ch_num}")
def answer11(n):
    ret_lst = []
    for i in range(20):
        ret_lst.append(n+i*5)
    return ret_lst

game.answer(ch_num, answer11(game.data(ch_num)))
# Question 11 end


# Question 12 start
ch_num = 12
print(f"Answering {ch_num}")
def answer12(lst):
    search_str = '192.168.1.212'
    connections = 0
    for i in lst:
        if i[0] == search_str:
            connections = i[1]
    return connections

game.answer(ch_num, answer12(game.data(ch_num)))
# Question 12 end


# Question 13 start
ch_num = 13
print(f"Answering {ch_num}")
def answer13(lst):
    return sum(lst)

game.answer(ch_num, answer13(game.data(ch_num)))
# Question 13 end


# Question 14 start
ch_num = 14
print(f"Answering {ch_num}")
def answer14(s):
    ret_lst = []
    comma_split = s.split(',')
    for i in comma_split:
        name, number = i.split(':')
        ret_lst.append((name, number))
    return ret_lst

game.answer(ch_num, answer14(game.data(ch_num)))
# Question 14 end


# Question 15 start
ch_num = 15
print(f"Answering {ch_num}")
def answer15(dic):
    dic.pop("192.168.1.243")
    return dic

game.answer(ch_num, answer15(game.data(ch_num)))
# Question 15 end

# Question 16 start
ch_num = 16
print(f"Answering {ch_num}")
def answer16(sentence):
    ret_s = []
    sentence_split = sentence.split()
    for s in sentence_split:
        ret_s.append(s[::-1])
    return " ".join(ret_s)

game.answer(ch_num, answer16(game.data(ch_num)))
# Question 16 end


# Question 17 start
ch_num = 17
print(f"Answering {ch_num}")
def answer17(tup):
    ret_lst = []
    for _ in range(10):
        ret_lst.append(tup)
    return ret_lst 

game.answer(ch_num, answer17(game.data(ch_num)))
# Question 17 end


# Question 18 start
ch_num = 18
print(f"Answering {ch_num}")
def answer18(dic):
    dic["yellow"] = 22
    return dic

game.answer(ch_num, answer18(game.data(ch_num)))
# Question 18 end


# Question 19 start
ch_num = 19
print(f"Answering {ch_num}")
def answer19(log):
    ips = set()
    log_lines = log.split("\n")
    for line in log_lines:
        if len(line) > 5:
            ips.add(line.split()[0])
    return ips

game.answer(ch_num, answer19(game.data(ch_num)))
# Question 19 end


# Question 20 start
ch_num = 20
print(f"Answering {ch_num}")
def answer20(log):
    dic = {}
    log_lines = log.split("\n")
    for line in log_lines:
        if len(line) > 5:
            status = line.split()[-2]
            n = 0
            if status in dic:
                n = dic[status]
            n += 1
            dic[status] = n
    return dic

game.answer(ch_num, answer20(game.data(ch_num)))
# Question 20 end


# Question 21 start
ch_num = 21
print(f"Answering {ch_num}")
def answer21(log):
    n = 0
    avg_sum = 0
    log_lines = log.split("\n")
    for line in log_lines:
        if len(line) > 5:
            line_split = line.split()
            if line_split[-2] == "200":
                n += 1
                avg_sum += int(line_split[-1])

    return int(avg_sum/n)

game.answer(ch_num, answer21(game.data(ch_num)))
# Question 21 end


# Question 22 start
ch_num = 22
print(f"Answering {ch_num}")
def answer22(log):
    n = 0
    log_lines = log.split("\n")
    for line in log_lines:
        if ".png" in line:
            n += 1
    return n

game.answer(ch_num, answer22(game.data(ch_num)))
# Question 22 end


# Question 23 start
ch_num = 23
print(f"Answering {ch_num}")
def answer23(lst):
    dic = {}
    for tup in lst:
        dic[tup[1]] = tup[0]
    return dic

game.answer(ch_num, answer23(game.data(ch_num)))
# Question 23 end


# Question 24 start
ch_num = 24
print(f"Answering {ch_num}")
def answer24(lst):
    lst = []
    for n in range(101):
        if n % 3 == 0:
            continue
        lst.append(n)
    return lst

game.answer(ch_num, answer24(game.data(ch_num)))
# Question 24 end


# Question 25 start
ch_num = 25
print(f"Answering {ch_num}")
def answer25(sha):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for c0 in chars:
        for c1 in chars:
            for c2 in chars:
                for c3 in chars:
                    test_code = f"{c0}{c1}{c2}{c3}"
                    sha_code = hashlib.sha1(test_code.encode()).hexdigest()
                    if sha == sha_code:
                        return test_code


game.answer(ch_num, answer25(game.data(ch_num)))
# Question 25 end


# Question 26 start
ch_num = 26
print(f"Answering {ch_num}")
def answer26(data):
    data = ast.literal_eval(data)
    passw = ""
    sha = data[0]
    test_data = data[1]
    #[
    #    ("Lars","Hansen","05","09","1984"),
    #    ("fido"),
    #    ("jan","08","08","2014"),
    #    ("barcelona","fodbold")
    #]

#game.answer(ch_num, answer26(game.data(ch_num)))
# Question 26 end


# Question 27 start
ch_num = 27
print(f"Answering {ch_num}")
def answer27(s):
    words = s.split(", ")
    if words[0] != "application":
        return "application"
    if words[1] != "transport":
        return "transport"
    if words[2] != "network":
        return "network"
    if words[3] != "link":
        return "link"
    if words[4] != "physical":
        return "physical"

game.answer(ch_num, answer27(game.data(ch_num)))
# Question 27 end


# Question 28 start
ch_num = 28
print(f"Answering {ch_num}")
def answer28(s):
    items = s.split(", ")
    for i in items:
        if ':' in i:
            if len(i) == len("xx:xx:xx:xx:xx:xx"):
                return i

game.answer(ch_num, answer28(game.data(ch_num)))
# Question 28 end


# Question 29 start
ch_num = 29
print(f"Answering {ch_num}")
def answer29(p):
    return 39

game.answer(ch_num, answer29(game.data(ch_num)))
# Question 29 end


# Question 30 start
ch_num = 30
print(f"Answering {ch_num}")
def answer30(p):
    return 3775708311

game.answer(ch_num, answer30(game.data(ch_num)))
# Question 30 end


# Question 31 start
ch_num = 31
print(f"Answering {ch_num}")
def answer31(p):
    return "0.client-channel.google.com"

game.answer(ch_num, answer31(game.data(ch_num)))
# Question 31 end


# Question 32 start
ch_num = 32
print(f"Answering {ch_num}")
def answer32(s):
    floor = 0
    room = 0
    for char in s:
        match char:
            case "^":
                floor += 1
            case "v":
                floor -= 1
            case ">":
                room += 1
            case "<":
                room -= 1
    return (floor, room)

game.answer(ch_num, answer32(game.data(ch_num)))
# Question 32 end
"""


# Question 33 start
ch_num = 33
print(f"Answering {ch_num}")

def calc(n):
    y = 0
    for i in range(n):
        y += 1+i
    return y

def answer33(s):
    last_move = ""
    count = 0
    floor = 0
    room = 0
    for char in s:
        match char:
            case "^":
                amount = 1
                if last_move == char:
                    count += 1
                    amount = calc(count)
                else:
                    count = 0
                    last_move = char
                floor += amount
            case "v":
                amount = 1
                if last_move == char:
                    count += 1
                    amount = calc(count)
                else:
                    count = 0
                    last_move = char
                floor -= amount
            case ">":
                amount = 1
                if last_move == char:
                    count += 1
                    amount = calc(count)
                else:
                    count = 0
                    last_move = char
                room += amount
            case "<":
                amount = 1
                if last_move == char:
                    count += 1
                    amount = calc(count)
                else:
                    count = 0
                    last_move = char
                room -= amount
    if floor < 0:
        floor = 100 - floor
    if room < 0:
        room = 100 - room
    return (floor, room)

game.answer(ch_num, answer33(game.data(ch_num)))
# Question 33 end



get_score = input("get scores? y/n: ")
if get_score == "y":
    print("Scores... ")
    game.score()