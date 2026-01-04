# Spotify Playlist Icon Generator

Goal
- Generate square playlist cover images with a large month/headline and a subtext (e.g. year).
- Main generator class: [`PlaylistIconGenerator`](PlaylistIconGenerator.py).
- Single-icon class: [`PlaylistIcon`](PlaylistIcon.py).

Quick links
- Project entry: [main.py](main.py)  
- Generator: [`PlaylistIconGenerator`](PlaylistIconGenerator.py) — implementation in [PlaylistIconGenerator.py](PlaylistIconGenerator.py)  
- Single icon: [`PlaylistIcon`](PlaylistIcon.py) — implementation in [PlaylistIcon.py](PlaylistIcon.py)  
- Size type: [`Size`](Types.py) — implementation in [Types.py](Types.py)  
- Dependency file: [Pipfile](Pipfile)  
- Fonts folder: [Fonts/Circular/Read Me.txt](Fonts/Circular/Read Me.txt) (CURRENTLY HARDCODED FOR LINUX)

Installing
1. Using pipenv (recommended since the repo includes a Pipfile):
   ```sh
   sudo apt install pipenv
   pipenv install
   pipenv shell