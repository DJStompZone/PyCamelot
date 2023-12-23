import pytest
from pycamelot.harmonic_mixing import HarmonicMixing

harmonic_mixing = HarmonicMixing()

@pytest.mark.parametrize("key, expected_camelot_key", [
    ('C', '8B'), ('G', '9B'), ('D', '10B'), ('A', '11B'), ('E', '12B'),
    ('B', '1B'), ('F#', '2B'), ('Db', '3B'), ('Ab', '4B'), ('Eb', '5B'),
    ('Bb', '6B'), ('F', '7B'),
    ('Am', '8A'), ('Em', '9A'), ('Bm', '10A'), ('F#m', '11A'), ('C#m', '12A'),
    ('G#m', '1A'), ('D#m', '2A'), ('Bbm', '3A'), ('Fm', '4A'), ('Cm', '5A'),
    ('Gm', '6A'), ('Dm', '7A'),
])
def test_get_camelot_key(key, expected_camelot_key):
    assert harmonic_mixing.get_camelot_key(key) == expected_camelot_key

@pytest.mark.parametrize("camelot_key, expected_compatible_keys", [
    ('8B', ['8B', '9B', '7B', '8A']),
    ('9B', ['9B', '10B', '8B', '9A']),
    ('10B', ['10B', '11B', '9B', '10A']),
    ('11B', ['11B', '12B', '10B', '11A']),
    ('12B', ['12B', '1B', '11B', '12A']),
    ('1B', ['1B', '2B', '12B', '1A']),
    ('2B', ['2B', '3B', '1B', '2A']),
    ('3B', ['3B', '4B', '2B', '3A']),
    ('4B', ['4B', '5B', '3B', '4A']),
    ('5B', ['5B', '6B', '4B', '5A']),
    ('6B', ['6B', '7B', '5B', '6A']),
    ('7B', ['7B', '8B', '6B', '7A']),
    ('8A', ['8A', '9A', '7A', '8B']),
    ('9A', ['9A', '10A', '8A', '9B']),
    ('10A', ['10A', '11A', '9A', '10B']),
    ('11A', ['11A', '12A', '10A', '11B']),
    ('12A', ['12A', '1A', '11A', '12B']),
    ('1A', ['1A', '2A', '12A', '1B']),
    ('2A', ['2A', '3A', '1A', '2B']),
    ('3A', ['3A', '4A', '2A', '3B']),
    ('4A', ['4A', '5A', '3A', '4B']),
    ('5A', ['5A', '6A', '4A', '5B']),
    ('6A', ['6A', '7A', '5A', '6B']),
    ('7A', ['7A', '8A', '6A', '7B']),
])
def test_get_compatible_keys(camelot_key, expected_compatible_keys):
    assert harmonic_mixing.get_compatible_keys(camelot_key) == expected_compatible_keys
    
    
def test_get_compatible_keys_invalid():
    with pytest.raises(ValueError):
        harmonic_mixing.get_compatible_keys('13Z')