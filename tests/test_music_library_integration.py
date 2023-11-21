from lib.music_library import MusicLibrary
from lib.track import Track

"""
Check to see if tracks can be added to the tracklist
"""
def test_track_added_to_list():
    track_list = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    track_list.add(track1)
    track_list.add(track2)
    assert track_list.tracks == [track1, track2]

"""
Check to see if search method shows correct track list
- One track with keyword equal
- Multiple tracks, where keyword is in a selection
- Keyword is in no tracks
"""

def test_search_method_keyword_in_one_track():
    track_list = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track_list.add(track1)
    assert track_list.search("Title1") == [track1]


def test_search_method_keyword_in_multiple_tracks():
    track_list = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    track3 = Track("Title3", "Artist2")
    track_list.add(track1)
    track_list.add(track2)
    track_list.add(track3)
    assert track_list.search("Artist2") == [track2,track3]

def test_search_method_keyword_in_no_tracks():
    track_list = MusicLibrary()
    track1 = Track("Title1", "Artist1")
    track2 = Track("Title2", "Artist2")
    track3 = Track("Title3", "Artist2")
    track_list.add(track1)
    track_list.add(track2)
    track_list.add(track3)
    assert track_list.search("Test") == []