import json
import random
import base64
import requests
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;35m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
dark_violet = "\033[38;5;91m"

class FacebookClient:
    def __init__(self, cookies, fb_dtsg, jazoest, id_page) -> None:
        self.headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }

        # Load profile page
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        _ = requests.get(url_profile, headers=self.headers).text

        #
        self.fb_dtsg = fb_dtsg
        self.jazoest = jazoest
        self.user_id = id_page
       

    @staticmethod
    def get_fb_dtsg_and_jazoest(cookie: str):
        """Fetch fb_dtsg and jazoest tokens using mbasic.facebook.com"""
        url = "https://mbasic.facebook.com/"
        headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers).text

        try:
            fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
            uid = cookie.split("c_user=")[1].split(";")[0]
            return fb_dtsg, jazoest, uid
        except IndexError:
            raise Exception("Could not extract fb_dtsg or jazoest. Check if cookie is valid.")


import json
import requests
import requests
import json

import requests
import json

def bio_update(cookies: str, fb_dtsg: str, user_id: str, new_bio: str):
    session = requests.Session()
    session.headers.update({
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.facebook.com",
        "referer": f"https://www.facebook.com/profile.php?id={user_id}",
        "x-fb-friendly-name": "ProfileCometSetBioMutation",
        "x-fb-lsd": "WK_MbVszi0WH2acEQtgRIS"   # often dynamic
    })
    #lsd

    # Load cookies into session
    for part in cookies.split(";"):
        if "=" in part:
            key, value = part.strip().split("=", 1)
            session.cookies.set(key, value)

    # GraphQL variables
    variables = {
        "input": {
            "attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start",
            "bio": new_bio,
            "publish_bio_feed_story": False,
            "actor_id": user_id,
            "client_mutation_id": "3"
        },
        "hasProfileTileViewID": True,
        "profileTileViewID": "cHJvZmlsZV90aWxlX3ZpZXc6MTAwMDkzNTY1MzcyMjgzOmludHJvOmludHJvX2JpbzppbnRyb19jYXJkX2Jpbzpwcm9maWxlX3RpbWVsaW5lOjE=",
        "scale": 1,
        "useDefaultActor": False
    }

    # Request body
    body = {
        "av": user_id,
        "__user": user_id,
        "__a": 1,
        "__req": "1m",
        "__hs": "19528.HYP:comet_pkg.2.1..2.1",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1007710268,
        "__s": "5vqroc:vabf9f:71x9mm",
        "__hsi": "7246895806497725079",
        "__comet_req": 15,
        "fb_dtsg": fb_dtsg,
        "jazoest": "25349",   # must be extracted dynamically
        "lsd": "Vp6T13bEXXl8SlALWzINx_",  # must be extracted dynamically
        "__spin_r": 1007710268,
        "__spin_b": "trunk",
        "__spin_t": 1687299415,
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "ProfileCometSetBioMutation",
        "variables": json.dumps(variables),
        "server_timestamps": True,
        "doc_id": "6123158884463798"
    }

    url = "https://www.facebook.com/api/graphql/"
    response = session.post(url, data=body)

    try:
        return response.json()
    except Exception:
        return response.text
import requests
import json

import requests
import json

import json
import requests
import time






