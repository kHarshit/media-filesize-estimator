"""Tests for Extraction class"""
import json

from lxml import etree

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

    treea = etree.parse("assets/sample_video_redfort.xml")
    treeb = etree.parse("sample_video_redfort.xml")
    assert set(treea.getroot().itertext()) == set(treeb.getroot().itertext())


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
            assert line in fileone
