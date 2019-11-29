from scipy.io import wavfile
from .core import predict

def setup():
    return

def infer(audio_path):
    try:
        sr, audio = wavfile.read(file)
    except ValueError:
        print("CREPE: Could not read %s" % file, file=sys.stderr)
        raise
    time, frequency, confidence, activation = predict(audio, sr, verbose=1)
    return time, frequency

