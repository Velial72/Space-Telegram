def fetch_nasa_epic():
    token = os.getenv('NASA_TOKEN')
    filename = 'epic'
    payload = {"api_key": token}
    folder_path = os.path.join('images')
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/image', params=payload)
    os.makedir('images')
    for name_image in response.json():
        name_count = len(os.listdir(folder_path))
        info_image = name_image['image'], name_image['date'].split(' ')[0].replace('-', '/')
        endpoint = f'https://api.nasa.gov/EPIC/archive/natural/{info_image[1]}/png/{info_image[0]}.png?api_key=DEMO_KEY'
        save_image(endpoint, folder_path, filename, name_count)
