from src.linked_list import LinkedList


class Playlist:
    def __init__(self):
        self.tracks = LinkedList()
        self.current = None

    def add_track(self, track):
        self.tracks.append(track)

        if self.current is None:
            self.current = self.tracks.head

    def next_track(self):
        if self.current is None:
            return None

        if self.current.next is not None:
            self.current = self.current.next

        return self.current.data

    def previous_track(self):
        if self.current is None:
            return None

        previous = None
        current = self.tracks.head

        while current is not None and current != self.current:
            previous = current
            current = current.next

        if previous is not None:
            self.current = previous

        return self.current.data

    def remove_track(self, track):
        node = self.tracks.find(track)

        if node is None:
            return False

        if self.current == node:
            if node.next is not None:
                self.current = node.next
            else:
                previous = None
                current = self.tracks.head

                while current is not None and current != node:
                    previous = current
                    current = current.next

                self.current = previous

        self.tracks.remove(track)

        if self.tracks.is_empty():
            self.current = None

        return True