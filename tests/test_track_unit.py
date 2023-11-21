import pytest #type: ignore
from lib.track import Track

"""""
Test to confirm the track is created and title and artist are as provided
"""

def test_create_track():
    track = Track("Track1", "Artist1")
    assert track.title == "Track1"
    assert track.artist == "Artist1"

""""
Test to confirm if title and artist are not empty strings
"""
def test_title_is_not_empty():
    with pytest.raises(Exception) as e:
        track = Track("", "Artist1")
    assert str(e.value) == "Need to include both a title and artist"

def test_artist_is_not_empty():
    with pytest.raises(Exception) as e:
        track = Track("Track1", "")
    assert str(e.value) == "Need to include both a title and artist"

def test_title_and_artist_are_not_empty():
    with pytest.raises(Exception) as e:
        track = Track("", "")
    assert str(e.value) == "Need to include both a title and artist"

""""
Test to confirm both the title and artist are both strings
"""

def test_title_is_string():
    with pytest.raises(Exception) as e:
        track = Track(12345,"Artist1")
    assert str(e.value) == "Title and artist must be a string"

def test_artist_is_string():
    with pytest.raises(Exception) as e:
        track = Track("Track1",["Artist1"])
    assert str(e.value) == "Title and artist must be a string"

""""
Given the keyword matches either the title or the artist, return True
"""

def test_keyword_equals_title():
    track = Track("Track1", "Artist1")
    assert track.matches("Track1") == True

def test_keyword_equals_artist():
    track = Track("Track1", "Artist1")
    assert track.matches("Artist1") == True

""""
Given the keyword does not match either the title or the artist, return False
"""
def test_keyword_not_equal_to_title_or_artist():
    track = Track("Track1", "Artist1")
    assert track.matches("Test") == False

"""
Given the keyword is a partial match for either the title or the artist, 
return True
"""

def test_keyword_partial_match():
    track = Track("Track1", "Artist1")
    assert track.matches("tra") == True