sample_text = "This exercise and forum is subtly different from the previous one -- here we're asked to reflect on our personal understanding on the story but also to examine the techniques the author's using to put them across. How is the story structured and told, how are characters and settings deployed to back up those themes? Both ‘Bartleby’ and ‘Girl’ are provocative and multi-layered, and the way we read them and the subjects they convey depends a lot on our own life experiences and our sense of these stories in history or of their continued relevance.What a story is about depends so much on the reader -- it's worth remembering that as writers, with all our certainties. There are no (or perhaps few?) wrong readings -- art evokes feelings and ideas independent of the artist's intentions."

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

counts = dict()
for word in sample_text.split():
    word = word.strip()
    word = word.lower()
    for ele in word:
        if ele in punctuations:
            word = ele.replace(ele, "")
    if word not in uninteresting_words and word.isalpha():
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
        
print(counts)
