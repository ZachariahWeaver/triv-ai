import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
usedCategories = ["Geography", "History", "Literature", "Music", "Science", "Sports"] #replace with an sql query that gets the 30< most recent categories
category = "Mythology"
category_prompt = "I want to create a quiz game clue set. In order to do this please generate a clueset object as follows string category, string-list clues(6 strings), string list responses(6 strings), the clues and responses should match based on index. Please try to be original with the clues and categories and avoid using these categories as they have been recently used:{}. if you want to use a similar category just make it more specific or unique in some way. My desired output, avoids any unnecessary introductory phrases in your response. Just give me a python object. Do not use any phrase before or after just give me the list."
clue_prompt = "please respond with a python list of 6 dicts, the key will be a clue and key will be the correct response ie {{'This is the first letter' : 'a'}} for the following quiz show (Jeopardy) category: {}"
clue_list = []

def promptOpenAI(prompt, insertedValue):
    prompt = prompt.format(insertedValue)

    response = prompt
    
    #openai.Completion.create(
    #model="text-davinci-003",
    #prompt = prompt
    #)
    print(response)
    return response




