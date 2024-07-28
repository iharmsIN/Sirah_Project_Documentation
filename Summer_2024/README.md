Summer 2024 Explanations
Search Engine Optimization
This was done by adding ownership on Google for the website.  The website used for understanding the different options was https://developers.google.com/search/docs/fundamentals/seo-starter-guide.
  meta code that can be added to html is 

'<meta itemprop="url" content="https://rjaques.github.io/Sirah-Project/"/>
<meta itemprop="name" content="Sirah Project"/>'


Explanation of .py files
split.py - this script will divide a witness file into passages.  The output is a folder with each passage as a .txt file.
Levenshtein2.py - this script runs a levenshtein distance comparison of two witnesses and requires witness files that are divided by the split.py.  The inputs are a target witness folder and a training witness folder.  The output changes the name of each file in the target folder to order it based on the most similar file in the training folder.  It also outputs a csv file of file names and levenshtein distances.  The code normalizes the arabic text and then sorts the target test by placing it with the most similar passage in the training folder.  This needs to be updated to use OpenITI normalization and to better predict passages that are not similar, but predict based on content or timeframe.
cosine_9.py - this script runs a cosine similarity comparison of two witnesses and requires witness files that are divided by the split.py.  The inputs are a target witness folder and a training witness folder.  The output changes the name of each file in the target folder to order it based on the most similar file in the training folder.  It also outputs a csv file of file names and cosine similarity score.  The code normalizes the arabic text and then sorts the target test by placing it with the most similar passage in the training folder.  This needs to be updated to use OpenITI normalization and to better predict passages that are not similar, but predict based on content or timeframe.
Combine.py - this script combines all files in a folder in the order specified by the name.  This is meant to combine the .txt files in a target folder after running a training model.
Word_Count.py - this script counts the most common arabic words in a .txt file.
FindPipes.py - this script takes a split folder as the input and will output which files contain the different pipes for the witnesses.