def setting_hometown(aku, col_token, my_town, sec_token,dtsg,cookies):
        variables = {
            "collectionToken": col_token,
            "input": {
                "hometown_city_id": my_town,
                "privacy": {
                    "allow": [],
                    "base_state": "EVERYONE",
                    "deny": [],
                    "tag_expansion_state": "UNSPECIFIED"
                },
                "actor_id": aku,
                "client_mutation_id": "1"
            },
            "scale": 1,
            "sectionToken": sec_token,
            "useDefaultActor": False
        }
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
            "sec-ch-ua-full-version-list": "\"Not.A/Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"114.0.5735.201\", \"Microsoft Edge\";v=\"114.0.1823.79\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua-platform-version": "\"10.0.0\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-asbd-id": "129477",
            "x-fb-friendly-name": "ProfileCometHometownProfileFieldSaveMutation",
            "x-fb-lsd": "WK_MbVszi0WH2acEQtgRIS",
            "origin": "https://www.facebook.com",
            "referer": f"https://www.facebook.com/profile.php?id={aku}",
        }
        body = {
            "av": aku,
            "__user": aku,
            "__a": 1,
            "__req": "1b",
            "__hs": "19528.HYP:comet_pkg.2.1..2.1",
            "dpr": 1,
            "__ccg": "EXCELLENT",
            "__rev": 1007710268,
            "__s": "79c0j6:m1nru1:83nmcf",
            "__hsi": "7246911319933780320",
            "__dyn": "7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2CVEbUGdG1Fwh888cA0z8c84q58jwTwNxe6Uak1xwJwxyo566k1Fw",
            "__csr": "g9IhX4TdsQYDlh2d9OTsj4jHdWWSJNfbFsQAlijBECQQDiiunAbpd9ljlDGDA88JeiArmLCipbarx6EBmirWnCSQnCunGRC-WDycLp8OVAq9hGtaqm8y9VEBbKvy8SJ3GyEKQ8CF2EiQ4e9KmJa9wJLhkE-5lplxeECczoPBUWKqQ9KiK5-7UOESfxevzVoOQ5qyEO4Ey2u-EC4p8Oqvh8jwRV8gzoiwRz8dXAwCzaypEbui58yu2W4opwxwiVoy5orwgQ27xOi5pu265Uborx-EdE6i2m2K2mcxa00zPUjw08gy02-q0pa0To2jIK0aEwvE3LwSw6VgsDwhUlw8K0lnwUxbwk86q0HU0aVUGO04Eg0afE2gHo0_i2q2yvBg8U0Pe1_Ao1yo0dyA04Po0hhJVp9609JwbW1LwKGH9jyH82C2Cq0efwhFE3aw",
            "__comet_req": 15,
            "fb_dtsg": dtsg,
            "jazoest": "25132",
            "lsd": "Zf8sjcp1MulGh6qIoX_Pv2",
            "__spin_r": 1007710268,
            "__spin_b": "trunk",
            "__spin_t": 1687303027,
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "ProfileCometHometownProfileFieldSaveMutation",
            "variables": json.dumps(variables),
            "server_timestamps": "true",
            "doc_id": "6434674599925799"
        }
        base_url = "https://web.facebook.com/api/graphql/"
        response = requests.post(
            base_url,
            headers=headers,
            cookies=cookies,
            data=body
        )
        if response == 200:
            print(f"{yellow}───────────────────────────────────────────────────────────────")
            print(f"{green}Successfully Set Bio✅")
            print(f"{yellow}───────────────────────────────────────────────────────────────")
        try:
            return response.json()
        except Exception:
            return response.text

