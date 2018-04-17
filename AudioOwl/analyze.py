import librosa
import madmom
from madmom.features.beats import *
from scipy import signal
import numpy as np

def peak_picking(beat_times, total_samples, kernel_size, offset):

    # smoothing the beat function
    cut_off_norm = len(beat_times)/total_samples*100/2
    b, a = signal.butter(1, cut_off_norm)
    beat_times = signal.filtfilt(b, a, beat_times)

    # creating a list of samples for the rnn beats
    beat_samples = np.linspace(0, total_samples, len(beat_times), endpoint=True, dtype=int)

    n_t_medians = signal.medfilt(beat_times, kernel_size=kernel_size)
    offset = 0.01
    peaks = []

    for i in range(len(beat_times)-1):
        if beat_times[i] > 0:
            if beat_times[i] > beat_times[i-1]:
                if beat_times[i] > beat_times[i+1]:
                    if beat_times[i] > (n_t_medians[i] + offset):
                        peaks.append(int(beat_samples[i]))
    return peaks


def analyze(y, sr):

    data = {}

    # sample rate
    data['sample_rate'] = sr

    # getting duration in seconds
    data['duration'] = librosa.get_duration(y=y, sr=sr)

    # beats prediction
    # rnn_processor = RNNBeatProcessor()
    # beats = rnn_processor(y)

    rnn_processor = RNNBeatProcessor(post_processor=None)
    predictions = rnn_processor(y)
    mm_processor = MultiModelSelectionProcessor(num_ref_predictions=None)
    beats = mm_processor(predictions)

    data['beat_samples'] = peak_picking(beats, len(y), 5, 0.01)

    if len(data['beat_samples']) < 3:
        data['beat_samples'] = peak_picking(beats, len(y), 25, 0.01)

    if data['beat_samples'] == []:
        data['beat_samples'] = [0]

    data['number_of_beats'] = len(data['beat_samples'])

    # tempo
    data['tempo_float'] = (len(data['beat_samples'])-1)*60/data['duration']
    data['tempo_int'] = int(data['tempo_float'])


    # noisiness featues
    data['zero_crossing'] = librosa.feature.zero_crossing_rate(y)[0].tolist()
    data['noisiness_median'] = float(np.median(data['zero_crossing']))
    data['noisiness_sum'] = sum( librosa.zero_crossings(y)/y.shape[0] )

    # spectral features
    notes = []

    try:
        chroma = librosa.feature.chroma_cqt(y, n_chroma=12, bins_per_octave=12, n_octaves=8, hop_length=512)

        # CONVERSION TABLE
        # 0     c	  261.63
        # 1     c#	  277.18
        # 2	    d	  293.66
        # 3	    d#	  311.13
        # 4	    e	  329.63
        # 5	    f	  349.23
        # 6	    f#	  369.99
        # 7	    g	  392.00
        # 8	    g#	  415.30
        # 9	    a	  440.00
        # 10	a#	  466.16
        # 11	b	  493.88

        for col in range(chroma.shape[1]):
            notes.append(int(np.argmax(chroma[:,col])))

        data['notes'] = notes
        data['dominant_note'] = int(np.argmax(np.bincount(np.array(notes))))
    except:
        data['notes'] = [0]
        data['dominant_note'] = 0

    return data
