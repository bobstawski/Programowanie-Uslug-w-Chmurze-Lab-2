import azure.cognitiveservices.speech as speechsdk

def recognize_speech(subscription_key, region):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

    print("Choose action (recognize/synthesize): ")
    action_choice = input().lower()

    if action_choice == "recognize":
        print("Choose input (microphone/file): ")
        input_choice = input().lower()

        if input_choice == "microphone":
            recognize_speech_from_microphone(speech_config)
        elif input_choice == "file":
            file_path = input("Enter file path: ")
            recognize_speech_from_file(speech_config, file_path)
        else:
            print("Invalid input choice.")
    elif action_choice == "synthesize":
        text_to_speech(speech_config)
    else:
        print("Invalid action choice.")

def recognize_speech_from_microphone(speech_config):
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into the microphone...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = speechsdk.CancellationDetails.from_result(result)
        print(f"CancellationReason: {cancellation.reason}")
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print(f"ErrorDetails: {cancellation.error_details}")

def recognize_speech_from_file(speech_config, file_path):
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Recognizing speech from file...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = speechsdk.CancellationDetails.from_result(result)
        print(f"CancellationReason: {cancellation.reason}")
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print(f"ErrorDetails: {cancellation.error_details}")

def text_to_speech(speech_config):
    text = input("Enter text to synthesize: ")
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    
    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesis is complete.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print(f"CancellationReason: {cancellation.reason}")
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print(f"ErrorDetails: {cancellation.error_details}")

if __name__ == "__main__":
    # Replace with your subscription key and region
    subscription_key = "confidential"
    region = "eastus"  # e.g., "westus"

    recognize_speech(subscription_key, region)
