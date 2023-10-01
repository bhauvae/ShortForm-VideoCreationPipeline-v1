import requests
from .media_object import Background_clip as Clip

""" Class """


class PEXELS_VIDEO_API:
    def __init__(self, PEXELS_API_KEY):
        self.PEXELS_AUTHORIZATION = {"Authorization": PEXELS_API_KEY}
        self.request = None
        self.json = None
        self.page = None
        self.total_results = None
        self.page_results = None
        self.has_next_page = None
        self.has_previous_page = None
        self.next_page = None
        self.prev_page = None

    """ Returns json for the given query """

    def search(self, query, results_per_page, page=1):
        query = query.replace(" ", "+")

        url = (
            "https://api.pexels.com/videos/search?query={}&per_page={}&page={}".format(
                query, results_per_page, page
            )
        )
        self.__request(url)
        # If there is no json data return None
        return None if not self.request else self.json

    """ Returns json of the next page if available """

    def search_next_page(self):
        if self.has_next_page:
            self.__request(self.next_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json

    """ Returns json of the previous page if available """

    def search_previous_page(self):
        if self.has_previous_page:
            self.__request(self.prev_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json

    """ Returns a list of video objects """

    def get_entries(self):
        if not self.json:
            return None
        return [Clip(json_video) for json_video in self.json["videos"]]

    """ Private methods """

    def __request(self, url):
        try:
            self.request = requests.get(
                url, timeout=60, headers=self.PEXELS_AUTHORIZATION
            )
            self.__update_page_properties()
        except requests.exceptions.RequestException:
            print("PEXELS: Request failed check your internet connection")
            self.request = None
            exit()

    def __update_page_properties(self):
        if self.request.ok:
            self.json = self.request.json()

            try:
                self.page = int(self.json["page"])
            except:
                self.page = None

            try:
                self.total_results = int(self.json["total_results"])
            except:
                self.total_results = None

            try:
                self.page_results = len(self.json["videos"])
            except:
                self.page_results = None

            try:
                self.next_page = self.json["next_page"]
                self.has_next_page = True
            except:
                self.next_page = None
                self.has_next_page = False

            try:
                self.prev_page = self.json["prev_page"]
                self.has_previous_page = True
            except:
                self.prev_page = None
                self.has_previous_page = False

        else:
            print("Wrong response you might have a wrong API key")
            print(self.request)
            print("API key: {}".format(self.PEXELS_AUTHORIZATION))
            self.request = None
            exit()
