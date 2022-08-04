# import packages which are necessary
import os
import sys

import matplotlib
import pymediainfo


class Extraction:
    """
    Using a media file as input, extract all the metadata in the required format
    """

    def __init__(self, location: str = "/"):
        """
        param: requires the location of the media file
        return : pymediainfo object with the extracted data
        """
        pass

    def jsonCreation(self):
        """
        Create a JSON file in the required location or else on a default location
        """
        pass

    def XMLCreation(self):
        """
        Create an XML file in the required location or else on a default location
        """
        pass

    def CSVCreation(self):
        """
        Create a CSV file in the required location or else on the default location
        """
        pass


class Estimation:
    """
    import Extraction class and create an object if the object is not created already
    """

    def __init__(self):
        """
        Get all the details from CSVCreation in Extraction class
        """
        pass

    def Estimate(self):
        """
        param : Particular media property which needs to be estimated against
        return : Estimation size of the media file
        """
        pass

    def plotGraph(self):
        """
        Using matplotlib give estimates on all the possible media properties
        """
        pass
