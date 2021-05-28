# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .helpers import *
from datetime import datetime, timezone
import maya

@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

###############################################################################

@login_required(login_url="/login/")
def news(request):

    # Number of articles to load
    article_nos = 10

    # US general news
    US_gen_articles = news_lookup("US_general")["articles"]
    US_gen_article_sources = []
    US_gen_article_titles = []
    US_gen_article_urls = []
    US_gen_article_publishedAts = []
    US_gen_article_imgs = []

    for i in range(article_nos):
        f = US_gen_articles[i]
        US_gen_article_sources.append(f["source"]["name"])
        US_gen_article_titles.append(f["title"])
        US_gen_article_urls.append(f["url"])
        US_gen_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        US_gen_article_publishedAts.append(dt_difference)

    US_gen_articles = zip(US_gen_article_sources, US_gen_article_titles, US_gen_article_urls, US_gen_article_publishedAts, US_gen_article_imgs)

    # UK general news
    UK_gen_articles = news_lookup("UK_general")["articles"]
    UK_gen_article_sources = []
    UK_gen_article_titles = []
    UK_gen_article_urls = []
    UK_gen_article_publishedAts = []
    UK_gen_article_imgs = []

    for i in range(article_nos):
        f = UK_gen_articles[i]
        UK_gen_article_sources.append(f["source"]["name"])
        UK_gen_article_titles.append(f["title"])
        UK_gen_article_urls.append(f["url"])
        UK_gen_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        UK_gen_article_publishedAts.append(dt_difference)

    UK_gen_articles = zip(UK_gen_article_sources, UK_gen_article_titles, UK_gen_article_urls, UK_gen_article_publishedAts, UK_gen_article_imgs)

    # US business news
    US_bz_articles = news_lookup("US_business")["articles"]
    US_bz_article_sources = []
    US_bz_article_titles = []
    US_bz_article_urls = []
    US_bz_article_publishedAts = []
    US_bz_article_imgs = []

    for i in range(article_nos):
        f = US_bz_articles[i]
        US_bz_article_sources.append(f["source"]["name"])
        US_bz_article_titles.append(f["title"])
        US_bz_article_urls.append(f["url"])
        US_bz_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        US_bz_article_publishedAts.append(dt_difference)

    US_bz_articles = zip(US_bz_article_sources, US_bz_article_titles, US_bz_article_urls, US_bz_article_publishedAts, US_bz_article_imgs)

    # UK business news
    UK_bz_articles = news_lookup("UK_business")["articles"]
    UK_bz_article_sources = []
    UK_bz_article_titles = []
    UK_bz_article_urls = []
    UK_bz_article_publishedAts = []
    UK_bz_article_imgs = []

    for i in range(article_nos):
        f = UK_bz_articles[i]
        UK_bz_article_sources.append(f["source"]["name"])
        UK_bz_article_titles.append(f["title"])
        UK_bz_article_urls.append(f["url"])
        UK_bz_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        UK_bz_article_publishedAts.append(dt_difference)

    UK_bz_articles = zip(UK_bz_article_sources, UK_bz_article_titles, UK_bz_article_urls, UK_bz_article_publishedAts, UK_bz_article_imgs)

    # US technology news
    US_tech_articles = news_lookup("US_technology")["articles"]
    US_tech_article_sources = []
    US_tech_article_titles = []
    US_tech_article_urls = []
    US_tech_article_publishedAts = []
    US_tech_article_imgs = []

    for i in range(article_nos):
        f = US_tech_articles[i]
        US_tech_article_sources.append(f["source"]["name"])
        US_tech_article_titles.append(f["title"])
        US_tech_article_urls.append(f["url"])
        US_tech_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        US_tech_article_publishedAts.append(dt_difference)

    US_tech_articles = zip(US_tech_article_sources, US_tech_article_titles, US_tech_article_urls, US_tech_article_publishedAts, US_tech_article_imgs)

    # UK technology news
    UK_tech_articles = news_lookup("UK_technology")["articles"]
    UK_tech_article_sources = []
    UK_tech_article_titles = []
    UK_tech_article_urls = []
    UK_tech_article_publishedAts = []
    UK_tech_article_imgs = []

    for i in range(article_nos):
        f = UK_tech_articles[i]
        UK_tech_article_sources.append(f["source"]["name"])
        UK_tech_article_titles.append(f["title"])
        UK_tech_article_urls.append(f["url"])
        UK_tech_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        UK_tech_article_publishedAts.append(dt_difference)

    UK_tech_articles = zip(UK_tech_article_sources, UK_tech_article_titles, UK_tech_article_urls, UK_tech_article_publishedAts, UK_tech_article_imgs)

    # US sports news
    US_sports_articles = news_lookup("US_sports")["articles"]
    US_sports_article_sources = []
    US_sports_article_titles = []
    US_sports_article_urls = []
    US_sports_article_publishedAts = []
    US_sports_article_imgs = []

    for i in range(article_nos):
        f = US_sports_articles[i]
        US_sports_article_sources.append(f["source"]["name"])
        US_sports_article_titles.append(f["title"])
        US_sports_article_urls.append(f["url"])
        US_sports_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        US_sports_article_publishedAts.append(dt_difference)

    US_sports_articles = zip(US_sports_article_sources, US_sports_article_titles, US_sports_article_urls, US_sports_article_publishedAts, US_sports_article_imgs)

    # UK sports news
    UK_sports_articles = news_lookup("UK_sports")["articles"]
    UK_sports_article_sources = []
    UK_sports_article_titles = []
    UK_sports_article_urls = []
    UK_sports_article_publishedAts = []
    UK_sports_article_imgs = []

    for i in range(article_nos):
        f = UK_sports_articles[i]
        UK_sports_article_sources.append(f["source"]["name"])
        UK_sports_article_titles.append(f["title"])
        UK_sports_article_urls.append(f["url"])
        UK_sports_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        UK_sports_article_publishedAts.append(dt_difference)

    UK_sports_articles = zip(UK_sports_article_sources, UK_sports_article_titles, UK_sports_article_urls, UK_sports_article_publishedAts, UK_sports_article_imgs)

    context = {
        "segment": "news",
        "US_gen_articles": US_gen_articles,
        "UK_gen_articles": UK_gen_articles,
        "US_bz_articles": US_bz_articles,
        "UK_bz_articles": UK_bz_articles,
        "US_tech_articles": US_tech_articles,
        "UK_tech_articles": UK_tech_articles,
        "US_sports_articles": US_sports_articles,
        "UK_sports_articles": UK_sports_articles,
    }

    html_template = loader.get_template( 'news.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login")
def finance(request):

    # Number of articles to load
    article_nos = 15

    # Default stocks, obtain data via IEX Cloud batch request
    default_US_tickers = ["AAPL","MSFT","AMZN","GOOGL","NFLX","BRK.B","TSLA","JPM","V","NVDA","DIS","T","CRM","SE","PINS","ROKU"]
    default_US_ETFs = ["VOO", "VTI", "VXUS", "VEA", "VWO", "QQQ", "QQQJ"]

    # Default US tickers
    try:
        default_US_instruments = iex_batch_lookup(default_US_tickers)
        default_US_companyNames = default_US_instruments["companyNames"]
        default_US_latestPrices = default_US_instruments["latestPrices"]
        default_US_changePercent = default_US_instruments["changePercents"]
        US_tickers = zip(default_US_companyNames, default_US_latestPrices, default_US_changePercent, default_US_tickers)
    except:
        US_tickers = None

    # Default US ETFs
    try:
        default_US_instruments = iex_batch_lookup(default_US_ETFs)
        default_US_ETFs_companyNames = default_US_instruments["companyNames"]
        default_US_ETFs_latestPrices = default_US_instruments["latestPrices"]
        default_US_ETFs_changePercents = default_US_instruments["changePercents"]
        US_ETFs_tickers = zip(default_US_ETFs_companyNames, default_US_ETFs_latestPrices, default_US_ETFs_changePercents, default_US_ETFs)
    except:
        US_ETFs_tickers = None

    # Financial news
    fin_articles = news_lookup("financial")["articles"]
    fin_article_sources = []
    fin_article_titles = []
    fin_article_urls = []
    fin_article_publishedAts = []
    fin_article_imgs = []

    for i in range(article_nos):
        f = fin_articles[i]
        fin_article_sources.append(f["source"]["name"])
        fin_article_titles.append(f["title"])
        fin_article_urls.append(f["url"])
        fin_article_imgs.append(f["urlToImage"])
        # Parse delta time since article's publishing time
        dt = maya.parse(f["publishedAt"]).datetime().replace(microsecond=0, second=0, minute=0)
        now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
        if str(now-dt)[0] == "0":
            dt_difference = "Less than an hour ago"
        elif str(now-dt)[0] == "1":
            dt_difference = "1 hour ago"
        else:
            dt_difference = str(now-dt)[0]+" hours ago"
        fin_article_publishedAts.append(dt_difference)

    fin_articles = zip(fin_article_sources, fin_article_titles, fin_article_urls, fin_article_publishedAts, fin_article_imgs)

    context = {
        "segment": "finance",
        "US_tickers": US_tickers,
        "US_ETFs_tickers": US_ETFs_tickers,
        "fin_articles": fin_articles,
    }

    html_template = loader.get_template( 'finance.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login")
def quote(request):
    """User symbol quote request"""

    # GET request, user's symbol input
    if request.method == "GET":

        # Obtain user's symbol input
        try:
            symbol = request.GET["symbol"]

        # Stock search page (initial access)
        except:
            context = {
                "segment": "quote"
            }
            html_template = loader.get_template( 'quote-blank.html' )
            return HttpResponse(html_template.render(context, request))

        # If no symbol entered
        if not symbol:
            context = {}

            html_template = loader.get_template( 'page-404.html' )
            return HttpResponse(html_template.render(context, request))

        # Scrap company stats
        mw_scrapped = mw_lookup(symbol)
        valuation = mw_scrapped["valuation"]
        efficiency = mw_scrapped["efficiency"]
        liquidity = mw_scrapped["liquidity"]
        profitability = mw_scrapped["profitability"]
        capitalization = mw_scrapped["capitalization"]

        if mw_scrapped == None:
            context = {}

            html_template = loader.get_template( 'quote-blank.html' )
            return HttpResponse(html_template.render(context, request))

        # Symbol specific news, initially load 20 articles
        articles = iex_news_lookup(symbol, 20)
        article_sources = []
        article_titles = []
        article_urls = []
        article_publishedAts = []
        article_imgs = []

        if articles == None:
            context = {
                "segment": "quote",
                "error": "We didn't find any symbols matching",
                "symbol": symbol,
            }

            html_template = loader.get_template( 'quote-blank.html' )
            return HttpResponse(html_template.render(context, request))

        for i in range(len(articles)):
            # Only load 12 english articles
            if len(article_sources) == 12:
                break
            f = articles[i]
            # Only save english language articles
            if f["lang"] == "en":
                article_sources.append(f["source"])
                article_titles.append(f["headline"])
                article_urls.append(f["url"])
                article_imgs.append(f["image"])

                # Convert datetime from millisecond epoch to datetime format
                s = f["datetime"] / 1000
                dt = datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

                #Parse delta time since article's publishing time
                dt = maya.parse(dt).datetime().replace(microsecond=0, second=0, minute=0)
                now = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
                difference = datetime.now(timezone.utc)-maya.parse(dt).datetime()
                if str(now-dt)[0] == "0":
                    dt_difference = "Less than an hour ago"
                elif "1 day" in str(now-dt):
                    dt_difference = "over a day ago"
                elif "2 day" in str(now-dt):
                    dt_difference = "over 2 days ago"
                else:
                    dt_difference = str(difference.seconds//3600) +" hours ago"
                article_publishedAts.append(dt_difference)

        symbol_articles = zip(article_sources, article_titles, article_urls, article_publishedAts, article_imgs)

        # Symbol company info
        info = iex_info_lookup(symbol)
        description = info["description"]
        CEO = info["CEO"]
        address = info["address"]
        city = info["city"]
        state = info["state"]
        country = info["country"]
        website = info["website"]
        employees = info["employees"]

        # Check if user has added symbol to watchlist
        # if request.user.is_anonymous == False:
        #     user=request.user
        #     already_exist = Watchlist.objects.filter(user=user, symbol=symbol).exists()
        # else:
        #     already_exist = None

        # IEX Cloud API call
        instrument = iex_lookup(symbol)
        # If no data returned
        if not instrument:
            context = {}
            html_template = load.get_template( 'page-403.html' )
            return HttpResponse(html_template.render(context, request))

        else:
            symbol = instrument["symbol"]
            companyName = instrument["companyName"]
            latestPrice = instrument["latestPrice"]
            changePercent = instrument["changePercent"]
            change = instrument["change"]

            context = {
                "segment": "quote",
                "symbol": symbol,
                "companyName": companyName,
                "latestPrice": latestPrice,
                "changePercent": changePercent,
                "change": change,
                "valuation": valuation,
                "efficiency": efficiency,
                "liquidity": liquidity,
                "profitability": profitability,
                "capitalization": capitalization,
                "symbol_articles": symbol_articles,
                "description": description,
                "CEO": CEO,
                "address": address,
                "city": city,
                "state": state,
                "country": country,
                "website": website,
                "employees": employees,
                # "already_exist": already_exist,
            }

            html_template = loader.get_template( 'quote.html' )
            return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def test(request):
    context = {
        "test": "Dinner lol",
    }

    html_template = loader.get_template( 'test.html' )
    return HttpResponse(html_template.render(context, request))
