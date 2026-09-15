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

    def move_track(self, old_index, new_index):
        if old_index < 0 or new_index < 0:
            raise IndexError("Index cannot be negative")

        tracks = self.tracks.to_list()

        if old_index >= len(tracks) or new_index >= len(tracks):
            raise IndexError("Index out of range")

        if old_index == new_index:
            return

        track = tracks.pop(old_index)
        tracks.insert(new_index, track)

        self.tracks = LinkedList()

        for item in tracks:
            self.tracks.append(item)

        current_track = self.current.data if self.current is not None else None

        self.current = self.tracks.find(current_track)