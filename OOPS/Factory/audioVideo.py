from abc import ABC, abstractmethod


class ContentService(ABC):
    @abstractmethod
    def service(self):
        pass


class Text(ContentService):
    def service(self):
        print("You Have Acccess to Text Only")


class AudioTestService(ContentService):
    def service(self):
        print("You Have Acccess to Audio + Text Only")


class VideoAudioTextService(ContentService):
    def service(self):
        print("You Have Acccess to Text, Audio and Video: ", " ", end="")


class AcessServiceFactory:
    @staticmethod
    def get_service(service_type):
        if service_type == "text":
            return Text()
        elif service_type == "audio":
            return AudioTestService()
        elif service_type == "video":
            return VideoAudioTextService()
        else:
            raise ValueError("Invalid Service Type")


service_type = input("Enter the service type (Text, Audio, Video")
print(service_type)
service = AcessServiceFactory.get_service(service_type)
service.service()
