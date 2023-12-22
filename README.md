# Instagram Anon Viewer


This is a simple script to retrieve Instagram user data using the Instagram Graph API. It requires an access token to access the user's media data. Please note that using the Instagram Graph API requires approval from Instagram, and you should comply with their platform policies when using this script.


## Usage

### Installation:
Ensure you have Python installed.
Install the required dependencies: 
```bash
pip install requests
```
Clone the repository: 
```bash 
git clone https://github.com/collateralusr/Instagram-Anon-View
instagram-anon-view
```


### Obtain Instagram API Access Token:
Go to the Facebook Developers page and create a new app.
Set up the app with Instagram Basic Display.
Obtain your Access Token following the official documentation.
### Run the Script:
Execute the script in a Python environment.
Input your Instagram API access code and the target Instagram username when prompted.
### Review the Data:
The script will print the raw JSON data received from the Instagram Graph API. You may want to modify the script to process and display the data as needed.

## Examples
```bash
Enter your Instagram API access code: YOUR_ACCESS_TOKEN
Enter your target's Instagram Username: target_username
{
  "id": "123456789",
  "media": {
    "data": [
      {
        "id": "987654321",
        "caption": "A beautiful sunset",
        "media_type": "IMAGE",
        "media_url": "https://example.com/sunset.jpg"
      },
      // Additional media items
    ],
    "paging": {
      "cursors": {
        "before": "before_cursor",
        "after": "after_cursor"
      },
      "next": "next_page_url"
    }
  }
}


```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
