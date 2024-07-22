#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"E:\git\learn\Mail Merge Project Start\Input\Letters\starting_letter.txt") as data:
    letter_blueprint = data.read()

with open(r"E:\git\learn\Mail Merge Project Start\Input\Names\invited_names.txt") as data:
    #names = data.read().split("\n")
    names = data.readlines()


for name in names:
   temp = letter_blueprint.replace("[name]", name.strip())
   with open(f"E:\\git\\learn\\Mail Merge Project Start\\Output\\ReadyToSend\\for_{name.strip()}.txt", "w") as data:
        data.write(temp)


