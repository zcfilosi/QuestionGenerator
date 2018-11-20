# QuestionGenerator
Designed to Read text, extract facts, generate questions from facts, place into CSV, and interface with programs such as quizlet or anki for simple generation of notecards for study
This is written for Python3 and utilizes the Kivy package for the GUI

## Updates
* 11/20/2018 - Initial commit made
  * Details: Functionality includes basic GUI created using Kivy package, utilizes nltk package in order to extract key words and phrases from text entered in textbox, key words and phrases are then separately queried using wikipedia api for python, extracting the first sentence of the most relevant search result for each key phrase. A listview button is then made for each separate key phrase, and clicking on the listview item opens a popup which includes the wikipedia summary extracted. 
  * Next Steps: Wish to improve the way that key words and phrases are extracted, as some proper nouns are not extracted and not all key words are phrases are extracted. Also wish to filter extracted phrases so more common and simple phrases are not included in the key words/phrases. Would also like to include save/load funcitonality to save collections of listview cards and load collections of listview cards, as well as the ability to manually create cards, and delete cards. Further functionality desired would be identification of factual statements and automatic generation of cards for factual statements. Simplest POC for this method would be separation of sentence subject from main clause and simply splitting the two parts of the sentence to the front/back ends of a card. 
