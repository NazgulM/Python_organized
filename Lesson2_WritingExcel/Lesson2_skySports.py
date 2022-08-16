from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


def get_static_league(url):
    result = requests.get(url)
    soup = bs(result.text, 'html.parser')
    # print(soup)
    table_list = []
    league_table = soup.find('table', class_='standing-table__table')
    # print(league_table.text)

    for data in league_table.find_all('tbody'):
        rows = data.find_all('tr', class_="standing-table__row")
        for row in rows:
            team_name = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            # print(team_name.text.strip())
            pl_points = row.find_all('td', class_='standing-table__cell is-hidden--bp35')
            # print(pl_points)
            pl_points = row.find_all('td', class_='standing-table__cell')
            # print(len(pl_points))
            pl_points = row.find_all('td', class_='standing-table__cell')[9].text
            # print(pl_points)

            teamPremLegData = {
                'name_team': team_name,
                'points': pl_points
            }
            table_list.append(teamPremLegData)

        return table_list


def main():
    url = 'https://www.skysports.com/premier-league-table'
    data = get_static_league(url)
    df = pd.DataFrame(data)
    print(df)

    df.to_excel('EnglandTeamPts2.xlsx')


if __name__ == '__main__':
    main()
