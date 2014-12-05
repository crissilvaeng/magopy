class MangaHost:

    template_image_url = 'http://img.mangahost.com/br/images/{0}/{1}/{2}.png'

    def __init__(self, title, chapter=0):
        self.title = title
        self.chapter = chapter

    @staticmethod
    def list_url(self):
        return "http://br.mangahost.com/mangas"

    def manga_url(self):
        return self.list_url() + self.title

    def chapter_url(self, chapter):
        self
        return self.manga_url() + "/" + chapter

    def page_url(self, page):
        return self.template_image_url.format(self.title, self.chapter, page)

    def change_chapter(self, chapter):
        self.chapter = chapter