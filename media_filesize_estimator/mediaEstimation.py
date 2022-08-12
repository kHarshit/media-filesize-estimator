# import packages which are necessary
from fileinput import filename
from math import floor

import pymediainfo

from media_filesize_estimator.mediaExtraction import Extraction


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

        # print("possible media properties to estimate file sizes are : ")
        # print("resolution, frame_rate,...")
        self.tracksData = mediainfoDictionary["tracks"]
        self.extractionObj = extractionObj
        self.resolutionSamples = [
            (3840, 2160),
            (2560, 1440),
            (1920, 1080),
            (1280, 720),
            (640, 360),
        ]
        pass

    def estimate(self, mediaProperty=None):
        """
        param : Particular media property which needs to be estimated against
        return : Estimation sizes of the media file
        """
        if mediaProperty == None:
            raise Exception("Please provide a media property to provide an estimation")
        mediaType = str(self.extractionObj.mediaType)
        mediaData = None
        for i in self.tracksData:
            if (i["track_type"]).lower() == mediaType:
                mediaData = i

        if mediaData == None:
            raise Exception(
                f"{mediaType} data is not provided in the given media file, please check the file and try again..."
            )

        if mediaType == "video":
            if mediaProperty == "resolution":
                video_width = int(mediaData["width"])  # type: ignore
                video_height = int(mediaData["height"])  # type: ignore
                video_bit_depth = int(mediaData["bit_depth"])  # type: ignore
                number_of_frames = int(mediaData["frame_count"])  # type: ignore
                video_size = self.calculateSize(
                    video_width, video_height, video_bit_depth, number_of_frames
                )
                print(
                    f"Uncompressed file size estimation of the given file in MB with resolution {video_width} x {video_height} : {floor(video_size)}"
                )
                resolutionList = self.resolutionSamples
                for i in resolutionList:
                    video_size = self.calculateSize(
                        i[0], i[1], video_bit_depth, number_of_frames
                    )
                    print(
                        f"Uncompressed file size estimation of the given file in MB with resolution {i[0]} x {i[1]} : {floor(video_size)}"
                    )

        # print(mediaTypeData)

        pass

    def plotGraph(self, mediaProperty=None):
        """
        Using matplotlib give estimates on all the possible media properties
        """
        pass

    def calculateSize(
        self,
        video_width=None,
        video_height=None,
        video_bit_depth=None,
        number_of_frames=None,
    ):
        """
        Calculate file size based on the parameters
        """
        size_of_frame = (video_width * video_height * video_bit_depth) / 8
        file_size = (size_of_frame * number_of_frames) / (1024 * 1024)
        return file_size
        pass


if __name__ == "__main__":
    x = Estimation(r"C:\Users\drdin\Downloads\project_test.mkv")
    y = x.estimate("resolution")
