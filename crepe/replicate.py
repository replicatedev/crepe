from scipy.io import wavfile
from .core import predict

def setup():
    return

def infer(model, audio_path):
    try:
        sr, audio = wavfile.read(audio_path)
    except ValueError:
        print("CREPE: Could not read %s" % audio_path, file=sys.stderr)
        raise
    time, frequency, confidence, activation = predict(audio, sr, verbose=1)
    return time, frequency

