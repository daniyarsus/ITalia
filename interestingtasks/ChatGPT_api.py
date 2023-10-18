import openai

KEY = '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'

openai.api_key = KEY
def generate_response(text):
    response = openai.Completion.create(
        prompt = text, #запрос
        engine = 'gpt-3.5-turbo-0301', #модель ИИ
        max_tokens = 100, #количество символов в запрросе
        tempature = 0.7, #креативеость ответа
        answer = 10, #количество ответов
#        stop = None, #окончание ответа словом
        timeout = 60 #максимальное время ответа
    )

    if response and response.choises:
        return response.choises[0].text.strip
    else:
        return None

generate_response(input())