def setting_kota_sekarang(aku, fbdtsg, sec_token, col_token, kota_ku, cookies):
  
    session = requests.Session()

  
    session.cookies.update(cookies)

 
    jsBody = "av=" + aku
    jsBody += "&__user=" + aku
    jsBody += "&__a=1"
    jsBody += "&__req=1b"
    jsBody += "&__hs=19528.HYP:comet_pkg.2.1..2.1"
    jsBody += "&dpr=1"
    jsBody += "&__ccg=GOOD"
    jsBody += "&__rev=1007710268"
    jsBody += "&__s=m90oht:rmixf7:3xdcvq"
    jsBody += "&__hsi=7246900448908587779"
    jsBody += "&__dyn=7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2CVEbUGdG1Fwh888cA0z8c84q58jwTwNxe6Uak1xwJwxyo566k1Fw"
    jsBody += "&__csr=g9IhX4TdsQYDlh2d9OTsj4sGPuKhHsjOWmyOhl9emyrjit99VugJAQBleCuGuhyrjAF6RHVACiOCUhG9FAC-BVJJ5VDBWJpLKFUzbSicyAq9hGtaqm8y9VEBbKvxqJ3GyEKQ8CF2EiQ4e9Kmha9wJLhkE-5lplxeECczoPBUWKqQ9KiK5-7UOESfxevzVoOQ5qyEO4Ey2u-EC4p8Oqvh8jwRV8gzoiz8ixmcwTKiq7UOECq2TAxi8DwKx66o8o4KEK5orwgQ27xOi5pu265Uborx-EdE6i2m2K2mcxa00zPUjw08gy02-q0pa0To2jIK0aEwvE3LwSw6VgsDwhUlw8K0lnwUxbwk86q0HU0aVUGO04Eg0afE2gHo0_i2q2yvBg8U0Pe1_Ao1yo0dyA04Po0hhJVp9609JwbW1LwKGH9jyH82C2Cq0efwhFE3aw"
    jsBody += "&__comet_req=15"
    jsBody += "&fb_dtsg=" + fbdtsg
    jsBody += "&jazoest=25238"
    jsBody += "&lsd=MeD4BrSEyju7FQSGzIzyKQ"
    jsBody += "&__spin_r=1007710268"
    jsBody += "&__spin_b=trunk"
    jsBody += "&__spin_t=1687300496"
    jsBody += "&fb_api_caller_class=RelayModern"
    jsBody += "&fb_api_req_friendly_name=ProfileCometCurrentCityProfileFieldSaveMutation"
    jsBody += "&variables=" + json.dumps({
        "collectionToken": col_token,
        "input": {
            "current_city_id": kota_ku,
            "privacy": {
                "allow": [],
                "base_state": "EVERYONE",
                "deny": [],
                "tag_expansion_state": "UNSPECIFIED"
            },
            "actor_id": aku,
            "client_mutation_id": "2"
        },
        "scale": 1,
        "sectionToken": sec_token,
        "useDefaultActor": False
    })
    jsBody += "&server_timestamps=true"
    jsBody += "&doc_id=6469992053095693"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-prefers-color-scheme": "light",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
        "sec-ch-ua-full-version-list": "\"Not.A/Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"114.0.5735.201\", \"Microsoft Edge\";v=\"114.0.1823.79\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-asbd-id": "129477",
        "x-fb-friendly-name": "ProfileCometCurrentCityProfileFieldSaveMutation",
        "x-fb-lsd": "WK_MbVszi0WH2acEQtgRIS"
    }

    response = session.post(
        "https://web.facebook.com/api/graphql/",
        headers=headers,
        data=jsBody
    )
    if response == 200:
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{green}Successfully Set City✅")
        print(f"{yellow}───────────────────────────────────────────────────────────────")
    try:
        pass
    except Exception:
        pass

def parse_cookie_string(cookie_str):
    cookies = {}
    for part in cookie_str.split(";"):
        if "=" in part:
            key, value = part.strip().split("=", 1)
            cookies[key] = value
    return cookies

import requests
import json
import base64

def get_fb_dtsg_and_jazoest(cookie: str):
    """Fetch fb_dtsg and jazoest tokens using mbasic.facebook.com"""
    url = "https://mbasic.facebook.com/"
    headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers).text

    try:
        fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
        uid = cookie.split("c_user=")[1].split(";")[0]
        return fb_dtsg, jazoest, uid
    except IndexError:
        raise Exception("Could not extract fb_dtsg or jazoest. Check if cookie is valid.")

