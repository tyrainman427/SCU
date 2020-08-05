from django.shortcuts import render
from newsapi import NewsApiClient
from decouple import config


def Index(request):
    newsapi = NewsApiClient(api_key=config('NEWS_API_KEY'))
    all_articles = newsapi.get_everything(q='blm',
                                      language='en',
                                      sort_by='relevancy',
                                      )


    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    publish_date = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        publish_date.append(myarticles["publishedAt"])
        link.append(myarticles['url'])


    mylist = zip(news, desc, img, publish_date,link)


    return render(request, 'news/news_list.html', context={"mylist":mylist})
