class Track:
    def __init__(self, title, artist):
        if title == "" or artist == "":
            raise Exception("Need to include both a title and artist")
        if type(title) != str or type(artist) != str:
            raise Exception("Title and artist must be a string")
        self.title = title
        self.artist = artist
        

    def matches(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.artist.lower()
        # keyword is a string
        # Returns true if the keyword matches either the title or artist