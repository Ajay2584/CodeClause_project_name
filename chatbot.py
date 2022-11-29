from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('CodeClause Bot')

 # Training with Personal Ques & Ans 
conversation = [
    "Hi",
    "Hi,What can i help you ?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "bye",
    "Bye",

    "About CodeClause",
    "We offer reliable, efficient delivery with high-caliber engineers & finely-tuned software development processes.We Believe In Leadership to lead the technology to build a better future Integrity to follow truth and be real Accountability for our every commitment."

"We Imagine"
"We Engineer"
"We Modernize"
"We Manage"
"Increasing revenue, improving efficiency, reducing cost—these are all accomplished by implementing innovative technology that’s purpose-built to solve the challenges holding your organization back.",

"Why CodeClause ?",
"CodeClause aspire to be the global sourcing choice of the world market and revolutionizes the way service processes function. To reach out to the common people across the globe and making Information Technology a tool for the “MASS” along with the tool for the “CLASS”. Creating innovative IT solutions and provide IT-enabled services to delight customers worldwide and build Relationships based on Trust, Values and Professionalism."
"Be passionate about clients success, "
"Be global and responsible, "
"Treat each person with respect, "
"Unyielding integrity in everything we do, "
"CodeClause has industry-specific software expertise in Technology, Financial, Healthcare, Media, Manufacturing, and many other sectors. The company specializes in offering Data & Analytics, Automation AI, IoT Services, Web Designing, Web Application Development, Mobile Application Development, Software Development, Digital Marketing, Software Testing, Quality Assurance services, and many more.",

"I have an issue ?",
" For any query  \n   ? "
" Email Us  -     "
"official@codeclause.com   "

" Call Us  -    "
"+91 7030020973",
"Roadmap for internship ",
"1 - Apply for an Internship \n" 
"2 - Apply for an internship in your internested domain. Internship duration will be one month. Any branch students as well as senior can apply to internship.Get an offer from codeclause \n"
"2 - Get Internship Batch Our team will check your profile as soon as possible and send you to offer letter of an internship.\n"
"3 - Get Internship Batch, Task Allocation, After offer letter you will get a batch for particular month to work in that duration., Task Allocation \n"
"4 - Verify the project submission, We will asssign some projects to you which are benificial to enhance your skills in your intrested domain.\n"
"5 - Complete the Tasks, Get LOR, Complete your allocated projects by given categories., Submit Tasks.\n"
"6 - Season 8, After completing your projects submit them on internship portal for evaluation.\n"
"7 - Verify the project submission, Season 7 After your submission of project our team will verify your submissions and our project completion criteria.Get Internship Completion Certificate. \n"
"8 - Get LOR After successfully evaluation of projects you will be eligible for internship certificate.\n",
"9 - Get Letter of Recommendation Season 5 If your are meeting to criteria of project completion then you will get letter of recommendation from CodeClause.Earn Swags & Rewards.\n"
"10 Get LOR, If your are meeting to criteria of project completion then you will get Swags & Rewards from CodeClause.",

"Internship Domains ",
"1 - Data Science   ,"
"2 - Artificial Intelligence  ,"
"3 - python development   ,"
"4 - web development   ,"
"5 - Android development   ,"
"6 - java development   ,"
"7 - Graphic Design   ,"
"8 - content writer",
"Internship Availabel ?",
"Yes..Please select domains",
"What is internship ?",
"An internship is a professional learning experience that offers meaningful, practical work related to a student’s field of study or career interest. An internship gives a student the opportunity for career exploration and development, and to learn new skills. It offers the employer the opportunity to bring new ideas and energy into the workplace, develop talent and potentially build a pipeline for future full-time employees.",
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)