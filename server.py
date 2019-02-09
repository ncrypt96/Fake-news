# Edit the procedure in the server script
from fake_news.nlp.cosine_bow import cosine_similartity_bow
from fake_news.crawler.query_data import Data
from fake_news.preprocessor.error_handle import line_loc

print("enter URL")
url = input()

data = Data(url)

# query from 6 to 3
for keys in range(6,2,-1):

    p = data.get_all_data(no_of_keywords=keys)

    # if the crawler returns something more than ueser data break
    if(len(p['titles'])>1):
        break





line_loc()
print(p["titles"])
line_loc()
print(cosine_similartity_bow(p["contents"]))