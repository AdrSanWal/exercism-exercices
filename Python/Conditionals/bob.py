def response(hey_bob):
    hey_bob = hey_bob.strip()
    question = hey_bob.endswith('?')
    yell = hey_bob.isupper()
    silence = hey_bob == ''

    bob_response = {
        True: "Whatever.",
        question: "Sure.",
        yell: "Whoa, chill out!",
        question * yell: "Calm down, I know what I'm doing!",
        silence: "Fine. Be that way!",
    }

    return bob_response[True]
