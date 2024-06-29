from nltk.downloader import Downloader


class NLTKDownloader:
    def __init__(self: object) -> None:
        self.downloader = Downloader()

    def __call__(self: object, requirements: list) -> None:
        self.downloader._update_index()
        for r in requirements:
            if self.downloader.status(r) == "installed":
                continue
            self.downloader.download(r)


downloader = NLTKDownloader()
