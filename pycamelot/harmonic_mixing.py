class HarmonicMixing:
    """
    A class to represent the table of harmonic mixing using Camelot notation.
    This class uses the circle of fifths to determine compatible keys for mixing.

    Attributes:
        circle_of_fifths (List[str]): A list representing the circle of fifths sequence.
        camelot_wheel (Dict[str, str]): A mapping from musical keys to their corresponding Camelot keys.
        enharmonics: (Dict[str, str]): A mapping of enharmonics to relate between equivalent sharps and flats 
    """
    
    circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']

    enharmonics = {
            'Gb': 'F#', 'Cb': 'B', 'Fb': 'E', 'Bbb': 'A#', 'E#': 'F', 'C#': 'Db',
            'G#': 'Ab', 'D#': 'Eb', 'A#': 'Bb'
        }

    def __init__(self):
        self.camelot_wheel = {}
        for i, key in enumerate(self.circle_of_fifths):
            camelot_number = ((i + 7) % 12) + 1
            self.camelot_wheel[key] = f"{camelot_number}B"
            relative_minor = self._get_relative_minor(key)
            self.camelot_wheel[relative_minor] = f"{camelot_number}A"
    
    def get_camelot_key(self, key):
        """
        Returns the Camelot key for a given musical key.

        Args:
            key (str): The musical key (e.g., 'C', 'Am').

        Returns:
            str: The corresponding Camelot key.

        Raises:
            ValueError: If the given key is not found in the Camelot wheel.
        """
        if key not in self.camelot_wheel:
            raise ValueError("Invalid key provided.")
        return self.camelot_wheel[key]
    
    def get_compatible_keys(self, camelot_key):
        """
        Returns a list of compatible keys for a given Camelot key.

        Args:
            camelot_key (str): The Camelot key (e.g., '5B', '6A').

        Returns:
            List[str]: A list of compatible Camelot keys.

        Raises:
            ValueError: If the given Camelot key is invalid.
        """
        if not (camelot_key[:-1].isdigit() and camelot_key[-1] in ('A', 'B')):
            raise ValueError("Invalid Camelot key provided.")
        key_number = int(camelot_key[:-1])
        key_letter = camelot_key[-1]
        perfect_mix = f"{key_number}{key_letter}"
        one_mix_up = f"{(key_number % 12) + 1}{key_letter}"
        one_mix_down = f"{(key_number - 2) % 12 + 1}{key_letter}"
        relative_key = f"{key_number}{'A' if key_letter == 'B' else 'B'}"
        
        return [perfect_mix, one_mix_up, one_mix_down, relative_key]
    
    @staticmethod
    def _get_relative_minor(major_key):
        """Determines the relative minor of a given major key using the Camelot wheel notation."""
        # This dictionary maps major keys to their relative minor keys according to the Camelot wheel
        major_to_minor = {
            'C': 'Am', 'G': 'Em', 'D': 'Bm', 'A': 'F#m', 'E': 'C#m',
            'B': 'G#m', 'F#': 'D#m', 'Db': 'Bbm', 'Ab': 'Fm', 'Eb': 'Cm',
            'Bb': 'Gm', 'F': 'Dm'
        }
        return major_to_minor[major_key]