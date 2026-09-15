# Playlist Manager

## Overview

This project is a Streamlit Playlist Manager application backed by a custom singly linked list implementation.

The application allows users to manage and navigate a playlist while using the linked list developed for the previous assignment.

## Features

The Playlist Manager supports:

* Adding tracks
* Removing tracks
* Moving to the next track
* Moving to the previous track
* Reordering tracks
* Displaying the current track
* Maintaining playlist state during Streamlit interactions

## Project Structure

```text
EGN310_MODULE_3_2/
├── src/
│   ├── linked_list.py
│   └── playlist.py
├── test/
│   ├── test_linked_list.py
│   └── test_playlist.py
├── app.py
├── requirements.txt
├── README.md
├── AI_LOG.md
└── .gitignore
```

## Implementation

The application uses a custom `LinkedList` class to store playlist tracks.

The `Playlist` class provides the application-level functionality for:

* Adding tracks
* Navigating between tracks
* Removing tracks
* Reordering tracks

The Streamlit interface uses `st.session_state` to preserve the playlist while the application reruns after user interactions.

## Testing

Automated tests are written using `pytest`.

Run the tests with:

```bash
pytest
```

The current test suite contains 40 tests.

Expected result:

```text
40 passed
```

## Running the Application Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in a local browser.

## Deployment

The application is deployed using Streamlit Community Cloud.

Live application:

*Add Streamlit deployment link here after deployment.*

## Author

Andres Rincon
