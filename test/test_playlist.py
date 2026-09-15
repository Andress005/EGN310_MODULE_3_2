from src.playlist import Playlist


def test_playlist_starts_empty():
    playlist = Playlist()

    assert playlist.tracks.is_empty()
    assert playlist.current is None


def test_add_track():
    playlist = Playlist()

    playlist.add_track("Song A")

    assert playlist.tracks.to_list() == ["Song A"]
    assert playlist.current.data == "Song A"


def test_add_multiple_tracks():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    assert playlist.tracks.to_list() == [
        "Song A",
        "Song B",
        "Song C"
    ]


def test_next_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    assert playlist.next_track() == "Song B"
    assert playlist.next_track() == "Song C"


def test_next_track_stays_on_last_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")

    playlist.next_track()

    assert playlist.next_track() == "Song B"


def test_previous_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    playlist.next_track()
    playlist.next_track()

    assert playlist.previous_track() == "Song B"
    assert playlist.previous_track() == "Song A"


def test_previous_track_stays_on_first_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")

    assert playlist.previous_track() == "Song A"