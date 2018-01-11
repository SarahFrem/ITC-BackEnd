import random
good_answers = 0
bad_answers = []

def addition(number1,number2):
    return number1+number2

def substraction(number1,number2):
    return number1-number2

def multiplication(number1,number2):
    return number1*number2

def division(number1,number2):
    return float(number1)/number2

def random_choice(start=0):
    operators=["+","-","*","/"]
    random_value_1 = random.randint(0,101)
    random_value_2 = random.randint(start,101)
    random_operators = operators[random.randint(0,len(operators)-1)]

    return (random_value_1,random_operators,random_value_2)

def play():
    global good_answers
    test = False
    result, result_division, user_answer = None, None, None

    number_1 = random_choice()[0]
    operator = random_choice()[1]

    if operator == '/':
        number_2 = random_choice(1)[2] #can not be 0
    else:
        number_2 = random_choice(0)[2] #can be 0


    print str(number_1) + operator + str(number_2) + ' =?'

    while not test:
        user_answer = raw_input("Please enter the result: ")  # be careful return a string
        try:
            float(user_answer) # can be int or float
            test = True
        except:
            pass  # conversion failed
            test = False

    if operator == '+':
        result = addition(number_1, number_2)
    elif operator == '-':
        result = substraction(number_1, number_2)
    elif operator == '*':
        result = multiplication(number_1, number_2)
    elif operator == '/':
        result_division = round(division(number_1, number_2), 2) #round the floating point value number

    if result == float(user_answer) or result_division == round(float(user_answer),2):
        print 'good job'
        good_answers += 1
    else:
        print 'wrong answer'
        if result!=None:
            print 'the right answer is:' + str(result)
            bad_answers.append(str(number_1) + operator + str(number_2) + ' ='+user_answer+' ('+str(result)+')')
        else:
            print 'the right answer is:' + str(result_division)
            bad_answers.append(str(number_1) + operator + str(number_2) + ' ='+user_answer+' ('+str(result_division)+')')

def summary_result_user():
    global good_answers
    percentage = round(float(good_answers)/(good_answers+len(bad_answers))*100, 2) #if no float, it will return 0 as an integer division
    if len(bad_answers) != 0:
        print 'summary of your bad results'
        for element in bad_answers:
            print element
    return 'You have answered correctly ' +str(good_answers)+ ' out of ' +str(good_answers+len(bad_answers))+ ' problems ('+ str(percentage)+'%)'
    #return bad_answers,len(bad_answers),good_answers,percentage


def want_to_play():
    global good_answers
    print 'welcome to elementary maths review'
    want_to = True
    while want_to:
        want_answer = raw_input('Do you still want to play ?').lower()
        if want_answer in ('yes','y'):
            play()
        elif want_answer in ('no','n',""):
            want_to = False
            if good_answers+len(bad_answers)==0: #avoid error for percentage with 0 answers
                print 'ok bye'
            else:
                print 'ok , here you are your summary: '
                print summary_result_user()


print want_to_play()



