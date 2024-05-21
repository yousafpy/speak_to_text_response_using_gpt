from rest_framework import generics, mixins, status
from rest_framework.response import Response
import speech_recognition as sr

from speech_to_gpt_resp.utils import chat_bot_message_gpt3


class GptResponse(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin
):

    def get(self, request, *args, **kwargs):
        recognizer = sr.Recognizer()

        # Reading Microphone as source
        with sr.Microphone() as source:
            print("Speak Anything :")

            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            # Listens for the user's input
            audio = recognizer.listen(source)

            try:
                # Using google speech recognition
                text = recognizer.recognize_google(audio)
                print("You said : {}".format(text))
                response = chat_bot_message_gpt3(str(format(text)))
                return Response(response)
            except sr.UnknownValueError:
                print("Sorry could not recognize what you said")
                return None
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return None


def tester():
    recognizer = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Speak Anything :")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        # Listens for the user's input
        audio = recognizer.listen(source)

        try:
            # Using google speech recognition
            text = recognizer.recognize_google(audio)
            print("You said : {}".format(text))
            response = chat_bot_message_gpt3(format(text))
            return response
        except sr.UnknownValueError:
            print("Sorry could not recognize what you said")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None