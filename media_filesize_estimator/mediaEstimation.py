# import packages which are necessary
from fileinput import filename
from math import floor

import pymediainfo
import matplotlib.pyplot as plt
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
        self.frameRateSamples = [24,30,60,90]
        pass

    def estimate(self, mediaProperty=None):
        """
        param : Particular media property which needs to be estimated against
        return : Estimation sizes of the media file
        """
        plotDetails = {}
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
            video_width = int(mediaData["width"])  # type: ignore
            video_height = int(mediaData["height"])  # type: ignore
            video_bit_depth = int(mediaData["bit_depth"])  # type: ignore
            number_of_frames = int(mediaData["frame_count"])  # type: ignore
            frame_rate = float(mediaData["frame_rate"])  # type: ignore
            duration_in_seconds = floor(number_of_frames/frame_rate) # type: ignore
            
            if mediaProperty == "resolution":
                video_size = floor(self.calculateSize(
                    video_width, video_height, video_bit_depth, number_of_frames
                ))
                key_string = str(video_width) +"x"+ str(video_height)
                plotDetails[key_string]=video_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with resolution {video_width} x {video_height} : {video_size}"
                )
                resolutionList = self.resolutionSamples
                for i in resolutionList:
                    video_size = floor(self.calculateSize(
                        i[0], i[1], video_bit_depth, number_of_frames
                    ))
                    key_string = str(i[0]) +"x"+ str(i[1])
                    plotDetails[key_string]=video_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with resolution {i[0]} x {i[1]} : {video_size}"
                    )
            
            elif mediaProperty == "frame_rate":
                new_number_of_frames = duration_in_seconds * frame_rate
                video_size = floor(self.calculateSize(
                    video_width, video_height, video_bit_depth, new_number_of_frames
                ))
                key_string = str(frame_rate) +" FPS"
                plotDetails[key_string]=video_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with frame rate {frame_rate} FPS : {video_size}"
                )
                frame_list = self.frameRateSamples
                for i in frame_list:
                    frame_rate = i
                    new_number_of_frames = duration_in_seconds * frame_rate
                    video_size = floor(self.calculateSize(
                        video_width, video_height, video_bit_depth, new_number_of_frames
                    ))
                    key_string = str(frame_rate) +" FPS"
                    plotDetails[key_string]=video_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with frame rate {frame_rate} FPS : {video_size}"
                    )

        print(plotDetails)
        return plotDetails

    def plotGraph(self, mediaProperty=None):
        """
        Using matplotlib give estimates on all the possible media properties
        """
        plotDetails = self.estimate(mediaProperty)
        print("Plotting the graph for the given parameter")
        
        x = [i+1 for i in range(len(plotDetails))]
        x_label = [i for i in plotDetails.keys()]
        y = [i for i in plotDetails.values()]
        
        plt.bar(x, y, tick_label=x_label)
        if mediaProperty == 'resolution':
            plt.xlabel("Resolutions")
        elif mediaProperty == 'frame_rate':
            plt.xlabel("Frame Rates")
        
        plt.ylabel("File Size in Mega Bytes(MB)")
        plt.title(f"File size estimation of : {mediaProperty}")
        plt.show()

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
    y = x.plotGraph("frame_rate")
