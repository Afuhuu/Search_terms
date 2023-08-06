import requests
import json
from datetime import date, timedelta
import time
import random
import os

# control 🎛️ room
enable_animation = "YES" # Set to "YES" to enable animations, set to "NO" to disable
enable_ascii_art = "YES" # Set to "YES" to enable ASCII art, set to "NO" to disable
reduce_sleep_time = "NO" # Set to "YES" to reduce sleep, set to "NO" to continue normal speed 
print_details = "YES" # Set to "YES" to enable printing, set to "NO" to disable 
enable_shuffling = "YES" # Set to "YES" to enable shuffling search terms, set to "NO" to disable
check_existing_terms = "YES" # Set to "YES" to enable to check for existing terms, set to "NO" to disable
enable_fun_fact = "YES"  # Set to "YES" to enable fun facts, set to "NO" to disable
fetch_timeout = 60  # time to automatically finish program if it's stuck 

# Other global variables
LANG = 'en-US'
GEO = 'US' #set to your country 
numberOfWords = 60 #change as you want 

# API endpoint for fetching random fun facts
FUN_FACTS_API = "https://useless-facts.sameerkumar.website/api"
start_time = time.time()
def load_existing_search_terms(file_path):
    existing_terms = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                existing_terms.add(line.strip().lower())
    except FileNotFoundError:
        pass
    return existing_terms

def get_random_fun_fact():
    response = requests.get(FUN_FACTS_API)
    if response.status_code == 200:
        fact = response.json()["data"]
        return fact
    return None

def getGoogleTrends(existing_terms, numberOfWords):
    search_terms = set()
    i = 0
    while len(search_terms) < numberOfWords and time.time() - start_time < fetch_timeout:
        i += 1
        r = requests.get('https://trends.google.com/trends/api/dailytrends?hl=' + LANG + '&ed=' + str(
            (date.today() - timedelta(days=i)).strftime('%Y%m%d')) + '&geo=' + GEO + '&ns=15')
        google_trends = json.loads(r.text[6:])
        if 'default' in google_trends and 'trendingSearchesDays' in google_trends['default']:
            trending_searches = google_trends['default']['trendingSearchesDays']
            if trending_searches and len(trending_searches) > 0:
                for topic in trending_searches[0].get('trendingSearches', []):
                    term = topic['title']['query'].lower()
                    if check_existing_terms == "YES" and term not in existing_terms:
                        search_terms.add(term)
                    for related_topic in topic.get('relatedQueries', []):
                        related_term = related_topic['query'].lower()
                        if check_existing_terms == "YES" and related_term not in existing_terms:
                            search_terms.add(related_term)
                if print_details == "YES":
                    print_colorful(f"Retrieved {len(search_terms)} unique search terms...")
        time.sleep(1 if reduce_sleep_time == "YES" else 2)

    return list(search_terms)[:numberOfWords]

def save_search_terms_to_file(search_terms, file_path):
    with open(file_path, 'a') as file:
        for term in search_terms:
            file.write(term + '\n')

def main():
    os.system('clear')

    if enable_ascii_art == "YES":
        header = [
            "\033[1;34m     ___           ___           ___           ___     ",
            "    /  /\\         /  /\\         /  /\\         /__/\\    ",
            "   /  /:/_       /  /::\\       /  /:/_       |  |::\\   ",
            "  /  /:/ /\\     /  /:/\\:\\     /  /:/ /\\      |  |:|:\\  ",
            " /  /:/ /:/_   /  /:/~/:/    /  /:/ /::\\     |__|:|\\:\\ ",
            "/__/:/ /:/ /\\ /__/:/ /:/___ /__/:/ /:/\\:\\    /__/:/ \\:\\",
            "\\  \\:\\/:/ /:/ \\  \\:\\/:::::/ \\  \\:\\/:/__\\/    \\__\\/   \\:\\",
            " \\  \\::/ /:/   \\  \\::/~~~~   \\  \\::/             /  /\\",
            "  \\  \\:\\/:/     \\  \\:\\        \\  \\:\\            /  /:/",
            "   \\  \\::/       \\  \\:\\        \\  \\:\\          /  /:/ ",
            "    \\__\\/         \\__\\/         \\__\\/          \\__\\/  ",
            "\033[0m"
        ]

        subtitles = [
            "\033[1;35m        trendy Search Term Generator",
            "        Based on Farzshad\033[0m"
        ]

        if enable_animation == "YES":
            for _ in range(2):
                os.system('clear')
                for line in header:
                    print(line)
                    time.sleep(0.05)
                time.sleep(1)
                os.system('clear')
                for line in subtitles:
                    print(line)
                    time.sleep(0.05)
                time.sleep(1)

    existing_search_terms = load_existing_search_terms('search_terms.txt')
    if check_existing_terms == "YES":
        new_search_terms = getGoogleTrends(existing_search_terms, numberOfWords)
        all_search_terms = existing_search_terms.union(new_search_terms)
    else:
        all_search_terms = existing_search_terms

    if enable_shuffling == "YES":
        shuffled_search_terms = list(all_search_terms)
        random.shuffle(shuffled_search_terms)

        if print_details == "YES":
            print("\n\033[1;33mShuffling search terms...\033[0m")
            time.sleep(2)

        if check_existing_terms == "YES":
            save_search_terms_to_file(new_search_terms, 'search_terms.txt')
        else:
            save_search_terms_to_file(existing_search_terms, 'search_terms.txt')

    if print_details == "YES" and enable_shuffling == "YES":
        if check_existing_terms == "YES":
            new_terms_count = len(new_search_terms)
        else:
            new_terms_count = 0
        print(f"\n\033[1;35mNew terms added: {new_terms_count}\033[0m")

    if enable_fun_fact == "YES":
        fun_fact = get_random_fun_fact()
        if fun_fact:
            print_colorful("\n🎉 Fun Fact: " + fun_fact + " 🎨")
        else:
            print("\nFailed to fetch a fun fact!")

    if print_details == "YES" and enable_shuffling == "YES":
        print("\n\033[1;34m don't forget to delete txt fter every use....\033[0m")

def print_colorful(text):
    colors = [31, 32, 33, 34, 35, 36]
    color = random.choice(colors)
    print(f"\033[{color}m{text}\033[0m")

if __name__ == "__main__":
    main()
