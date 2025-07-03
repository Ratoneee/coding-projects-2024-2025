import os
import shutil
import tempfile
import pytest
from game_asset_organizer import get_file_type, organize_files

def test_get_file_type():
    assert get_file_type("model.fbx") == "3D Models"
    assert get_file_type("thing.obj") == "3D Models"
    assert get_file_type("script.py") == "Code"
    assert get_file_type("game.cs") == "Code"
    assert get_file_type("texture.png") == "Textures"
    assert get_file_type("image.jpg") == "Textures"
    assert get_file_type("music.mp3") == "Sounds"
    assert get_file_type("sound.wav") == "Sounds"
    assert get_file_type("data.txt") == "Others"
    assert get_file_type("file.zip") == "Others"

def test_organize_files_creates_correct_folders_and_moves_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_files = [
            ("hero.fbx", "3D Models"),
            ("enemy.cs", "Code"),
            ("sky.jpg", "Textures"),
            ("theme.wav", "Sounds"),
            ("readme.txt", "Others")
        ]
        
        for filename, _ in test_files:
            with open(os.path.join(temp_dir, filename), "w") as f:
                f.write("mock content")

        organize_files(temp_dir)

        for filename, category in test_files:
            name_without_ext = os.path.splitext(filename)[0]
            expected_path = os.path.join(temp_dir, category, name_without_ext, filename)
            assert os.path.exists(expected_path), f"{filename} was not moved correctly"

        expected_folders = ["3D Models", "Code", "Textures", "Sounds", "Others"]
        for folder in expected_folders:
            assert os.path.exists(os.path.join(temp_dir, folder)), f"{folder} folder is missing"
