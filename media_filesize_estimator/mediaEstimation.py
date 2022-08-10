# import packages which are necessary
from fileinput import filename

import matplotlib
import pymediainfo
from mediaExtraction import Extraction


class Estimation:
    """
    import Extraction class and create an object if the object is not created already
    """

    def __init__(self, mediaFilePath=None):
        """
        Initialise Extraction class to check if the given media file is valid or not
        """
        extractionObj = Extraction(mediaFilePath)
        try:
            mediainfoObject = pymediainfo.MediaInfo.parse(extractionObj.mediaFilePath)
            mediainfoDictionary = mediainfoObject.to_data()
        except:
            print("An error occured, please check the file and try again")

        self.tracksData = mediainfoDictionary["tracks"]
        pass

    def Estimate(self, mediaProperty=None):
        """
        param : Particular media property which needs to be estimated against
        return : Estimation sizes of the media file
        """

        pass

    def plotGraph(self, mediaProperty=None):
        """
        Using matplotlib give estimates on all the possible media properties
        """
        pass
