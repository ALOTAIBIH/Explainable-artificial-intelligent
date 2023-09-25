import sys
import json
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#from example_hr import chris_diverse_hr
from example_hr import chris_diverse_hr

# creates training data, loads the classifier etc
russ = chris_diverse_hr()

# prints explanation texts and returns them
explanations = russ.explain(1, 1)
clearConsole()

inputs=russ.dev_data_sampled
#inputs.to_csv("inputs.csv")
x = int(input("\n-------------------------\nperson num (1-" + str(len(inputs)) + " / -1 to exit): "))
while x != -1 and x > 0 and x < len(inputs):
    print("Employee number: ", x)
    explanations = russ.explain(x, 4) 

    for i in range(len(russ.column_names)-1):
        print(i, " --> ", russ.column_names[i], ":", inputs.values[x][i])
    
    explained_instance = x

    
    feature_index = int(input("\n----------------------\nenter feature index (-1 to exit): "))
    while feature_index >= 0 and feature_index <= 31:
        feature_val = int(input("enter feature value: "))
        inputs.values[x][feature_index] = feature_val
        print("New decision: ", russ.evaluate_decision(inputs.values[x]))
        feature_index = int(input("\n----------------------\nenter feature index (-1 to exit): "))


    for i in range(len(russ.column_names)-1):
        print(i, " --> ", russ.column_names[i], ":", inputs.values[x][i])
    print(russ.evaluate_decision(inputs.values[x]))

    x = int(input("\n-------------------------\nnext employee num (1-70 / -1 to exit): "))
    clearConsole()

clearConsole()



