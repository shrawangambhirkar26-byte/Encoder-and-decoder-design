# 8 to 3 Encoder

def encoder(inputs):

    if inputs[0]==1:
        return "000"
    elif inputs[1]==1:
        return "001"
    elif inputs[2]==1:
        return "010"
    elif inputs[3]==1:
        return "011"
    elif inputs[4]==1:
        return "100"
    elif inputs[5]==1:
        return "101"
    elif inputs[6]==1:
        return "110"
    elif inputs[7]==1:
        return "111"


data=[0,0,0,1,0,0,0,0]

print("Input:",data)
print("Output:",encoder(data))