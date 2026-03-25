#Use NewsAPI, Requests and argprase (CLI) modules to build a news app
import requests, pycountry
from datetime import datetime

class GetNews:
    def __init__(self):
        self.api_key="f90793657ec24f4aa889fbd7a4f50416"
        self.params={
            "apiKey":self.api_key,
            "pagesize":10
        }

    def fetch_news(self,url,country=None,category=None,query=None,from_date=None,to_date=None):
        if country:
            self.params["country"]=country
        if category:
            self.params["category"]=category
        if query:
            self.params["q"]=query
        if from_date:
            self.params["from"]=from_date
        if to_date:
            self.params["to"]=to_date
        try:
            response=requests.get(url,self.params)
            response.raise_for_status()
            if url=="https://newsapi.org/v2/top-headlines":
                articles=response.json().get("articles",[])
                if not articles:
                    print("\nNo Article Found")
                    return
                for headlines in articles:
                    print(f"\n{headlines.get('title')}")
                exit()
            else:
                articles=response.json().get("articles",[])
                if not articles:
                    print("\nNo Article Found")
                    return
                for article in articles:
                    print("\n\n                                      Article ")
                    print("\n\nTitle:", article.get('title'))
                    print("\nAuthor:", article.get('author'))
                    print("\nDescription:", article.get('description'))
                    print("\nURL:", article.get('url'))
                    print("\nPublished At:", article.get('publishedAt'))

                exit()
        except requests.exceptions.HTTPError as httperr:
            print(f"\nHTTP error occured : {httperr}")
        except requests.exceptions.RequestException as reqerr:
            print(f"\nRequest error occured : {reqerr}")
        except Exception as err:
            print(f"\n error occured : {err}")

    def choose_category(self):
        valid_categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
        while True:
            txt3='''\nChoose Category :)  
- Business: News related to business and finance.
- Entertainment: News related to movies, TV, music, and other entertainment topics.
- General: General news that doesn't fit into other specific categories.
- Health: News related to health and medical topics.
- Science: News related to scientific discoveries and advancements.
- Sports: News related to sports events and athletes.
- Technology: News related to technology and gadgets.'''
            print(txt3)          
            category=input("\nEnter Category : ").strip().lower()
            if category in valid_categories:
                return category
            else:
               print("\nIncorrect Category :( ")

    def country_iso(self):
        while True:
            try:
                country=input("\nEnter Country (Official name) : ").strip().lower()
                temp=pycountry.countries.lookup(country)
                country =temp.alpha_2 
                return country 
            except LookupError:
                print("\nCountry Not Found :(")

    def keyword(self):
        query=input("\nEnter keyword : ").lower().strip()
        return query
    
    def from_date(self):
        while True:
            from_date=input("\nFrom Date - Enter date in this format - YYYY-MM-DD :  ").strip()
            try:
                datetime.strptime(from_date,"%Y-%m-%d")
                return from_date
            except ValueError:
                print("\nIncorrect Date Format ")

    def to_date(self):
        while True:
            to_date=input("\nTo Date - Enter date in this format - YYYY-MM-DD :  ").strip()
            try:
                datetime.strptime(to_date,"%Y-%m-%d")
                return to_date
            except ValueError:
                print("\nIncorrect Date Format ")

    def top_headlines(self):
        url="https://newsapi.org/v2/top-headlines"
        while True:
            txt2='''
1. Fetch News By Category 
2. Fetch News By Country
3. Fetch News By Keyword
4. Fetch News By Category and Country
5. Fetch News By Country and Keyword 
6. Fetch News By Category and Keyword
7. Fetch News By Category, Country and Keyword'''
            print(txt2)
            inp2=input("\nEnter you option (1-6) : ")
            if inp2=="1":
                category=self.choose_category()
                self.fetch_news(url=url,category=category)

            elif inp2=="2":
                country=self.country_iso()
                self.fetch_news(url=url,country=country)

            elif inp2=="3":
                query=self.keyword()
                self.fetch_news(url=url,query=query)
    
            elif inp2=="4":
                category=self.choose_category()
                country=self.country_iso()
                self.fetch_news(url=url,country=country,category=category)

            elif inp2=="5":
                country=self.country_iso()
                query=self.keyword()
                self.fetch_news(url=url,country=country,query=query)

            elif inp2=="6":
                query=self.keyword()
                category=self.choose_category()
                self.fetch_news(url=url,query=query,category=category)

            elif inp2=="7":
                country=self.country_iso()
                category=self.choose_category()
                query=self.keyword()
                self.fetch_news(url=url,query=query,category=category,country=country)
            
            else:
                print("\nIncorrect Input :(")

    def article_summary(self):
        url="https://newsapi.org/v2/everything"
        while True:
            txt4='''
1. Fetch News with Keyword
2. Fetch News within Date Range
3. Fetch News using Keyword and Date Range'''
            print(txt4)
            inp3=input("\nChoose Option : ").strip()
            if inp3=="1":
                query=self.keyword()
                self.fetch_news(url=url,query=query)
                
            elif inp3=="2":
                from_date=self.from_date()
                to_date=self.to_date()
                self.fetch_news(url=url,from_date=from_date,to_date=to_date,query="news")
    
            elif inp3=="3":
                from_date=self.from_date()
                to_date=self.to_date()
                query=self.keyword()
                self.fetch_news(url=url,query=query,from_date=from_date,to_date=to_date)
            
            else:
                print("\nIncorrect Input :(")            

    def print_help(self):
        help_text = """
        News App Help Documentation
        ===========================
    
        Overview
        --------
        This news app allows users to fetch the latest news headlines and articles based on various criteria such as category, country, keyword, and date range. The app uses the NewsAPI to retrieve news data and provides a command-line interface (CLI) for user interaction.
    
        Main Menu
        ---------
        1. Top Headlines: Fetches top news headlines.
        2. Article Summary: Fetches detailed articles.
        3. Exit: Exits the application.
    
        Top Headlines Menu
        ------------------
        1. Fetch News By Category: Fetches top headlines by category.
        2. Fetch News By Country: Fetches top headlines by country.
        3. Fetch News By Keyword: Fetches top headlines by keyword.
        4. Fetch News By Category and Country: Fetches top headlines by both category and country.
        5. Fetch News By Country and Keyword: Fetches top headlines by both country and keyword.
        6. Fetch News By Category and Keyword: Fetches top headlines by both category and keyword.
        7. Fetch News By Category, Country, and Keyword: Fetches top headlines by category, country, and keyword.
    
        Article Summary Menu
        --------------------
        1. Fetch News with Keyword: Fetches articles by keyword.
        2. Fetch News within Date Range: Fetches articles within a specified date range.
        3. Fetch News using Keyword and Date Range: Fetches articles by keyword within a specified date range.
    
        Example Usage
        -------------
        Fetching Top Headlines by Category:
        1. Choose the "Top Headlines" option.
        2. Select "Fetch News By Category".
        3. Enter the desired category (e.g., business, entertainment).
    
        Fetching Articles by Keyword and Date Range:
        1. Choose the "Article Summary" option.
        2. Select "Fetch News using Keyword and Date Range".
        3. Enter the desired keyword.
        4. Enter the start date in YYYY-MM-DD format.
        5. Enter the end date in YYYY-MM-DD format.
    
        Error Handling
        --------------
        The app handles various errors such as HTTP errors, request errors, and invalid inputs. Appropriate error messages are displayed to guide the user.
        """
        print(help_text)

    def main(self):
        while True:
            txt1='''
1. Top Headlines 
2. Article Summary
3. Help
4. Exit
            '''
            print(txt1)
            inp1=input("Enter 1, 2 or 3 : ").strip()
            if inp1=="1":
                self.top_headlines()
            elif inp1=="2":
                self.article_summary()
            elif inp1=="3":
                self.print_help()
            elif inp1=="4":
                break
            else:
                print("\nIncorrect Input :( ")    

obj1=GetNews()
obj1.main()