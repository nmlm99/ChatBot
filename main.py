matches = db.prefix("prefix")
keys = db.keys()
value = db["key"]
db["key"] = "value"
from replit import db
import random
import time

print()
print(
    'Hi, \nYou can talk to me about anything! To stop the conversation just type "/quit"'
)
print('-' * 73, '\n')
stop = False

while stop == False:#Keeps code running
    OtherWord = ''
    SimilarWord = ''
    Pronoun = ''

    UserText = input('You >>> ').lower().split()#Formats code so it is lower case and the sentence is seperated into a list.

    Dictionary = [
        'bright', 'clever', 'encouraging', 'gentle', 'hopeful', 'kind',
        'loving', 'open', 'supportive', 'sympathetic', 'attractive',
        'beautiful', 'bold', 'brave', 'cheerful', 'comfortable', 'excited',
        'festive', 'free', 'jolly', 'optimistic', 'proud', 'appreciative',
        'ecstatic', 'elated', 'glad', 'happy', 'joyful', 'respectful',
        'upbeat', 'annoyed', 'disgusted', 'evil', 'guilty', 'hurtful',
        'obnoxious', 'oppressive', 'overbearing', 'sarcastic', 'awful',
        'depressed', 'heavy', 'irritated', 'pessimistic', 'tearful', 'tense',
        'terrible', 'tired', 'ugly', 'weak', 'angry', 'distressed', 'grumpy',
        'miserable', 'mad', 'moody', 'nervous', 'sad', 'selfish', 'sour',
        'anxious', 'cautious', 'horrified', 'intelligent', 'mysterious',
        'political', 'quizzical', 'religious', 'secretive', 'secular',
        'strong', 'composed', 'easygoing', 'shy', 'accepting', 'calm',
        'confident', 'cool', 'easy', 'neutral', 'passive', 'reserved',
        'satisfied', 'surprised', 'tranquil', 'admirable', 'agreeable',
        'amused', 'authentic', 'believable', 'charming', 'content',
        'courteous', 'dedicated', 'delighted', 'eager', 'enjoyable',
        'enthusiastic', 'excellent', 'extraordinary', 'faithful', 'fortunate',
        'friendly', 'fun', 'genuine', 'grateful', 'great', 'honest',
        'honorable', 'humorous', 'keen', 'likable', 'lucky', 'magnificent',
        'noble', 'outstanding', 'passionate', 'peaceful', 'pleasant',
        'pleasing', 'pleasurable', 'positive', 'relaxed', 'reliable',
        'respectable', 'superb', 'thankful', 'trustful', 'worthy', 'amazed',
        'interested', 'engaged', 'hostile', 'enraged', 'insulting', 'sore',
        'upset', 'hateful', 'joyous', 'overjoyed', 'gleeful', 'disappointed',
        'discouraged', 'ashamed', 'powerless', 'dissatisfied', 'playful',
        'courageous', 'energetic', 'provocative', 'impulsive', 'doubtful',
        'uncertain', 'indecisive', 'perplexed', 'embarrassed', 'hesitant',
        'peaceful', 'pleased', 'encouraged', 'incapable', 'alone', 'scared',
        'fatigued', 'useless', 'inferior', 'vulnerable', 'empty', 'forced',
        'sensitive', 'devoted', 'admiration', 'warm', 'fearful', 'terrified',
        'suspicious', 'alarmed', 'panic', 'worried'
    ]#All the words it can recognise

    PronounDictionary = ['he', 'she', 'they', 'i', 'you', 'we']#Pronouns

    OtherDictionary = [
        '/quit', 'mental', 'depression', 'drugs', 'alcohol', 'homelessness',
        'old', 'coronavirus', 'abuse', 'suicide', 'racism', 'unemployment',
        'stress', 'bullying', 'safety', 'anxiety', 'hi', 'hello', 'bye',
        'vaccine', 'python', 'anxiety', 'media', 'cyber',
        'hobbies', 'movies', 'tv', 'travel', 'music', 'time', 'food',
        'suicidal'
    ]#Other words it can reognise

    ResponseA = [
        'What do #person# think it means to be bright?',
        'Do #person# think that #person# are clever? How would that change the conversation?',
        'What do #person# think it means to be encouraging? Does it answer the question?',
        'Do #person# think #person# are gentle?',
        'Do #person# want to be hopeful. Why do #person# want to be hopeful?',
        'Do #person# feel when #person# are kind?',
        'Why do #person# need love?',
        'How do #person# feel when #person# are open about something? Do #person# want to feel that way?',
        'Do #person# think that #person# are supportive?',
        'Would #person# prefer is #person# were not sympathetic?',
        'Do #person# want to be attractive?',
        'How does that make #person# feel?',
        'Do #person# think that #person# are bold? What makes them that way?',
        'How do #person# define bravery? Is the definition #person# just gave the same as what someone else would give?',
        'If #person# are cheerful who else is cheerful?',
        'At the moment are #person# comfortable with where #person# are in life? What makes it that way?',
        'What are #person# excited about?', 'Do #person# celebrate festivals?',
        'At the moment do #person# think #person# are free?', 'Tell me more',
        'What are #person# optimistic about. Do #person# think that #person# should be optimistic about that?',
        'What are #person# most proud of?', 'Why do #person# appreciate that?',
        'Why are #person# so happy because of that?',
        'Why do #person# think that?', 'What are #person# glad happened?',
        'What does happiness mean?', 'Are #person# certain about that?',
        'Why are #person# respectful? ', 'What do #person# think?',
        'What are #person# annoyed by?', 'Please tell me more',
        'Why do #person# say that?', 'Do #person# believe that?',
        'Have #person# ever been hurtful?', 'What makes that annoying?',
        'Do #person# think that ,that is ok?',
        'If someone else was in that scenario would #person# act the same?',
        'Tell me more?', 'What makes it that way?',
        'Why do #person# feel that way if #person# need urgent help #person# can call the SAMARITANS at 116 123 (charges may apply)',
        'What do #person# mean by heavy?', 'Is that what #person# want?',
        'Why do #person# always expect the worst has that always happened?',
        'What makes them feel that way?',
        'How do #person# feel when #person# are tense?', 'Tell me more.',
        'What does that tell us?', 'Do #person# think #person# are ugly?',
        'Are #person# sure about that?', 'What makes them angry?',
        'What causes this distress', 'Tell me more',
        'Do #person# really think #person# are miserable?',
        'Do #person# think #person# are mad?', 'Why do #person# ask that?',
        'Why do #person# think #person# are nervous do #person# really think that?',
        'Do #person# think that #person# are sad?',
        'If #person# are selfish what else is true?',
        'What does that tell #person#?', 'What makes #person# anxious?',
        'Why do #person# think #person# are cautious?',
        'What are #person# horrified by?',
        'What do #person# think it means to be intelligent?',
        'What is the mystery?', 'Why do #person# engage in politics?',
        'Tell me more?', 'Do #person# believe in that?',
        'Do #person# have secrets?', 'Tell me more',
        'What makes someone strong?',
        'Are #person# composed in most situations?', 'Tell me more...',
        'Do #person# think it is ok to be shy?', 'What do #person# accept?',
        'What makes them calm?', 'Are #person# confident?',
        'What do #person# mean when #person# say cool?', 'What is easy?',
        'What are #person# neutral in?', 'Are #person# passive aggressive?',
        'Can #person# add more detail to that?',
        'What are #person# satisfied by?', 'What makes it a surprise?',
        'What does that tell #person#?',
        'What qualities to #person# admire in them?',
        'What do #person# agree with?', 'What is so funny?',
        'What is that authenticity?', 'Why do #person# believe that?',
        'Tell me more', 'What makes them happy?',
        'Why are #person# respectful?',
        'What do #person# get from this dedication?',
        'Maybe #person# can answer the question?', 'Where does that come from',
        'What makes that enjoyable?#', 'Why are #person# so enthusiastic?',
        'Have #person# ever been excellent?',
        'Do #person# think #person# are extraordinary',
        'Who do #person# have faith in?',
        'What are #person# fortunate to have?', 'Do y.ou have friends?',
        'What do #person# find fun?', 'What is genuine?',
        'What are #person# grateful for?', 'Are #person# great?',
        'What do #person# think about honesty?',
        'What makes someone honorable?', "What's so funny?",
        'What are #person# keen about?', 'What makes a person likable?',
        'Do #person# think that #person# are lucky?', 'What is magnificent?',
        'Do #person# know any noble people?',
        'What makes someone outstanding?',
        'What are #person# passionate about?', 'Are #person# peaceful?',
        'What makes them that way?', 'Why do #person# say that?',
        'Why do #person# say that?', 'In what way do #person# mean that?',
        'What do #person# do to feel relaxed?',
        'What makes something or someone reliable?', 'Tell me more',
        'What does that tell us?', 'What are #person# thankful for?',
        'Who do #person# trust?',
        'Do you consider yourself worthy of that? Why?',
        'What are #person# amazed by?', 'What are #person# interested in?',
        'Tell me more', 'What makes people hostile?',
        'What is the cause of this anger?',
        'Do #person# think that these insults are ok?',
        'What does that tell us?',
        'Are #person# upset? What does that tell #person#?',
        'Why do #person# think #person# receive hate?',
        'Do #person# like being happy?', 'What does that tell us...',
        'Can #person# add more detail?', 'Why are #person# disappointed?',
        'What are #person# discouraged from doing?',
        'Why are #person# ashamed?', 'Why do #person# feel that way?',
        'Why are #person# not feeling satisfied?', 'Tell me more',
        'Where do #person# get that courage?',
        'What is a sport #person# like playing?',
        'Maybe you can answer the question?',
        'Why do #person# have that impulse?', 'What are #person# doubting?',
        'Why are #person# uncertain about that?',
        'What can #person# not decide on?',
        'Why do you think #person# are confused?', 'What is so embarrassing?',
        'What are #person# hesitant to do?',
        'Would you consider yourself as peaceful?', 'What are you pleased by?',
        'What are you encouraged to do?',
        'What are you incapable of doing. Why is that?',
        'How do you feel when you are alone?', 'Why are you scared?',
        'Why are you so tired? What does that tell us?', 'What is useless?',
        'Why is it so much better than that?',
        'Why is it vulnerable what can you do?',
        'Do you think there is a reason that it is empty?',
        'What have you been forced to do?', 'What are you sensitive to do?',
        'What are you devoted to?', 'Why do #person# admire that?',
        'Tell me more information...', 'Why are you fearful of that?',
        'What is so scary?', 'What is so suspicious about that?',
        'What is so alarming', 'What caused the panic?', 'Why are you worried?'
    ]#First set of dictionary responses.

    ResponseB = [
        'Do #person# think #person# are bright? What does that tell #person#?',
        'How does that make #person# feel when #person# are clever?',
        'Do #person# think #person# are encouraging',
        'What does it mean to be gentle?',
        'What are #person# hoping for do #person# think that #person# are going to get what #person# are hoping for?',
        'Do #person# think that #person# are kind?',
        'Do #person# think love exists?',
        'Do #person# want to be open? How does that affect #person#?',
        'Do #person# want to be supportive? Why do #person# want to be supportive?',
        'Why do #person# ask about sympathy?',
        'If #person# are attractive what else is true?',
        'What do #person# think?', 'DO #person# think that #person# are bold?',
        'Perhaps #person# can answer the question?',
        'What do #person# think it means to be cheerful?',
        'Do #person# think #person# need comfort?',
        'Why are #person# excited about that?',
        'Do #person# think #person# are festive?',
        'What do #person# mean when #person# say freedom? What does that tell us?',
        'How have #person# been lately?', 'What do #person# mean by optimism?',
        'Why are #person# proud of that?', 'Why do #person# say that?',
        'Tell me more?', 'Tell me more', 'What will #person# do next?',
        'Do #person# want to have happiness?',
        'How are #person#? Do #person# want to be this way?',
        'Do #person# want respect?',
        'Perhaps #person# can answer the question?',
        'Why are #person# annoyed?', 'What are #person# disgusted by?',
        'What makes that evil?', 'What makes that true?',
        'What will #person# do next?', 'How does that affect them?',
        'What are #person# oppressing?', 'What does that tell us?',
        'Can #person# add more detail?', 'What is awful?',
        'DO #person# think that #person# are meant to feel this way?',
        'Tell me more', 'Are #person# sure #person# feel that way?',
        'Has that ever came true?', 'Tell me more...',
        'Do #person# every doubt themselves?',
        'Are #person# certain about that?', 'Tell me more?',
        'Why do #person# say that?', 'Tell me about that',
        'Why are #person# angry when #person# are angry?',
        'Do #person# like feeling distressed?',
        'Can #person# add more detail to that?',
        'Did #person# come here because #person# are miserable?',
        'Why does it matter that #person# are mad>',
        'Perhaps #person# can answer the question?',
        'Would #person# prefer if #person# were not nervous?',
        'Is it ok to be sad?',
        'Could #person# explain why #person# are selfish?',
        'Why do #person# say that?', 'Tell me more',
        'Is the reason that #person# are cautious backed up by facts?',
        'Tell me more',
        "Do #person# think #person# are intelligent. If #person# don't why not?",
        'What do #person# find mysterious?', "Do #person# think that's right?",
        'Why do #person# say that?',
        'Why do #person# think that #person# believe in that?',
        'What makes secrets good or bad?',
        'Can #person# add more detail to that?',
        'DO #person# think that #person# are strong? Why not?',
        "How do #person# view other people who don't like #person#?",
        'Can #person# add more detail to that?', 'Are #person# shy?',
        'What do #person# not accept?', 'What makes them calm?',
        'Are #person# confident', 'Do you/they see themselves as cool?',
        'What is hard?', 'ph7', 'Tell me more', 'Tell me more...',
        'What are #person# satisfied by?', 'Why are #person# surprised?',
        'Do you see yourself as calm? If not why is that?',
        'Maybe #person# can answer the question?', 'Tell me more',
        'Tell me a joke...', 'What makes it so authentic?',
        'What makes it so believable...', '<<<', 'Tell me more',
        'Why are #person# respectful?', 'What does that tell #person#?',
        'What does that tell #person#?', 'Is that all #person# know?',
        'Do #person# think that is enjoyable?',
        'What makes #person# enthusiastic?',
        'What do #person# mean by excellence', 'What does that tell #person#?',
        'What do #person# mean by faithful',
        "What would #person# do if #person# didn't have something that #person# were fortunate to have?",
        'Tell me about y.our friends...', 'Why do #person# find that fun?',
        'What does that tell us?',
        "What would #person# have done if #person# didn't have something that #person# are grateful for?",
        'Tell me more...', 'Maybe #person# have the answer to the question?',
        'Tell me more...', 'Tell me a joke',
        'Do #person# think it is ok to be keen about that?',
        'Do #person# think that #person# are likable?',
        'What makes #person# lucky?', 'Tell me more',
        'Can #person# add more detail to that?', 'Are #person# outstanding?',
        "Do #person# think it is ok to have a passion that people don't like?",
        'Have #person# ever not been peaceful? Why was that?',
        'Maybe #person# can answer the question?', 'Tell me more...',
        'What does that tell us?', 'Tell me more', 'Why are #person# relaxed?',
        'Are #person# reliable?', 'Why do #person# respect people?',
        'Tell me more...', 'Why are #person# thankful for things?',
        'Why do #person# trust them?', 'What does being worth mean?',
        'Why are #person# amazed?', 'Why are #person# interested in that?',
        'Can #person# add more detail to that?',
        'Have #person# ever been hostile?', 'Tell me more...',
        'Why do #person# say that?', 'Can #person# add more detail to that?',
        'Why do #person# think that?', 'What do you mean by hateful?',
        'How are you?', 'That is interesting can you tell me more?',
        'Tell me more', 'Why are you disappointed?',
        'What have you been discouraged from doing?',
        'What are you ashamed of? Why is that?',
        'What would you do if you had power?',
        'What are you not satisfied with Why do you say that?',
        'Explain to me again...', 'Do you see yourself as courageous?',
        'What is your favorite sport?', 'Maybe you have the answer?',
        'Why do you have that impulse?',
        'What are you doubting? Should you be doubting that?',
        'What is so uncertain about that?', 'What can you not decide on?',
        'What is so confusing?', 'What does being embarrassed tell you?',
        'Why are you hesitating?', 'Are you normally peaceful?',
        'What are you pleased by?',
        'What have you been encouraged to do? Do you think that it is the right thing to do?',
        'What are you incapable of doing why is that?',
        'Do you like being alone?',
        'What are you scared of? Should you be scared of that?',
        'Why are you so tired?', 'What is useless why is it useless?',
        'Tell me more...', 'What is vulnerable? What can you do about it?',
        'What is empty',
        'What are you being forced to do? Is it the right thing?',
        'Tell me more...', 'What are you devoted to doing?',
        'What do you admire?', 'Maybe you have the answer?',
        'What are you scared of why are you scared of it?',
        'What does that tell you and other people?', 'Why are you suspicious?',
        'What are you alarmed about?', 'Why do you panic?',
        'What are you worried about?Should you really be worried about that?'
    ]#Second set of dictionary responses

    SubjectPronounResponse = ['they', 'they', 'they', 'you', 'you',
                              'they']#Pronouns to add in the response.

    OtherDictionaryResponses = [
        'TERMINATING PROGRAM',
        'Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices. Mental health is important at every stage of life, from childhood and adolescence through adulthood If #person# need urgent help or just want to speak to someone #person# can call MIND at 0300 123 3393',
        'Depression is when #person# have a low mood that lasts for weeks or months and affects #person#r daily life.If #person# currently have depression or think #person# have depression #person# can contact MIND at 0300 123 3393 or CHILDLINE if #person# want support.',
        'Drugs are chemicals or substances that change the way our bodies work there are many legal drugs however there are also illegal ones these can be dangerous if #person# abuse them and could have major negative effects on #person# such as dizziness,diarrhea drowsiness #person# think #person# are addicted to drugs #person# can call FRANK DRUGS HELPLINE on 0300 123 6600.',
        'Alcohol could become dangerous if #person# have an addiction or have too much #person# can call DRINKLINE at 0300 123 1110 if #person# are worried about #person#r own or some else`s drinking habits.',
        'If #person# are homeless or at risk of homelessness #person# can call CENTREPOINT at 0808 800 0661',
        'Everyone gets old it is a natural process.',
        'The main symptoms of COVID-19 are a high temperature ,continuous cough and a loss or change to #person#r sense of smell or taste',
        'If #person# are experiencing domestic abuse #person# are not alone #person# can call REFUGE at 0808 2000 247 if #person# need help because of a abusive partner.',
        'If #person# are feeling like #person# want to die it is important to tell someone help and support is available right now if #person# need it You do not have to struggle with difficult feelings alone #person# can call SOS Silence of Suicide at 0300 1020 505 if #person# need help...',
        'You should never have to put up with racism or discrimination if #person# need help #person# can contact the police , the government , the NHS then if #person# want #person# can take legal action against them...',
        'Unemployment is rising rapidly if #person# want to file for unemployment benefits #person# can call the general unemployment helpline 0800 328 5644.',
        'Being stressed is ok if #person# constantly feel stressed it could be because of #person#r mental health..',
        'Bullying is not ok if #person# are affected by bullying #person# can contact the police or CHILDLINE at 0800 1111',
        'If #person# don`t feel safe #person# can contact the police at 999.',
        'If #person# feel anxious it could be a sign of a mental ',
        'Hi, How are #person#!', 'Hello , What are #person# doing?',
        'Bye to quit the program type /QUIT or close the program...',
        'Vaccines contain weakened or inactive parts of a organism that trigger an immune response within the body.',
        "print('This chat bot was written in python!')",
        'Feeling anxious is normal...',
        'Social media can be a great tool however it could get #person# addicted to #person#r phone and #person# could be vulnerable to cyber bullies.',
        'Cyber bullying is not ok if #person# have been cyber bullied #person# can contact CEOP.',
        'What are #person#r hobbies?', 'What is #person#r favorite movie?',
        'What do #person# watch on TV?', 'Where did #person# travel too?',
        'Whats #person#r favourite song?',
        'What do #person# do in #person#r free time?',
        'My favorite food is pizza',
        'If #person# feel suicidal #person# can contact the SAMARITANS at 116 123'
    ]#Other dictionary responses.

    NoMatchResponses = [
        'Why do #person# say that?', 'Maybe you know the answer?',
        'Please tell me more', 'Do #person# think that is everything?',
        'Maybe you do not have the solution?', 'Please tell me more about it.',
        'How have you been?', 'Can you explain that to me in more detail?',
        'How does that make you feel as a whole?',
        'How do #person# feel when #person# say that?',
        'That is quite intresting what does that tell you?',
        'Maybe #person# need a break?', 'Do you think that it is right?',
        'Why do you say that?', 'How has that changed you (if it has)?',
        'Please contniue', 'Can you add more detail?',
        'How do #person# feel at the moment'
    ]#Responses if no similar words found.

    UserTextLength = len(UserText)

    #Goes through each word in the sentence and checks if it is in the dictionaries.
    #If it is it saves the word and the location of that word in the dictionary 
    # (the location corresponds to the location of the response)

    UserWordCount = 0
    while UserWordCount != UserTextLength:
        UserWord = UserText[UserWordCount]
        if UserWord in Dictionary:
            SimilarWordLocation = Dictionary.index(UserWord)
            SimilarWord = Dictionary[SimilarWordLocation]
        UserWordCount = UserWordCount + 1

    UserWordCount2 = 0
    while UserWordCount2 != UserTextLength:
        UserWord2 = UserText[UserWordCount2]
        if UserWord2 in PronounDictionary:
            PronounWordLocation = PronounDictionary.index(UserWord2)
            Pronoun = PronounDictionary[PronounWordLocation]
        UserWordCount2 = UserWordCount2 + 1

    UserWordCount3 = 0
    while UserWordCount3 != UserTextLength:
        UserWord3 = UserText[UserWordCount3]
        if UserWord3 in OtherDictionary:
            OtherWordLocation = OtherDictionary.index(UserWord3)
            OtherWord = OtherDictionary[OtherWordLocation]
        UserWordCount3 = UserWordCount3 + 1

    #Checks if any of the words matched with the ones in the dictionary
    #If it has the program marks that section as True.

    if Pronoun == '':
        PronounWordLocation = 3  #Pronoun=i --> you

    if SimilarWord == '':
        MatchFound1 = False
    else:
        MatchFound1 = True
    if OtherWord == '':
        MatchFound2 = False
    else:
        MatchFound2 = True

    #Depending on if the words have matched the program picks the response type(where the response is from).
    if MatchFound1 == True and MatchFound2 == True:
        ResponseType = 'otherResponse'
    if MatchFound1 == True and MatchFound2 == False:
        ResponseType = 'Response'
    if MatchFound1 == False and MatchFound2 == True:
        ResponseType = 'otherResponse'
    if MatchFound1 == False and MatchFound2 == False:
        ResponseType = 'randomResponse'

    #Sets the response as the one allocated above.

    if ResponseType == 'otherResponse':
        Response = OtherDictionaryResponses[OtherWordLocation]
    if ResponseType == 'Response':
        ResponseList = random.randrange(1, 3)
        if ResponseList == 1:
            Response = ResponseA[SimilarWordLocation]
        if ResponseList == 2:
            Response = ResponseB[SimilarWordLocation]
    if ResponseType == 'randomResponse':
        Response = NoMatchResponses[random.randrange(0, len(NoMatchResponses))]

    #Swaps the placeholder '#person#' with the pronoun to make the sentence sound more human.

    if '#person#' in Response:
        Response = Response.replace(
            '#person#', SubjectPronounResponse[PronounWordLocation])
    
    #Capitalizes the first letter of the response.
    Response = Response.capitalize()

    #The program sleeps for 0.5 seconds to make the conversation feel more natural.
    time.sleep(0.5)
    
    #Prints the response.
    print('Bot >>> ', Response)

    #If the user typed in '/quit' the program stops.
    if '/quit' in UserText:
        stop = True

print('\n PROGRAM STOPPED')

#RESOURCES USED:
#W3 Schools (https://www.w3schools.com/)
#Stack Overflow (https://stackoverflow.com/)
#Based on ELIZA (https://en.wikipedia.org/wiki/ELIZA)

#RESPONSE SYSTEM
#The response system works by matching a word from the users input into the dictionary.
# User Input = 'I am happy'
# dictionary=['happy','sad']
# responses = ['You are happy','You are sad']

#The program recognises that the word happy is in the dictionary it then finds out the location of the word in the dictionary (in this case 0).
#The location of the word in the dictionary corresponds to the location of the response so the program can print out the response.

#In the actual program there are more steps such as more dictionaries so it can understand more types of words
# , dictionaries that are used if the program can't understand the input
# , The program can detect who is talking e.g you or someone else so that the response can be about the correct person.

#Made By Yash Ganeshgudi 2021
#Version 1.0.3