"""Tests for Extraction class"""
import json

from media_filesize_estimator.mediaExtraction import Extraction


def ordered(obj):
    """Compare two json objects' data"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def test_dummy():
    "Dummy test"
    assert 1 == 1


# def test_json():
#     """Test JSON data creation"""
#     extractionObj = Extraction("assets/sample_video_redfort.mp4")
#     extractionObj.jsonCreation("assets/test_metadata.json")
#     with open("assets/sample_video_redfort.json") as fa, open(
#         "assets/test_metadata.json"
#     ) as fb:
#         data_a = json.load(fa)
#         data_b = json.load(fb)
#         assert ordered(data_a) == ordered(data_b)


# def test_xml():
#     """Test XML data creation"""
#     extractionObj = Extraction("assets/sample_video_redfort.mp4")
#     extractionObj.jsonCreation("assets/test_metadata.xml")
#     pass


# def test_csv():
#     """Test CSV data creation"""
#     extractionObj = Extraction("assets/sample_video_redfort.mp4")
#     extractionObj.jsonCreation("assets/test_metadata.csv")
#     pass
