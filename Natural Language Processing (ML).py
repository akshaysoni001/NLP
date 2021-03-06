# Spam Classifier( Machine Learning with Natural Language Processing)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
# nltk.download()

paragraph = '''In all probability this will be my last speech to you. Even if the Government allow me to march tomorrow morning, this will be my last speech on the sacred banks of the Sabarmati. Possibly these may be the last words of my life here.
I have already told you yesterday what I had to say. Today I shall confine myself to what you should do after my companions and I are arrested. The programme of the march to Jalalpur must be fulfilled as originally settled. The enlistment of the volunteers for this purpose should be confined to Gujarat only. From what I have been and heard during the last fortnight, I am inclined to believe that the stream of civil resisters will flow unbroken.
But let there be not a semblance of breach of peace even after all of us have been arrested. We have resolved to utilize all our resources in the pursuit of an exclusively nonviolent struggle. Let no one commit a wrong in anger. This is my hope and prayer. I wish these words of mine reached every nook and corner of the land. My task shall be done if I perish and so do my comrades. It will then be for the Working Committee of the Congress to show you the way and it will be up to you to follow its lead. So long as I have reached Jalalpur, let nothing be done in contravention to the authority vested in me by the Congress. But once I am arrested, the whole responsibility shifts to the Congress. No one who believes in non-violence, as a creed, need, therefore, sit still. My compact with the Congress ends as soon as I am arrested. In that case volunteers. Wherever possible, civil disobedience of salt should be started. These laws can be violated in three ways. It is an offence to manufacture salt wherever there are facilities for doing so. The possession and sale of contraband salt, which includes natural salt or salt earth, is also an offence. The purchasers of such salt will be equally guilty. To carry away the natural salt deposits on the seashore is likewise violation of law. So is the hawking of such salt. In short, you may  choose any one or all of these devices to break the salt monopoly.
We are, however, not to be content with this alone. There is no ban by the Congress and wherever the local workers have self-confidence other suitable measures may be adopted. I stress only one condition, namely, let our pledge of truth and nonviolence as the only means for the attainment of Swaraj be faithfully kept. For the rest, every one has a free hand. But, than does not give a license to all and sundry to carry on their own responsibility. Wherever there are local leaders, their orders should be obeyed by the people. Where there are no leaders and only a handful of men have faith in the programme, they may do what they can, if they have enough self-confidence. They have a right, nay it is their duty, to do so. The history of the is full of instances of men who rose to leadership, by sheer force of self-confidence, bravery and tenacity. We too, if we sincerely aspire to Swaraj and are impatient to attain it, should have similar self-confidence. Our ranks will swell and our hearts strengthen, as the number of our arrests by the Government increases.
Much can be done in many other ways besides these. The Liquor and foreign cloth shops can be picketed. We can refuse to pay taxes if we have the requisite strength. The lawyers can give up practice. The public can boycott the law courts by refraining from litigation. Government servants can resign their posts. In the midst of the despair reigning all round people quake with fear of losing employment. Such men are unfit for Swaraj. But why this despair? The number of Government servants in the country does not exceed a few hundred thousands. What about the rest? Where are they to go? Even free India will not be able to accommodate a greater number of public servants. A Collector then will not need the number of servants, he has got today. He will be his own servant. Our starving millions can by no means afford this enormous expenditure. If, therefore, we are sensible enough, let us bid good-bye to Government employment, no matter if it is the post of a judge or a peon. Let all who are co-operating with the Government in one way or another, be it by paying taxes, keeping titles, or sending children to official schools, etc. withdraw their co-operation in all or as many watts as possible. Then there are women who can stand shoulder to shoulder with men in this struggle.
You may take it as my will. It was the message that I desired to impart to you before starting on the march or for the jail. I wish that there should be no suspension or abandonment of the war that commences tomorrow morning or earlier, if I am arrested before that time. I shall eagerly await the news that ten batches are ready as soon as my batch is arrested. I believe there are men in India to complete the work our begun by me. I have faith in the righteousness of our cause and the purity of our weapons. And where the means are clean, there God is undoubtedly present with His blessings. And where these three combine, there defeat is an impossibility. A Satyagrahi, whether free or incarcerated, is ever victorious. He is vanquished only, when he forsakes truth and nonviolence and turns a deaf ear to the inner voice. If, therefore, there is such a thing as defeat for even a Satyagrahi, he alone is the cause of it. God bless you all and keep off all obstacles from the path in the struggle that begins tomorrow.'''


sentances = nltk.sent_tokenize(paragraph)
stm = PorterStemmer()
wordnet = WordNetLemmatizer()

new_words = []
new_words2 = []
for i in range(len(sentances)):
    sentances[i] = re.sub('[^a-zA-Z]', ' ', sentances[i])
    sentances[i] = sentances[i].lower()
    words = nltk.word_tokenize(sentances[i])
    word = [stm.stem(word) for word in words if word not in set(
        stopwords.words('english'))]
    words = ' '.join(word)
    new_words.append(words)

for i in range(len(sentances)):
    sentances[i] = re.sub('[^a-zA-Z]', ' ', sentances[i])
    sentances[i] = sentances[i].lower()
    words = nltk.word_tokenize(sentances[i])
    word = [wordnet.lemmatize(word) for word in words if word not in set(
        stopwords.words('english'))]
    words = ' '.join(word)
    new_words2.append(words)


# print(new_words)
# print(new_words2)

# BagOfWords
cv = CountVectorizer()
x = cv.fit_transform(new_words2).toarray()
print(x)

# TF-IDF
tfidf = TfidfVectorizer()
y = tfidf.fit_transform(new_words2)
print(y)
