import requests
import json
from requests.utils import requote_uri
from bs4 import BeautifulSoup


class TafeScrape:

    def __init__(self, info:str) -> None:
        self.info = str(info)
        self.url_timetable = "https://timetables.tafeqld.edu.au/Group/GroupTable?"
        self.url_get_week = "https://timetables.tafeqld.edu.au/Group/WeekTable?"
        self.url_search = "https://timetables.tafeqld.edu.au/Group/SearchGroup?"

    def url_timetable_(self) -> str:
        """
        Retruns a complete url for Tafe timetable page

        Returns:
            https://timetables.tafeqld.edu.au/Group/GroupTable?id=22334VIC_S1%2C%2015-03-21%20Cyber%20Security%20CDG%20Mar%202021%20SB&week=202132
        """
        self.info = self.convert_name()
        return str(self.url_timetable +
                   "id=" + requote_uri(self.info) +
                   "&week=" + self.get_week_output())

    def url_week_(self) -> str:
        """
        Returns a complete url for a get request on Tafe's back end

        Returns:
            https://timetables.tafeqld.edu.au/Group/WeekTable?group=22334VIC_S1%2C%2015-03-21%20Cyber%20Security%20CDG%20Mar%202021%20SB&weekNo=0&func=SelectGroup
        """
        return str(self.url_get_week +
                        "group=" + requote_uri(self.info) +
                        "&weekNo=0&func=SelectGroup")

    def url_search_(self, region:str="TQBN") -> str:
        """
        Returns a complete url for a get request on Tafe's back end

        Args:
            region:
                TQBN = TAFE Queensland Brisbane
                TQEC = TAFE Queensland East Coast
                TQGC = TAFE Queensland Gold Coast
                TQNT = TAFE Queensland North
                TQSW = TAFE Queensland South West

        Returns:
            https://timetables.tafeqld.edu.au/Group/SearchGroup?searchStr=cyber&database=TQBN
        """
        return str(self.url_search +
                        "searchStr=" + requote_uri(self.info) +
                        "&database=" + region)

    def get_timetable_output(self) -> str:
        """
        Parses the html data and outputs text of page

        Fetches:
            <div class="pageheader" id="GroupName">Group: 22334VIC Cert IV Cyber Security - QLD Government Customer &amp; Digital Group Mar 2021 South Bank</div>
            <div class="pageheader">Week: 02/08/2021 - 08/08/2021 (Week 32, 2021)</div>

            <table class="table">
                <tr class="group-header">
                    <td colspan="6" class="RoomName">
                        <span class="h4">Monday, August 2, 2021</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p><b>6:00PM - 9:00PM online delivery</b></p>
                        <b>Room</b>
                        <br />
                        SB,Lvl 1.Rm 007 - Zoom/MS Teams (Southbank) <br />
                        <b>Unit(s)</b>
                        <br />
                        ICTPRG405, BSBWHS401, VU21995, VU21992, VU21991, VU21996, VU21997
                    </td>
                </tr>
                <tr class="group-header">
                    <td colspan="6" class="RoomName">
                        <span class="h4">Tuesday, August 3, 2021</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p><b>6:00PM - 9:00PM online delivery</b></p>
                        <b>Room</b>
                        <br />
                        SB,Lvl 1.Rm 007 - Zoom/MS Teams (Southbank) <br />
                        <b>Unit(s)</b>
                        <br />
                        ICTPRG405, BSBWHS401, VU21995, VU21992, VU21991, VU21996, VU21997
                    </td>
                </tr>
                <tr class="group-header">
                    <td colspan="6" class="RoomName">
                        <span class="h4">Wednesday, August 4, 2021</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p><b>9:00AM - 12:00PM </b></p>
                        <b>Room</b>
                        <br />
                        <a href="http://maps.google.com/maps?q=-27.479393,153.019917" target="_blank">SB,G Block.Lvl 2,Rm 005 - Computer Lab(30C) PCSM (Southbank)</a> <br />
                        <b>Unit(s)</b>
                        <br />
                        ICTPRG405, BSBWHS401, VU21995, VU21992, VU21991, VU21996, VU21997
                    </td>
                </tr>
                <tr>
                    <td>
                        <p><b>1:00PM - 4:00PM </b></p>
                        <b>Room</b>
                        <br />
                        <a href="http://maps.google.com/maps?q=-27.479393,153.019917" target="_blank">SB,G Block.Lvl 2,Rm 005 - Computer Lab(30C) PCSM (Southbank)</a> <br />
                        <b>Unit(s)</b>
                        <br />
                        ICTPRG405, BSBWHS401, VU21995, VU21992, VU21991, VU21996, VU21997
                    </td>
                </tr>
                <tr class="group-header">
                    <td colspan="6" class="RoomName">
                        <span class="h4">Thursday, August 5, 2021</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p><b>9:00AM - 1:00PM Independent Learning</b></p>
                        <b>Unit(s)</b>
                        <br />
                        ICTPRG405, BSBWHS401, VU21995, VU21992, VU21991, VU21996, VU21997
                    </td>
                </tr>
            </table>
            <i>This timetable last changed: 02/08/2021</i>
        
        Return:
            Group: 22334VIC Cert IV Cyber Security 2B Jan 2021 South Bank
            Week: 09/08/2021 - 15/08/2021 (Week 33, 2021)
            Monday, August 9, 2021
            8:00AM - 11:00AM
            Room
            SB,G Block.Lvl 2,Rm 009 - Computer Lab(29C) PCSM (Southbank)
            Unit(s)
            VU21991, VU21995
            Tuesday, August 10, 2021
            9:00AM - 1:00PM Independent Learning
            Unit(s)
            ICTPRG405, BSBWHS401, VU21991, VU21992, VU21997, VU21996, VU21995
            Thursday, August 12, 2021
            8:00AM - 11:00AM
            Room
            SB,G Block.Lvl 2,Rm 005 - Computer Lab(30C) PCSM (Southbank)
            Unit(s)
            VU21992
            11:30AM - 2:30PM
            Room
            SB,G Block.Lvl 2,Rm 005 - Computer Lab(30C) PCSM (Southbank)
            Unit(s)
            BSBWHS401, VU21996
            This timetable last changed: 09/08/2021

        """
        data = requests.get(self.url_timetable_(), timeout=5)
        soup = BeautifulSoup(data.text, 'html.parser')
        output = ""
        week_days = ["Monday", "Tuesday", "Wensdays", "Thursday", "Friday"]
        for string in soup.stripped_strings:
            if string.startswith(tuple(week_days)):
              string = "\n" + string
            output += string + "\n"
        return str(output)

    def get_week_output(self) -> str:
        """
        Returns the json data for the current week

        Fetches:
            {
              "success": true,
              "responseText": [
                {
                  "WeekNo": 202132,
                  "WeekText": "02/08/2021 - 08/08/2021 (Week 32, 2021)"
                },
                {
                  "WeekNo": 202133,
                  "WeekText": "09/08/2021 - 15/08/2021 (Week 33, 2021)"
                },
                {
                  "WeekNo": 202134,
                  "WeekText": "16/08/2021 - 22/08/2021 (Week 34, 2021)"
                },
                {
                  "WeekNo": 202135,
                  "WeekText": "23/08/2021 - 29/08/2021 (Week 35, 2021)"
                },
                {
                  "WeekNo": 202136,
                  "WeekText": "30/08/2021 - 05/09/2021 (Week 36, 2021)"
                },
                {
                  "WeekNo": 202137,
                  "WeekText": "06/09/2021 - 12/09/2021 (Week 37, 2021)"
                },
                {
                  "WeekNo": 202138,
                  "WeekText": "13/09/2021 - 19/09/2021 (Week 38, 2021)"
                },
                {
                  "WeekNo": 202139,
                  "WeekText": "20/09/2021 - 26/09/2021 (Week 39, 2021)"
                },
                {
                  "WeekNo": 202140,
                  "WeekText": "27/09/2021 - 03/10/2021 (Week 40, 2021)"
                },
                {
                  "WeekNo": 202141,
                  "WeekText": "04/10/2021 - 10/10/2021 (Week 41, 2021)"
                },
                {
                  "WeekNo": 202142,
                  "WeekText": "11/10/2021 - 17/10/2021 (Week 42, 2021)"
                },
                {
                  "WeekNo": 202143,
                  "WeekText": "18/10/2021 - 24/10/2021 (Week 43, 2021)"
                },
                {
                  "WeekNo": 202144,
                  "WeekText": "25/10/2021 - 31/10/2021 (Week 44, 2021)"
                },
                {
                  "WeekNo": 202145,
                  "WeekText": "01/11/2021 - 07/11/2021 (Week 45, 2021)"
                },
                {
                  "WeekNo": 202146,
                  "WeekText": "08/11/2021 - 14/11/2021 (Week 46, 2021)"
                },
                {
                  "WeekNo": 202147,
                  "WeekText": "15/11/2021 - 21/11/2021 (Week 47, 2021)"
                },
                {
                  "WeekNo": 202148,
                  "WeekText": "22/11/2021 - 28/11/2021 (Week 48, 2021)"
                },
                {
                  "WeekNo": 202149,
                  "WeekText": "29/11/2021 - 05/12/2021 (Week 49, 2021)"
                },
                {
                  "WeekNo": 202150,
                  "WeekText": "06/12/2021 - 12/12/2021 (Week 50, 2021)"
                },
                {
                  "WeekNo": 202151,
                  "WeekText": "13/12/2021 - 19/12/2021 (Week 51, 2021)"
                }
              ],
              "weekNo": 202132
            }
		
		Returns:
			"weekNo": 202132
        """
        data = requests.get(self.url_week_(), timeout=5)
        find_week = json.loads(data.text)
        return str(find_week["weekNo"])

    def get_search_output(self) -> str:
        """Parses the json data and outputs text of search results

        Returns:
            [
              {
                "ID": "22334VIC_S1, 15-03-21 Cyber Security CDG Mar 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security - QLD Government Customer & Digital Group Mar 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1A Jul 2021 MG",
                "Name": "22334VIC Cert IV Cyber Security 1A Jul 2021 Mount Gravatt"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1A Jul 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security 1A Jul 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1B Jul 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security 1B Jul 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1C Jul 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security 1C Jul 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1D Jul 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security 1D Jul 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 1N Jul 2021 SB",
                "Name": "22334VIC Cert IV Cyber Security 1N Jul 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 2A Jan 21 MG",
                "Name": "22334VIC Cert IV Cyber Security 2A Jan 21 Mount Gravatt"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 2A Jan 21 SB",
                "Name": "22334VIC Cert IV Cyber Security 2A Jan 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 2B Jan 21 SB",
                "Name": "22334VIC Cert IV Cyber Security 2B Jan 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security 2E Jan 21 SB",
                "Name": "22334VIC Cert IV Cyber Security 2E Jan 2021 South Bank"
              },
              {
                "ID": "22334VIC_S2, 12-07-21 Cyber Security Jul 2021 BR",
                "Name": "22334VIC Cert IV Cyber Security Jul 2021 Bracken Ridge"
              }
            ]
        """
        data = requests.get(self.url_search_(), timeout=5)
        json_data = json.loads(data.text)
        output = ""
        for i in range(len(json_data)):
            output += json_data[i]["Name"] + "\n"
        return str(output)

    def convert_name(self) -> str:
        """Converts the a name to a json ID for url construction"""
        data = requests.get(self.url_search_(), timeout=5)
        json_data = json.loads(data.text)
        for i in range(len(json_data)):
            if self.info == json_data[i]["Name"]:
                return str(json_data[i]["ID"])
            else:
                return str(json_data[i]["ID"])
