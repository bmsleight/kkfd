#!/usr/bin/env python

import logging

def incoming_message(number = "", full_message = ""):
    """ Processing full_message based upon the first verb
    """
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.warning(number + ", " + full_message) 

    verb_mapping = {
    'join': join_request,
    'leave': leave_request,
    'winner': winner,
    'paid': paid
    }
    [verb, rest_of_message] = full_message.split(' ', 1) 
    # Use first word as key verbs
    verb_mapping.get(verb.lower(), 
                     not_valid_messsage
                     )(number, rest_of_message)


def join_request(number = "", rest_of_message = ""):
    """Processing a join request
    """
    print("Join request " + number)
    # Is mobile number already a member
    # Is username already used
    #  Given the above
    #  Welcome message - inc. next deadline
    #  Use templates

def leave_request(number = "", rest_of_message = ""):
    """Processing a leave request
    """
    print("Leave request " + number)

def winner(number = "", rest_of_message = ""):
    """Select a winner for this round
    """
    print("Winner " + number)

def paid(number = "", rest_of_message = ""):
    """Payment details
    """
    print("Wiiner " + number)

def not_valid_messsage(number = "", rest_of_message = ""):
    """Select a winner for this round
    """
    logging.warning("Message not valid")

incoming_message(number = "44123456789", full_message = "Join please")
