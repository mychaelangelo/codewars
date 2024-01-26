def wave(people):
    num_people = len(people) - people.count(' ') # count all chars except spaces
    people = [people] * num_people # list of people

    curr_word = 0
    curr_letter = 0

    while curr_word < len(people):
        curr_word_as_list = list(people[curr_word])
        if curr_word_as_list[curr_letter] != ' ':
            curr_word_as_list[curr_letter] =  curr_word_as_list[curr_letter].upper()
            people[curr_word] = ''.join(curr_word_as_list)
            curr_word += 1
            curr_letter += 1
        else:
            curr_letter += 1
    return people

print(wave("hi me"))