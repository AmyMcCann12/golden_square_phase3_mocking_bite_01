import pytest
from lib.music_library import MusicLibrary
from unittest.mock import Mock
"""
Check to see if the track list is created
"""

def test_check_track_list_exists():
    track_list = MusicLibrary()
    assert track_list.tracks == []

"""
Check to see if tracks can be added to the tracklist
"""

def test_tracks_added_to_track_list():
    track_list = MusicLibrary()

    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'

    fake_track2 = Mock()
    fake_track2.title = 'Title2'
    fake_track2.artist = 'Artist2'

    track_list.add(fake_track1)
    track_list.add(fake_track2)

    assert track_list.tracks == [fake_track1,fake_track2]


"""
Check to see if the keyword in search is a string.
Throw an exception if not
"""
def test_keyword_in_search_is_string():
    track_list = MusicLibrary()
    with pytest.raises(Exception) as e:
        track_list.search(999)
    assert str(e.value) == 'Keyword must be a string'


"""
Check to see if search method shows correct track list
"""
def test_search_method_keyword_in_one_track():
    track_list = MusicLibrary()

    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'
    fake_track1.matches.return_value = True

    track_list.add(fake_track1)

    assert track_list.search('Title1') == [fake_track1]


def test_search_method_keyword_in_multiple_tracks():
    track_list = MusicLibrary()

    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'
    fake_track1.matches.return_value = False

    fake_track2 = Mock()
    fake_track2.title = 'Title2'
    fake_track2.artist = 'Artist2'
    fake_track2.matches.return_value = True

    track_list.add(fake_track1)
    track_list.add(fake_track2)

    assert track_list.search('Title2') == [fake_track2]

def test_search_method_keyword_in_no_tracks():
    track_list = MusicLibrary()

    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'
    fake_track1.matches.return_value = False

    fake_track2 = Mock()
    fake_track2.title = 'Title2'
    fake_track2.artist = 'Artist2'
    fake_track2.matches.return_value = False

    track_list.add(fake_track1)
    track_list.add(fake_track2)

    assert track_list.search('Test') == []