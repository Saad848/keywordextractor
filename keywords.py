# 09/09/2020
# Key words algorithms:

# 1) YAKE  https://pypi.org/project/yake/
# 2) RAKE  https://pypi.org/project/rake-nltk/
# 3) Text Rank
# 4) Gensim  https://dev.to/b_dmarius/python-keywords-extraction-machine-learning-project-series-part-2-2bii
# 5) TF-IDF
# 6) spaCy

from rake_nltk import Metric,Rake


r = Rake() 

kt = input('''
	
╔═╗┌┐┌┌┬┐┌─┐┬─┐  ┬ ┬┌─┐┬ ┬┬─┐  ┌─┐┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌─┐┬ ┬
║╣ │││ │ ├┤ ├┬┘  └┬┘│ ││ │├┬┘  ├─┘├─┤├┬┘├─┤│ ┬├┬┘├─┤├─┘├─┤
╚═╝┘└┘ ┴ └─┘┴└─   ┴ └─┘└─┘┴└─  ┴  ┴ ┴┴└─┴ ┴└─┘┴└─┴ ┴┴  ┴ ┴ ''')


print(r.extract_keywords_from_text(kt))
print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases_with_scores())
# print(r.get_ranked_phrases_with_scores())








#If you want to control the max or min words in a phrase, for it to be
# considered for ranking you can initialize a Rake instance as below:
# r = Rake(min_length=2, max_length=4)


# kt ='''It is the purpose of being together, which forms the relationship between people. 
# There is no there is no existence of the purpose is found than two entities remain strangers to each other. 
# When common interest is in existence and common thinking are present between the two, it is likely to 
# say that people will be much closer to each other. Ultimately the base of a relationship is rooted in the question 
# of why someone wants to spend time with someone?But sometimes the relation is already provided by nature like 
# family where bond is pre-created. This form of relationship is free from any questions, In this type of blood 
# relationship there is no strange part.﻿'''


 