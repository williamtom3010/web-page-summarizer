import pyttsx3
from transformers import pipeline


def get_summary(text):

    summarizer = pipeline("summarization", model='t5-base', tokenizer='t5-base', framework= 'pt')


    # text = ''' Iron Man is a 2008 American superhero film based on the Marvel Comics character of 
    # the same name. Produced by Marvel Studios and distributed by Paramount Pictures,[a] it is the 
    # first film in the Marvel Cinematic Universe (MCU). Directed by Jon Favreau from a screenplay by the 
    # writing teams of Mark Fergus and Hawk Ostby, and Art Marcum and Matt Holloway, the film stars Robert Downey Jr. 
    # as Tony Stark / Iron Man alongside Terrence Howard, Jeff Bridges, Gwyneth Paltrow, Leslie Bibb, and Shaun Toub. 
    # In the film, following his escape from captivity by a terrorist group, world-famous industrialist and 
    # master engineer Stark builds a mechanized suit of armor and becomes the superhero Iron Man.
    # A film featuring Iron Man was in development at Universal Pictures, 20th Century Fox, and New 
    # Line Cinema at various times since 1990 before Marvel Studios reacquired the rights in 2005. 
    # Marvel put the project in production as its first self-financed film, with Paramount Pictures distributing. 
    # Favreau signed on as director in April 2006 and faced opposition from Marvel when trying to cast 
    # Downey in the title role; the actor was signed in September.  '''

    summary = summarizer(text, max_length= 150, min_length= 10, do_sample=False)

    text_speech = summary[0]['summary_text']
    return text_speech
    # pyttsx3.speak(text_speech)




