# importing modules for image extraction
from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio

reader = easyocr.Reader(['ta'])  #for recognizing the language in the image
import PIL
from PIL import ImageDraw
#***********************************************************************************************#
im=PIL.Image.open('mk1jX.jpg')   # for reading the image
bounds=reader.readtext('mk1jX.jpg',add_margin=0.55,width_ths=0.7,link_threshold=0.8,decoder='beamsearch',blocklist='=-')  # for reading the text in the image
print(bounds)
#***********************************************************************************************#
# for making the boundung bozes around the texts
def draw_boxes(image, bounds, color='yellow',width=2):
    draw=ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image
draw_boxes(im,bounds)
im.show()
#***********************************************************************************************#
# to extract and  print the text from the image
text_list=reader.readtext('mk1jX.jpg',link_threshold=0.8,add_margin=0.55,width_ths=0.7,decoder='beamsearch',blocklist='=-',detail=0)
print(text_list)

text_comb=' '.join(text_list)     #to join and print the text as a single string
print(text_comb)
#***********************************************************************************************#
#to print the text as a single string
translator = Translator()
print(translator.detect(text_comb))
#todetect the language in the text
#***********************************************************************************************#
text_en=translator.translate(text_comb,src='ta',dest='en')     # to convert the text from given language to english
print(text_en.text)
# to translate the text to audio file
ta_tts=gTTS(text_en.text)
ta_tts.save('english.mp3')
Audio('english.mp3',autoplay=True)  # with us accent
ta_tts=gTTS(text_en.text,lang='hi')    #with the change in  dest location(lang=hi here we used indian accent)  we can get that that location accent
ta_tts.save('hi_english.mp3')
Audio('hi_english.mp3',autoplay=True)   #with indian accent
#***********************************************************************************************#
#to change the text to indian language(hindi)
text_hi=translator.translate(text_comb, src='ta', dest='hi')
print(text_hi.text)
ta_tts_hi=gTTS(text_hi.text, lang='hi')
ta_tts_hi.save('hindi.mp3')
Audio('hindi.mp3',autoplay=True)
#***********************************************************************************************#
#to change the language to telugu
text_fr=translator.translate(text_comb,src='ta',dest='te')
print(text_fr.text)
ta_tts_fr=gTTS(text_fr.text,lang='te')
ta_tts_fr.save('telugu.mp3')
Audio('telugu.mp3',autoplay=True)




