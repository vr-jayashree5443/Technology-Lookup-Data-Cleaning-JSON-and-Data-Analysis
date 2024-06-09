# Technology-Lookup-Data-Cleaning-JSON-and-Data-Analysis

This project involves cleaning and processing data from a JSON file containing technology lookup information. The primary goal is to prepare the data for analysis and create a lookup system to identify technologies based on input URLs.

## Overview

- **Original File**: [Project-4 Technology Lookup Data Cleaning(JSON).ipynb](https://colab.research.google.com/drive/18b5gUuvYL08ZBnaUjnZfg9f_dK8kOm0O)
- **Dataset**: [technologies.json](https://raw.githubusercontent.com/sahilrahmann/Technology-Lookup-Web-Application/main/technologies.json)
- **Secondary JSON**: [technologies.json](https://raw.githubusercontent.com/chorsley/python-Wappalyzer/master/Wappalyzer/data/technologies.json)

## Part 1: Cleaning

1. **Transpose Data**: Convert rows to columns and vice versa for easier manipulation.
2. **Categories Column**: Replace category codes with actual category names using a secondary JSON file.
3. **Description Column**: Handle null values.
4. **Headers Column**: Extract and process unique keys.

## Part 2: Lookup System

1. **Extract Domain Name**: Use regular expressions to extract the domain name from the input URL.
2. **Scraping**: Utilize BeautifulSoup and Requests libraries to scrape content from the input URL.
3. **Identify Technologies**:
    - Search for technology-related information in request headers, cookies, and HTML content.
    - Match technology attributes to those in the dataset to identify relevant technologies.

## Usage

The function `Technology()` accepts a URL input and returns a list of technologies detected on the corresponding webpage.

Example Usage:
```python
technologies = Technology()
print(technologies)
```

### Note
Ensure that all necessary libraries are installed (`pandas`, `requests`, `BeautifulSoup`).

**Integrated with Flask**
Input page:
![image](https://github.com/vr-jayashree5443/Technology-Lookup-Data-Cleaning-JSON-and-Data-Analysis/assets/128161257/a2b985dd-61b4-4810-b026-109ec8dd69f1)


Output page:
![image](https://github.com/vr-jayashree5443/Technology-Lookup-Data-Cleaning-JSON-and-Data-Analysis/assets/128161257/b5588235-1bfd-4641-ab58-e86ad0a54227)

