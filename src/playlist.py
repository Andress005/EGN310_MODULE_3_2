from src.linked_list import LinkedList


class Playlist:
    def __init__(self):
        self.tracks = LinkedList()

    def add_track(self, track):
        self.tracks.append(track)