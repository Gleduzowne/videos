#!/usr/bin/env python3
"""
YouTube Video Upload Script

Usage:
  python scripts/upload_to_youtube.py --file=output.mp4 --title="My Video Title" --description="Description here" --category="22" --keywords="tag1,tag2" --privacyStatus="private"

Setup:
- You need to create a project in Google Cloud Console, enable the YouTube Data API v3, and download OAuth 2.0 credentials as client_secrets.json.
- Place client_secrets.json in the same directory as this script.
- The first run will open a browser for authentication.

Install dependencies:
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

"""
import os
import sys
import argparse
import http.client
import httplib2
import random
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Explicitly tell the underlying HTTP transport library not to retry, since we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (http.client.NotConnected, http.client.IncompleteRead, http.client.ImproperConnectionState, ConnectionResetError, httplib2.ServerNotFoundError)

# Always retry when an apiclient.errors.HttpError with one of these status codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "client_secrets.json"


def get_authenticated_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)


def initialize_upload(youtube, options):
    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=options.keywords.split(",") if options.keywords else None,
            categoryId=options.category
        ),
        status=dict(
            privacyStatus=options.privacyStatus
        )
    )

    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    resumable_upload(insert_request)


def resumable_upload(request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print("Uploading file...")
            status, response = request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print(f"Video id '{response['id']}' was successfully uploaded.")
                else:
                    print(f"The upload failed with an unexpected response: {response}")
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"
        if error:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                print("No longer attempting to retry.")
                break
            sleep_seconds = random.random() * (2 ** retry)
            print(f"Sleeping {sleep_seconds} seconds and retrying...")
            time.sleep(sleep_seconds)
            error = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Video file to upload")
    parser.add_argument("--title", required=True, help="Video title")
    parser.add_argument("--description", default="", help="Video description")
    parser.add_argument("--category", default="22", help="Numeric video category. Default is 22 (People & Blogs)")
    parser.add_argument("--keywords", default="", help="Comma-separated list of video keywords/tags")
    parser.add_argument("--privacyStatus", default="private", choices=["public", "private", "unlisted"], help="Video privacy status")
    args = parser.parse_args()

    if not os.path.exists(CLIENT_SECRETS_FILE):
        print(f"ERROR: {CLIENT_SECRETS_FILE} not found. Please follow the setup instructions in the script.")
        sys.exit(1)

    youtube = get_authenticated_service()
    try:
        initialize_upload(youtube, args)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")

if __name__ == '__main__':
    main()
