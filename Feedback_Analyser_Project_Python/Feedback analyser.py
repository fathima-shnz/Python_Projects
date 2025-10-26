feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]}

#Add more feedbacks
num_fb = int(input("How many feedbacks do you want to add? "))
s_no = 11
for i in range(num_fb):
    s_no += 1
    print(f"Enter feedback {i+1}")
    name = input("Name: ")
    feedback = input("Feedback: ")
    rating = int(input("Rating(1 to 5): "))

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data["Rating"].append(rating)
   

#Clean feedback data
cleaned_feedback = []
for fb in feedback_data['Feedback']:
    for char in ('.',',','!','?'):
        fb = fb.replace(char, '')
    fb = ' '.join(fb.split())
    fb = fb.lower()
    cleaned_feedback.append(fb)
feedback_data['Feedback'] = cleaned_feedback


#function counting feedback words:
def count_word_in_feedbacks(word):
    count = 0
    word = word.lower()
    for string in feedback_data['Feedback']:
        if word in string.split():
            count += 1
    return count
print(f"Feedbacks containing good: {count_word_in_feedbacks('good')}")
print(f"Feedbacks containing poor: {count_word_in_feedbacks('poor')}")
print(f"Feedbacks containing excellent: {count_word_in_feedbacks('excellent')}")


#Final summary and insights

#Display Data
print(feedback_data)

#Average rating
ratings = feedback_data['Rating']
average_rating = sum(ratings) / len(ratings)
print(f"Average rating: {average_rating}")

#Longest word count
ind_longest = 0
max_words = 0
for i, fb in enumerate(feedback_data['Feedback']):
    word_count = len(fb.split())
    if word_count > max_words:
        max_words = word_count
        ind_longest = i
print("Longest feedback: ")
print(f"{feedback_data['Feedback'][ind_longest]}")

#Unique words
unique = set()
for fb in feedback_data['Feedback']:
    for i in fb.split():
        unique.add(i)
print(sorted(unique))











