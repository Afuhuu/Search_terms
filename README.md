# Search Term Generator

The **Search Term Generator** is a Python script that fetches trending search terms from Google Trends, shuffles them, and provides you with a list of unique search terms. It also has an option to fetch and display a random fun fact using the Useless Facts API.

## Features

- Fetches trending search terms from Google Trends.
- Shuffles the search terms.
- Displays a random fun fact using the Useless Facts API.
- Saves retrieved search terms to a text file.
- Customizable options to control animations, shuffling, sleep time, and more.
- Ability to check and avoid adding duplicate search terms.

## Getting Started

1. Clone this repository or download the `main.py` file.
2. Open the `main.py` file and customize the configuration variables in the "Control Room" section as desired.
3. Run the script using Python: `python main.py`

## Configuration Variables (Control Room)

- `enable_animation`: Set to "YES" to enable animation of the header and subtitles.
- `enable_ascii_art`: Set to "YES" to display an ASCII art header and subtitles.
- `reduce_sleep_time`: Set to "YES" to reduce sleep time during term fetching.
- `print_details`: Set to "YES" to print details while fetching terms.
- `enable_shuffling`: Set to "YES" to shuffle the search terms.
- `check_existing_terms`: Set to "YES" to check for existing terms and avoid duplicates.
- `enable_fun_fact`: Set to "YES" to display a random fun fact.
- `fetch_timeout`: Timeout for term fetching in seconds.
- `LANG`: Language for Google Trends.
- `GEO`: Geographical region for Google Trends.
- `numberOfWords`: Number of search terms to retrieve.

## Credits

- ASCII art header by [ASCII Art Studio](https://www.asciiart.eu/).
- Fun facts provided by [Useless Facts API](https://useless-facts.sameerkumar.website/api).
- algorithm and logic based on farzshad's Microsoft rewards farmer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
