# import and download required packages
import nltk
from random import choice
import Search_Scrape as ss
import copy
import ast
import os



from openai import OpenAI
from openai import AuthenticationError


# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer


# define variables
stemmer = PorterStemmer()
# functions for manipulating lists
def list_replace(my_list, old_value, new_value):
    for index, value in enumerate(my_list):
        if value == old_value:
            my_list[index] = new_value
            break
    
    return my_list
def most_frequent(List):
    return max(set(List), key = List.count)
def final_output(item_list):
    return ', '.join([item for item in item_list if '*' not in item])
# nltk functions
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    output=[]
    for words in word:
        output.append(stemmer.stem(words.lower()))
    return output



# chatbot function


chatlist=['Ask me anything! I can search google for an answer.','I can do many things to help out. Just ask me!', 'if you want to play a game, just ask me!','what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.',"What's your favorite thing to do in your free time?",    "Have you traveled anywhere recently? Where did you go?",    "What's your favorite type of music?",    "Do you have any hobbies that you enjoy?",    "What do you like to do on the weekends?"]
history=['','']
mood_history=['','']
chat_history=['','']
def personal(qstn):
    global chatlist
    global history
    global mood_history
    global chat_history
    # set variables
    #global history
    #global chat_history
    #global messages
    chatty=''
    moodometer=[]
    intent=[]
    # format
    if 'thank you' in qstn:
        qstn=qstn.replace('thank you', 'thanks')
    together=qstn
    tokenized_input=tokenize(qstn)
    qstn=stem(tokenized_input)
    #print(qstn)
        
    
    # organize
    for keyword in qstn:
        # greeting
        if keyword in ['hello', 'hi', 'howdy', 'greetings', 'good day']:
            intent.append('*greet')
        # question words
        if keyword in ['who', 'what', 'where', 'when', 'why', 'how']:
            intent.append('*question')
        if keyword in ['who', 'what']:
            intent.append('*q_identify')
        if keyword in ['where', 'when']:
            intent.append('*q_place')
        if keyword in ['whi', 'how']:
            intent.append('*q_info')
        # verbs
        if keyword in ['do', 'did', 'have', 'had', 'has', 'does']:
            intent.append('*helping action')
        if keyword in ['is', 'am', 'was', 'are', 'were', 'been', 'be', 'being', 'feel', "'s"]:
            intent.append('*to be')
        if keyword in ['you','your']:
            intent.append('*personal')
        # nouns
        if keyword in ['i', "i'm", 'me', 'my']:
            intent.append('*user_personal')
        # adjectives
        if keyword in ["good", "fine", "well", "great", "excellent", "fantastic", "wonderful", "superb", "splendid", "terrific", "awesome", "amazing", "marvelous", "outstanding", "exceptional", "fabulous", "incredible", "super", "pleased", "satisfied", "content", "delighted", "joyful", "happy", "cheerful", "radiant"]:
            intent.append('*good')
        if keyword in ['bad',"poor", "awful", "terrible", "horrible", "dreadful", "atrocious", "abysmal", "lousy", "mediocre", "inferior", "unsatisfactory", "subpar", "deficient", "unacceptable", "unpleasant", "displeasing", "disappointing", "unsatisfying", "unfortunate", "wretched", "miserable", "unfavorable", "negative", "bleak", "gloomy", "grim"]:
            intent.append('*bad')
        if keyword in ['like',"enjoy", "appreciate", "adore", "love", "favor", "relish", "prefer", "cherish", "savor", "fancy", "admire","favorit"]:
            intent.append('*like')
        if keyword in ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "violet", "indigo", "maroon", "navy", "beige", "turquoise", "teal"]:
            intent.append('*color')
        # other
        if keyword in ['yes','no','maybe','ok', 'nope', 'yup', 'nice']:
            intent.append('*neutral')
        if keyword in ["noth", "zero", "nil", "naught", "nought", "void", "zilch", "zip", "nada", "null", "none", "nonexistence", "insignificance"]:
            intent.append('*nothing')
        if keyword in ['thank','thanks', 'grate','gratitud']:
            intent.append('*thanks')
        #if keyword in ['write','recip','recommend','list','advic','tip','compos']:
            #intent.append('*gpt')
        #if keyword in ['imag','pictur','illustr']:
            #intent.append('*dall-e')
    # generate output
    output=[]
    format_var=[]
    for intents in intent:
        format_var.append(intents)
    debug_format_var=copy.deepcopy(format_var)
    greetings=['Hello user',"Hi",'Howdy']
    greet_response=["I'm fine, how are you?","I am doing great!"]
    introduce=['I am CustomChat, and I am an easily customizable Python Chatbot. Ask me general information, or just have a conversation.']
    doing=['I am computing your input']
    good_response=['That is great','That is good','Great!']
    bad_response=['That is not good.', 'I am sorry.']
    thank_response=['Your welcome','Anytime']
    doing_today=["I like to process your input","My hobby is to listen to you","I like listening to you talk"]
    # rock paper scissors
    if 'Do you want to throw rock, paper, or scissors?' in history[0]:
        c_throw=choice(['rock','paper','scissors'])
        if 'rock' in together:
            if 'rock' in c_throw:
                format_var=['Tie!']
            elif 'paper' in c_throw:
                format_var=['You lose!']
            elif 'scissors' in c_throw:
                format_var=['You win!']
        if 'paper' in together:
            if 'rock' in c_throw:
                format_var=['You win!']
            elif 'paper' in c_throw:
                format_var=['Tie!']
            elif 'scissors' in c_throw:
                format_var=['You lose!']
        if 'scissors' in together:
            if 'rock' in c_throw:
                format_var=['You lose!']
            elif 'paper' in c_throw:
                format_var=['You win!']
            elif 'scissors' in c_throw:
                format_var=['Tie!']
    # check for context
    if 'how are you?' in history[0] and '*user_personal' in format_var and '*to be' in format_var:
        if '*bad' in format_var:
            format_var=list_replace(format_var,'*user_personal',choice(bad_response))
            moodometer=[1,2,2,2,3]
        else:
            format_var=list_replace(format_var,'*user_personal',choice(good_response))
            moodometer=[2,2,2,3]
    if "What's your favorite type of music?" in chat_history[0] and '*user_personal' in format_var:
        format_var=list_replace(format_var,'*user_personal','My favorite music is Jazz.')
        moodometer=[1,2,2,2,3]
    if "what is your favorite color?" in chat_history[0] and '*color' in format_var:
        format_var=list_replace(format_var,'*color','I like the color light blue.')
        moodometer=[1,2,2,2,3]
    if "What do you like to do on the weekends?" in chat_history[0] or "What do you like to do on the weekends?" in chat_history[1]:
        if '*nothing' in format_var:
            format_var=list_replace(format_var,'*nothing',choice(['I know you do something','Everyone does something']))
            moodometer=[1,3]
        if '*user_personal' in format_var and '*like' in format_var:
            format_var=list_replace(format_var,'*user_personal',choice(doing_today))
            moodometer=[1,2,2,2,2,2,3]
    if "what are you doing today?" in chat_history[0] or "what are you doing today?" in chat_history[0] or 'Do you have any hobbies that you enjoy?' in chat_history[0]:
        if '*nothing' in format_var:
            format_var=list_replace(format_var,'*nothing',choice(['I know you do something','Everyone does something']))
            moodometer=[1,3]
        if '*user_personal' in format_var and '*to be' in format_var:
            format_var=list_replace(format_var,'*user_personal',choice(doing_today))
            moodometer=[1,2,2,2,2,2,3]
    if "Have you traveled anywhere recently? Where did you go?" in chat_history[0] and '*user_personal' in format_var:
        format_var=list_replace(format_var,'*user_personal','That sounds fun')
        moodometer=[1,2,3]
    if '*user_personal' in format_var and '*like' in format_var:
        if 'what is your favorite food?' in chat_history[0]:
            format_var=list_replace(format_var,'*user_personal',choice(["I like to eat electricity"]))
            moodometer=[1,2,2,2,3]
        elif "What's your favorite thing to do in your free time?" in chat_history[0]:
            format_var=list_replace(format_var,'*user_personal',choice(doing_today))
            moodometer=[1,2,2,2,3]
    if "Tell me about yourself." in chat_history[0] and '*user_personal' in format_var:
        if '*to be' in format_var:
            format_var=list_replace(format_var,'*user_personal',"I am a robot")
            moodometer=[1,2,2,2,3]
        if '*like' in format_var:
            format_var=list_replace(format_var,'*user_personal',choice(doing_today))
            moodometer=[1,2,2,2,3]
    # analize
    if '*to be' in format_var and '*good' in format_var:
        moodometer=[5]
    if '*greet' in format_var:
        format_var=list_replace(format_var,'*greet',choice(greetings))
        moodometer=[1,2,2,2,3]
    if '*q_info' in format_var and '*to be' in format_var and '*personal' in format_var:
        format_var=list_replace(format_var, '*question', choice(greet_response))
        moodometer=[1,2,2,2,2,2,2,3]
    if '*q_identify' in format_var and '*to be' in format_var and '*personal' in format_var:
        format_var=list_replace(format_var, '*question', choice(introduce))
        moodometer=[1,2,3]
    if '*q_identify' in format_var and '.to be' in format_var and '*personal' in format_var and '*helping_action' in format_var:
        format_var=list_replace(format_var, '*question', choice(doing))
        moodometer=[1,2,2,2,2,3]   
    if '*neutral' in format_var:
        format_var=list_replace(format_var, '*neutral', 'ok')
        moodometer=[1,2,3]
    if '*thanks' in format_var:
        format_var=list_replace(format_var, '*thanks', choice(thank_response))
    if together == 'RESET':
        format_var=['reset','*RESET']
        moodometer=[1]
    # other functions
    if 'rock paper scissors' in together:
        format_var.append('Do you want to throw rock, paper, or scissors?')
        moodometer=[1,3]
    # determine mood
    if moodometer==[]:
        moodometer=[1,2,3]
    final=final_output(format_var)
    history.insert(0, final)
    if final == '':
        moodometer=[5]
    # Determine mood
    #global mood_history
    #global chatlist
    mood=choice(moodometer)
    mood_average=most_frequent(mood_history)
    mood_history.insert(0, mood)
    moodometer.append(mood_average)
    moodometer.append(mood_average)   
    if 5 in moodometer:
        mood=2
    else:
        mood=choice(moodometer)
    if mood == 1:
        chatty=''
        pass
    if mood == 2:
        if chatlist != []:
            chatty=choice(chatlist)
            chatlist.remove(chatty)
        else:
            chatty='This conversation is going very long.'
        chat_history.insert(0, chatty)
    if mood == 3:
        chatty=''
        pass
    if mood == 4:
        chatty=''
        pass
    # finished
    return final, chatty, qstn, debug_format_var


