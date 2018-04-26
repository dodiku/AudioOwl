from .analyze import analyze

def analyze_file(path, sr=22050):
    import librosa
    y, sr = librosa.load(path, sr=sr)
    return analyze(y, sr)


def analyze_samples(y, sr=22050):
    return analyze(y, sr)

def get_waveform(path, sr=22050):
    import librosa
    y, sr = librosa.load(path, sr=sr)
    return y
