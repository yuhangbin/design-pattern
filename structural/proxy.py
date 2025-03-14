
class ThirdPartyYouTubeLib:
    def __init__(self):
        pass

    def listVideos(self):
        pass
    
    def getVideoInfo(self, id):
        pass

    def downloadVideo(self, id):
        pass

class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def listVideos(self):
        return ["video1", "video2", "video3"]

    def getVideoInfo(self, id):
        return {"title": "video1", "author": "John Doe"}

    def downloadVideo(self, id):
        return f"Downloading video {id}"
    

class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service
        # Cached values dictionary
        # key: video id
        # value: video info
        self.listCache = None
        self.videoCache = None

    def listVideos(self):
        if self.listCache is None:
            self.listCache = self.service.listVideos()
        return self.listCache

    def getVideoInfo(self, id):
        if self.videoCache is None:
            self.videoCache = self.service.getVideoInfo(id)
        return self.videoCache

    def downloadVideo(self, id):
        if not self.videoCache.get(id):
            self.videoCache[id] = self.service.downloadVideo(id)
        return self.videoCache[id]

class YouTubeManager:
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service
    
    def renderVideoPage(self, id):
        info = self.service.getVideoInfo(id)
        print(f"Video page (cached): {info['title']}")
    
    def renderListPanel(self):
        videos = self.service.listVideos()
        print(f"List of videos (cached): {videos}")
    
    def reactOnUserInput(self):
        self.renderVideoPage("1")
        self.renderListPanel()

if __name__ == "__main__":
    service = ThirdPartyYouTubeClass()
    proxy = CachedYouTubeClass(service)
    manager = YouTubeManager(proxy)
    manager.reactOnUserInput()



