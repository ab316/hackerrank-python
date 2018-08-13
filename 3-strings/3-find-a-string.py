# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    sub_length = len(sub_string)
    for i in range(len(string) - sub_length + 1):
        if string[i:i+sub_length] == sub_string:
            count += 1

    return count


string = input()
sub_string = input()
print(count_substring(string, sub_string))
