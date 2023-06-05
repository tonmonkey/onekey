# Output the result
def input_data(date):
    with open("result.txt", mode="a+",encoding='utf-8') as fd:
        fd.write(date + "\n")