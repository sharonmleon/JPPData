file = open("/Users/sharonleon/Documents/GitHub/JPPNarrative/Community/CommunityKinship.html", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))