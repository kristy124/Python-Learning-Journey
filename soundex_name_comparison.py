def convert_to_digits(string):
    """
    convert_to_digits - Replaces the letters from the provided string with soundex digits

    :param string: a string we want to convert to soundex digits
    :return: a string converted to soundex digits
    """
    soundex_dict = {
        "aeiouyhw": 0,
        "bfpv": 1,
        "cgjkqsxz": 2,
        "dt": 3,
        "l": 4,
        "mn": 5,
        "r": 6
    }

    string_numbers = ""
    for char in string: # for each character in the string
        for key in soundex_dict:
            if char in key: # if the character is in the key of soundex_dict, add the index of the key
                string_numbers += str(soundex_dict[key])
    return string_numbers


def remove_consecutive_digits(string):
    """
    convert_to_digits - Removes any multiple repeating digits from a string

    :param string: a string to check for multiple repeating digits
    :return: a string without repeating digits
    """

    new_name = ""
    prev_num = ""
    for num in string:
        if num == prev_num:
            continue
        new_name += num
        prev_num = num

    return new_name


def first_digit_check(name, name_without_zeros):
    """
    first_digit_check - Converts the first digit of a digitized name to its initial starting letter based on
    specific conditions

    :param name: a name in lowercase
    :param names_zero_stripped: a list of digitized names without zeros
    :return: a list of soundex digits with its initial starting letter
    """
    F = name[0] # the first letter of the name
    F_number = convert_to_digits(F)  # the digitized first letter of the name
    D = ""
    if len(name_without_zeros) == 0:
        D = F
    elif name_without_zeros[0] == F_number:
        D = F + name_without_zeros[1:]
    elif name_without_zeros[0] != F_number:
        D = F + name_without_zeros
    return D


def soundex_length_check(string):
    """
    soundex_length_check - Converts the length of a string to 4 characters

    :param string: a string of any length
    :return: a string with a length of 4 characters
    """
    new_string = ""
    if len(string) == 4:
        new_string = string
    elif len(string) < 4:
        new_string = string.ljust(4, "0") # ensures the code has a length of 4 by adding "0"s to the right of the string
    elif len(string) > 4:
        new_string = string[:4] # slices the string from index 0 to index 4
    return new_string


def convert_to_soundex(string):
    """
    convert_to_soundex - Converts a string to its soundex code

    :param string: a string of a name
    :return: a string as its soundex code
    """
    name_lower = string.lower()
    name_digitized = convert_to_digits(name_lower)
    name_unrepeated = remove_consecutive_digits(name_digitized)
    name_without_zeros = name_unrepeated.replace("0", "")
    name_first_digit = first_digit_check(name_lower, name_without_zeros)
    soundex_name = soundex_length_check(name_first_digit)
    return soundex_name

def same_soundex_check(paired_names):
    """
    same_soundex_check - Checks for whether a list of names have the same soundex code

    :param paired_names: a list of tuples that store a soundex code and its paired name
    :return: a list of strings that denote which names have the same soundex code
    """
    sorted_names = sorted(paired_names)

    output = []
    for i, (soundex, name) in enumerate(sorted_names):
        for j in range(i, len(sorted_names)):
            if name != sorted_names[j][1]:
                if soundex == sorted_names[j][0]:
                    output.append(f"{name} and {sorted_names[j][1]} have the same Soundex encoding.")
    return output


def main():
    names_list = []
    name_input = input('Enter names, one on each line. Type DONE to quit entering names.\n')

    while name_input != "DONE":
        names_list.append(name_input)
        name_input = input()

    soundex_names = [convert_to_soundex(name) for name in names_list]

    # store the Soundex names in a tuple (soundex,name) for each pair in a list
    paired_names = list(zip(soundex_names, names_list))

    output_to_print = same_soundex_check(paired_names) # returns a list of strings to print later

    for line in output_to_print:
        print(line)


main()