def set_education(cookie: str):
    """Auto-update Facebook Education section for a user"""

    fb_dtsg, jazoest, uid = get_fb_dtsg_and_jazoest(cookie)

   
    collection_token = base64.b64encode(f"app_collection:{uid}:2327158227:201".encode()).decode()
    section_token = base64.b64encode(f"app_section:{uid}:2327158227".encode()).decode()
    schoollist = ["104076956295773"]
    school_name = ""
    randomz = random.randint(0,len(schoollist) - 1 )
    school_id = schoollist[randomz]
    if school_id == 104076956295773: 
        school_name = "UP Diliman Campus, Quezon City, Philippines"
    
    
    
    school_type = "college"
    degree_name = ""
    concentrations = [{"id": "", "name": ""}]
    description = ""
    has_graduated = True

    # --- Step 4: Prepare request ---
    variables = {
        "collectionToken": collection_token,
        "sectionToken": section_token,
        "input": {
            "school_id": school_id,
            "school_name": school_name,
            "school_type": school_type,
            "degree_name": degree_name,
            "concentrations": concentrations,
            "description": description,
            "has_graduated": has_graduated,
            "start": {},
            "end": {},
            "privacy": {"base_state": "EVERYONE", "allow": [], "deny": []},
            "actor_id": uid,
            "client_mutation_id": "1"
        },
        "scale": 1,
        "useDefaultActor": False
    }

    url = "https://www.facebook.com/api/graphql/"
    data = {
        "fb_dtsg": fb_dtsg,
        "jazoest": jazoest,
        "__a": "1",
        "variables": json.dumps(variables),
        "doc_id": "31469420822671680",
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "cookie": cookie
    }

    
    response = requests.post(url, headers=headers, data=data)
    if response == 200: 
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{green}SuccessFully Set Education ✅ ") 
        print(f"{yellow}───────────────────────────────────────────────────────────────")
    else: 
        pass

        

import requests
import base64
import json

def get_fb_dtsg_and_jazoest(cookie: str):
    """Fetch fb_dtsg and jazoest tokens using mbasic.facebook.com"""
    url = "https://mbasic.facebook.com/"
    headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers).text

    try:
        fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
        uid = cookie.split("c_user=")[1].split(";")[0]
        return fb_dtsg, jazoest, uid
    except IndexError:
        raise Exception("Could not extract fb_dtsg or jazoest. Check if cookie is valid.")

def set_work_experience(cookie: str, employer_id: str, position_id: str,
                        location_id: str, is_current=True, description=""):
    fb_dtsg, jazoest, uid = get_fb_dtsg_and_jazoest(cookie)

    # Encode collection and section tokens
    collection_token = base64.b64encode(f"app_collection:{uid}:2327158227:201".encode()).decode()
    section_token = base64.b64encode(f"app_section:{uid}:2327158227".encode()).decode()

    variables = {
        "collectionToken": collection_token,
        "input": {
            "employer_id": employer_id,
            "position_id": position_id,
            "location_id": location_id,
            "is_current": is_current,
            "description": description,
            "actor_id": uid,
            "client_mutation_id": "1",
            "mutation_surface": "PROFILE",
            "privacy": {
                "base_state": "EVERYONE",
                "allow": [],
                "deny": [],
                "tag_expansion_state": "UNSPECIFIED"
            },
            "start_date": {},
            "end_date": {}
        },
        "scale": 1,
        "sectionToken": section_token,
        "useDefaultActor": False
    }

    payload = {
        "fb_dtsg": fb_dtsg,
        "jazoest": jazoest,
        "lsd": "",
        "__comet_req": "15",
        "server_timestamps": True,
        "doc_id": "24308463808846665",  # GraphQL mutation ID for work experience
        "variables": json.dumps(variables)
    }

    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post("https://www.facebook.com/api/graphql/", data=payload, headers=headers)
    if response == 200: 
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{green}SuccessFully Set Work ✅")                  
        print(f"{yellow}───────────────────────────────────────────────────────────────")
    else: 
        pass



import requests
import base64
import json

def get_fb_dtsg_and_jazoest(cookie: str):
    """Fetch fb_dtsg and jazoest tokens using mbasic.facebook.com"""
    url = "https://mbasic.facebook.com/"
    headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers).text

    try:
        fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
        uid = cookie.split("c_user=")[1].split(";")[0]
        return fb_dtsg, jazoest, uid
    except IndexError:
        raise Exception("Could not extract fb_dtsg or jazoest. Check if cookie is valid.")

