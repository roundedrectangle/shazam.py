# Stub file for rust implementation
# idk how to change the submodule name
# so it's also called shazam for now

from typing import Dict, List, Literal


class FrequencyPeak:
    fft_pass_number: int
    peak_magnitude: int
    corrected_peak_frequency_bin: int
    sample_rate_hz: int

    def get_frequency_hz(self) -> float: ...

    def get_amplitude_pcm(self) -> float: ...

    def get_seconds(self) -> float: ...


# before you ask I don't actually know
class FrequencyBand:
    _250_520: Literal[0]
    _520_1450: Literal[1]
    _1450_3500: Literal[2]
    _3500_5500: Literal[3]


class DecodedSignature:
    sample_rate_hz: int
    number_samples: int
    frequency_band_to_sound_peaks: Dict[FrequencyBand, List[FrequencyPeak]]

    # TODO: method types


def make_signature_from_buffer(bytes: bytes) -> DecodedSignature: ...
