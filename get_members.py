import requests
import csv

# Set up constants
API_URL = "https://snyk.io/api/v1/"
API_TOKEN = "XXXXX"  # Replace with your API token
GROUP_ID = "XXXXX"  # Replace with your Group ID

headers = {
    "Authorization": f"token {API_TOKEN}"
}

def list_orgs_in_group(group_id):
    response = requests.get(API_URL + f"group/{group_id}/orgs", headers=headers)
    response.raise_for_status()
    return response.json()['orgs']

def list_members_in_org(org_id):
    response = requests.get(API_URL + f"org/{org_id}/members?includeGroupAdmins=true", headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    with open('snyk_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(['Org Name', 'Org ID', 'Member Name', 'Member ID', 'Member Email'])

        orgs = list_orgs_in_group(GROUP_ID)
        for org in orgs:
            members = list_members_in_org(org['id'])
            for member in members:
                csvwriter.writerow([org['name'], org['id'], member['name'], member['id'], member['email']])

if __name__ == "__main__":
    main()
