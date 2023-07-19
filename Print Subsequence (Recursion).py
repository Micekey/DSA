def print_ss(ques,ans):
    if len(ques) == 0:
        print(ans)
        return
    first = ques[0]
    print_ss(ques[1:],ans + first)
    print_ss(ques[1:],ans + "")

print_ss("abc","")
