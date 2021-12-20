#Like the previous exercise, but considering user may enter different letter cases
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return "That word does not exist."
#
# word = input("Enter word: ").lower()
# print(vocabulary(word))


d = dict(weather = "clima", earth = "terra", rain = "chuva")
user_word = input("Enter Words: ")
def Portugese(word):
    try:
        return d[word.lower()]
    except:
        return ("We couldn't find that word!")
print(Portugese(user_word))