import requests, json

def emotion_detection(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    formatted = json.loads(response.text)
    emotions = formatted['emotionPredictions'][0]['emotion']
    
    dominant_emotion = ''
    score = 0
    for emotion in emotions:
        if emotions[emotion] > score:
            dominant_emotion = emotion
            score = emotions[emotion]

    emotions['dominant_emotion'] = dominant_emotion

    return emotions