messages=[{
        "role":"system",
        "content":'keep everything to one line'
            }]
s_messages=[{
        "role":"system",
        "content":'I have a webscraper. Organize the output into a single, clean sentence. If necessary, use your own knowledge or context to give the desired output. Output just the cleaned sentence.'
        }]

def chat_gpt(prompt,model,apikey):
    global messages
    client = OpenAI(
        api_key=apikey
    )
    prompt=prompt
    messages.append({
        "role":"user",
        "content":prompt
        })
    chat_completion = client.chat.completions.create(
        messages = messages,
        model=model
    )     
    g_output=chat_completion.choices[0].message.content
    return g_output
def dall_e(prompt,model,size,apikey):
    client = OpenAI(
        api_key=apikey
    )
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality="standard",
        n=1,
    )
    d_output=response.data[0].url
    return d_output
def search(prompt,model,apikey):
    client = OpenAI(
        api_key=apikey
    )
    s_messages.append({
        "role":"user",
        "content":ss.scrape(prompt)
        })
    chat_completion = client.chat.completions.create(
        messages = s_messages,
        model=model
    )
        
    s_output=chat_completion.choices[0].message.content
    return s_output
# Moodometer cheat sheet
# 1 is good
# 2 is chatty
# 3 is neutral
# 4 is bad

################################################################################################################################################################################
