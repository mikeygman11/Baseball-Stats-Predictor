#Copyright 2021 Michael Galanaugh
#Organizing historical MLB data



from typing import KeysView
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

team_map = {
    'ARI': 'Arizona Diamondbacks',
    'ATL': 'Atlanta Braves',
    'BAL': 'Baltimore Orioles',
    'BOS': 'Boston Red Sox',
    'CHC': 'Chicago Cubs',
    'CHW': 'Chicago White Sox',
    'CIN': 'Cincinnati Reds',
    'CLE': 'Cleveland Indians',
    'COL': 'Colorado Rockies',
    'DET': 'Detroit Tigers',
    'HOU': 'Houston Astros',
    'KCR': 'Kansas City Royals',
    'ANA': 'Los Angeles Angels',
    'LAD': 'Los Angeles Dodgers',
    'FLA': 'Miami Marlins',
    'MIL': 'Milwaukee Brewers',
    'MIN': 'Minnesota Twins',
    'NYM': 'New York Mets',
    'NYY': 'New York Yankees',
    'OAK': 'Oakland Athletics',
    'PHI': 'Philadelphia Phillies',
    'PIT': 'Pittsburgh Pirates',
    'SDP': 'San Diego Padres',
    'SFG': 'San Francisco Giants',
    'SEA': 'Seattle Mariners',
    'STL': 'St. Louis Cardinals',
    'TBD': 'Tampa Bay Rays',
    'TEX': 'Texas Rangers',
    'TOR': 'Toronto Blue Jays',
    'WSN': 'Washington Nationals'
}


def main():
    print("Hi")
    scrape_mlb_batting()
    scrape_mlb_pitching()

def scrape_nym():
    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.set_window_size(900,900)
    browser.set_window_position(0, 0)
    sleep(1)
    browser.get("https://www.baseball-reference.com/teams/NYM/batteam.shtml")
    page = browser.page_source
    bs = BeautifulSoup(page, "lxml")
    filter = bs.find_all(id = "div_yby_team_bat")
    #print(filter)
    batting_stats_list = []
    header = bs.find("thead").find_all("th")
    for item in header:
        batting_stats_list.append(item.text)
    rows = bs.find("tbody").find_all("tr")
    years = bs.find("tbody").find_all("tr")
    for row in rows:
        yearly_stats = []
        #print(row.text + '\n')
        #print(row)
        yr = row.find("th")
        yearly_stats.append(yr.text)
        tds = row.find_all("td")
        for td in tds:
            yearly_stats.append(td.text)
        print(yearly_stats)
    print(batting_stats_list)

def scrape_mlb_batting():
    team = input()
    upperTeam = team.upper()
    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.set_window_size(900,900)
    browser.set_window_position(0, 0)
    sleep(1)
    browser.get("https://www.baseball-reference.com/teams/" + upperTeam + "/batteam.shtml")
    page = browser.page_source
    bs = BeautifulSoup(page, "lxml")
    filter = bs.find_all(id = "div_yby_team_bat")
    #print(filter)
    batting_stats_list = []
    header = bs.find("thead").find_all("th")
    for item in header:
        batting_stats_list.append(item.text)
    rows = bs.find("tbody").find_all("tr")
    years = bs.find("tbody").find_all("tr")
    for row in rows:
        yearly_stats = []
        #print(row.text + '\n')
        #print(row)
        yr = row.find("th")
        yearly_stats.append(yr.text)
        tds = row.find_all("td")
        for td in tds:
            yearly_stats.append(td.text)
        print(yearly_stats)
    print(batting_stats_list)

def scrape_mlb_pitching():
    team = input()
    upperTeam = team.upper()
    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.set_window_size(900,900)
    browser.set_window_position(0, 0)
    sleep(1)
    browser.get("https://www.baseball-reference.com/teams/" + upperTeam + "/pitchteam.shtml")
    page = browser.page_source
    bs = BeautifulSoup(page, "lxml")
    filter = bs.find_all(id = "div_yby_team_pitch")
    #print(filter)
    pitching_stats_list = []
    header = bs.find("thead").find_all("th")
    for item in header:
        pitching_stats_list.append(item.text)
    rows = bs.find("tbody").find_all("tr")
    years = bs.find("tbody").find_all("tr")
    for row in rows:
        yearly_stats = []
        #print(row.text + '\n')
        #print(row)
        yr = row.find("th")
        yearly_stats.append(yr.text)
        tds = row.find_all("td")
        for td in tds:
            yearly_stats.append(td.text)
        print(yearly_stats)
    print(pitching_stats_list)

main()