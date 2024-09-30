#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answ = a / b
        print("Inside answ: {:.1f}".format(answ))
    except:
        answ = None
        print("Inside answ: {}".format(answ))
    finally:
        return answ
