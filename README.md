# "Modified Rey Auditory Verbal Learning Test" or ModRey  

On 26-05-2023 I read an articles by the [AP](https://apnews.com/article/multivitamin-memory-aging-9dd73199796b280c42e141d59da11504) and [Washington Post](https://www.washingtonpost.com/wellness/2023/05/24/multivitamin-benefits-aging-memory-loss/) positing that consuming a multivitamin supplementation improves memory for those 60 and older.  
They described scientific research published under "Older Adults: A Randomized Clinical Trial." Lok-Kin Yeung, et.al. The American Journal of Clinical Nutrition. Available online 24 May 2023:  
https://ajcn.nutrition.org/article/S0002-9165(23)48904-6/fulltext (*behind paywall*)  
https://www.sciencedirect.com/science/article/abs/pii/S0002916523489046?dgcid=author (*behind paywall*)  

The articles about this research described short delay word list recall testing used to measure memory health.  That test was called the ["Modified Rey Auditory Verbal Learning Test" or ModRey](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5829025/).  

The script in this repo is my attempt to *emulate* this test.  
1. It selects 20 words from a google resource "20k.txt" at https://github.com/first20hours/google-10000-english.  ToDo: *I need a list better taylored to a ModRey test -- where using semantically and phonemically unrelated words improves the quality of test results*.  
2. Presents each for 3 seconds.  
3. After displaying all 20, it prompts the user to input the words they remenber.  
4. Finally, it outputs the number of matches and which input strings matched members of the list presented.  

After reading about the research results (*where [participants correctly recalled between 7.10 and 7.81 words]https://apnews.com/article/multivitamin-memory-aging-9dd73199796b280c42e141d59da11504)*) and taking this test -- it might be interesting to see how my list-retention capabilities change over time.  


