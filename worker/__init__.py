wlcm_msg = """
🚀 **Hey there !
Welcome to Uncensorify Bot!** 🌈✨

I'm your automated guardian on a mission to keep our Telegram experience respectful and clean 🌐 
No uncensored words allowed on this chat journey! 🚫💬
"""

btn_txt = "Add me to your chat 🚀"

censr_msg = "Apologies for the previous message; it seems some words were not suitable."

def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def censored(input_string):
    file_name = 'worker/censored.txt'
    word_list = load_words_from_file(file_name)

    for word in word_list:
        if word.lower() in input_string.lower():
            return True

    return False