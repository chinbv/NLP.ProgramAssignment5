import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki=wiki_wiki.page("Test 1")
print(p_wiki.text)

wiki_html=wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
)

p_html=wiki_html.page("perl")
print(p_html.text)