def set_relationship_status(cookie: str, status="SINGLE"):
    fb_dtsg, jazoest, uid = get_fb_dtsg_and_jazoest(cookie)

    # Encode collection and section tokens
    collection_token = base64.b64encode(f"app_collection:{uid}:2327158227:201".encode()).decode()
    section_token = base64.b64encode(f"app_section:{uid}:2327158227".encode()).decode()

    variables = {
        "collectionToken": collection_token,
        "input": {
            "actor_id": uid,
            "status_const": status,
            "privacy": {
                "base_state": "EVERYONE",
                "allow": [],
                "deny": [],
                "tag_expansion_state": "UNSPECIFIED"
            },
            "client_mutation_id": "3",
            "subtitle": None,
            "logging_data": {}
        },
        "scale": 1,
        "sectionToken": section_token,
        "useDefaultActor": False
    }

    payload = {
        "fb_dtsg": fb_dtsg,
        "jazoest": jazoest,
        "lsd": "",
        "__comet_req": "15",
        "server_timestamps": True,
        "doc_id": "24515926678046349",  # GraphQL mutation ID for relationship status
        "variables": json.dumps(variables)
    }

    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post("https://www.facebook.com/api/graphql/", data=payload, headers=headers)
    if response == 200: 
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{green}Successfully Set Relationship✅")
        print(f"{yellow}───────────────────────────────────────────────────────────────")
    else: 
        pass
import requests
import base64
import json

def get_fb_dtsg_and_jazoest(cookie: str):
    """Fetch fb_dtsg and jazoest tokens using mbasic.facebook.com"""
    url = "https://mbasic.facebook.com/"
    headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers).text

    try:
        fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
        uid = cookie.split("c_user=")[1].split(";")[0]
        return fb_dtsg, jazoest, uid
    except IndexError:
        raise Exception("Could not extract fb_dtsg or jazoest. Check if cookie is valid.")

def set_pronouns(cookie: str, pronouns="MALE_SINGULAR"):
    fb_dtsg, jazoest, uid = get_fb_dtsg_and_jazoest(cookie)

    # Encode collection and section tokens
    collection_token = base64.b64encode(f"app_collection:{uid}:2327158227:201".encode()).decode()
    section_token = base64.b64encode(f"app_section:{uid}:2327158227".encode()).decode()

    variables = {
        "collectionToken": collection_token,
        "input": {
            "client_mutation_id": "1",
            "actor_id": uid,
            "expressive_pronouns": [],
            "expressive_pronouns_privacy": {
                "base_state": "SELF",
                "allow": [],
                "deny": [],
                "tag_expansion_state": "UNSPECIFIED"
            },
            "system_pronouns": pronouns,
            "logging_data": {}
        },
        "scale": 1,
        "sectionToken": section_token,
        "useDefaultActor": False
    }

    payload = {
        "fb_dtsg": fb_dtsg,
        "jazoest": jazoest,
        "lsd": "",
        "__comet_req": "15",
        "server_timestamps": True,
        "doc_id": "24023805800635051",  # GraphQL mutation ID for pronouns
        "variables": json.dumps(variables)
    }

    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post("https://www.facebook.com/api/graphql/", data=payload, headers=headers)
    if response == 200: 
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{green}Successfully Set Pronouce ✅")
        print(f"{yellow}───────────────────────────────────────────────────────────────")

    else:
        pass



