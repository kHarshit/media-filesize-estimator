# import packages which are necessary
import errno
from fileinput import filename
from msilib.schema import Error
import os
import mimetypes

import pymediainfo


class Extraction:
    """
    Using a media file as input, extract all the metadata in the required format
    """

    def __init__(self, location = None):
        """
        param: requires the location of the media file
        """
        if location == None:
            raise Exception("File not provided. Please provide a media file to work on")
        location = r"{}".format(location)
        if os.path.exists(location):
            self.mediaFilePath = location
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), location)
        
        self.fileNameWithExtension = os.path.basename(self.mediaFilePath)
        self.fileName = (self.fileNameWithExtension).split('.')[0]
        mimetypes.init()
        mimestart = mimetypes.guess_type(self.fileNameWithExtension)[0]
        
        if mimestart != None:
            mimestart = mimestart.split('/')[0]
            if mimestart in ['video','audio','image']:
                print("The given media file is of type : {}".format(mimestart))
            else:
                raise Exception("The provided file is not a media file. Please provide a valid media file")
        else:
            raise Exception("Unable to identify the file type, please try with Video, Audio or Image files only")

        pass

    def jsonCreation(self, extractionPath = None):
        """
        Create a JSON file in the required location or else on the default location
        """
        print("Extracting data from file : {}".format(self.fileNameWithExtension))
        try:
            jsonData = pymediainfo.MediaInfo.parse(self.mediaFilePath, output='JSON')
        except:
            print("An error occured, please check the file and try again")
        
        extractionType = '.json'
        return(self.fileCreation(jsonData, extractionPath, extractionType))

    def XMLCreation(self, extractionPath = None):
        """
        Create an XML file in the required location or else on a default location
        """
        print("Extracting data from file : {}".format(self.fileNameWithExtension))
        try:
            XMLData = pymediainfo.MediaInfo.parse(self.mediaFilePath, output='XML')
        except:
            print("An error occured, please check the file and try again")
        
        extractionType = '.xml'
        return(self.fileCreation(XMLData, extractionPath, extractionType))

    def CSVCreation(self, extractionPath = None):
        """
        Create a CSV file in the required location or else on the default location
        """
        print("Extracting data from file : {}".format(self.fileNameWithExtension))
        try:
            mediainfoObject = pymediainfo.MediaInfo.parse(self.mediaFilePath)
            mediainfoDictionary = mediainfoObject.to_data()
        except:
            print("An error occured, please check the file and try again")
        
        tracksData = mediainfoDictionary['tracks']
        extractionType = '.csv'
        return(self.fileCreation(tracksData, extractionPath, extractionType))

    def fileCreation(self, data, extractionPath, extractionType):
        """
        Create files based on the paths and data
        """
        filename = self.fileName
        if extractionPath == None:
            print("Extraction location for the file not found, Extracting in the current working directory")
            extractionPath = os.getcwd()
        if not(os.path.exists(extractionPath)):
            raise Exception("The directory to extract the file does not exist, please verify and try again")
        
        filenameWithExtension = filename + extractionType
        finalFile = os.path.join(extractionPath, filenameWithExtension)
        
        if extractionType == '.csv':
            if os.path.exists(finalFile):
                print("File already created overwriting the content")
            with open(finalFile, 'w+') as f:
                for track in data:
                    for key in track.keys():
                        f.write("%s, %s\n" % (key, track[key]))
        else:
            if os.path.exists(finalFile):
                print("File already created overwriting the content")
            with open(finalFile, 'w') as f:
                f.write(data)
        returnStatment = "Extraction completed successfully to file : {}".format(finalFile)
        print(returnStatment)
        return returnStatment
