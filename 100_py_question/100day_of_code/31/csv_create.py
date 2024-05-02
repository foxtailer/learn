with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\ru.txt", encoding="utf-8") as russ:
    ru_data = russ.readlines()
    for i in range(len(ru_data)):
        ru_data[i] = ru_data[i].replace("\n", "")


with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\en_50k.txt") as engg:
    eng_data = engg.readlines()
    for i in range(len(eng_data)):
        eng_data[i] = eng_data[i].replace("\n", "")

with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\dictionary.csv", "a") as result:
    for j in range(len(ru_data)):
        result.write(f"{eng_data[j]},{ru_data[j]}\n")

print(ru_data)
    # with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\ru.txt") as russ:
    #     ru_data = russ.readlines()

    #     with open(r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\dictionary.csv", "a") as result:
    #         for i in len(ru_data):
    #             temp = f"{ru_data[i]},{eng_data[i]}"
    #             result.write(temp)