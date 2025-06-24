# Week-2 Assignment-1
# TF-IDF Comparison
## Corpus
- the sun is a star
- the moon is a satellite
- the sun and moon are celestial bodies
## Observation
1. **Common Words**
   'CountVectorizer' simply counts raw frequency, so common words like "the, and, but.." appears frequently.
   'TF-IDF' reduces the weight of common words. Since they appear in all documents, its IDF is log(3/3) = 0, so TF-IDF = 0.
   Thus, words like "the, and, but.." has high importance in 'CountVectorizer' but nearly no importance in 'TF-IDF'.
2. **Unique Words**
   Words like "star", "satellite", and "bodies" have higher TF-IDF scores because they occur in fewer documents, makes them different from others.
## Conclusion
   TF-IDF provides better word weighting by giving higher weight to words which are frequent & rare in corpus.
 