import random
import base64
def banner():
    print(f"""{dark_violet}
      
          
            
          
                       
                    
██╗  ██╗██╗   ██╗██████╗  █████╗     ███╗   ███╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ██╗   ██╗ █████╗ 
██║  ██║██║   ██║██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║     ██║ ██╔╝██╔═══██╗██║   ██║██╔══██╗
███████║██║   ██║██║  ██║███████║    ██╔████╔██║███████║██║     █████╔╝ ██║   ██║██║   ██║███████║
██╔══██║██║   ██║██║  ██║██╔══██║    ██║╚██╔╝██║██╔══██║██║     ██╔═██╗ ██║   ██║╚██╗ ██╔╝██╔══██║
██║  ██║╚██████╔╝██████╔╝██║  ██║    ██║ ╚═╝ ██║██║  ██║███████╗██║  ██╗╚██████╔╝ ╚████╔╝ ██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
                                                                                                   

            
\033[0m""")
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_tokens():
    # Ask user for input/output choice
    print("\nChoose which file to process:")
    print("1. FRAACCOUNT.txt")
    print("2. FRAPAGES.txt")
    print("3. RPWACCOUNT.txt")
    print("4. RPWPAGES.txt")

    choice = input("Enter choice (1/2/3/4): ").strip()

    file_map = {
        "1": ("/sdcard/boostphere/FRAACCOUNT.txt", "/sdcard/boostphere/FRAACCOUNTCOOKIE.txt"),
        "2": ("/sdcard/boostphere/FRAPAGES.txt", "/sdcard/boostphere/FRAPAGESCOOKIE.txt"),
        "3": ("/sdcard/boostphere/RPWACCOUNT.txt", "/sdcard/boostphere/RPWACCOUNTCOOKIE.txt"),
        "4": ("/sdcard/boostphere/RPWPAGES.txt", "/sdcard/boostphere/RPWPAGESCOOKIE.txt"),
    }

    if choice not in file_map:
        print("❌ Invalid choice, exiting.")
        return

    input_path, output_path = file_map[choice]

    # Colors
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    dark_violet = "\033[35m"

    results = []

    def task(line):
        line = line.strip()
        if '|' not in line:
            return None, None
        uid, token = line.split('|', 1)
        try:
            # First request to get app info
            r1 = requests.get(
                'https://graph.facebook.com/app',
                params={'access_token': token.strip()},
                timeout=10
            )
            data1 = r1.json()
            if 'error' in data1:
                return f"{green}[{uid}] {red}Invalid token: {yellow}{data1['error']['message']}", None

            # Second request to get session cookies
            r2 = requests.get(
                'https://api.facebook.com/method/auth.getSessionforApp',
                params={
                    'access_token': token.strip(),
                    'format': 'json',
                    'new_app_id': data1['id'],
                    'generate_session_cookies': '1'
                },
                timeout=10
            )
            data2 = r2.json()

            if 'session_cookies' in data2:
                cookies = ';'.join([f"{c['name']}={c['value']}" for c in data2['session_cookies']])
                return f"{red}[{uid}] {green}Successfully Retrieved Session", f"{uid}|{cookies}"
            else:
                return f"{red}[{uid}] {yellow}Failed to retrieve session cookies.", None

        except Exception as e:
            return f"[{uid}] Error: {e}", None

    # Read input file (uid|token lines)
    with open(input_path, "r") as infile:
        lines = infile.readlines()

    # Run threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(task, line): line for line in lines}
        for future in as_completed(futures):
            status, result = future.result()
            if status:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(status)
            if result:
                results.append(result)

    # Write results to chosen output file
    if results:
        with open(output_path, 'w') as outfile:
            outfile.write('\n'.join(results))
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"{green}Cookies saved to: {output_path}\033[0m")


# Run the method


