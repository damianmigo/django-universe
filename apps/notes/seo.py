from djangoseo import seo


class BasicMetadata(seo.Metadata):
    title = seo.Tag(max_length=68, head=True)
    keywords = seo.KeywordTag()
    description = seo.MetaTag(max_length=155)

    class Meta:
        seo_views = ('notes',)
