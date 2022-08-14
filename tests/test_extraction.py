"""Tests for Extraction class"""
import json
import xml.etree.ElementTree as ET

from media_filesize_estimator.mediaExtraction import Extraction


def ordered(obj):
    """Compare two json objects' data"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def test_json():
    """Test JSON data creation"""
    extractionObj = Extraction("assets/sample_video_redfort.mp4")
    extractionObj.jsonCreation()  # creates in current folder
    with open("assets/sample_video_redfort.json") as fa, open(
        "sample_video_redfort.json"
    ) as fb:
        data_a = json.load(fa)
        data_b = json.load(fb)
        assert ordered(data_a) == ordered(data_b)


def test_xml():
    """Test XML data creation"""
    extractionObj = Extraction("assets/sample_video_redfort.mp4")
    extractionObj.XMLCreation()  # creates in current folder

    root_a = ET.parse("assets/sample_video_redfort.xml").getroot()
    root_b = ET.parse("sample_video_redfort.xml").getroot()
    # compare params
    for param in [
        "{https://mediaarea.net/mediainfo}Video_Codec_List",
        "{https://mediaarea.net/mediainfo}Audio_Format_Listl",
        "{https://mediaarea.net/mediainfo}FileSize",
    ]:
        for a, b in zip(root_a.iter(param), root_b.iter(param)):
            assert a.text == b.text


def test_csv():
    """Test CSV data creation"""
    extractionObj = Extraction("assets/sample_video_redfort.mp4")
    extractionObj.CSVCreation()  # creates in current folder

    with open("assets/sample_video_redfort.csv") as fa, open(
        "sample_video_redfort.csv"
    ) as fb:
        fileone = fa.readlines()
        filetwo = fb.readlines()
        for line in filetwo:
            # ignore file name
            if (
                ("complete_name" not in line)
                and ("file_name") not in line
                and ("folder_name") not in line
                and ("_date") not in line
            ):
                print(line)
                assert line in fileone
