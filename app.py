import streamlit as st
from src.playlist import Playlist

st.set_page_config(
    page_title="Playlist Manager",
    page_icon="🎵"
)

st.title("🎵 Playlist Manager")
st.write("Manage your playlist using a custom linked list.")

if "playlist" not in st.session_state:
    st.session_state.playlist = Playlist()

playlist = st.session_state.playlist

st.header("Add a Track")

track_name = st.text_input("Track name")

if st.button("Add Track"):
    if track_name.strip():
        playlist.add_track(track_name.strip())
        st.success(f'Added "{track_name.strip()}" to the playlist.')
    else:
        st.warning("Please enter a track name.")

st.header("Your Playlist")

tracks = playlist.tracks.to_list()

if tracks:
    for index, track in enumerate(tracks):
        if playlist.current is not None and track == playlist.current.data:
            st.write(f"▶️ **{index + 1}. {track}**")
        else:
            st.write(f"{index + 1}. {track}")
else:
    st.write("Your playlist is empty.")

st.header("Playback Controls")

col1, col2 = st.columns(2)

with col1:
    if st.button("⏮️ Previous"):
        playlist.previous_track()

with col2:
    if st.button("⏭️ Next"):
        playlist.next_track()

st.header("Remove a Track")

if tracks:
    track_to_remove = st.selectbox(
        "Select a track to remove",
        tracks
    )

    if st.button("🗑️ Remove Track"):
        playlist.remove_track(track_to_remove)
        st.success(f'Removed "{track_to_remove}" from the playlist.')
else:
    st.write("There are no tracks to remove.")

st.header("Reorder a Track")

if len(tracks) >= 2:
    track_to_move = st.selectbox(
        "Select a track to move",
        tracks,
        key="move_track"
    )

    current_index = tracks.index(track_to_move)

    new_position = st.number_input(
        "New position",
        min_value=1,
        max_value=len(tracks),
        value=current_index + 1,
        step=1
    )

    if st.button("↕️ Move Track"):
        playlist.move_track(current_index, new_position - 1)
        st.success(
            f'Moved "{track_to_move}" to position {new_position}.'
        )
else:
    st.write("Add at least two tracks to reorder the playlist.")
