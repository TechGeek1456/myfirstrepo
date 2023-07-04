def max_3_nums(*args):
    my_list=list(args)
    if len(my_list)>3:
        return "more than 3 numbers passed"
    else:
        return(max(my_list))


result=max_3_nums(1,2,3,4)
print(result)