def main():
    banner()
    print("Select account file to use:")
    print(f"{yellow}───────────────────────────────────────────────────────────────")
    print(f"{green}[1] {red}FRA Accounts")
    print(f"{yellow}───────────────────────────────────────────────────────────────")
    print(f"{green}[2] {red}FRA Pages")
    print(f"{yellow}───────────────────────────────────────────────────────────────")
    print(f"{green}[3] {red}RPW Accounts")
    print(f"{yellow}───────────────────────────────────────────────────────────────")
    print(f"{green}[4] {red}RPW Pages")
    print(f"{yellow}───────────────────────────────────────────────────────────────")
    choice = input(f"{green}Choose: ").strip()
    
    files = {
        "1": "/sdcard/boostphere/FRAACCOUNTCOOKIE.txt",
        "2": "/sdcard/boostphere/FRAPAGESCOOKIE.txt",
        "3": "/sdcard/boostphere/RPWACCOUNTCOOKIE.txt",
        "4": "/sdcard/boostphere/RPWPAGESCOOKIE.txt"
    }
    
    if choice not in files:
        print(f"{yellow}───────────────────────────────────────────────────────────────")
        print(f"{red}Invalid choice!")
        return
    
    accounts_file = files[choice]
    
    # Read all uid|cookie lines
    with open(accounts_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if '|' in line]
    
    for line in lines:
        aku, COOKIE = line.split('|', 1)
        
        kota_list = ["106042439427784", "109144912452921", "109144912452921","110125409010382",
                     "108343052523582","116118201734523","108450295845257","109907432369509",
                     "184977461524319","113301478684099","108062649215723","111997308816787",
                     "109155499103263","106061992757459","114593885223523","108174219211222"]
        
        fb_dtsg, jazoest, uid = FacebookClient.get_fb_dtsg_and_jazoest(COOKIE)
        client = FacebookClient(COOKIE, fb_dtsg, jazoest, uid)
        cokz = parse_cookie_string(COOKIE)
        
        rand_kota = random.randint(0, len(kota_list) - 1)
        kota_ku = kota_list[rand_kota]
        
        col_token = base64.b64encode(f"app_collection:{aku}:2327158227:201".encode()).decode()
        sec_token = base64.b64encode(f"app_section:{aku}:2327158227".encode()).decode()
        
        print("Selected City:", kota_ku)
        print("Collection Token:", col_token)
        print("Section Token:", sec_token)
        
        bioz = ["Professional overthinker","Life’s short—smile while you still have teeth.","Born to express, not to impress","I put the “pro” in procrastinate.","Too glam to give a damn","I may be wrong, but I doubt it.","Still waiting for my Hogwarts letter.","I followed my heart… it led me to the fridge.","I’m not lazy—just energy efficient.","In a committed relationship with Netflix.","Dream big. Work hard. Stay humble.","Building a life I love.","Be yourself; everyone else is taken.","Progress, not perfection.","I dont chase dreams—I hunt goals.","I'm the storm they warned you about","I’m not special, I’m just a limited edition.","Just living life.","Keep it simple.","Always learning.","Grateful. Humble. Blessed.","Here for a good time.","Work in progress.","Loving life, one day at a time.","Simply me.","Trying to be better every day.","No filter needed.","CEO of my own life.","Entrepreneur | Dreamer | Doer","Making ideas happen.","Marketing geek with big goals.","Life through my lens."]
        bio = random.choice(bioz)
        
        school_id = "106106769421063"
        my_town = "110340245656034"
        doc_id = "31469420822671680"
        school_name = "University of Ibadan"
        
        # Call functions
        setting_kota_sekarang(aku, client.fb_dtsg, sec_token, col_token, kota_ku, cokz)
        setting_hometown(aku, col_token, my_town, sec_token, client.fb_dtsg, cokz)
        bio_update(COOKIE, client.fb_dtsg, aku, bio)
        set_education(COOKIE)
        set_work_experience(
            cookie=COOKIE,
            employer_id="130834093453317",
            position_id="1671268736243232",
            location_id="110941395597405",
            description="Automated work experience update")
        set_relationship_status(COOKIE, status="SINGLE")
        set_pronouns(COOKIE, pronouns="MALE_SINGULAR")

if __name__ == "__main__":
    banner()
    print(f"{green}Choose: ")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{red}[1]Convert Tokens to Cookie")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{green}[2]Auto Set")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    azx  = input(f"{green} Input: ")
    if azx == '1':
        process_tokens()
    elif azx == '2':
        main()
    else:
        print(f"{red} Invalid")



    

