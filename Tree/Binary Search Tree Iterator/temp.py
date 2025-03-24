import requests
import pandas as pd
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "https://www.montclair.edu/school-of-computing/staff-directory/"
response = requests.get(url)
html_content = response.text

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Lists to store faculty details
name_list, title_list, phone_list, email_list, office_list = [], [], [], [], []

# Locate the 'Full Time Faculty' section
full_time_header = soup.find('h2', string='Full Time Faculty')

if full_time_header:
    current_sibling = full_time_header.find_next_sibling()
    while current_sibling and current_sibling.name != 'h2':
        if current_sibling.name == 'div' \
            and 'profile' in current_sibling.get('class',[]) \
            and 'smallphoto' in current_sibling.get('class', []):
            profile_data = current_sibling.find('div', class_='profile-data')

            if profile_data:
                # Extract name
                name_tag = profile_data.find('p', class_='name').find('a') if profile_data.find('p',
                                                                                                class_='name') else None
                name = name_tag.text.strip() if name_tag else 'N/A'
                name_list.append(name)

                # Extract title
                title_tag = profile_data.find('p', class_='title')
                title = title_tag.text.strip() if title_tag else 'N/A'
                title_list.append(title)

                # Extract contact details
                contact_dl = profile_data.find('dl', class_='compact')
                phone = 'N/A'
                email = 'N/A'
                office = 'N/A'

                if contact_dl:
                    # Phone extraction
                    phone_dt = contact_dl.find('dt', string='Phone')
                    if phone_dt:
                        phone_dd = phone_dt.find_next_sibling('dd')
                        if phone_dd:
                            phone_span = phone_dd.find('span', class_='a11y-phone-number')
                            phone = phone_span.text.strip() if phone_span else phone_dd.text.strip()
                    # Email extraction
                    email_dt = contact_dl.find('dt', string='Email')
                    if email_dt:
                        email_dd = email_dt.find_next_sibling('dd')
                        if email_dd:
                            email_a = email_dd.find('a')
                            email = email_a.text.strip() if email_a else 'N/A'
                    # Office location extraction
                    location_dt = contact_dl.find('dt', string='Location')
                    if location_dt:
                        location_dd = location_dt.find_next_sibling('dd')
                        office = location_dd.text.strip() if location_dd else 'N/A'

                phone_list.append(phone)
                email_list.append(email)
                office_list.append(office)

        current_sibling = current_sibling.find_next_sibling()

# Create DataFrame
df = pd.DataFrame({
    'Name': name_list,
    'Title': title_list,
    'Phone': phone_list,
    'Email': email_list,
    'Office': office_list
})

print(df)