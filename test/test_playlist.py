from src.playlist import Playlist


def test_playlist_starts_empty():
    playlist = Playlist()

    assert playlist.tracks.is_empty()


def test_add_track():
    playlist = Playlist()

    playlist.add_track("Song A")

    assert playlist.tracks.to_list() == ["Song A"]


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