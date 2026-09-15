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

def test_remove_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    assert playlist.remove_track("Song B") is True
    assert playlist.tracks.to_list() == ["Song A", "Song C"]


def test_remove_current_track_moves_to_next():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    playlist.next_track()

    assert playlist.current.data == "Song B"

    playlist.remove_track("Song B")

    assert playlist.current.data == "Song C"


def test_remove_last_track():
    playlist = Playlist()

    playlist.add_track("Song A")

    assert playlist.remove_track("Song A") is True
    assert playlist.tracks.is_empty()
    assert playlist.current is None


def test_remove_missing_track():
    playlist = Playlist()

    playlist.add_track("Song A")

    assert playlist.remove_track("Song B") is False
    assert playlist.tracks.to_list() == ["Song A"]

def test_move_track_forward():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    playlist.move_track(0, 2)

    assert playlist.tracks.to_list() == [
        "Song B",
        "Song C",
        "Song A"
    ]


def test_move_track_backward():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    playlist.move_track(2, 0)

    assert playlist.tracks.to_list() == [
        "Song C",
        "Song A",
        "Song B"
    ]


def test_move_track_same_position():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")

    playlist.move_track(1, 1)

    assert playlist.tracks.to_list() == [
        "Song A",
        "Song B"
    ]


def test_move_track_invalid_index():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")

    try:
        playlist.move_track(5, 0)
        assert False
    except IndexError:
        assert True


def test_move_track_negative_index():
    playlist = Playlist()

    playlist.add_track("Song A")

    try:
        playlist.move_track(-1, 0)
        assert False
    except IndexError:
        assert True


def test_move_track_preserves_current_track():
    playlist = Playlist()

    playlist.add_track("Song A")
    playlist.add_track("Song B")
    playlist.add_track("Song C")

    playlist.next_track()

    playlist.move_track(1, 0)

    assert playlist.tracks.to_list() == [
        "Song B",
        "Song A",
        "Song C"
    ]

    assert playlist.current.data == "Song B"