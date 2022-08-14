# import packages which are necessary
from fileinput import filename
from math import floor

import matplotlib.pyplot as plt
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
        self.frameRateSamples = [24, 30, 60, 90]
        self.bitDepths = [8, 10, 12, 16]
        self.sampleRates = [8, 16, 44.1, 48]
        self.channels = [1, 2, 4, 6, 8]
        pass

    def estimate(self, mediaProperty=None):
        """
        param : Particular media property which needs to be estimated against
        return : Estimation sizes of the media file in a dictionary
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
            duration_in_seconds = floor(number_of_frames / frame_rate)

            if mediaProperty == "resolution":
                video_size = self.calculateVideoSize(
                    video_width, video_height, video_bit_depth, number_of_frames
                )
                key_string = str(video_width) + "x" + str(video_height)
                plotDetails[key_string] = video_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with resolution {key_string} : {video_size} MB"
                )
                resolutionList = self.resolutionSamples
                for i in resolutionList:
                    video_size = self.calculateVideoSize(
                        i[0], i[1], video_bit_depth, number_of_frames
                    )
                    key_string = str(i[0]) + "x" + str(i[1])
                    plotDetails[key_string] = video_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with resolution {key_string} : {video_size} MB"
                    )

            elif mediaProperty == "frame_rate":
                new_number_of_frames = duration_in_seconds * frame_rate
                video_size = self.calculateVideoSize(
                    video_width, video_height, video_bit_depth, new_number_of_frames
                )
                key_string = str(frame_rate) + " FPS"
                plotDetails[key_string] = video_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with frame rate {key_string} : {video_size} MB"
                )
                frame_list = self.frameRateSamples
                for i in frame_list:
                    frame_rate = i
                    new_number_of_frames = duration_in_seconds * frame_rate
                    video_size = self.calculateVideoSize(
                        video_width, video_height, video_bit_depth, new_number_of_frames
                    )
                    key_string = str(frame_rate) + " FPS"
                    plotDetails[key_string] = video_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with frame rate {key_string} : {video_size} MB"
                    )

            elif mediaProperty == "bit_depth":
                video_size = self.calculateVideoSize(
                    video_width, video_height, video_bit_depth, number_of_frames
                )
                key_string = str(video_bit_depth) + " bit"
                plotDetails[key_string] = video_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {video_size} MB"
                )
                bit_depth_list = self.bitDepths
                for i in bit_depth_list:
                    new_video_bit_depth = i
                    video_size = self.calculateVideoSize(
                        video_width, video_height, new_video_bit_depth, number_of_frames
                    )
                    key_string = str(new_video_bit_depth) + " bit"
                    plotDetails[key_string] = video_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {video_size} MB"
                    )
            else:
                raise Exception(
                    f"Please test with a different property as the given video file does not estimate property : {mediaProperty}"
                )

        elif mediaType == "audio":
            audio_sampling_rate = int(mediaData["sampling_rate"])  # type: ignore
            audio_channels = int(mediaData["channel_s"])  # type: ignore
            try:
                audio_bit_depth = int(mediaData["bit_depth"])  # type: ignore
            except:
                # compressed files might or might not have bit depth
                # if bit depth is not mentioned we are assuming it as 8 by default
                audio_bit_depth = 8
            audio_duration = round(int(mediaData["duration"]) / 1000)  # type: ignore

            if mediaProperty == "sampling_rate":
                audio_size = self.calculateAudioSize(
                    audio_sampling_rate, audio_bit_depth, audio_channels, audio_duration
                )
                key_string = str(round(audio_sampling_rate / 1000, 1)) + " kHz"
                plotDetails[key_string] = audio_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with sample rate {key_string} : {audio_size} MB"
                )
                sampleRateList = [i * 1000 for i in self.sampleRates]
                for i in sampleRateList:
                    audio_sampling_rate = i
                    audio_size = self.calculateAudioSize(
                        audio_sampling_rate,
                        audio_bit_depth,
                        audio_channels,
                        audio_duration,
                    )
                    key_string = str(round(audio_sampling_rate / 1000, 1)) + " kHz"
                    plotDetails[key_string] = audio_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with sample rate {key_string} : {audio_size} MB"
                    )
            elif mediaProperty == "bit_depth":
                audio_size = self.calculateAudioSize(
                    audio_sampling_rate, audio_bit_depth, audio_channels, audio_duration
                )
                key_string = str(audio_bit_depth) + " bit"
                plotDetails[key_string] = audio_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {audio_size} MB"
                )
                bit_depth_list = self.bitDepths
                for i in bit_depth_list:
                    audio_bit_depth = i
                    audio_size = self.calculateAudioSize(
                        audio_sampling_rate,
                        audio_bit_depth,
                        audio_channels,
                        audio_duration,
                    )
                    key_string = str(audio_bit_depth) + " bit"
                    plotDetails[key_string] = audio_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {audio_size} MB"
                    )
            elif mediaProperty == "channels":
                audio_size = self.calculateAudioSize(
                    audio_sampling_rate, audio_bit_depth, audio_channels, audio_duration
                )
                key_string = str(audio_channels) + " channel"
                plotDetails[key_string] = audio_size
                print(
                    f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {audio_size} MB"
                )
                audio_channel_list = self.channels
                for i in audio_channel_list:
                    audio_channels = i
                    audio_size = self.calculateAudioSize(
                        audio_sampling_rate,
                        audio_bit_depth,
                        audio_channels,
                        audio_duration,
                    )
                    key_string = str(audio_channels) + " channel"
                    plotDetails[key_string] = audio_size
                    print(
                        f"Uncompressed file size estimation of the given file in MB with bit depth {key_string} : {audio_size} MB"
                    )
            else:
                raise Exception(
                    f"Please test with a different property as the given audio file does not estimate property : {mediaProperty}"
                )

        return plotDetails

    def plotGraph(self, mediaProperty=None, outGraphPath="./"):
        """
        Using matplotlib give estimates on all the possible media properties
        """
        plotDetails = self.estimate(mediaProperty)
        print(f"Plotting the graph for the given parameter : {mediaProperty}")

        x = [i + 1 for i in range(len(plotDetails))]
        x_label = [i for i in plotDetails.keys()]
        y = [i for i in plotDetails.values()]
        colors = ["red" if i == 0 else "blue" for i in range(len(x_label))]

        plt.bar(x, y, tick_label=x_label, color=colors)
        if mediaProperty == "resolution":
            plt.xlabel("Resolutions of the Video")
        elif mediaProperty == "frame_rate":
            plt.xlabel("Frame Rates of the Video")
        elif mediaProperty == "bit_depth":
            plt.xlabel("Bit Depths")
        elif mediaProperty == "sampling_rate":
            plt.xlabel("Sample Rates of the Audio")
        elif mediaProperty == "channels":
            plt.xlabel("Number of Audio Channels")

        plt.ylabel("File Size in Mega Bytes(MB)")
        plt.title(f"File size estimation of : {mediaProperty}")
        save_path = f"{outGraphPath}/estimated_filesize.png"
        plt.savefig(save_path)

        return save_path

    def calculateVideoSize(
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
        file_size = round(((size_of_frame * number_of_frames) / (1024 * 1024)), 3)
        return file_size

    def calculateAudioSize(
        self,
        audio_sampling_rate=None,
        audio_bit_depth=None,
        audio_channels=None,
        audio_duration=None,
    ):
        """
        Calculate file size based on the parameters
        """
        file_size_bytes = (
            audio_sampling_rate * audio_bit_depth * audio_channels * audio_duration
        ) / 8
        file_size = round(file_size_bytes / (1024 * 1024), 3)
        return file_size
